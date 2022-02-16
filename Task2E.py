from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
all_stations = build_station_list()

# need to find which stations have the current relative highest water level
# this is part of task 2C - so I will use the function from 2C to get a list of 5 the stations needed.

from floodsystem.flood import stations_highest_rel_level

risky_stations = stations_highest_rel_level(all_stations, 5)

for i in range(5):
    station = risky_stations[i]
    output = plot_water_levels(station, 10)