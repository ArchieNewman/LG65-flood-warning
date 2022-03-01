"""Allows you to plot the graph for a chosen town/station for the last N days"""

from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.plot import plot_water_levels_with_fit
from floodsystem.stationdata import build_station_list
stations = build_station_list()

print("Please enter a town or station id. This is case-sensitive")
x = input()

chosen_station = None

for i in range(len(stations)):
    station_entry = stations[i]
    s_name = station_entry.name
    s_town = station_entry.town
    if x == s_name or x == s_town:
        chosen_station = station_entry
        break

print("")
if chosen_station == None:
    print("Station not found")


print("Please enter the number of days you'd like to view data for. This must be a positive number")
print("Some stations may not have any data if you enter a small number. If you get an error, try entering a larger number.")
stuff = input()
N = float(stuff)

new_name = chosen_station.measure_id
dates, levels = fetch_measure_levels(new_name, datetime.timedelta(days=N))
# And then uses my function to plot them
plot_water_levels_with_fit(chosen_station, dates, levels, 4)