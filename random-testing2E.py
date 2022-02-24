# Imports
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import datetime
all_stations = build_station_list()


# This creates a list of the first 5 stations in all_stations (so I can test without 2c)
risky_stations = []
for i in range(5):
    risky_stations.append(all_stations[i])


# Uses fetch_water_levels to get the dates, levels for the risky_stations for the past 10 days (same code as from actual 2E)
for i in range(len(risky_stations)):
    new_name = risky_stations[i].measure_id
    dates, levels = fetch_measure_levels(new_name, datetime.timedelta(days=10))
    # And then uses my function to plot them
    plot_water_levels(risky_stations[i], dates, levels)