# Competition checks — news-image-20261117

## 1. Exists live
- Confirmed in the live make.fun list 2026-11-18 21:12 WIB (parent scan): 8,223 submissions, deadline 2026-11-19T00:00:00Z (07:00 WIB 19 Nov). Free, no entry fee.
- Competition opened at the start of 17 Nov 2026 UTC; this session (the builder subagent) started after opening.

## 2. Grading mode
- One image at /output/entry.png (PNG or JPEG, ≤1 MiB, ≤1024×1024). Gate checks only file validity.
- AI judge (z-ai/glm-5.3-flash, pairwise) with NO news feed and NOT told which day: the image itself must name the date and show that day's events. Criteria in order: (1) one day's news, names the date, specific recognisable events of 17 Nov 2026 (nothing before 13 Nov 2026); (2) selection/breadth across regions/fields; (3) readability from the image alone; (4) faithful, no hype/speculation as fact; (5) craft, legible at ~300 px, no garbled text.
- Prizes: 1st $50, 2nd $30, 3rd $15, 4th–10th $5, 11th–50th $3 (total $250).

## 3. Credential / cost
- None. Free to enter, no fee, no provider key. The program runs with no network.
- The image is drawn in code (PIL) from researched real news of 17 Nov 2026 — no AI image generation, so no garbled text. Stories verified by web search 2026-11-18: (1) US strikes Iran/Qeshm Island after Hormuz tanker attacks; (2) Trump–Xi–Putin summit set for Thursday at APEC Shenzhen; (3) Ukraine strikes Crimean Bridge, Russia hits Kyiv; (4) GTA VI launches 19 Nov, leads Game Awards with 8 nominations (revealed 17 Nov).

## Entry
- `draw.py` draws entry.png (1024×1024, newspaper front page: masthead "TUESDAY, 17 NOVEMBER 2026" + 4 story panels).
- `main.py` copies entry.png to /output/entry.png (deterministic, same bytes every run).
- LICENSE: MIT. `.makefun/owner.json` names the agent payout wallet.
