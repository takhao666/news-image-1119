# news-image-1119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/takhao666/news-image-1119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/takhao666/news-image-1119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

An entry for make.fun's `news-image-20261119` competition: one image that sums up the world's news of Thursday 19 November 2026.

`entry.png` (1024×1024, PNG) is a newspaper front page: a big
**19 NOVEMBER 2026** masthead, a lead story on the first-ever
Trump–Xi–Putin trilateral in Shenzhen, four more illustrated stories,
a wide panel on children in war, and an "Also today" strip. Every
story on it happened or was first reported on 19 November 2026, and
each one is drawn with its own picture, so the day reads even at small
size. `render.py` draws the image with Pillow and the DejaVu fonts
(text rendered programmatically, so every word stays crisp and
legible). Re-run it to regenerate `entry.png`:

```sh
python3 render.py
```

`main.ts` (Node 22, standard library only) copies `entry.png` to
`/output/entry.png` and verifies the copy by length and sha256, so both
grading runs write identical bytes.

## The stories

**Lead — Trump, Xi and Putin meet in Shenzhen** (illustrated): Xi hosts
Trump and Putin at APEC for the first three-way meeting of the leaders
of the three nuclear powers. Nuclear arms and the war with Iran top the
agenda; US officials expect no deal. (NYT / CNA / The Hindu, 19 Nov 2026)

**Ukraine — Crimean Bridge hit again** (illustrated): a third attack
this week halts traffic on the 19 km link to Crimea, days after a
strike brought down a road span. (Reuters / CNN, 19 Nov 2026)

**The Hague — World Court rules on Rohingya genocide** (illustrated):
the ICJ delivers its verdict today in The Gambia's case against
Myanmar over the 2017 crackdown. A first if it finds a state guilty of
genocide. (Al Jazeera, 19 Nov 2026)

**Markets — Anthropic debuts on Nasdaq** (illustrated): Claude-maker
Anthropic starts trading today as ANT, valued at about $1.4 trillion —
set to be the biggest listing ever. (Motley Fool / Financial Express,
19 Nov 2026)

**Culture — GTA VI rolls out worldwide** (illustrated): Rockstar's epic
unlocks at midnight in each market, New Zealand first — 13 years after
GTA V, and already a 99 on Metacritic. (Reuters / CNA, 19 Nov 2026)

**Children in war:** a record 589 million children — nearly one in
four worldwide — now live in conflict zones, the most since records
began in 1990, a new Save the Children report finds. (ReliefWeb,
19 Nov 2026)

**Also today:** a Van Gogh sells for a record $190.4m at Sotheby's in
New York; Israeli tanks cross Gaza's Yellow Line in the first ground
raid since the 2025 ceasefire; NASA confirms Voyager 1 is now one
light-day from Earth; Iran says three tankers hit mines east of the
Strait of Hormuz.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
# writes out/entry.png — a 1024x1024 PNG, under 1 MiB
```

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=hvn9m3q0&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
