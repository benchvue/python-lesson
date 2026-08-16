"""
Week 7 · Step 5 · Let the user choose 1 to 16 days
==================================================

One new parameter, "forecast_days", and one new widget, a Slider.
Move the slider -> new request -> new DataFrame -> redraw. The x axis
follows the data automatically, because we hand matplotlib real datetimes
and let it choose the range.

Requests are cached, so sliding back to a day you already viewed is instant
and does not hit the server again.

Run:  python 05_forecast_days_slider.py
"""

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import openmeteo_requests
import pandas as pd
import requests_cache
from matplotlib.widgets import Slider
from retry_requests import retry

LATITUDE = 52.52
LONGITUDE = 13.41
URL = "https://api.open-meteo.com/v1/forecast"
LINE_COLOR = "#BF3B2B"

cache_session = requests_cache.CachedSession(".cache", expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)


def timezone_name(resp):
    tz = resp.Timezone()
    return tz.decode() if isinstance(tz, bytes) else tz


def fetch(forecast_days):
    """Ask for N days and return (DataFrame, timezone label)."""
    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "hourly": "temperature_2m",
        "timezone": "America/New_York",
        "forecast_days": forecast_days,      # <- the only new parameter
    }
    response = openmeteo.weather_api(URL, params=params)[0]
    hourly = response.Hourly()

    dates = pd.date_range(
        start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
        end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
        freq=pd.Timedelta(seconds=hourly.Interval()),
        inclusive="left",
    ).tz_convert(timezone_name(response))

    df = pd.DataFrame({
        "date": dates,
        "temperature_2m": hourly.Variables(0).ValuesAsNumpy(),
    })
    return df, timezone_name(response)


# --- Figure layout: chart on top, slider underneath ----------------------
fig, ax = plt.subplots(figsize=(12, 5.6))
fig.subplots_adjust(bottom=0.24)

slider_ax = fig.add_axes([0.12, 0.08, 0.76, 0.035])
day_slider = Slider(
    ax=slider_ax,
    label="forecast_days",
    valmin=1,
    valmax=16,
    valinit=7,
    valstep=1,          # integers only - the API rejects 7.4 days
    color=LINE_COLOR,
)


def draw(forecast_days):
    """Fetch for this many days and redraw the whole axes."""
    df, tz = fetch(int(forecast_days))

    ax.clear()

    # 24 h * 16 days = 384 points. Circles overlap past roughly a week,
    # so show them only while they still mean something.
    marker = "o" if len(df) <= 200 else None

    ax.plot(
        df["date"], df["temperature_2m"],
        color=LINE_COLOR, linewidth=1.6,
        marker=marker, markersize=4,
        markerfacecolor="white", markeredgecolor=LINE_COLOR, markeredgewidth=1.2,
    )

    ax.set_title(
        f"{int(forecast_days)}-day hourly forecast · {len(df)} points · "
        f"{LATITUDE:.2f}°N {LONGITUDE:.2f}°E",
        fontsize=13, fontweight="bold", loc="left",
    )
    ax.set_xlabel(f"Local time ({tz})")
    ax.set_ylabel("Temperature (°C)")
    ax.grid(True, color="#C9D6DF", linewidth=0.6, alpha=0.8)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)

    # x range: exactly the data we have, no empty margins
    ax.set_xlim(df["date"].iloc[0], df["date"].iloc[-1])

    # Tick density has to change with the range, or 16 days becomes a smear.
    if forecast_days <= 2:
        ax.xaxis.set_major_locator(mdates.HourLocator(interval=3))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
    elif forecast_days <= 8:
        ax.xaxis.set_major_locator(mdates.DayLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%a %d"))
    else:
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))

    fig.canvas.draw_idle()


day_slider.on_changed(draw)
draw(day_slider.val)
plt.show()

# Extensions for the keen ones:
#   * add a second Slider for latitude, or TextBox widgets for a city
#   * request "hourly": "temperature_2m,relative_humidity_2m" and plot a
#     second line on a twin y axis - Variables(1) holds the second name
#   * add "past_days" (0-92) to show history to the left of today
