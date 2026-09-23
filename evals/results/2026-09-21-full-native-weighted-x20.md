# Signal eval — 2026-09-21 · mode `full` · contract `native` · arm `weighted` · 20 run(s) per case

| Metric | Value |
| --- | --- |
| Cases × runs | 260 |
| Risk-type recall (primary) | 90% |
| Risk-type precision | 94% |
| Economic-buyer accuracy | 93% |
| Attribution coverage | 92% |
| Data gaps present when expected | 100% |
| Parse: native / recovered / failed | 260 / 0 / 0 |
| Mean tokens in / out (analysis call) | 3,004 / 1,450 |
| Mean analysis latency | 35,921 ms |
| Cost per run (analysis call, USD) | $0.0308 |
| Cost for the whole run (analysis calls, USD) | $7.9974 |
| Prices | list, read 2026-09-23 |
| Hard fails | 0 |

| Case | Expected risk | Predicted | Recall | Buyer | Attribution | Gaps | Parse | ms | Cost |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| adoption-failure #1 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 42239 | $0.0417 |
| champion-loss #1 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 36740 | $0.0304 |
| chat-positive-crm-negative #1 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 37007 | $0.0310 |
| frustrated-not-gone #1 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 37445 | $0.0311 |
| healthy #1 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 30310 | $0.0263 |
| most-mentioned-not-buyer #1 | Relationship gap | Power user concentration | 0% | ✓ | 100% | ✓ | native | 37185 | $0.0302 |
| power-user-concentration #1 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 38432 | $0.0328 |
| reduced-footprint #1 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 31242 | $0.0282 |
| relationship-gap #1 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 31418 | $0.0275 |
| silent-decay #1 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 41338 | $0.0318 |
| stalled-expansion #1 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 33931 | $0.0311 |
| truncated-transcript #1 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 29041 | $0.0260 |
| vibe-risk #1 | Vibe risk | Sentiment mismatch | 0% | ✓ | 100% | ✓ | native | 37551 | $0.0289 |
| adoption-failure #2 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 43242 | $0.0430 |
| champion-loss #2 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 39922 | $0.0313 |
| chat-positive-crm-negative #2 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 46555 | $0.0340 |
| frustrated-not-gone #2 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 31750 | $0.0279 |
| healthy #2 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 36218 | $0.0270 |
| most-mentioned-not-buyer #2 | Relationship gap | Sentiment mismatch | 0% | ✓ | 100% | ✓ | native | 30652 | $0.0272 |
| power-user-concentration #2 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 37224 | $0.0319 |
| reduced-footprint #2 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 32054 | $0.0282 |
| relationship-gap #2 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 34246 | $0.0295 |
| silent-decay #2 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 32949 | $0.0279 |
| stalled-expansion #2 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 33402 | $0.0304 |
| truncated-transcript #2 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 32575 | $0.0280 |
| vibe-risk #2 | Vibe risk | Silent decay | 0% | ✓ | 100% | ✓ | native | 38603 | $0.0311 |
| adoption-failure #3 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 42894 | $0.0427 |
| champion-loss #3 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 32796 | $0.0289 |
| chat-positive-crm-negative #3 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 34982 | $0.0305 |
| frustrated-not-gone #3 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 37885 | $0.0270 |
| healthy #3 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 26379 | $0.0247 |
| most-mentioned-not-buyer #3 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 36969 | $0.0309 |
| power-user-concentration #3 | Power user concentration | Power user concentration | 100% | ✓ | 50% (missing CSV data) | ✓ | native | 39927 | $0.0337 |
| reduced-footprint #3 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 31262 | $0.0277 |
| relationship-gap #3 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 46878 | $0.0326 |
| silent-decay #3 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 38515 | $0.0292 |
| stalled-expansion #3 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 33948 | $0.0307 |
| truncated-transcript #3 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 31791 | $0.0256 |
| vibe-risk #3 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 38508 | $0.0300 |
| adoption-failure #4 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 43007 | $0.0430 |
| champion-loss #4 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 31025 | $0.0275 |
| chat-positive-crm-negative #4 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 33986 | $0.0282 |
| frustrated-not-gone #4 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 34630 | $0.0297 |
| healthy #4 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 28909 | $0.0257 |
| most-mentioned-not-buyer #4 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 37745 | $0.0324 |
| power-user-concentration #4 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 45669 | $0.0344 |
| reduced-footprint #4 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 33960 | $0.0282 |
| relationship-gap #4 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 35807 | $0.0291 |
| silent-decay #4 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 42984 | $0.0322 |
| stalled-expansion #4 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 38138 | $0.0313 |
| truncated-transcript #4 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 40049 | $0.0284 |
| vibe-risk #4 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 37759 | $0.0301 |
| adoption-failure #5 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 46061 | $0.0451 |
| champion-loss #5 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 36624 | $0.0301 |
| chat-positive-crm-negative #5 | Sentiment mismatch | Relationship gap | 0% | ✓ | 100% | ✓ | native | 37010 | $0.0305 |
| frustrated-not-gone #5 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 36346 | $0.0300 |
| healthy #5 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 28575 | $0.0250 |
| most-mentioned-not-buyer #5 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 40701 | $0.0297 |
| power-user-concentration #5 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 51930 | $0.0351 |
| reduced-footprint #5 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 37945 | $0.0302 |
| relationship-gap #5 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 33119 | $0.0285 |
| silent-decay #5 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 31699 | $0.0274 |
| stalled-expansion #5 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 36082 | $0.0314 |
| truncated-transcript #5 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 36428 | $0.0292 |
| vibe-risk #5 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 33037 | $0.0282 |
| adoption-failure #6 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 42158 | $0.0431 |
| champion-loss #6 | Champion loss | Champion loss | 100% | ✓ | 100% | ✓ | native | 42343 | $0.0302 |
| chat-positive-crm-negative #6 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 39800 | $0.0305 |
| frustrated-not-gone #6 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 36258 | $0.0280 |
| healthy #6 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 27075 | $0.0250 |
| most-mentioned-not-buyer #6 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 35634 | $0.0305 |
| power-user-concentration #6 | Power user concentration | Power user concentration | 100% | ✓ | 50% (missing CSV data) | ✓ | native | 38574 | $0.0335 |
| reduced-footprint #6 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 31161 | $0.0281 |
| relationship-gap #6 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 32862 | $0.0283 |
| silent-decay #6 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 36841 | $0.0304 |
| stalled-expansion #6 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 34591 | $0.0313 |
| truncated-transcript #6 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 32488 | $0.0275 |
| vibe-risk #6 | Vibe risk | Sentiment mismatch | 0% | ✓ | 100% | ✓ | native | 32862 | $0.0274 |
| adoption-failure #7 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 45469 | $0.0434 |
| champion-loss #7 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 40080 | $0.0332 |
| chat-positive-crm-negative #7 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 34847 | $0.0294 |
| frustrated-not-gone #7 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 36767 | $0.0315 |
| healthy #7 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 29619 | $0.0269 |
| most-mentioned-not-buyer #7 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 40269 | $0.0328 |
| power-user-concentration #7 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 40479 | $0.0337 |
| reduced-footprint #7 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 33642 | $0.0294 |
| relationship-gap #7 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 32990 | $0.0280 |
| silent-decay #7 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 36246 | $0.0301 |
| stalled-expansion #7 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 35166 | $0.0318 |
| truncated-transcript #7 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 32692 | $0.0289 |
| vibe-risk #7 | Vibe risk | Silent decay | 0% | ✓ | 100% | ✓ | native | 34025 | $0.0286 |
| adoption-failure #8 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 39407 | $0.0408 |
| champion-loss #8 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 35984 | $0.0287 |
| chat-positive-crm-negative #8 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 44940 | $0.0344 |
| frustrated-not-gone #8 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 33749 | $0.0290 |
| healthy #8 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 32591 | $0.0272 |
| most-mentioned-not-buyer #8 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 37904 | $0.0317 |
| power-user-concentration #8 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 34589 | $0.0305 |
| reduced-footprint #8 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 32423 | $0.0288 |
| relationship-gap #8 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 37926 | $0.0317 |
| silent-decay #8 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 35289 | $0.0292 |
| stalled-expansion #8 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 36734 | $0.0323 |
| truncated-transcript #8 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 32702 | $0.0285 |
| vibe-risk #8 | Vibe risk | Sentiment mismatch | 0% | ✓ | 100% | ✓ | native | 36376 | $0.0301 |
| adoption-failure #9 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 41578 | $0.0418 |
| champion-loss #9 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 29973 | $0.0269 |
| chat-positive-crm-negative #9 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 36419 | $0.0307 |
| frustrated-not-gone #9 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 28828 | $0.0254 |
| healthy #9 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 30377 | $0.0273 |
| most-mentioned-not-buyer #9 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 38853 | $0.0318 |
| power-user-concentration #9 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 34512 | $0.0292 |
| reduced-footprint #9 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 35613 | $0.0299 |
| relationship-gap #9 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 34802 | $0.0299 |
| silent-decay #9 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 38026 | $0.0312 |
| stalled-expansion #9 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 38359 | $0.0330 |
| truncated-transcript #9 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 30611 | $0.0273 |
| vibe-risk #9 | Vibe risk | Silent decay | 0% | ✓ | 100% | ✓ | native | 36891 | $0.0288 |
| adoption-failure #10 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 42686 | $0.0425 |
| champion-loss #10 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 33978 | $0.0298 |
| chat-positive-crm-negative #10 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 35106 | $0.0301 |
| frustrated-not-gone #10 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 34863 | $0.0298 |
| healthy #10 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 27922 | $0.0255 |
| most-mentioned-not-buyer #10 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 35800 | $0.0296 |
| power-user-concentration #10 | Power user concentration | Power user concentration | 100% | ✓ | 50% (missing CSV data) | ✓ | native | 38156 | $0.0324 |
| reduced-footprint #10 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 33001 | $0.0280 |
| relationship-gap #10 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 33908 | $0.0278 |
| silent-decay #10 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 36025 | $0.0296 |
| stalled-expansion #10 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 35803 | $0.0315 |
| truncated-transcript #10 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 32259 | $0.0274 |
| vibe-risk #10 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 33532 | $0.0288 |
| adoption-failure #11 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 45169 | $0.0436 |
| champion-loss #11 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 39101 | $0.0311 |
| chat-positive-crm-negative #11 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 35461 | $0.0298 |
| frustrated-not-gone #11 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 34406 | $0.0289 |
| healthy #11 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 27516 | $0.0248 |
| most-mentioned-not-buyer #11 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 37058 | $0.0321 |
| power-user-concentration #11 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 40136 | $0.0338 |
| reduced-footprint #11 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 35542 | $0.0299 |
| relationship-gap #11 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 38490 | $0.0309 |
| silent-decay #11 | Silent decay | Silent decay | 100% | ✓ | 100% | ✓ | native | 35304 | $0.0288 |
| stalled-expansion #11 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 32902 | $0.0306 |
| truncated-transcript #11 | Reduced footprint, Adoption failure | Adoption failure | 50% | ✓ | 100% | ✓ | native | 34396 | $0.0302 |
| vibe-risk #11 | Vibe risk | Sentiment mismatch | 0% | ✓ | 100% | ✓ | native | 35418 | $0.0297 |
| adoption-failure #12 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 38684 | $0.0403 |
| champion-loss #12 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 30845 | $0.0271 |
| chat-positive-crm-negative #12 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 41199 | $0.0341 |
| frustrated-not-gone #12 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 32348 | $0.0277 |
| healthy #12 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 33542 | $0.0262 |
| most-mentioned-not-buyer #12 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 36155 | $0.0302 |
| power-user-concentration #12 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 37753 | $0.0315 |
| reduced-footprint #12 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 33601 | $0.0294 |
| relationship-gap #12 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 40689 | $0.0325 |
| silent-decay #12 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 35768 | $0.0301 |
| stalled-expansion #12 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 35902 | $0.0317 |
| truncated-transcript #12 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 29474 | $0.0257 |
| vibe-risk #12 | Vibe risk | Silent decay | 0% | ✓ | 100% | ✓ | native | 33710 | $0.0291 |
| adoption-failure #13 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 42584 | $0.0430 |
| champion-loss #13 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 35893 | $0.0295 |
| chat-positive-crm-negative #13 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 36874 | $0.0297 |
| frustrated-not-gone #13 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 34046 | $0.0291 |
| healthy #13 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 29161 | $0.0263 |
| most-mentioned-not-buyer #13 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 41107 | $0.0337 |
| power-user-concentration #13 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 36757 | $0.0317 |
| reduced-footprint #13 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 33472 | $0.0289 |
| relationship-gap #13 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 35690 | $0.0310 |
| silent-decay #13 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 39209 | $0.0316 |
| stalled-expansion #13 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 35976 | $0.0319 |
| truncated-transcript #13 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 30163 | $0.0271 |
| vibe-risk #13 | Vibe risk | Silent decay | 0% | ✓ | 100% | ✓ | native | 32305 | $0.0281 |
| adoption-failure #14 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 42562 | $0.0422 |
| champion-loss #14 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 32252 | $0.0281 |
| chat-positive-crm-negative #14 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 36187 | $0.0312 |
| frustrated-not-gone #14 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 33234 | $0.0293 |
| healthy #14 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 28193 | $0.0260 |
| most-mentioned-not-buyer #14 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 39971 | $0.0327 |
| power-user-concentration #14 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 40256 | $0.0337 |
| reduced-footprint #14 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 30464 | $0.0274 |
| relationship-gap #14 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 34956 | $0.0294 |
| silent-decay #14 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 39250 | $0.0319 |
| stalled-expansion #14 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 38219 | $0.0326 |
| truncated-transcript #14 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 30028 | $0.0264 |
| vibe-risk #14 | Vibe risk | Sentiment mismatch | 0% | ✓ | 100% | ✓ | native | 31749 | $0.0271 |
| adoption-failure #15 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 43426 | $0.0426 |
| champion-loss #15 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 38783 | $0.0319 |
| chat-positive-crm-negative #15 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 35331 | $0.0302 |
| frustrated-not-gone #15 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 35063 | $0.0297 |
| healthy #15 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 28122 | $0.0256 |
| most-mentioned-not-buyer #15 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 35178 | $0.0299 |
| power-user-concentration #15 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 37454 | $0.0321 |
| reduced-footprint #15 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 36003 | $0.0305 |
| relationship-gap #15 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 38302 | $0.0303 |
| silent-decay #15 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 36929 | $0.0311 |
| stalled-expansion #15 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 36039 | $0.0326 |
| truncated-transcript #15 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 34973 | $0.0295 |
| vibe-risk #15 | Vibe risk | Silent decay | 0% | ✓ | 100% | ✓ | native | 34826 | $0.0291 |
| adoption-failure #16 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 40861 | $0.0411 |
| champion-loss #16 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 39477 | $0.0306 |
| chat-positive-crm-negative #16 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 34225 | $0.0296 |
| frustrated-not-gone #16 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 35882 | $0.0302 |
| healthy #16 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 29424 | $0.0258 |
| most-mentioned-not-buyer #16 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 42451 | $0.0331 |
| power-user-concentration #16 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 40382 | $0.0333 |
| reduced-footprint #16 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 35498 | $0.0297 |
| relationship-gap #16 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 36039 | $0.0304 |
| silent-decay #16 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 36427 | $0.0302 |
| stalled-expansion #16 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 34252 | $0.0315 |
| truncated-transcript #16 | Reduced footprint, Adoption failure | Adoption failure | 50% | ✓ | 100% | ✓ | native | 32323 | $0.0279 |
| vibe-risk #16 | Vibe risk | Silent decay | 0% | ✓ | 100% | ✓ | native | 36058 | $0.0296 |
| adoption-failure #17 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 39566 | $0.0405 |
| champion-loss #17 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 33876 | $0.0295 |
| chat-positive-crm-negative #17 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 36469 | $0.0302 |
| frustrated-not-gone #17 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 33845 | $0.0293 |
| healthy #17 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 29280 | $0.0259 |
| most-mentioned-not-buyer #17 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 35751 | $0.0300 |
| power-user-concentration #17 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 44244 | $0.0369 |
| reduced-footprint #17 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 30014 | $0.0278 |
| relationship-gap #17 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 37577 | $0.0307 |
| silent-decay #17 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 33372 | $0.0287 |
| stalled-expansion #17 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 34051 | $0.0312 |
| truncated-transcript #17 | Reduced footprint, Adoption failure | Adoption failure | 50% | ✓ | 100% | ✓ | native | 29612 | $0.0271 |
| vibe-risk #17 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 34737 | $0.0295 |
| adoption-failure #18 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 44474 | $0.0439 |
| champion-loss #18 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 34508 | $0.0294 |
| chat-positive-crm-negative #18 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 37272 | $0.0319 |
| frustrated-not-gone #18 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 34005 | $0.0293 |
| healthy #18 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 30055 | $0.0267 |
| most-mentioned-not-buyer #18 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 36618 | $0.0315 |
| power-user-concentration #18 | Power user concentration | Power user concentration | 100% | ✓ | 50% (missing CSV data) | ✓ | native | 40465 | $0.0348 |
| reduced-footprint #18 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 31735 | $0.0284 |
| relationship-gap #18 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 40050 | $0.0326 |
| silent-decay #18 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 36053 | $0.0294 |
| stalled-expansion #18 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 37163 | $0.0327 |
| truncated-transcript #18 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 31390 | $0.0280 |
| vibe-risk #18 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 32087 | $0.0277 |
| adoption-failure #19 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 44376 | $0.0438 |
| champion-loss #19 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 35281 | $0.0296 |
| chat-positive-crm-negative #19 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 40447 | $0.0313 |
| frustrated-not-gone #19 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 35838 | $0.0298 |
| healthy #19 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 29509 | $0.0257 |
| most-mentioned-not-buyer #19 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 36100 | $0.0306 |
| power-user-concentration #19 | Power user concentration | Power user concentration | 100% | ✓ | 50% (missing CSV data) | ✓ | native | 38860 | $0.0334 |
| reduced-footprint #19 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 35526 | $0.0294 |
| relationship-gap #19 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 34102 | $0.0293 |
| silent-decay #19 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 35788 | $0.0303 |
| stalled-expansion #19 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 34307 | $0.0317 |
| truncated-transcript #19 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 37694 | $0.0311 |
| vibe-risk #19 | Vibe risk | Sentiment mismatch | 0% | ✓ | 100% | ✓ | native | 37936 | $0.0308 |
| adoption-failure #20 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 42454 | $0.0422 |
| champion-loss #20 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 37527 | $0.0314 |
| chat-positive-crm-negative #20 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 41774 | $0.0342 |
| frustrated-not-gone #20 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 33328 | $0.0285 |
| healthy #20 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 28890 | $0.0259 |
| most-mentioned-not-buyer #20 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 37073 | $0.0291 |
| power-user-concentration #20 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 35253 | $0.0307 |
| reduced-footprint #20 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 32550 | $0.0291 |
| relationship-gap #20 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 35829 | $0.0303 |
| silent-decay #20 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 36236 | $0.0302 |
| stalled-expansion #20 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 35649 | $0.0318 |
| truncated-transcript #20 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 29910 | $0.0272 |
| vibe-risk #20 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 35415 | $0.0295 |
