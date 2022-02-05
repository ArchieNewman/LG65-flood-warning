#importing relevant modules
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_stations
from floodsystem.geo import stations_by_river
stations = build_station_list()

rivers_ws = rivers_with_stations(stations)
print(rivers_ws)
#well this part works it seems