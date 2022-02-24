from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import update_water_levels

#Demo program for exercise 2B

def run():

    tol = 0.8 #sets tolerance to 0.8, relative water level above 0.8 will be flagged up

    stations = build_station_list() #builds list of stations
    update_water_levels(stations) #updates the data to latest

    stations_over = stations_level_over_threshold(stations, tol) #generates the list of tuples with relative water level over tolerance

    for tup in stations_over: #for every tuple in the list
        print(tup[0].name, tup[1]) #prints name of station and relative river level
