"""
Week 7 · Step 4 · Draw the line, one circle per hour
====================================================

Step 3 ended with a DataFrame. A DataFrame is all matplotlib needs.
New here: marker="o" puts a visible dot on every real measurement, so
students can see that a "line chart" is really points joined up.

Run:  python 04_line_chart.py
"""

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry

# --- 1. Fetch (identical to Step 3) --------------------------------------
cache_session = requests_cache.CachedSession(".cache", expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 52.52,
    "longitude": 13.41,
    "hourly": "temperature_2m",
    "timezone": "America/New_York",
}
response = openmeteo.weather_api(url, params=params)[0]

hourly = response.Hourly()


def timezone_name(resp):
    """Timezone() gives bytes on most versions, str on some. Handle both."""
    tz = resp.Timezone()
    return tz.decode() if isinstance(tz, bytes) else tz


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
print(df.head())

# --- 2. Draw --------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    df["date"],                # x: time
    df["temperature_2m"],      # y: degrees
    color="#BF3B2B",           # the line
    linewidth=1.6,
    marker="o",                # <- a circle on every data point
    markersize=4,
    markerfacecolor="white",   # hollow circles read better on a projector
    markeredgecolor="#BF3B2B",
    markeredgewidth=1.2,
    label="temperature_2m",
)

# --- 3. Label it. An unlabelled chart is not finished. --------------------
ax.set_title(
    f"Hourly temperature · {response.Latitude():.2f}°N {response.Longitude():.2f}°E",
    fontsize=14, fontweight="bold", loc="left",
)
ax.set_xlabel("Local time (" + timezone_name(response) + ")")
ax.set_ylabel("Temperature (°C)")
ax.grid(True, color="#C9D6DF", linewidth=0.6, alpha=0.8)
ax.legend(loc="upper right", frameon=False)
for side in ("top", "right"):
    ax.spines[side].set_visible(False)

# Readable date ticks: one label per day, plus small ticks every 6 hours.
ax.xaxis.set_major_locator(mdates.DayLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%a %d %b"))
ax.xaxis.set_minor_locator(mdates.HourLocator(byhour=(6, 12, 18)))
fig.autofmt_xdate(rotation=0, ha="center")

fig.tight_layout()
plt.show()

# Ask the class: what happens to the circles if you request 16 days instead
# of 7? Step 5 answers it.
