"""
Week 7 · Step 3b · The same thing without the helper library
============================================================

03_print_terminal.py used openmeteo_requests, which hides the JSON from you.
This version uses only `requests` + `json`, so the dictionary from Step 2 is
right there on screen. Teach 3b if you want students to see the raw shape;
teach 03 if you want the shorter production-style code. They print the
same table.

Run:            python 03b_print_with_requests.py
Save a copy:    python 03b_print_with_requests.py --save
                (writes data/sample_response.json, so the lesson still runs
                 later even if the classroom Wi-Fi dies)
"""

import json
import sys
from pathlib import Path

import pandas as pd
import requests

URL = "https://api.open-meteo.com/v1/forecast"
PARAMS = {
    "latitude": 52.52,
    "longitude": 13.41,
    "hourly": "temperature_2m",
    "timezone": "America/New_York",
}
SAMPLE = Path(__file__).parent / "data" / "sample_response.json"


def get_data():
    """Ask the server. If that fails, fall back to a saved copy."""
    try:
        response = requests.get(URL, params=PARAMS, timeout=10)
        print("Asked for:", response.url)          # the exact URL from Step 2
        response.raise_for_status()                # 404 / 400 raise here
        return response.json()                     # JSON text -> Python dict
    except requests.RequestException as error:
        print("Network request failed:", error)
        if SAMPLE.exists():
            print("Using the saved copy at", SAMPLE)
            return json.loads(SAMPLE.read_text())
        raise SystemExit(
            "No saved copy either. Connect to the internet and run again, "
            "or run once with --save while you do have a connection."
        )


data = get_data()

if "--save" in sys.argv:
    SAMPLE.parent.mkdir(exist_ok=True)
    SAMPLE.write_text(json.dumps(data))
    print("Saved a copy to", SAMPLE)

# --- What did we actually get? -------------------------------------------
print("\nTop-level keys:", list(data.keys()))
print("Inside 'hourly':", list(data["hourly"].keys()))
print("Units:", data["hourly_units"])

times = data["hourly"]["time"]              # list of strings
temps = data["hourly"]["temperature_2m"]    # list of numbers, same length
print(f"\n{len(times)} timestamps, {len(temps)} temperatures - they line up 1:1")
print("First three pairs:")
for t, c in zip(times[:3], temps[:3]):
    print(f"  {t}  {c:5.1f} °C")

# --- Two parallel lists -> one table -------------------------------------
df = pd.DataFrame({
    "date": pd.to_datetime(times),   # strings -> real datetimes
    "temperature_2m": temps,
})
print("\nHourly data\n", df)
print("\nWarmest hour:\n", df.loc[df["temperature_2m"].idxmax()])
