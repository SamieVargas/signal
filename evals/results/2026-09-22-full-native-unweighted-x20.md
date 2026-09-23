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
| Cost per run (analysis call, USD) | $0.0292 |
| Cost for the whole run (analysis calls, USD) | $7.6039 |
| Prices | list, read 2026-09-23 |
| Hard fails | 0 |

| Case | Expected risk | Predicted | Recall | Buyer | Attribution | Gaps | Parse | ms | Cost |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| adoption-failure #1 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 41656 | $0.0411 |
| champion-loss #1 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 35791 | $0.0276 |
| chat-positive-crm-negative #1 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 35583 | $0.0279 |
| frustrated-not-gone #1 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 32272 | $0.0274 |
| healthy #1 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 26927 | $0.0244 |
| most-mentioned-not-buyer #1 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 37053 | $0.0306 |
| power-user-concentration #1 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 39783 | $0.0314 |
| reduced-footprint #1 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 34279 | $0.0292 |
| relationship-gap #1 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 30058 | $0.0260 |
| silent-decay #1 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 33097 | $0.0282 |
| stalled-expansion #1 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 35717 | $0.0308 |
| truncated-transcript #1 | Reduced footprint, Adoption failure | Adoption failure | 50% | ✓ | 100% | ✓ | native | 28675 | $0.0263 |
| vibe-risk #1 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 31549 | $0.0265 |
| adoption-failure #2 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 41906 | $0.0411 |
| champion-loss #2 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 33513 | $0.0280 |
| chat-positive-crm-negative #2 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 38894 | $0.0303 |
| frustrated-not-gone #2 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 33390 | $0.0275 |
| healthy #2 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 28357 | $0.0235 |
| most-mentioned-not-buyer #2 | Relationship gap | Sentiment mismatch | 0% | ✗ | 100% | ✓ | native | 37488 | $0.0300 |
| power-user-concentration #2 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 40772 | $0.0329 |
| reduced-footprint #2 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 33141 | $0.0275 |
| relationship-gap #2 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 34485 | $0.0282 |
| silent-decay #2 | Silent decay | Silent decay | 100% | ✓ | 100% | ✓ | native | 34808 | $0.0281 |
| stalled-expansion #2 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 35498 | $0.0313 |
| truncated-transcript #2 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 29929 | $0.0258 |
| vibe-risk #2 | Vibe risk | Silent decay | 0% | ✓ | 100% | ✓ | native | 34593 | $0.0280 |
| adoption-failure #3 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 40986 | $0.0416 |
| champion-loss #3 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 37885 | $0.0312 |
| chat-positive-crm-negative #3 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 39336 | $0.0317 |
| frustrated-not-gone #3 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 30197 | $0.0256 |
| healthy #3 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 31568 | $0.0250 |
| most-mentioned-not-buyer #3 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 36372 | $0.0278 |
| power-user-concentration #3 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 38572 | $0.0321 |
| reduced-footprint #3 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 30181 | $0.0264 |
| relationship-gap #3 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 36909 | $0.0295 |
| silent-decay #3 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 35124 | $0.0293 |
| stalled-expansion #3 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 36787 | $0.0321 |
| truncated-transcript #3 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 28250 | $0.0243 |
| vibe-risk #3 | Vibe risk | Sentiment mismatch | 0% | ✓ | 100% | ✓ | native | 33690 | $0.0277 |
| adoption-failure #4 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 40295 | $0.0406 |
| champion-loss #4 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 36935 | $0.0288 |
| chat-positive-crm-negative #4 | Sentiment mismatch | Relationship gap | 0% | ✓ | 100% | ✓ | native | 37581 | $0.0315 |
| frustrated-not-gone #4 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 35881 | $0.0293 |
| healthy #4 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 27363 | $0.0232 |
| most-mentioned-not-buyer #4 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 40430 | $0.0323 |
| power-user-concentration #4 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 38551 | $0.0313 |
| reduced-footprint #4 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 32807 | $0.0267 |
| relationship-gap #4 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 32754 | $0.0267 |
| silent-decay #4 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 44076 | $0.0298 |
| stalled-expansion #4 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 32803 | $0.0301 |
| truncated-transcript #4 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 27257 | $0.0247 |
| vibe-risk #4 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 33817 | $0.0274 |
| adoption-failure #5 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 39584 | $0.0395 |
| champion-loss #5 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 36277 | $0.0296 |
| chat-positive-crm-negative #5 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 39752 | $0.0320 |
| frustrated-not-gone #5 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 33505 | $0.0278 |
| healthy #5 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 29070 | $0.0252 |
| most-mentioned-not-buyer #5 | Relationship gap | Sentiment mismatch | 0% | ✗ | 100% | ✓ | native | 37968 | $0.0313 |
| power-user-concentration #5 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 35721 | $0.0300 |
| reduced-footprint #5 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 31469 | $0.0274 |
| relationship-gap #5 | Relationship gap | Power user concentration | 0% | ✗ | 100% | ✓ | native | 37351 | $0.0295 |
| silent-decay #5 | Silent decay | Silent decay | 100% | ✓ | 100% | ✓ | native | 32041 | $0.0269 |
| stalled-expansion #5 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 33863 | $0.0302 |
| truncated-transcript #5 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 30024 | $0.0251 |
| vibe-risk #5 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 35450 | $0.0295 |
| adoption-failure #6 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 40752 | $0.0411 |
| champion-loss #6 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 35158 | $0.0289 |
| chat-positive-crm-negative #6 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 38095 | $0.0304 |
| frustrated-not-gone #6 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 38039 | $0.0282 |
| healthy #6 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 26994 | $0.0230 |
| most-mentioned-not-buyer #6 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 37385 | $0.0300 |
| power-user-concentration #6 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 34460 | $0.0298 |
| reduced-footprint #6 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 31939 | $0.0277 |
| relationship-gap #6 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 30074 | $0.0270 |
| silent-decay #6 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 37180 | $0.0302 |
| stalled-expansion #6 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 33196 | $0.0304 |
| truncated-transcript #6 | Reduced footprint, Adoption failure | Adoption failure | 50% | ✓ | 100% | ✓ | native | 30318 | $0.0263 |
| vibe-risk #6 | Vibe risk | Sentiment mismatch | 0% | ✓ | 100% | ✓ | native | 35363 | $0.0291 |
| adoption-failure #7 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 39253 | $0.0400 |
| champion-loss #7 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 36079 | $0.0297 |
| chat-positive-crm-negative #7 | Sentiment mismatch | Relationship gap | 0% | ✓ | 100% | ✓ | native | 33990 | $0.0278 |
| frustrated-not-gone #7 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 33732 | $0.0282 |
| healthy #7 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 27162 | $0.0237 |
| most-mentioned-not-buyer #7 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 33610 | $0.0287 |
| power-user-concentration #7 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 37355 | $0.0314 |
| reduced-footprint #7 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 32492 | $0.0282 |
| relationship-gap #7 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 33165 | $0.0289 |
| silent-decay #7 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 39110 | $0.0315 |
| stalled-expansion #7 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 32963 | $0.0295 |
| truncated-transcript #7 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 31840 | $0.0251 |
| vibe-risk #7 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 31638 | $0.0263 |
| adoption-failure #8 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 42330 | $0.0427 |
| champion-loss #8 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 35154 | $0.0291 |
| chat-positive-crm-negative #8 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 37783 | $0.0314 |
| frustrated-not-gone #8 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 33744 | $0.0279 |
| healthy #8 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 27196 | $0.0239 |
| most-mentioned-not-buyer #8 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 33883 | $0.0294 |
| power-user-concentration #8 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 38034 | $0.0321 |
| reduced-footprint #8 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 31389 | $0.0273 |
| relationship-gap #8 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 35169 | $0.0282 |
| silent-decay #8 | Silent decay | Silent decay | 100% | ✓ | 100% | ✓ | native | 31956 | $0.0274 |
| stalled-expansion #8 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 34547 | $0.0306 |
| truncated-transcript #8 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 28556 | $0.0248 |
| vibe-risk #8 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 30425 | $0.0262 |
| adoption-failure #9 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 44063 | $0.0427 |
| champion-loss #9 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 28993 | $0.0261 |
| chat-positive-crm-negative #9 | Sentiment mismatch | Relationship gap | 0% | ✓ | 100% | ✓ | native | 40446 | $0.0324 |
| frustrated-not-gone #9 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 30255 | $0.0272 |
| healthy #9 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 26132 | $0.0242 |
| most-mentioned-not-buyer #9 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 39898 | $0.0300 |
| power-user-concentration #9 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 33936 | $0.0295 |
| reduced-footprint #9 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 33703 | $0.0288 |
| relationship-gap #9 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 28205 | $0.0260 |
| silent-decay #9 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 31846 | $0.0270 |
| stalled-expansion #9 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 37169 | $0.0317 |
| truncated-transcript #9 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 30263 | $0.0266 |
| vibe-risk #9 | Vibe risk | Silent decay | 0% | ✓ | 100% | ✓ | native | 35772 | $0.0294 |
| adoption-failure #10 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 38358 | $0.0401 |
| champion-loss #10 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 33538 | $0.0279 |
| chat-positive-crm-negative #10 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 34461 | $0.0281 |
| frustrated-not-gone #10 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 30324 | $0.0262 |
| healthy #10 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 24870 | $0.0224 |
| most-mentioned-not-buyer #10 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 33504 | $0.0279 |
| power-user-concentration #10 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 37784 | $0.0317 |
| reduced-footprint #10 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 38267 | $0.0312 |
| relationship-gap #10 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 32730 | $0.0285 |
| silent-decay #10 | Silent decay | Silent decay | 100% | ✓ | 100% | ✓ | native | 31559 | $0.0268 |
| stalled-expansion #10 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 40055 | $0.0338 |
| truncated-transcript #10 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 26543 | $0.0240 |
| vibe-risk #10 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 35965 | $0.0290 |
| adoption-failure #11 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 41525 | $0.0406 |
| champion-loss #11 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 32229 | $0.0276 |
| chat-positive-crm-negative #11 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 32484 | $0.0286 |
| frustrated-not-gone #11 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 34872 | $0.0294 |
| healthy #11 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 26430 | $0.0231 |
| most-mentioned-not-buyer #11 | Relationship gap | Sentiment mismatch | 0% | ✗ | 100% | ✓ | native | 33239 | $0.0286 |
| power-user-concentration #11 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 34135 | $0.0304 |
| reduced-footprint #11 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 27688 | $0.0252 |
| relationship-gap #11 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 34721 | $0.0287 |
| silent-decay #11 | Silent decay | Silent decay | 100% | ✓ | 100% | ✓ | native | 30615 | $0.0261 |
| stalled-expansion #11 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 37634 | $0.0310 |
| truncated-transcript #11 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 28418 | $0.0252 |
| vibe-risk #11 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 37137 | $0.0299 |
| adoption-failure #12 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 37290 | $0.0390 |
| champion-loss #12 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 32082 | $0.0280 |
| chat-positive-crm-negative #12 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 33296 | $0.0288 |
| frustrated-not-gone #12 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 32657 | $0.0277 |
| healthy #12 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 28849 | $0.0248 |
| most-mentioned-not-buyer #12 | Relationship gap | Sentiment mismatch | 0% | ✗ | 100% | ✓ | native | 34367 | $0.0289 |
| power-user-concentration #12 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 33539 | $0.0293 |
| reduced-footprint #12 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 34174 | $0.0273 |
| relationship-gap #12 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 31392 | $0.0267 |
| silent-decay #12 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 34675 | $0.0284 |
| stalled-expansion #12 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 41860 | $0.0347 |
| truncated-transcript #12 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 29121 | $0.0258 |
| vibe-risk #12 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 30996 | $0.0270 |
| adoption-failure #13 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 42957 | $0.0407 |
| champion-loss #13 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 30631 | $0.0267 |
| chat-positive-crm-negative #13 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 36185 | $0.0297 |
| frustrated-not-gone #13 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 35188 | $0.0293 |
| healthy #13 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 24417 | $0.0225 |
| most-mentioned-not-buyer #13 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 35100 | $0.0293 |
| power-user-concentration #13 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 36850 | $0.0311 |
| reduced-footprint #13 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 35780 | $0.0300 |
| relationship-gap #13 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 37746 | $0.0285 |
| silent-decay #13 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 39990 | $0.0302 |
| stalled-expansion #13 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 33466 | $0.0301 |
| truncated-transcript #13 | Reduced footprint, Adoption failure | Adoption failure | 50% | ✓ | 100% | ✓ | native | 34809 | $0.0292 |
| vibe-risk #13 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 33350 | $0.0274 |
| adoption-failure #14 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 43476 | $0.0420 |
| champion-loss #14 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 35568 | $0.0285 |
| chat-positive-crm-negative #14 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 33128 | $0.0279 |
| frustrated-not-gone #14 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 34459 | $0.0261 |
| healthy #14 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 28497 | $0.0253 |
| most-mentioned-not-buyer #14 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 31690 | $0.0270 |
| power-user-concentration #14 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 36985 | $0.0305 |
| reduced-footprint #14 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 34204 | $0.0290 |
| relationship-gap #14 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 35435 | $0.0284 |
| silent-decay #14 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 31509 | $0.0266 |
| stalled-expansion #14 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 39212 | $0.0326 |
| truncated-transcript #14 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 33295 | $0.0261 |
| vibe-risk #14 | Vibe risk | Sentiment mismatch | 0% | ✓ | 100% | ✓ | native | 29831 | $0.0258 |
| adoption-failure #15 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 42367 | $0.0412 |
| champion-loss #15 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 34685 | $0.0289 |
| chat-positive-crm-negative #15 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 37080 | $0.0307 |
| frustrated-not-gone #15 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 28637 | $0.0253 |
| healthy #15 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 25688 | $0.0234 |
| most-mentioned-not-buyer #15 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 35122 | $0.0290 |
| power-user-concentration #15 | Power user concentration | Power user concentration | 100% | ✓ | 50% (missing CSV data) | ✓ | native | 37295 | $0.0309 |
| reduced-footprint #15 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 31932 | $0.0274 |
| relationship-gap #15 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 31451 | $0.0279 |
| silent-decay #15 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 37199 | $0.0292 |
| stalled-expansion #15 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 32457 | $0.0295 |
| truncated-transcript #15 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 32230 | $0.0270 |
| vibe-risk #15 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 34681 | $0.0280 |
| adoption-failure #16 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 40481 | $0.0403 |
| champion-loss #16 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 30658 | $0.0267 |
| chat-positive-crm-negative #16 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 37730 | $0.0320 |
| frustrated-not-gone #16 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 35727 | $0.0284 |
| healthy #16 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 27960 | $0.0246 |
| most-mentioned-not-buyer #16 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 36341 | $0.0285 |
| power-user-concentration #16 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 36449 | $0.0305 |
| reduced-footprint #16 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 32883 | $0.0286 |
| relationship-gap #16 | Relationship gap | Champion loss | 0% | ✗ | 100% | ✓ | native | 34919 | $0.0288 |
| silent-decay #16 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 35162 | $0.0277 |
| stalled-expansion #16 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 41924 | $0.0339 |
| truncated-transcript #16 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 30537 | $0.0254 |
| vibe-risk #16 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 37452 | $0.0295 |
| adoption-failure #17 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 44222 | $0.0405 |
| champion-loss #17 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 39553 | $0.0304 |
| chat-positive-crm-negative #17 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 37638 | $0.0291 |
| frustrated-not-gone #17 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 33226 | $0.0261 |
| healthy #17 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 25490 | $0.0231 |
| most-mentioned-not-buyer #17 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 36936 | $0.0301 |
| power-user-concentration #17 | Power user concentration | Power user concentration | 100% | ✓ | 50% (missing CSV data) | ✓ | native | 40966 | $0.0331 |
| reduced-footprint #17 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 32668 | $0.0275 |
| relationship-gap #17 | Relationship gap | Power user concentration | 0% | ✗ | 100% | ✓ | native | 29886 | $0.0262 |
| silent-decay #17 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 38699 | $0.0299 |
| stalled-expansion #17 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 33147 | $0.0297 |
| truncated-transcript #17 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 32838 | $0.0282 |
| vibe-risk #17 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 33291 | $0.0259 |
| adoption-failure #18 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 43403 | $0.0424 |
| champion-loss #18 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 35263 | $0.0280 |
| chat-positive-crm-negative #18 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 35176 | $0.0294 |
| frustrated-not-gone #18 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 32383 | $0.0261 |
| healthy #18 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 32045 | $0.0256 |
| most-mentioned-not-buyer #18 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 39403 | $0.0318 |
| power-user-concentration #18 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 35795 | $0.0312 |
| reduced-footprint #18 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 30931 | $0.0268 |
| relationship-gap #18 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 32454 | $0.0265 |
| silent-decay #18 | Silent decay | Silent decay | 100% | ✓ | 100% | ✓ | native | 36755 | $0.0300 |
| stalled-expansion #18 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 33936 | $0.0303 |
| truncated-transcript #18 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 28870 | $0.0247 |
| vibe-risk #18 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 31951 | $0.0267 |
| adoption-failure #19 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 41448 | $0.0397 |
| champion-loss #19 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 30350 | $0.0259 |
| chat-positive-crm-negative #19 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 34704 | $0.0293 |
| frustrated-not-gone #19 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 39012 | $0.0316 |
| healthy #19 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 27609 | $0.0245 |
| most-mentioned-not-buyer #19 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 39019 | $0.0308 |
| power-user-concentration #19 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 35536 | $0.0280 |
| reduced-footprint #19 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 31902 | $0.0278 |
| relationship-gap #19 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 33290 | $0.0284 |
| silent-decay #19 | Silent decay | Silent decay | 100% | ✓ | 100% | ✓ | native | 35751 | $0.0281 |
| stalled-expansion #19 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 41866 | $0.0337 |
| truncated-transcript #19 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 33169 | $0.0270 |
| vibe-risk #19 | Vibe risk | Vibe risk | 100% | ✓ | 100% | ✓ | native | 33773 | $0.0279 |
| adoption-failure #20 | Adoption failure | Adoption failure | 100% | ✗ | 100% | ✓ | native | 40414 | $0.0380 |
| champion-loss #20 | Champion loss | Champion loss | 100% | ✗ | 100% | ✓ | native | 34241 | $0.0268 |
| chat-positive-crm-negative #20 | Sentiment mismatch | Sentiment mismatch | 100% | ✓ | 100% | ✓ | native | 37257 | $0.0308 |
| frustrated-not-gone #20 | Frustrated not gone | Frustrated not gone | 100% | ✓ | 100% | ✓ | native | 34596 | $0.0266 |
| healthy #20 | (none) | Healthy | 100% | ✓ | 100% | ✓ | native | 28913 | $0.0239 |
| most-mentioned-not-buyer #20 | Relationship gap | Power user concentration | 0% | ✗ | 100% | ✓ | native | 32651 | $0.0278 |
| power-user-concentration #20 | Power user concentration | Power user concentration | 100% | ✓ | 100% | ✓ | native | 43975 | $0.0320 |
| reduced-footprint #20 | Reduced footprint | Reduced footprint | 100% | ✓ | 100% | ✓ | native | 36260 | $0.0280 |
| relationship-gap #20 | Relationship gap | Relationship gap | 100% | ✗ | 100% | ✓ | native | 35991 | $0.0299 |
| silent-decay #20 | Silent decay | Silent decay | 100% | ✓ | 0% (missing CSV data) | ✓ | native | 33378 | $0.0276 |
| stalled-expansion #20 | Stalled expansion | Stalled expansion | 100% | ✓ | 100% | ✓ | native | 36897 | $0.0311 |
| truncated-transcript #20 | Reduced footprint, Adoption failure | Reduced footprint | 50% | ✓ | 100% | ✓ | native | 28408 | $0.0258 |
| vibe-risk #20 | Vibe risk | Silent decay | 0% | ✓ | 100% | ✓ | native | 31068 | $0.0266 |
