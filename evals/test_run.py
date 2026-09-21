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

import run  # noqa: E402
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

    print("main() with a stub client writes results")
    with tempfile.TemporaryDirectory() as tmp:
        code = run.main(["--only", "most-mentioned-not-buyer", "--contract", "native", "--out", tmp],
                        client=FakeClient(analysis_reply=json.dumps(brief)))
        files = sorted(os.listdir(tmp))
        check("exit 0", code == 0)
        check("wrote .md and .json", any(f.endswith(".md") for f in files) and any(f.endswith(".json") for f in files))
        failing = FakeClient(analysis_reply="not json at all")
        code = run.main(["--only", "most-mentioned-not-buyer", "--out", tmp], client=failing)
        check("a failed parse is a hard fail (exit 1)", code == 1)

    print("\nALL CHECKS PASSED")


if __name__ == "__main__":
    main()
