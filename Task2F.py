import numpy as np
import matplotlib.pyplot as plt
from floodsystem.plot import plot_water_levels_with_fit
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import datetime
all_stations = build_station_list()

# This creates a list of the first 10 stations in all_stations (so I can test without 2c)
risky_stations = []
for i in range(10):
    risky_stations.append(all_stations[i])

# When task C is completed, delete above section and uncomment this!
# from floodsystem.flood import stations_highest_rel_level
# risky_stations = stations_highest_rel_level(all_stations, 5)


# Uses fetch_water_levels to get the dates, levels for the risky_stations for the past 2 days, with polynomial degree of 4
# as specificed in demonstration requirements
for i in range(len(risky_stations)):
    new_name = risky_stations[i].measure_id
    dates, levels = fetch_measure_levels(new_name, datetime.timedelta(days=2))
    # And then uses my function to plot them
    plot_water_levels_with_fit(risky_stations[i], dates, levels, 4)