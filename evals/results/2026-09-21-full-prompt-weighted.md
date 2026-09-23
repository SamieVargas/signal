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
| Cost per run (analysis call, USD) | $0.0323 |
| Cost for the whole run (analysis calls, USD) | $0.4205 |
| Prices | list, read 2026-09-23 |
| Hard fails | 0 |

| Case | Expected risk | Predicted | Recall | Buyer | Attribution | Gaps | Parse | ms | Cost |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| adoption-failure | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | recovered_by_parser | 47888 | $0.0433 |
| champion-loss | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 44774 | $0.0331 |
| chat-positive-crm-negative | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | recovered_by_parser | 39499 | $0.0316 |
| frustrated-not-gone | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | recovered_by_parser | 42081 | $0.0313 |
| healthy | (none) | Healthy | 100% | ✓ | 100% | ✓ | recovered_by_parser | 35635 | $0.0285 |
| most-mentioned-not-buyer | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | recovered_by_parser | 45192 | $0.0343 |
| power-user-concentration | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 48184 | $0.0346 |
| reduced-footprint | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 40448 | $0.0315 |
| relationship-gap | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | recovered_by_parser | 42676 | $0.0327 |
| silent-decay | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | recovered_by_parser | 40225 | $0.0311 |
| stalled-expansion | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | recovered_by_parser | 40371 | $0.0328 |
| truncated-transcript | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 33877 | $0.0268 |
| vibe-risk | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 36811 | $0.0289 |
