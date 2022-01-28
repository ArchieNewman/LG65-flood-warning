# This file literally just runs inconsistent_typical_range_stations on the entire list of stations

# imports the required function from station
from cgi import test
from floodsystem.station import inconsistent_typical_range_stations

# creates the list of stations (for testing purposes)
from floodsystem.stationdata import build_station_list
test_stations = build_station_list()

# Runs the function and prints the result
demo1F = inconsistent_typical_range_stations(test_stations)
print(demo1F)