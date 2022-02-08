#importing relevant modules

from floodsystem.geo import rivers_with_stations
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import  build_station_list
import inspect

#tests for 1D

def test_rivers_with_station():

    stations = build_station_list() #builds station list
    rivers_ws = rivers_with_stations(stations) #builds a list of rivers with monitoring stations


    assert type(rivers_ws) == set #checks that output is a set (list with no duplicates)
    assert len(rivers_ws) > 0 and len(rivers_ws) <= len(stations) #cant have more rivers with stations than total rivers

    for i in rivers_ws:
        assert type(i) == str #checks that all items are strings


def test_stations_by_river():

    stations = build_station_list() 
    river_stations_dict = stations_by_river(stations) #builds a dictionary of rivers and stations

    assert type(river_stations_dict) == dict #checks that it is a dictionary

    for key in river_stations_dict:
        assert type(key) == str #checks all keys are strings
        assert type (river_stations_dict[key])== list #checks all values are a list

        freq = 0
        for i in river_stations_dict:
            if i == key:
                freq +=1
            else:
                pass

        assert freq == 1 #make sure there are no duplicates

    assert len(river_stations_dict) == len(rivers_with_stations(stations)) #checks that the number of rivers in both the list and dictionary is the same (no duplicates or ones missing)
 

 #Tests for 1E
Station_Test_E = build_station_list()
print(rivers_by_station_number(Station_Test_E, 2))
