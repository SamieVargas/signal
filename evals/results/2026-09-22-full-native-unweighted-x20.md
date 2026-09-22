# Signal eval — 2026-09-22 · mode `full` · contract `native` · arm `unweighted` · 20 run(s) per case

| Metric | Value |
| --- | --- |
| Cases × runs | 260 |
| Risk-type recall (primary) | 90% |
| Risk-type precision | 93% |
| Economic-buyer accuracy | 69% |
| Attribution coverage | 95% |
| Data gaps present when expected | 100% |
| Parse: native / recovered / failed | 260 / 0 / 0 |
| Mean tokens in / out (analysis call) | 2,815 / 1,387 |
| Mean analysis latency | 34,479 ms |
| Hard fails | 0 |

| Case | Expected risk | Predicted | Recall | Buyer | Attribution | Gaps | Parse | ms |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| adoption-failure #1 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 41656 |
| champion-loss #1 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 35791 |
| chat-positive-crm-negative #1 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 35583 |
| frustrated-not-gone #1 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 32272 |
| healthy #1 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 26927 |
| most-mentioned-not-buyer #1 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 37053 |
| power-user-concentration #1 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 39783 |
| reduced-footprint #1 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 34279 |
| relationship-gap #1 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 30058 |
| silent-decay #1 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 33097 |
| stalled-expansion #1 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 35717 |
| truncated-transcript #1 | Reduced footprint, Adoption failure | Adoption failure | 50% | ✓ | 100% | ✓ | native | 28675 |
| vibe-risk #1 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 31549 |
| adoption-failure #2 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 41906 |
| champion-loss #2 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 33513 |
| chat-positive-crm-negative #2 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 38894 |
| frustrated-not-gone #2 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 33390 |
| healthy #2 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 28357 |
| most-mentioned-not-buyer #2 | Relationship gap | Sentiment mismatch | 0% | ✗ | 100% | ✓ | native | 37488 |
| power-user-concentration #2 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 40772 |
| reduced-footprint #2 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 33141 |
| relationship-gap #2 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 34485 |
| silent-decay #2 | Silent decay | Silent decay | 100% | ✓ | 100% | ✓ | native | 34808 |
| stalled-expansion #2 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 35498 |
| truncated-transcript #2 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 29929 |
| vibe-risk #2 | Vibe risk | Silent decay | 0% | ✓ | 100% | ✓ | native | 34593 |
| adoption-failure #3 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 40986 |
| champion-loss #3 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 37885 |
| chat-positive-crm-negative #3 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 39336 |
| frustrated-not-gone #3 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 30197 |
| healthy #3 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 31568 |
| most-mentioned-not-buyer #3 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 36372 |
| power-user-concentration #3 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 38572 |
| reduced-footprint #3 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 30181 |
| relationship-gap #3 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 36909 |
| silent-decay #3 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 35124 |
| stalled-expansion #3 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 36787 |
| truncated-transcript #3 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 28250 |
| vibe-risk #3 | Vibe risk | Sentiment mismatch | 0% | ✓ | 100% | ✓ | native | 33690 |
| adoption-failure #4 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 40295 |
| champion-loss #4 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 36935 |
| chat-positive-crm-negative #4 | Sentiment mismatch | Relationship gap | 0% | ✓ | 100% | ✓ | native | 37581 |
| frustrated-not-gone #4 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 35881 |
| healthy #4 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 27363 |
| most-mentioned-not-buyer #4 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 40430 |
| power-user-concentration #4 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 38551 |
| reduced-footprint #4 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 32807 |
| relationship-gap #4 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 32754 |
| silent-decay #4 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 44076 |
| stalled-expansion #4 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 32803 |
| truncated-transcript #4 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 27257 |
| vibe-risk #4 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 33817 |
| adoption-failure #5 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 39584 |
| champion-loss #5 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 36277 |
| chat-positive-crm-negative #5 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 39752 |
| frustrated-not-gone #5 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 33505 |
| healthy #5 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 29070 |
| most-mentioned-not-buyer #5 | Relationship gap | Sentiment mismatch | 0% | ✗ | 100% | ✓ | native | 37968 |
| power-user-concentration #5 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 35721 |
| reduced-footprint #5 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 31469 |
| relationship-gap #5 | Relationship gap | Power user concentration | 0% | ✗ | 100% | ✓ | native | 37351 |
| silent-decay #5 | Silent decay | Silent decay | 100% | ✓ | 100% | ✓ | native | 32041 |
| stalled-expansion #5 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 33863 |
| truncated-transcript #5 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 30024 |
| vibe-risk #5 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 35450 |
| adoption-failure #6 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 40752 |
| champion-loss #6 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 35158 |
| chat-positive-crm-negative #6 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 38095 |
| frustrated-not-gone #6 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 38039 |
| healthy #6 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 26994 |
| most-mentioned-not-buyer #6 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 37385 |
| power-user-concentration #6 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 34460 |
| reduced-footprint #6 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 31939 |
| relationship-gap #6 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 30074 |
| silent-decay #6 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 37180 |
| stalled-expansion #6 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 33196 |
| truncated-transcript #6 | Reduced footprint, Adoption failure | Adoption failure | 50% | ✓ | 100% | ✓ | native | 30318 |
| vibe-risk #6 | Vibe risk | Sentiment mismatch | 0% | ✓ | 100% | ✓ | native | 35363 |
| adoption-failure #7 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 39253 |
| champion-loss #7 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 36079 |
| chat-positive-crm-negative #7 | Sentiment mismatch | Relationship gap | 0% | ✓ | 100% | ✓ | native | 33990 |
| frustrated-not-gone #7 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 33732 |
| healthy #7 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 27162 |
| most-mentioned-not-buyer #7 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 33610 |
| power-user-concentration #7 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 37355 |
| reduced-footprint #7 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 32492 |
| relationship-gap #7 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 33165 |
| silent-decay #7 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 39110 |
| stalled-expansion #7 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 32963 |
| truncated-transcript #7 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 31840 |
| vibe-risk #7 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 31638 |
| adoption-failure #8 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 42330 |
| champion-loss #8 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 35154 |
| chat-positive-crm-negative #8 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 37783 |
| frustrated-not-gone #8 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 33744 |
| healthy #8 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 27196 |
| most-mentioned-not-buyer #8 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 33883 |
| power-user-concentration #8 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 38034 |
| reduced-footprint #8 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 31389 |
| relationship-gap #8 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 35169 |
| silent-decay #8 | Silent decay | Silent decay | 100% | ✓ | 100% | ✓ | native | 31956 |
| stalled-expansion #8 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 34547 |
| truncated-transcript #8 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 28556 |
| vibe-risk #8 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 30425 |
| adoption-failure #9 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 44063 |
| champion-loss #9 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 28993 |
| chat-positive-crm-negative #9 | Sentiment mismatch | Relationship gap | 0% | ✓ | 100% | ✓ | native | 40446 |
| frustrated-not-gone #9 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 30255 |
| healthy #9 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 26132 |
| most-mentioned-not-buyer #9 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 39898 |
| power-user-concentration #9 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 33936 |
| reduced-footprint #9 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 33703 |
| relationship-gap #9 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 28205 |
| silent-decay #9 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 31846 |
| stalled-expansion #9 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 37169 |
| truncated-transcript #9 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 30263 |
| vibe-risk #9 | Vibe risk | Silent decay | 0% | ✓ | 100% | ✓ | native | 35772 |
| adoption-failure #10 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 38358 |
| champion-loss #10 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 33538 |
| chat-positive-crm-negative #10 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 34461 |
| frustrated-not-gone #10 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 30324 |
| healthy #10 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 24870 |
| most-mentioned-not-buyer #10 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 33504 |
| power-user-concentration #10 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 37784 |
| reduced-footprint #10 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 38267 |
| relationship-gap #10 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 32730 |
| silent-decay #10 | Silent decay | Silent decay | 100% | ✓ | 100% | ✓ | native | 31559 |
| stalled-expansion #10 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 40055 |
| truncated-transcript #10 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 26543 |
| vibe-risk #10 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 35965 |
| adoption-failure #11 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 41525 |
| champion-loss #11 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 32229 |
| chat-positive-crm-negative #11 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 32484 |
| frustrated-not-gone #11 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 34872 |
| healthy #11 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 26430 |
| most-mentioned-not-buyer #11 | Relationship gap | Sentiment mismatch | 0% | ✗ | 100% | ✓ | native | 33239 |
| power-user-concentration #11 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 34135 |
| reduced-footprint #11 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 27688 |
| relationship-gap #11 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 34721 |
| silent-decay #11 | Silent decay | Silent decay | 100% | ✓ | 100% | ✓ | native | 30615 |
| stalled-expansion #11 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 37634 |
| truncated-transcript #11 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 28418 |
| vibe-risk #11 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 37137 |
| adoption-failure #12 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 37290 |
| champion-loss #12 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 32082 |
| chat-positive-crm-negative #12 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 33296 |
| frustrated-not-gone #12 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 32657 |
| healthy #12 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 28849 |
| most-mentioned-not-buyer #12 | Relationship gap | Sentiment mismatch | 0% | ✗ | 100% | ✓ | native | 34367 |
| power-user-concentration #12 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 33539 |
| reduced-footprint #12 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 34174 |
| relationship-gap #12 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 31392 |
| silent-decay #12 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 34675 |
| stalled-expansion #12 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 41860 |
| truncated-transcript #12 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 29121 |
| vibe-risk #12 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 30996 |
| adoption-failure #13 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 42957 |
| champion-loss #13 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 30631 |
| chat-positive-crm-negative #13 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 36185 |
| frustrated-not-gone #13 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 35188 |
| healthy #13 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 24417 |
| most-mentioned-not-buyer #13 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 35100 |
| power-user-concentration #13 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 36850 |
| reduced-footprint #13 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 35780 |
| relationship-gap #13 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 37746 |
| silent-decay #13 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 39990 |
| stalled-expansion #13 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 33466 |
| truncated-transcript #13 | Reduced footprint, Adoption failure | Adoption failure | 50% | ✓ | 100% | ✓ | native | 34809 |
| vibe-risk #13 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 33350 |
| adoption-failure #14 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 43476 |
| champion-loss #14 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 35568 |
| chat-positive-crm-negative #14 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 33128 |
| frustrated-not-gone #14 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 34459 |
| healthy #14 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 28497 |
| most-mentioned-not-buyer #14 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 31690 |
| power-user-concentration #14 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 36985 |
| reduced-footprint #14 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 34204 |
| relationship-gap #14 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 35435 |
| silent-decay #14 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 31509 |
| stalled-expansion #14 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 39212 |
| truncated-transcript #14 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 33295 |
| vibe-risk #14 | Vibe risk | Sentiment mismatch | 0% | ✓ | 100% | ✓ | native | 29831 |
| adoption-failure #15 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 42367 |
| champion-loss #15 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 34685 |
| chat-positive-crm-negative #15 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 37080 |
| frustrated-not-gone #15 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 28637 |
| healthy #15 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 25688 |
| most-mentioned-not-buyer #15 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 35122 |
| power-user-concentration #15 | Power user concentration | Power user concentration | 100% | ✓ | 50% (missing CSV data) | ✓ | native | 37295 |
| reduced-footprint #15 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 31932 |
| relationship-gap #15 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 31451 |
| silent-decay #15 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 37199 |
| stalled-expansion #15 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 32457 |
| truncated-transcript #15 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 32230 |
| vibe-risk #15 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 34681 |
| adoption-failure #16 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 40481 |
| champion-loss #16 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 30658 |
| chat-positive-crm-negative #16 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 37730 |
| frustrated-not-gone #16 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 35727 |
| healthy #16 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 27960 |
| most-mentioned-not-buyer #16 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 36341 |
| power-user-concentration #16 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 36449 |
| reduced-footprint #16 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 32883 |
| relationship-gap #16 | Relationship gap | Champion loss | 0% | ✗ | 100% | ✓ | native | 34919 |
| silent-decay #16 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 35162 |
| stalled-expansion #16 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 41924 |
| truncated-transcript #16 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 30537 |
| vibe-risk #16 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 37452 |
| adoption-failure #17 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 44222 |
| champion-loss #17 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 39553 |
| chat-positive-crm-negative #17 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 37638 |
| frustrated-not-gone #17 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 33226 |
| healthy #17 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 25490 |
| most-mentioned-not-buyer #17 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 36936 |
| power-user-concentration #17 | Power user concentration | Power user concentration | 100% | ✓ | 50% (missing CSV data) | ✓ | native | 40966 |
| reduced-footprint #17 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 32668 |
| relationship-gap #17 | Relationship gap | Power user concentration | 0% | ✗ | 100% | ✓ | native | 29886 |
| silent-decay #17 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 38699 |
| stalled-expansion #17 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 33147 |
| truncated-transcript #17 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 32838 |
| vibe-risk #17 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 33291 |
| adoption-failure #18 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 43403 |
| champion-loss #18 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 35263 |
| chat-positive-crm-negative #18 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 35176 |
| frustrated-not-gone #18 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 32383 |
| healthy #18 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 32045 |
| most-mentioned-not-buyer #18 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 39403 |
| power-user-concentration #18 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 35795 |
| reduced-footprint #18 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 30931 |
| relationship-gap #18 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 32454 |
| silent-decay #18 | Silent decay | Silent decay | 100% | ✓ | 100% | ✓ | native | 36755 |
| stalled-expansion #18 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 33936 |
| truncated-transcript #18 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 28870 |
| vibe-risk #18 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 31951 |
| adoption-failure #19 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 41448 |
| champion-loss #19 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 30350 |
| chat-positive-crm-negative #19 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 34704 |
| frustrated-not-gone #19 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 39012 |
| healthy #19 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 27609 |
| most-mentioned-not-buyer #19 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 39019 |
| power-user-concentration #19 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 35536 |
| reduced-footprint #19 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 31902 |
| relationship-gap #19 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 33290 |
| silent-decay #19 | Silent decay | Silent decay | 100% | ✓ | 100% | ✓ | native | 35751 |
| stalled-expansion #19 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 41866 |
| truncated-transcript #19 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 33169 |
| vibe-risk #19 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 33773 |
| adoption-failure #20 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 40414 |
| champion-loss #20 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 34241 |
| chat-positive-crm-negative #20 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 37257 |
| frustrated-not-gone #20 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 34596 |
| healthy #20 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 28913 |
| most-mentioned-not-buyer #20 | Relationship gap | Power user concentration | 0% | ✗ | 100% | ✓ | native | 32651 |
| power-user-concentration #20 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 43975 |
| reduced-footprint #20 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 36260 |
| relationship-gap #20 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 35991 |
| silent-decay #20 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 33378 |
| stalled-expansion #20 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 36897 |
| truncated-transcript #20 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 28408 |
| vibe-risk #20 | Vibe risk | Silent decay | 0% | ✓ | 100% | ✓ | native | 31068 |
