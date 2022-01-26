# A demonstration file for Task 1C

# imports the required function from geo
from floodsystem.geo import stations_within_radius 

# creates the list of stations (for testing purposes)
from floodsystem.stationdata import build_station_list
stations = build_station_list()

# The coordinates of Cambridge City Centre
cam_centre = (52.2053, 0.1218)

# Runs the function and prints the result
demo1C = stations_within_radius(stations, cam_centre, 10)
print(demo1C)