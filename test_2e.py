"""Tests the plotting function developed as part of 2E"""

# Imports
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.station import MonitoringStation

fictional_station = MonitoringStation("station_id", "measure_id",
                                    "Line at y=1 and y=9, and a line that goes diagonally from 0 to 10 across 11 days",
                                    "coord", [1, 9], "made up river", "New Madeupville")

dates = []
for i in range(11):
    date = datetime.date(2022, 1, 11-i)
    dates.append(date)
    # remember that the actual dates go backwards!

levels = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

plot_water_levels(fictional_station, dates, levels)

#print("Check that this forms a Z shape, that all three lines are plotted, and that the graph has a legend and title")