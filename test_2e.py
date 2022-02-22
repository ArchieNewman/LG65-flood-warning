# Imports
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.station import MonitoringStation

fictional_station = MonitoringStation("station_id", "measure_id", "fake station", "coord", [0, 10], "made up river", "New Madeupville")

dates = []
for i in range(11):
    date = datetime.date(2022, 1, i+1)
    print(date)
    dates.append(date)

levels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plot_water_levels(fictional_station, dates, levels)

print("Check that this forms a Z shape, that all three lines are plotted, and that the graph has a legend and title")