# Signal eval — 2026-09-21 · mode `full` · contract `prompt` · arm `weighted` · 1 run(s) per case

| Metric | Value |
| --- | --- |
| Cases × runs | 13 |
| Risk-type recall (primary) | 96% |
| Risk-type precision | 100% |
| Economic-buyer accuracy | 92% |
| Attribution coverage | 92% |
| Data gaps present when expected | 100% |
| Parse: native / recovered / failed | 5 / 8 / 0 |
| Mean tokens in / out (analysis call) | 1,753 / 1,806 |
| Mean analysis latency | 41,359 ms |
| Hard fails | 0 |

| Case | Expected risk | Predicted | Recall | Buyer | Attribution | Gaps | Parse | ms |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| adoption-failure | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | recovered_by_parser | 47888 |
| champion-loss | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 44774 |
| chat-positive-crm-negative | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | recovered_by_parser | 39499 |
| frustrated-not-gone | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | recovered_by_parser | 42081 |
| healthy | (none) | Healthy | 100% | ✓ | 100% | ✓ | recovered_by_parser | 35635 |
| most-mentioned-not-buyer | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | recovered_by_parser | 45192 |
| power-user-concentration | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 48184 |
| reduced-footprint | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 40448 |
| relationship-gap | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | recovered_by_parser | 42676 |
| silent-decay | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | recovered_by_parser | 40225 |
| stalled-expansion | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | recovered_by_parser | 40371 |
| truncated-transcript | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 33877 |
| vibe-risk | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 36811 |
