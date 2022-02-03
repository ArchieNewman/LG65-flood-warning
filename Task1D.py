#program to test the rivers_with_station function
#importing relevant modules
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_stations
from floodsystem.geo import stations_by_river

#task 1D demo program
def run():
    #part one
    stations = build_station_list # builds a list  of stations

    rivers_ws = rivers_with_stations(stations) #creates a list of stations with one or more monitoring stations
    sorted_rivers_ws = sorted(rivers_ws) #sorts the list into alphabetical order

    print(len(rivers_ws), "stations.") #prints the number of rivers with one or more monitoring stations- in the form "xxx stations."
    print("The First 10-", sorted_rivers_ws[:10]) #prints the first 10 rivers with stations in alphabetical order



    #part 2