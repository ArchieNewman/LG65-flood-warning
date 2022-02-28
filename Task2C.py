from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels
 

def run():

    N = 10

    stations = build_station_list()
    update_water_levels(stations)

    N_highest_stations = stations_highest_rel_level(stations, N) # list of N stations with largest relative water level

    for station in N_highest_stations:
        print(station.name, station.relative_water_level()) #prints name and relative water level for each station in the list


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning system ***")
    run()

 