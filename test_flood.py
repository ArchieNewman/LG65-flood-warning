from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels
import inspect

#Task 2C tests

def test_stations_highest_rel_level():
    

    stations = build_station_list() #creates station list
    update_water_levels(stations) #updates water levels to recent data

    for N in range(1, 1000): #tests a range of values of N
        N_highest_stations = stations_highest_rel_level(stations, N)
        assert type(N_highest_stations) == list #checks output is a list
        assert len(N_highest_stations) == N #checks length of the list is correct

        for station in N_highest_stations: #checks that the stations are all types of monitoring stations
            assert isinstance(station, MonitoringStation) == True #isinstance() function returns True if the specified object is of the specified type, otherwise False


