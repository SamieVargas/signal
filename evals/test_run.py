"""Smoke test for the eval runner on one stubbed case. No API key.

    python evals/test_run.py
"""
import json
import os
import sys
import tempfile
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "tests"))
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "tools"))

import run  # noqa: E402
import recost  # noqa: E402
from test_pipeline import FakeClient, SAMPLE_BRIEF, check  # noqa: E402


class FakeBatches:
    """Stands in for client.messages.batches: create / retrieve / results.

    Answers each request by calling the stub's messages.create with the
    request's own params, so a batched reply is exactly what the live path
    would have got. `polls` is how many retrieve() calls report in_progress
    before "ended"; `fail_ids` come back as errored results; results are
    yielded in reverse order because the real API promises no order."""

    def __init__(self, messages, *, polls=2, fail_ids=()):
        self.messages, self.polls, self.fail_ids = messages, polls, set(fail_ids)
        self.created, self.retrieves = [], 0

    def _counts(self, n, done):
        return SimpleNamespace(processing=0 if done else n, succeeded=n if done else 0,
                               errored=0, canceled=0, expired=0)

    def create(self, requests):
        requests = list(requests)
        self.created.append(requests)
        return SimpleNamespace(id="msgbatch_test", processing_status="in_progress",
                               request_counts=self._counts(len(requests), False))

    def retrieve(self, batch_id):
        self.retrieves += 1
        done = self.retrieves > self.polls
        return SimpleNamespace(id=batch_id, processing_status="ended" if done else "in_progress",
                               request_counts=self._counts(len(self.created[-1]), done))

    def results(self, batch_id):
        for req in reversed(self.created[-1]):
            if req["custom_id"] in self.fail_ids:
                err = SimpleNamespace(type="error", error=SimpleNamespace(type="invalid_request_error",
                                                                          message="max_tokens exceeds the model limit"))
                yield SimpleNamespace(custom_id=req["custom_id"], result=SimpleNamespace(type="errored", error=err))
            else:
                yield SimpleNamespace(custom_id=req["custom_id"],
                                      result=SimpleNamespace(type="succeeded", message=self.messages.create(**req["params"])))


def batch_client(polls=2, fail_ids=(), usage=(3000, 1500), **kw):
    client = FakeClient(usage=usage, **kw)
    client.messages.batches = FakeBatches(client.messages, polls=polls, fail_ids=fail_ids)
    return client


def main():
    case = run.load_cases(run.GOLDEN, only=["most-mentioned-not-buyer"])[0]
    expected = case["expected"]

    print("scoring functions")
    check("risk recall: hit", run.score_risk(["Relationship gap"], "Relationship gap")["recall"] == 1.0)
    check("risk recall: miss", run.score_risk(["Relationship gap"], "Vibe risk")["recall"] == 0.0)
    check("risk recall: one of two expected", run.score_risk(["A", "B"], "A")["recall"] == 0.5)
    check("no-risk case: Healthy scores precision 1", run.score_risk([], "Healthy")["precision"] == 1.0)
    check("no-risk case: an invented risk scores precision 0", run.score_risk([], "Vibe risk")["precision"] == 0.0)
    check("buyer: name inside 'Name, Title'", run.score_buyer("Marcus Chen", "Marcus Chen, VP Operations"))
    check("buyer: case and whitespace normalized", run.score_buyer("marcus  chen", "MARCUS CHEN — VP"))
    check("buyer: different person fails", not run.score_buyer("Marcus Chen", "Priya Nair, Platform Admin"))
    attr = run.score_attribution(["QBR notes", "Teams chat"], {"situation": ["QBR notes"], "contact_read": ["Teams chat", "CRM notes"]})
    check("attribution: full coverage", attr["coverage"] == 1.0 and not attr["missing"])
    attr = run.score_attribution(["QBR notes", "Teams chat"], {"situation": ["QBR notes"]})
    check("attribution: partial coverage names the gap", attr["coverage"] == 0.5 and attr["missing"] == ["Teams chat"])

    print("one stubbed case end to end")
    brief = dict(SAMPLE_BRIEF)
    brief.update({
        "risk_type": "Relationship gap",
        "contact_persona": {**SAMPLE_BRIEF["contact_persona"], "primary_contact": "Marcus Chen, VP Operations"},
        "section_sources": {"situation": ["QBR notes", "CRM notes"], "contact_read": ["Teams chat"],
                            "where_to_press": ["QBR notes"], "do_this_today": ["CRM notes"]},
        "data_gaps": ["direct conversation with Marcus"],
    })
    client = FakeClient(analysis_reply=json.dumps(brief))
    r = run.run_case(client, case, mode="full", contract="native", weighted=True)
    check("control files are not summarized",
          all("expected.json" not in c["messages"][-1]["content"] and "account.json" not in c["messages"][-1]["content"]
              for c in client.messages.calls if isinstance(c["messages"][-1]["content"], str)))
    check("one summary call per document", len(client.messages.calls) == r["docs"] + 1)
    check("native contract sent output_config", "output_config" in client.messages.calls[-1])
    check("scores: recall 1", r["scores"]["risk"]["recall"] == 1.0)
    check("scores: buyer matched", r["scores"]["buyer"] is True)
    check("scores: attribution covered", r["scores"]["attribution"]["coverage"] == 1.0)
    check("scores: gaps present", r["scores"]["gaps_ok"] is True)
    check("no hard fail", not r["hard_fail"])

    print("aggregate + table")
    r["run"] = 1; r["expected_risk"] = expected["risk_types"]
    agg = run.aggregate([r])
    table = run.render_table([r], agg, mode="full", contract="native", arm="weighted", runs=1)
    check("aggregate recall 100%", agg["risk_recall"] == 1.0)
    check("table has the case row", "| most-mentioned-not-buyer |" in table and "Relationship gap" in table)

    print("cost column and rows")
    check("stub client records no tokens, so cost is None", r["meta"]["cost_usd"] is None)
    check("aggregate says so", agg["cost_per_run_usd"] is None and agg["cost_total_usd"] is None
          and agg["pricing"] == {"dated": run.config.PRICES_DATED, "batch": False, "multiplier": 1.0, "covers": "analysis call"})
    check("table rows say not recorded",
          "| Cost per run (analysis call, USD) | not recorded |" in table
          and "| Cost for the whole run (analysis calls, USD) | not recorded |" in table
          and f"| Prices | list, read {run.config.PRICES_DATED} |" in table
          and table.splitlines()[-1].endswith("| not recorded |"))
    check("case table header ends with Cost", "| Parse | ms | Cost |" in table)
    priced = [dict(r, meta=dict(r["meta"], input_tokens=3000, output_tokens=1500)),
              dict(r, meta=dict(r["meta"], input_tokens=1000, output_tokens=500))]
    for x in priced:
        run.attach_cost(x["meta"])
    check("cost per case-run from its tokens", round(priced[0]["meta"]["cost_usd"], 4) == 0.0315
          and round(priced[1]["meta"]["cost_usd"], 4) == 0.0105)
    pagg = run.aggregate(priced)
    check("cost per run is the mean, whole run the sum",
          round(pagg["cost_per_run_usd"], 4) == 0.0210 and round(pagg["cost_total_usd"], 4) == 0.0420)
    ptable = run.render_table(priced, pagg, mode="full", contract="native", arm="weighted", runs=2)
    check("four decimals in the table", "| Cost per run (analysis call, USD) | $0.0210 |" in ptable
          and "| Cost for the whole run (analysis calls, USD) | $0.0420 |" in ptable
          and ptable.splitlines()[-1].endswith("| $0.0105 |"))
    bagg = run.aggregate(priced, batch=True)
    check("aggregate pricing records the batch basis", bagg["pricing"]["batch"] is True and bagg["pricing"]["multiplier"] == 0.5)

    print("recost rewrites only the cost cells of an existing table")
    old_lines = ptable.splitlines()
    stripped = []
    for line in old_lines:
        if line.startswith(("| Cost per run", "| Cost for the whole run", "| Prices |")):
            continue
        if line.startswith(("| Case |", "| --- | --- | --- |", "| most-mentioned")):
            line = line.rstrip()[: line.rstrip().rfind("|", 0, -1) + 1]  # drop the last cell
        stripped.append(line)
    old_md = "\n".join(stripped) + "\n"
    check("the stripped table has no dollars", "$" not in old_md and "| Cost |" not in old_md)
    data = {"runs": 2, "models": run.config.MODELS,
            "results": [{k: v for k, v in x.items() if k != "brief"} | {"meta": {k: v for k, v in x["meta"].items() if k != "cost_usd"}} for x in priced]}
    new_results, new_agg = recost.recost_results(data)
    rewritten = recost.rewrite_table(old_md, new_results, new_agg, 2)
    check("recost reproduces the runner's table exactly", rewritten == ptable)
    check("recost is idempotent", recost.rewrite_table(rewritten, new_results, new_agg, 2) == ptable)
    check("recost with batch=true in the JSON halves the figures",
          round(recost.recost_results(dict(data, batch=True))[1]["cost_total_usd"], 4) == 0.0210)
    with tempfile.TemporaryDirectory() as tmp:
        Path(tmp, "x.json").write_text(json.dumps(data), encoding="utf-8")
        Path(tmp, "x.md").write_text(old_md, encoding="utf-8")
        recost.main([str(Path(tmp, "x.json"))])
        check("recost.main rewrites the .md beside the .json", Path(tmp, "x.md").read_text(encoding="utf-8") == ptable)
    try:
        recost.rewrite_table(old_md, new_results[:1], new_agg, 2)
        check("recost refuses a row count that does not match the JSON", False)
    except SystemExit:
        check("recost refuses a row count that does not match the JSON", True)

    print("main() with a stub client writes results")
    with tempfile.TemporaryDirectory() as tmp:
        code = run.main(["--only", "most-mentioned-not-buyer", "--contract", "native", "--out", tmp],
                        client=FakeClient(analysis_reply=json.dumps(brief)))
        files = sorted(os.listdir(tmp))
        check("exit 0", code == 0)
        check("wrote .md and .json", any(f.endswith(".md") for f in files) and any(f.endswith(".json") for f in files))
        written = json.loads(Path(tmp, next(f for f in files if f.endswith(".json"))).read_text(encoding="utf-8"))
        check("json carries the pricing and the cost fields",
              written["pricing"]["dated"] == run.config.PRICES_DATED and "cost_per_run_usd" in written["aggregate"]
              and "cost_total_usd" in written["aggregate"] and "cost_usd" in written["results"][0]["meta"])
        failing = FakeClient(analysis_reply="not json at all")
        code = run.main(["--only", "most-mentioned-not-buyer", "--out", tmp], client=failing)
        check("a failed parse is a hard fail (exit 1)", code == 1)

    print("batch mode: request construction")
    reply = json.dumps(brief)
    live = FakeClient(analysis_reply=reply, usage=(3000, 1500))
    live_r = run.run_case(live, case, mode="full", contract="native", weighted=True)
    live_params = {k: v for k, v in live.messages.calls[-1].items() if k != "system"}  # the stub logs system=None
    with tempfile.TemporaryDirectory() as tmp:
        client = batch_client(analysis_reply=reply)
        sleeps = []
        code = run.main(["--batch", "--only", "most-mentioned-not-buyer", "--contract", "native", "--runs", "2", "--out", tmp],
                        client=client, sleep=sleeps.append)
        reqs = client.messages.batches.created[-1]
        check("one batch, one request per case-run", len(client.messages.batches.created) == 1 and len(reqs) == 2)
        check("custom_id is case-run-arm-contract",
              [r["custom_id"] for r in reqs] == ["most-mentioned-not-buyer-1-weighted-native", "most-mentioned-not-buyer-2-weighted-native"])
        check("each request carries the live path's params (model, max_tokens, messages, output_config)",
              all(r["params"] == live_params for r in reqs))
        check("native contract puts output_config in the batch request",
              reqs[0]["params"]["output_config"]["format"]["type"] == "json_schema")
        check("summaries were made live, one call per document per run",
              len([c for c in client.messages.calls if "output_config" not in c]) == 2 * live_r["docs"])

        print("batch mode: polling until ended")
        check("polled until processing_status was ended", client.messages.batches.retrieves == 3)
        check("slept between polls with backoff", sleeps == [5.0, 10.0])

        print("batch mode: results mapped back to case and run")
        check("exit 0", code == 0)
        files = sorted(os.listdir(tmp))
        check("results filename carries -batch", any(f.endswith("-x2-batch.md") for f in files) and any(f.endswith("-x2-batch.json") for f in files))
        data = json.loads(Path(tmp, next(f for f in files if f.endswith("-batch.json"))).read_text(encoding="utf-8"))
        check("json says batch", data["batch"] is True and data["pricing"]["batch"] is True)
        check("two results in table order despite reversed delivery",
              [(r["case"], r["run"]) for r in data["results"]] == [("most-mentioned-not-buyer", 1), ("most-mentioned-not-buyer", 2)])
        check("each result remembers its custom_id", data["results"][1]["custom_id"] == "most-mentioned-not-buyer-2-weighted-native")
        check("same scoring path: recall, buyer, attribution, parse path as the live run",
              all(r["scores"] == live_r["scores"] and r["meta"]["parse_path"] == live_r["meta"]["parse_path"] for r in data["results"]))
        check("no latency in batch mode, so the column is blank",
              data["results"][0]["meta"]["latency_ms"] is None)
        md = Path(tmp, next(f for f in files if f.endswith("-batch.md"))).read_text(encoding="utf-8")
        check("table header says batch", "· batch" in md.splitlines()[0])

        print("batch mode: cost with the multiplier")
        check("live cost at list from 3,000 / 1,500 tokens", round(live_r["meta"]["cost_usd"], 4) == 0.0315)
        check("batch cost is half", round(data["results"][0]["meta"]["cost_usd"], 4) == 0.0158
              and abs(data["results"][0]["meta"]["cost_usd"] - live_r["meta"]["cost_usd"] / 2) < 1e-12)
        check("aggregate rows: per run and whole run at batch price",
              "| Cost per run (analysis call, USD) | $0.0158 |" in md
              and "| Cost for the whole run (analysis calls, USD) | $0.0315 |" in md
              and f"| Prices | batch (0.5× list), read {run.config.PRICES_DATED} |" in md)

    print("batch mode: an errored result")
    with tempfile.TemporaryDirectory() as tmp:
        client = batch_client(analysis_reply=reply, polls=0, fail_ids=["most-mentioned-not-buyer-2-weighted-native"])
        code = run.main(["--batch", "--only", "most-mentioned-not-buyer", "--contract", "native", "--runs", "2", "--out", tmp],
                        client=client, sleep=lambda s: None)
        check("an errored result is a hard fail (exit 1)", code == 1)
        data = json.loads(Path(tmp, next(f for f in sorted(os.listdir(tmp)) if f.endswith(".json"))).read_text(encoding="utf-8"))
        ok, bad = data["results"]
        check("the other case-run still scored", ok["scores"]["risk"]["recall"] == 1.0 and ok["error"] is None)
        check("the errored one counts as a failed parse", bad["meta"]["parse_path"] == "failed" and bad["hard_fail"] is True)
        check("with the cause recorded", bad["error"] == "batch result errored (invalid_request_error: max_tokens exceeds the model limit)")
        check("and no tokens, so no cost", bad["meta"]["cost_usd"] is None)
        check("parse-path accounting counts it", data["aggregate"]["parse_paths"] == {"native": 1, "recovered_by_parser": 0, "failed": 1})

    print("batch mode: dry run is unchanged")
    with tempfile.TemporaryDirectory() as tmp:
        client = batch_client(analysis_reply=reply)
        code = run.main(["--batch", "--dry-run", "--only", "most-mentioned-not-buyer", "--out", tmp], client=client)
        check("dry run exits 0 and creates no batch", code == 0 and not client.messages.batches.created and not os.listdir(tmp))

    print("an interrupted run writes what it has, marked partial")

    class Interrupting:
        """Answers like the fake client until the Nth analysis call, then raises the way Ctrl+C does."""
        def __init__(self, inner, after):
            self.inner, self.after, self.calls = inner, after, 0
            self.messages = self
        def create(self, **kw):
            self.calls += 1
            if self.calls > self.after:
                raise KeyboardInterrupt
            return self.inner.messages.create(**kw)

    with tempfile.TemporaryDirectory() as tmp:
        client = Interrupting(FakeClient(analysis_reply=json.dumps(brief)), after=6)
        code = run.main(["--only", "most-mentioned-not-buyer", "--contract", "native", "--runs", "3", "--out", tmp], client=client)
        files = sorted(os.listdir(tmp))
        check("exit 130 on interrupt", code == 130)
        check("files carry the partial suffix", any(f.endswith("-partial.md") for f in files) and any(f.endswith("-partial.json") for f in files))
        data = json.loads(Path(tmp, next(f for f in files if f.endswith("-partial.json"))).read_text(encoding="utf-8"))
        check("json records completed and planned", data["partial"] is True and 0 < data["completed"] < data["planned"])
        md = Path(tmp, next(f for f in files if f.endswith("-partial.md"))).read_text(encoding="utf-8")
        check("table header says PARTIAL", "PARTIAL" in md.splitlines()[0])

    print("\nALL CHECKS PASSED")


def test_eval_runner():
    """pytest entry point: the checks above, in one collected test."""
    main()


if __name__ == "__main__":
    main()
