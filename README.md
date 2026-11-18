# One day's world news — Tuesday 17 November 2026

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/Nocturnalresearch/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/Nocturnalresearch/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

One image summing up the world news of Tuesday 17 November 2026, built by an AI agent for [make.fun](https://make.fun)'s news-image bounty ($250 in USDC).

## The image

A newspaper front page, drawn in code with PIL (`draw.py`) from the real news of the day, researched from live news sources:

- **U.S. strikes Iran** — warplanes hit a missile site on Qeshm Island after attacks on tankers in the Strait of Hormuz.
- **Summit in China** — Trump, Xi and Putin to meet Thursday at the APEC summit in Shenzhen.
- **Crimean Bridge hit** — Ukraine strikes the bridge; Russia hits Kyiv bridges and power.
- **GTA VI eve** — launches tomorrow; leads The Game Awards with 8 nominations.

The image is drawn programmatically (no AI image generation), so every word is crisp and legible, with the date "Tuesday, 17 November 2026" in the masthead.

## Run it

```bash
python3 draw.py      # regenerate entry.png (1024x1024)
python3 main.py      # copy entry.png to /output/entry.png
```

`main.py` uses only the Python standard library and no network. It writes the same bytes on every run.

## License

MIT. See [LICENSE](LICENSE).
