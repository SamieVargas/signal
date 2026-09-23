"""Smoke test for the eval runner on one stubbed case. No API key.

    python evals/test_run.py
"""
import json
import os
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "tests"))
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "tools"))

import run  # noqa: E402
import recost  # noqa: E402
from test_pipeline import FakeClient, SAMPLE_BRIEF, check  # noqa: E402


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
