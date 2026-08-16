# Week 7 — Data visualization from a REST API

**Live site:** https://benchvue.github.io/python-lesson/week-7/

Week 6 plotted data that was already on your computer. This week the data lives on someone
else's server, and you fetch it over the internet before you can draw anything.

The example is [Open-Meteo](https://open-meteo.com/): a free weather API, no sign-up, no API key.

**By the end of the session students can:** read an API URL, look at a raw JSON reply, turn that
reply into a pandas DataFrame, draw a line chart with a marker on every point, and add a control
that changes how much data is requested.

---

## Files

| File | Step | What it is |
|---|---|---|
| `01_data_flow.html` | 1 | The pipeline as a box → box → box chain, all six on one row. |
| `02_browser_json.html` | 2 | Pick a city — the globe spins to it — build the URL, then read the reply as **JSON** or as a **chart**. No Python yet. |
| `03_print_terminal.py` | 3 | Fetch and print a table with the official `openmeteo_requests` client. |
| `03b_print_with_requests.py` | 3b | Same result with plain `requests` + `json`, so the dictionary is visible. |
| `04_line_chart.py` | 4 | Line chart with a circle on every hourly value. |
| `05_forecast_days_slider.py` | 5 | A 1–16 day slider; the x axis rescales itself. |
| `quiz.html` | — | 8-question self-check, beginner level, same format as the Week 4 quiz. |
| `requirements.txt` | — | Everything to install. |

Suggested timing for a 90-minute class: 10 / 15 / 20 / 20 / 20, then the quiz in the last 5.

---

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Check it worked:

```bash
python -c "import openmeteo_requests, pandas, matplotlib; print('ready')"
```

---

## Step 1 — The whole picture first

Open `01_data_flow.html`. Six boxes, five arrows, left to right on a single row (they stack
vertically on a laptop narrower than 1080px). Each box is a thing you will type today; each arrow
is the single call that moves data into the next box.

```
 BOX 01        BOX 02         BOX 03        BOX 04        BOX 05        BOX 06
┌────────┐   ┌────────┐    ┌────────┐   ┌────────┐   ┌──────────┐  ┌────────┐
│ Weather│──▶│ Request│───▶│ JSON   │──▶│ dict + │──▶│ pandas   │─▶│ chart  │
│ server │   │ URL    │    │ reply  │   │ lists  │   │ DataFrame│  │        │
└────────┘   └────────┘    └────────┘   └────────┘   └──────────┘  └────────┘
   their      HTTPS GET     200 OK ·    json.loads()  pd.DataFrame  plt.plot(
   machine                  text                          ()        marker="o")

└──────────── new this week ───────────┘└──────────── Week 6 again ────────────┘
```

The page outlines boxes 01–03 in red for exactly that reason. Say it out loud: only the first
three boxes are new, and every error today will come from those three.

---

## Step 2 — See the reply in a browser

An API request is just a URL. Paste this into any browser tab:

```
https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&timezone=America%2FNew_York
```

Everything after `?` is a list of `key=value` pairs joined by `&`:

| Parameter | Meaning |
|---|---|
| `latitude` / `longitude` | Where. 52.52 / 13.41 is Berlin. |
| `hourly` | Which measurements you want, comma-separated. |
| `timezone` | How timestamps are labelled. The `/` is escaped as `%2F`. |
| `forecast_days` | 1–16. Optional, defaults to 7. Used in Step 5. |

The reply looks like this (long lists shortened):

```json
{
  "latitude": 52.52,
  "longitude": 13.419998,
  "timezone": "America/New_York",
  "elevation": 38.0,
  "hourly_units": { "time": "iso8601", "temperature_2m": "°C" },
  "hourly": {
    "time": ["2026-08-16T00:00", "2026-08-16T01:00", "..."],
    "temperature_2m": [18.5, 18.3, 17.6, "..."]
  }
}
```

Two things students must notice, because everything later depends on them:

1. `time` and `temperature_2m` are **two separate lists of the same length**. Position 0 in one
   matches position 0 in the other. Nothing else connects them.
2. The units live in `hourly_units`, not next to the numbers.

### `02_browser_json.html`

- **City picker** — 16 Western European and 16 US cities. Choosing one fills `latitude`,
  `longitude` and `timezone`. Editing the coordinates by hand switches the picker to *Custom*.
  Worth saying out loud: **the API has no idea what a city is** — the dropdown is a convenience in
  the page, and the request only ever carries numbers.
- **Globe** — sits to the right of the fields and turns to put the chosen city in the middle, so
  the coordinates stop being abstract. Small dots mark every city in the list. Students can drag it
  to spin it by hand. It is drawn with plain SVG maths, no map library and no tiles to download.
- **JSON view** — the reply, colour-coded, with long lists shortened to their first 6 values so the
  *shape* stays readable. Untick the box to see all 384 numbers.
- **Chart view** — the same data drawn as a line with circle markers, plus min / max / mean. When
  more than one variable is requested, buttons appear to switch series. This is a preview of
  Step 4: the browser and matplotlib are drawing the identical numbers.

Good pairs to compare in class: Lisbon vs Chicago (ocean vs continental daily swing), Phoenix vs
Seattle, Honolulu vs Oslo. Watching the globe swing from Europe to Hawaii also makes the point that
longitude and the timezone setting are two different things.

> Firefox pretty-prints JSON on its own; in Chrome or Edge, a JSON viewer extension helps.

---

## Step 3 — Print it in the terminal

Run `03_print_terminal.py`. Expected output, roughly:

```
Coordinates: 52.5°N 13.4°E
Elevation: 38.0 m asl
Timezone: b'America/New_York'b'GMT-4'
Timezone difference to GMT+0: -14400s

Hourly data
                          date  temperature_2m
0    2026-08-16 00:00:00-04:00           18.50
1    2026-08-16 01:00:00-04:00           18.30
..                         ...             ...
167  2026-08-22 23:00:00-04:00           15.10
```

Three things to explain while it is on screen:

- **Why the caching and retry setup?** Thirty students hitting one free API at once is rude and
  slow. `requests_cache` stores replies in a local `.cache` file for an hour; a repeat run costs
  no network at all.
- **Why `pd.date_range`?** The API does not send a timestamp beside every value. It sends a start,
  an end and an interval, plus one flat list of numbers. You rebuild the timestamps yourself.
- **Why `Variables(0)`?** The index follows the order in *your* `hourly` parameter. Ask for
  `"temperature_2m,relative_humidity_2m"` and humidity is `Variables(1)`.

`03b_print_with_requests.py` gets the same table using only `requests` and `json`, so the
dictionary from Step 2 is visible in the code. Run it once with `--save` while you are online and
it writes `data/sample_response.json`, which it falls back to if the classroom Wi-Fi dies later.

**Stop here until every screen shows a table.** Debugging a chart and a network call at the same
time is what makes this lesson go badly.

---

## Step 4 — Draw the line

Run `04_line_chart.py`. The plotting call is one line, and the new argument is `marker`:

```python
ax.plot(
    df["date"],                # x: real datetimes, so matplotlib handles the axis
    df["temperature_2m"],      # y: degrees
    color="#BF3B2B",
    linewidth=1.6,
    marker="o",                # a circle on every measured hour
    markersize=4,
    markerfacecolor="white",   # hollow circles stay readable on a projector
    markeredgecolor="#BF3B2B",
)
```

Worth saying: a line chart is not a continuous measurement. It is 168 points joined by straight
segments, and `marker="o"` is what makes that honest. The rest of the script is labelling — title,
axis labels, grid, date ticks — and none of it is optional in a finished chart.

Quick variations to try live: `marker="s"`, `linestyle="--"`, `ax.fill_between(...)`,
`ax.axhline(20, color="grey")`.

---

## Step 5 — Add the 1–16 day control

One parameter changes the amount of data:

```python
params = {
    "latitude": 52.52,
    "longitude": 13.41,
    "hourly": "temperature_2m",
    "timezone": "America/New_York",
    "forecast_days": 16,     # 1 to 16
}
```

`05_forecast_days_slider.py` wires that to a `matplotlib.widgets.Slider`. Moving it triggers
`draw()`, which fetches, clears the axes and replots.

The x axis rescales on its own because the data carries its own datetimes — you never hard-code a
range. Two adjustments do have to be made by hand, and they are the real lesson of this step:

- **Ticks.** One label per day is fine at 7 days and unreadable at 16, so the tick locator changes
  with the range (3-hourly labels under 2 days, daily up to 8, every second day beyond that).
- **Markers.** 16 days is 384 points; the circles merge into a stripe. The script drops them above
  200 points — the same rule the Chart view in Step 2 uses.

```
forecast_days = 1   →  24 points   →  hh:mm ticks, circles visible
forecast_days = 7   →  168 points  →  one tick per day, circles visible
forecast_days = 16  →  384 points  →  tick every 2 days, no circles
```

Ask the class to predict the number of points before each move. Then ask why sliding back to a
value you already viewed is instant — the answer is the cache from Step 3.

---

## Quiz

`quiz.html` — 8 short multiple-choice questions, pitched at a first-time beginner: where the
settings start in a URL, what `&` separates, what JSON is, which list holds the times, how the two
lists line up, what `marker="o"` draws, how many numbers 2 days produces, and which line of a
4-line script draws the picture. It scores itself, explains every answer, and has a reset button.
Open it in a browser; nothing to install.

---

## When it breaks

| Symptom | Cause | Fix |
|---|---|---|
| `ModuleNotFoundError: openmeteo_requests` | Wrong interpreter, or venv not active | Re-activate the venv, `pip install -r requirements.txt` |
| `ConnectionError` / timeout | Offline, or a school firewall | Open the URL in a browser to confirm; use the `03b … --save` copy |
| `{"error":true,"reason":"Data corrupted..."}` | Misspelled parameter or variable name | Check spelling against the browser URL in Step 2 |
| `AttributeError: 'str' object has no attribute 'decode'` | Newer client returns `str` from `Timezone()` | Use the `timezone_name()` helper in `04`/`05` |
| Chart window opens then closes instantly | Missing `plt.show()`, or a headless backend | Keep `plt.show()`; run from a normal terminal, not a notebook cell that captures output |
| Nothing changes when re-running | Cached reply, under one hour old | Delete `.cache`, or lower `expire_after` |
| x labels overlap | Too many ticks | Change the locator, as in Step 5 |
| Chart view in the browser stays empty | Nothing fetched yet, or the request failed | Press **Fetch it here** first and read the status line |

---

## Homework

1. **Your town.** Find your city in the Step 2 picker, copy its coordinates into `04_line_chart.py`
   and re-run it. Put the place name in the chart title.
2. **A second series.** Request `"hourly": "temperature_2m,relative_humidity_2m"`, read the second
   variable with `Variables(1)`, and plot it on a twin y axis (`ax2 = ax.twinx()`).
3. **Two cities, one chart.** Call the API twice with different coordinates, plot both lines, add a
   legend, and write one sentence saying what the chart shows.
4. **Daily instead of hourly.** Swap `hourly` for `daily=temperature_2m_max,temperature_2m_min`
   and draw both lines. How does the number of points change?
5. **Look backwards.** Add `"past_days": 7` and mark today with `ax.axvline`.
6. **Write it down.** Save your DataFrame with `df.to_csv("forecast.csv", index=False)` and the
   figure with `fig.savefig("forecast.png", dpi=150)` — that closes the loop back to Week 6, which
   started from a file like this one.

---

## Vocabulary from today

**API** — an agreed way for one program to ask another for data.
**REST** — the common style where each URL names a resource and `GET` means "give me a copy".
**Endpoint** — the address you call, here `https://api.open-meteo.com/v1/forecast`.
**Query parameters** — the `key=value` pairs after `?` that narrow the request.
**Percent-encoding** — how awkward characters travel in a URL; `/` becomes `%2F`.
**JSON** — text made of objects, lists, numbers and strings; Python reads it as dicts and lists.
**Status code** — `200` fine, `400` your request was wrong, `429` you asked too often, `5xx` their problem.
**Cache** — a local copy kept so the same question is not asked twice.

---

## Reference

- Open-Meteo forecast docs — <https://open-meteo.com/en/docs>
- pandas `date_range` — <https://pandas.pydata.org/docs/reference/api/pandas.date_range.html>
- matplotlib date axes — <https://matplotlib.org/stable/gallery/text_labels_and_annotations/date.html>
- matplotlib widgets — <https://matplotlib.org/stable/api/widgets_api.html>
