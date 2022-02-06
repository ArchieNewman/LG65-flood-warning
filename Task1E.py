#demonstration program for Task 1E

#importing relevant modules
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number

def run():
    stations = build_station_list() #builds a list of stations

    N = 9

    print(rivers_by_station_number(stations, N)) #prints a list of the tuples- station and number of stations


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
