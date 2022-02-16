from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
all_stations = build_station_list()

# Does the function for the first 5 stations in the list of stations, instead of for the "at risk" stations that
# are identified by the program from 1C in the actual task2E file.

print("5 graphs will now open. Please check they all look normal.")

for i in range(5):
    station = all_stations[i]
    output = plot_water_levels(station, 10)




