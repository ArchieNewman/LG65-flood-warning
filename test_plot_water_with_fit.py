"""Tests the levels with fit function developed in the second part of 2F by inputting
linear data to see if the fitted curved matches it."""

# Imports
from floodsystem.plot import plot_water_levels_with_fit
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.station import MonitoringStation
from floodsystem.analysis import polyfit

fictional_station = MonitoringStation("station_id", "measure_id",
                                    "The best-fit polynomial should exactly line up with the actual level line",
                                    "coord", [1, 9], "made up river", "New Madeupville")

dates = []
for i in range(11):
    date = datetime.date(2022, 1, 11-i)
    dates.append(date)                          # Creates a list of 11 dates, counting backwards

levels = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]         # Linear data (going backwards like the dates)

plot_water_levels_with_fit(fictional_station, dates, levels, 4)
