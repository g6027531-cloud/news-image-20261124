[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/g6027531-cloud/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/g6027531-cloud/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

# Tuesday 24 November 2026 — 32 dated stories, 7 regions

A single 1024×1024 newspaper front page summing up the world news of
Tuesday 24 November 2026, under the fresh masthead **The Global Briefing**.
It is the density upgrade over the three earlier editions in this series
(6–7 stories each): **32 dated stories across 7 regions** — Middle East,
Europe, East Asia, South Asia, Southeast Asia, Africa, and the Americas —
with a lead story, three front stories, a 26-story region grid, and a
two-item also-strip. Every headline, summary and drawing was made for this
day alone: the artwork is original geometric illustration drawn with a
render script (`render.py`); no photographs, logos or third-party artwork
are used.

See the competition on make.fun: https://make.fun/bounty/news-image-20261124

## How it runs

`main.ts` (Node 22, standard library only) copies the checked-in image
`assets/entry.png` to `/output/entry.png` (or to `$MAKEFUN_OUTPUT_DIR`
outside the grader), then verifies the copy by byte length and SHA-256
and fails loudly on any mismatch. It makes no network calls and its
output is byte-identical on every run.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

To re-render the image from scratch, run `python3 render.py`; it is
deterministic and writes `assets/entry.png`.

## Stories featured (32)

Lead: US jury finds Huawei guilty of trade-secret theft and bank fraud
(10 of 12 counts; racketeering acquittal; appeal planned).

Front: four tankers hit mines in the Strait of Hormuz (claims unconfirmed);
Ukraine hits Russian ships in the Gulf of Finland and off Libya; drone
hits the Riyadh PIF tower, 11 wounded.

Middle East: IRGC says it attacked a container ship in Hormuz; Houthis
60 km from Aden and ready to attack; Saudi strikes on Yemen buses and
trucks, 25 dead or missing; Gaza meningitis epidemic alert (272 cases in
October); Israel kills the Hamas internal security chief in a Gaza strike.

Europe: Poland accuses Russia of a new airspace violation; Zelensky urges
four-party talks soon; NATO vows defence against a space threat; Turkish
Air Force helicopter crash kills five crew.

East Asia: China sentences an official to death for spying; South Korea
orders shelter on Ulleungdo after Russian jets approach; Asian stocks rally
on Huang's return (Taiex +9%); Nvidia slips 5.6% after its record $952bn
day; Shenzhou-24 crew named, with Pakistan's first astronaut to fly.

South & Southeast Asia: Indonesia nominates two vice-presidential
candidates; Malaysia to return thousands of migrants to Myanmar; Hasina
plans a 16 December return to Bangladesh; Hanoi restaurant explosion kills
at least six.

Africa: Senegal regains the Africa Cup of Nations title at CAS; DR Congo
searches for a missing plane as rebels claim a shootdown; Libya's Haftar
visits Turkey for the first time.

The Americas: 25 held hostage in a Cartagena supermarket; car bomb injures
23 in Villavicencio; US drone helped capture "El Chapo Isidro", whom Mexico
will try; Pentagon rebukes Canada over defence spending and the F-35
review; US blacklists Megaspeed, the firm at the centre of the Nvidia
scandal.

Also: Iraq orders federal control of Kurdish oilfields and crossings; UK
sanctions the Houthis and four senior officials.

## Dating caveats

The Villavicencio bomb went off on Monday night and the El Chapo Isidro
capture happened at the weekend; both were confirmed on Tuesday 24
November. Shenzhou-24's crew was named on Tuesday; the launch is set for
Wednesday 25 November. Nvidia's record $952bn surge was Monday in the US;
Tuesday brought Asia's rally and Nvidia's 5.6% fall. The Hormuz mine claims
and the Congo shootdown claim are unconfirmed. The China spy death sentence
was reported by Gold Wall Press. These caveats are also printed in the
image footer.

## Sources

Reuters, AP, CNN, Al Jazeera, Le Temps, Nature, Xinhua, Saba; day digest:
Daily Summary Of (30 stories, 64 sources, first-reported times on 24
November 2026 UTC).
