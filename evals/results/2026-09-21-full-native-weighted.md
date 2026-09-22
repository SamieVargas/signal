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
| Hard fails | 0 |

| Case | Expected risk | Predicted | Recall | Buyer | Attribution | Gaps | Parse | ms |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| adoption-failure #1 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 42239 |
| champion-loss #1 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 36740 |
| chat-positive-crm-negative #1 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 37007 |
| frustrated-not-gone #1 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 37445 |
| healthy #1 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 30310 |
| most-mentioned-not-buyer #1 | Relationship gap | Power user concentration | 0% | ✓ | 100% | ✓ | native | 37185 |
| power-user-concentration #1 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 38432 |
| reduced-footprint #1 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 31242 |
| relationship-gap #1 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 31418 |
| silent-decay #1 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 41338 |
| stalled-expansion #1 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 33931 |
| truncated-transcript #1 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 29041 |
| vibe-risk #1 | Vibe risk | Sentiment mismatch | 0% | ✓ | 100% | ✓ | native | 37551 |
| adoption-failure #2 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 43242 |
| champion-loss #2 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 39922 |
| chat-positive-crm-negative #2 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 46555 |
| frustrated-not-gone #2 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 31750 |
| healthy #2 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 36218 |
| most-mentioned-not-buyer #2 | Relationship gap | Sentiment mismatch | 0% | ✓ | 100% | ✓ | native | 30652 |
| power-user-concentration #2 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 37224 |
| reduced-footprint #2 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 32054 |
| relationship-gap #2 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 34246 |
| silent-decay #2 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 32949 |
| stalled-expansion #2 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 33402 |
| truncated-transcript #2 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 32575 |
| vibe-risk #2 | Vibe risk | Silent decay | 0% | ✓ | 100% | ✓ | native | 38603 |
| adoption-failure #3 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 42894 |
| champion-loss #3 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 32796 |
| chat-positive-crm-negative #3 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 34982 |
| frustrated-not-gone #3 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 37885 |
| healthy #3 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 26379 |
| most-mentioned-not-buyer #3 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 36969 |
| power-user-concentration #3 | Power user concentration | Power user concentration | 100% | ✓ | 50% (missing CSV data) | ✓ | native | 39927 |
| reduced-footprint #3 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 31262 |
| relationship-gap #3 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 46878 |
| silent-decay #3 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 38515 |
| stalled-expansion #3 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 33948 |
| truncated-transcript #3 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 31791 |
| vibe-risk #3 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 38508 |
| adoption-failure #4 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 43007 |
| champion-loss #4 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 31025 |
| chat-positive-crm-negative #4 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 33986 |
| frustrated-not-gone #4 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 34630 |
| healthy #4 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 28909 |
| most-mentioned-not-buyer #4 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 37745 |
| power-user-concentration #4 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 45669 |
| reduced-footprint #4 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 33960 |
| relationship-gap #4 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 35807 |
| silent-decay #4 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 42984 |
| stalled-expansion #4 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 38138 |
| truncated-transcript #4 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 40049 |
| vibe-risk #4 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 37759 |
| adoption-failure #5 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 46061 |
| champion-loss #5 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 36624 |
| chat-positive-crm-negative #5 | Sentiment mismatch | Relationship gap | 0% | ✓ | 100% | ✓ | native | 37010 |
| frustrated-not-gone #5 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 36346 |
| healthy #5 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 28575 |
| most-mentioned-not-buyer #5 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 40701 |
| power-user-concentration #5 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 51930 |
| reduced-footprint #5 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 37945 |
| relationship-gap #5 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 33119 |
| silent-decay #5 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 31699 |
| stalled-expansion #5 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 36082 |
| truncated-transcript #5 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 36428 |
| vibe-risk #5 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 33037 |
| adoption-failure #6 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 42158 |
| champion-loss #6 | Champion loss | Champion loss | 100% | ✓ | 100% | ✓ | native | 42343 |
| chat-positive-crm-negative #6 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 39800 |
| frustrated-not-gone #6 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 36258 |
| healthy #6 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 27075 |
| most-mentioned-not-buyer #6 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 35634 |
| power-user-concentration #6 | Power user concentration | Power user concentration | 100% | ✓ | 50% (missing CSV data) | ✓ | native | 38574 |
| reduced-footprint #6 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 31161 |
| relationship-gap #6 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 32862 |
| silent-decay #6 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 36841 |
| stalled-expansion #6 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 34591 |
| truncated-transcript #6 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 32488 |
| vibe-risk #6 | Vibe risk | Sentiment mismatch | 0% | ✓ | 100% | ✓ | native | 32862 |
| adoption-failure #7 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 45469 |
| champion-loss #7 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 40080 |
| chat-positive-crm-negative #7 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 34847 |
| frustrated-not-gone #7 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 36767 |
| healthy #7 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 29619 |
| most-mentioned-not-buyer #7 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 40269 |
| power-user-concentration #7 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 40479 |
| reduced-footprint #7 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 33642 |
| relationship-gap #7 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 32990 |
| silent-decay #7 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 36246 |
| stalled-expansion #7 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 35166 |
| truncated-transcript #7 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 32692 |
| vibe-risk #7 | Vibe risk | Silent decay | 0% | ✓ | 100% | ✓ | native | 34025 |
| adoption-failure #8 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 39407 |
| champion-loss #8 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 35984 |
| chat-positive-crm-negative #8 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 44940 |
| frustrated-not-gone #8 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 33749 |
| healthy #8 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 32591 |
| most-mentioned-not-buyer #8 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 37904 |
| power-user-concentration #8 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 34589 |
| reduced-footprint #8 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 32423 |
| relationship-gap #8 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 37926 |
| silent-decay #8 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 35289 |
| stalled-expansion #8 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 36734 |
| truncated-transcript #8 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 32702 |
| vibe-risk #8 | Vibe risk | Sentiment mismatch | 0% | ✓ | 100% | ✓ | native | 36376 |
| adoption-failure #9 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 41578 |
| champion-loss #9 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 29973 |
| chat-positive-crm-negative #9 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 36419 |
| frustrated-not-gone #9 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 28828 |
| healthy #9 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 30377 |
| most-mentioned-not-buyer #9 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 38853 |
| power-user-concentration #9 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 34512 |
| reduced-footprint #9 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 35613 |
| relationship-gap #9 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 34802 |
| silent-decay #9 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 38026 |
| stalled-expansion #9 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 38359 |
| truncated-transcript #9 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 30611 |
| vibe-risk #9 | Vibe risk | Silent decay | 0% | ✓ | 100% | ✓ | native | 36891 |
| adoption-failure #10 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 42686 |
| champion-loss #10 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 33978 |
| chat-positive-crm-negative #10 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 35106 |
| frustrated-not-gone #10 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 34863 |
| healthy #10 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 27922 |
| most-mentioned-not-buyer #10 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 35800 |
| power-user-concentration #10 | Power user concentration | Power user concentration | 100% | ✓ | 50% (missing CSV data) | ✓ | native | 38156 |
| reduced-footprint #10 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 33001 |
| relationship-gap #10 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 33908 |
| silent-decay #10 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 36025 |
| stalled-expansion #10 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 35803 |
| truncated-transcript #10 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 32259 |
| vibe-risk #10 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 33532 |
| adoption-failure #11 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 45169 |
| champion-loss #11 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 39101 |
| chat-positive-crm-negative #11 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 35461 |
| frustrated-not-gone #11 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 34406 |
| healthy #11 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 27516 |
| most-mentioned-not-buyer #11 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 37058 |
| power-user-concentration #11 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 40136 |
| reduced-footprint #11 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 35542 |
| relationship-gap #11 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 38490 |
| silent-decay #11 | Silent decay | Silent decay | 100% | ✓ | 100% | ✓ | native | 35304 |
| stalled-expansion #11 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 32902 |
| truncated-transcript #11 | Reduced footprint, Adoption failure | Adoption failure | 50% | ✓ | 100% | ✓ | native | 34396 |
| vibe-risk #11 | Vibe risk | Sentiment mismatch | 0% | ✓ | 100% | ✓ | native | 35418 |
| adoption-failure #12 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 38684 |
| champion-loss #12 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 30845 |
| chat-positive-crm-negative #12 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 41199 |
| frustrated-not-gone #12 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 32348 |
| healthy #12 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 33542 |
| most-mentioned-not-buyer #12 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 36155 |
| power-user-concentration #12 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 37753 |
| reduced-footprint #12 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 33601 |
| relationship-gap #12 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 40689 |
| silent-decay #12 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 35768 |
| stalled-expansion #12 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 35902 |
| truncated-transcript #12 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 29474 |
| vibe-risk #12 | Vibe risk | Silent decay | 0% | ✓ | 100% | ✓ | native | 33710 |
| adoption-failure #13 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 42584 |
| champion-loss #13 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 35893 |
| chat-positive-crm-negative #13 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 36874 |
| frustrated-not-gone #13 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 34046 |
| healthy #13 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 29161 |
| most-mentioned-not-buyer #13 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 41107 |
| power-user-concentration #13 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 36757 |
| reduced-footprint #13 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 33472 |
| relationship-gap #13 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 35690 |
| silent-decay #13 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 39209 |
| stalled-expansion #13 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 35976 |
| truncated-transcript #13 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 30163 |
| vibe-risk #13 | Vibe risk | Silent decay | 0% | ✓ | 100% | ✓ | native | 32305 |
| adoption-failure #14 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 42562 |
| champion-loss #14 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 32252 |
| chat-positive-crm-negative #14 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 36187 |
| frustrated-not-gone #14 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 33234 |
| healthy #14 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 28193 |
| most-mentioned-not-buyer #14 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 39971 |
| power-user-concentration #14 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 40256 |
| reduced-footprint #14 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 30464 |
| relationship-gap #14 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 34956 |
| silent-decay #14 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 39250 |
| stalled-expansion #14 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 38219 |
| truncated-transcript #14 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 30028 |
| vibe-risk #14 | Vibe risk | Sentiment mismatch | 0% | ✓ | 100% | ✓ | native | 31749 |
| adoption-failure #15 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 43426 |
| champion-loss #15 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 38783 |
| chat-positive-crm-negative #15 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 35331 |
| frustrated-not-gone #15 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 35063 |
| healthy #15 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 28122 |
| most-mentioned-not-buyer #15 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 35178 |
| power-user-concentration #15 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 37454 |
| reduced-footprint #15 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 36003 |
| relationship-gap #15 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 38302 |
| silent-decay #15 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 36929 |
| stalled-expansion #15 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 36039 |
| truncated-transcript #15 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 34973 |
| vibe-risk #15 | Vibe risk | Silent decay | 0% | ✓ | 100% | ✓ | native | 34826 |
| adoption-failure #16 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 40861 |
| champion-loss #16 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 39477 |
| chat-positive-crm-negative #16 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 34225 |
| frustrated-not-gone #16 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 35882 |
| healthy #16 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 29424 |
| most-mentioned-not-buyer #16 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 42451 |
| power-user-concentration #16 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 40382 |
| reduced-footprint #16 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 35498 |
| relationship-gap #16 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 36039 |
| silent-decay #16 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 36427 |
| stalled-expansion #16 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 34252 |
| truncated-transcript #16 | Reduced footprint, Adoption failure | Adoption failure | 50% | ✓ | 100% | ✓ | native | 32323 |
| vibe-risk #16 | Vibe risk | Silent decay | 0% | ✓ | 100% | ✓ | native | 36058 |
| adoption-failure #17 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 39566 |
| champion-loss #17 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 33876 |
| chat-positive-crm-negative #17 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 36469 |
| frustrated-not-gone #17 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 33845 |
| healthy #17 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 29280 |
| most-mentioned-not-buyer #17 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 35751 |
| power-user-concentration #17 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 44244 |
| reduced-footprint #17 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 30014 |
| relationship-gap #17 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 37577 |
| silent-decay #17 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 33372 |
| stalled-expansion #17 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 34051 |
| truncated-transcript #17 | Reduced footprint, Adoption failure | Adoption failure | 50% | ✓ | 100% | ✓ | native | 29612 |
| vibe-risk #17 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 34737 |
| adoption-failure #18 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 44474 |
| champion-loss #18 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 34508 |
| chat-positive-crm-negative #18 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 37272 |
| frustrated-not-gone #18 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 34005 |
| healthy #18 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 30055 |
| most-mentioned-not-buyer #18 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 36618 |
| power-user-concentration #18 | Power user concentration | Power user concentration | 100% | ✓ | 50% (missing CSV data) | ✓ | native | 40465 |
| reduced-footprint #18 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 31735 |
| relationship-gap #18 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 40050 |
| silent-decay #18 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 36053 |
| stalled-expansion #18 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 37163 |
| truncated-transcript #18 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 31390 |
| vibe-risk #18 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 32087 |
| adoption-failure #19 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 44376 |
| champion-loss #19 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 35281 |
| chat-positive-crm-negative #19 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 40447 |
| frustrated-not-gone #19 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 35838 |
| healthy #19 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 29509 |
| most-mentioned-not-buyer #19 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 36100 |
| power-user-concentration #19 | Power user concentration | Power user concentration | 100% | ✓ | 50% (missing CSV data) | ✓ | native | 38860 |
| reduced-footprint #19 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 35526 |
| relationship-gap #19 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 34102 |
| silent-decay #19 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 35788 |
| stalled-expansion #19 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 34307 |
| truncated-transcript #19 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 37694 |
| vibe-risk #19 | Vibe risk | Sentiment mismatch | 0% | ✓ | 100% | ✓ | native | 37936 |
| adoption-failure #20 | Adoption failure | Adoption failure | 100% | ✓ | 100% | ✓ | native | 42454 |
| champion-loss #20 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 37527 |
| chat-positive-crm-negative #20 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 41774 |
| frustrated-not-gone #20 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 33328 |
| healthy #20 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 28890 |
| most-mentioned-not-buyer #20 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 37073 |
| power-user-concentration #20 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 35253 |
| reduced-footprint #20 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 32550 |
| relationship-gap #20 | Relationship gap | Relationship gap | 100% | ✓ | 100% | ✓ | native | 35829 |
| silent-decay #20 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 36236 |
| stalled-expansion #20 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 35649 |
| truncated-transcript #20 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 29910 |
| vibe-risk #20 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 35415 |
