"""
Week 7 · Step 3 · Print the reply in the terminal
=================================================

Goal: get the same data you just read in the browser, but inside Python,
and stop there. No chart yet. If this prints a table, the hard part is done.

Run:  python 03_print_terminal.py
"""

import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry

# --- 1. Set up the client -------------------------------------------------
# CachedSession: the same request within an hour is answered from a local
# .cache file instead of the network. Kind to the server, fast in class.
# retry: if the network hiccups, try again up to 5 times before giving up.
cache_session = requests_cache.CachedSession(".cache", expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# --- 2. Describe the request ----------------------------------------------
# These are the same key/value pairs you saw after the "?" in Step 2.
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 52.52,
    "longitude": 13.41,
    "hourly": "temperature_2m",
    "timezone": "America/New_York",
}

responses = openmeteo.weather_api(url, params=params)

# --- 3. Read the metadata -------------------------------------------------
# One response per location. We asked for one, so take the first.
response = responses[0]
print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation: {response.Elevation()} m asl")
print(f"Timezone: {response.Timezone()}{response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")

# --- 4. Read the hourly values --------------------------------------------
# The API does not send a timestamp next to every number. It sends a start
# time, an end time and an interval, plus one flat list of values. We rebuild
# the timestamps ourselves with pd.date_range - that is what this block does.
hourly = response.Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()  # 0 = first name in "hourly"

hourly_data = {
    "date": pd.date_range(
        start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
        end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
        freq=pd.Timedelta(seconds=hourly.Interval()),
        inclusive="left",  # the end time itself is not a data point
    ).tz_convert(response.Timezone().decode())
}

hourly_data["temperature_2m"] = hourly_temperature_2m

# --- 5. Into a DataFrame --------------------------------------------------
hourly_dataframe = pd.DataFrame(data=hourly_data)
print("\nHourly data\n", hourly_dataframe)

# --- 6. Sanity checks worth doing out loud in class -----------------------
print("\nRows:", len(hourly_dataframe))
print("First hour:", hourly_dataframe["date"].iloc[0])
print("Last hour: ", hourly_dataframe["date"].iloc[-1])
print("Warmest:   ", round(hourly_dataframe["temperature_2m"].max(), 1), "°C")
print("Coldest:   ", round(hourly_dataframe["temperature_2m"].min(), 1), "°C")
