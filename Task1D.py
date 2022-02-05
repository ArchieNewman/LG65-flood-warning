#program to test the rivers_with_station function
#importing relevant modules
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_stations
from floodsystem.geo import stations_by_river

#task 1D demo program
def run():
    #part one- making part of the function that prints the number of rivers with stations and shows a list of the first 10 
    #alphabetically sorted rivers with stations
    stations = build_station_list() # builds a list  of stations        #Added () after build_station_list

    rivers_ws = rivers_with_stations(stations) #creates a list of stations with one or more monitoring stations
    sorted_rivers_ws = sorted(rivers_ws) #sorts the list into alphabetical order

    print(len(rivers_ws), "stations.") #prints the number of rivers with one or more monitoring stations- in the form "xxx stations."
    print("The First 10-", sorted_rivers_ws[:10]) #prints the first 10 rivers with stations in alphabetical order
    #Part 1 works now, the only problem was the missed ()


    #part 2- making part of the function that prints the names of the stations located on specific rivers

    river_stations = stations_by_river(stations) #builds a dictionary of rivers with their stations

    station_names_RiverAire = [] #makes an empty list to add the stations on the river aire
    for station in river_stations['River Aire']: #cycles through the list of stations on the river aire
        station_names_RiverAire.append(station.name) #adds the station name to the river specific list

    station_names_RiverCam = [] #repeat for river cam
    for station in river_stations['River Cam']:
        station_names_RiverCam.append(station.name)

    station_names_RiverThames = [] #repeat for river Thames
    for station in river_stations['River Thames']:
        station_names_RiverThames.append(station.name)

    print(sorted(station_names_RiverAire)) #sorts and prints the station names on each river
    print(sorted(station_names_RiverCam))
    print(sorted(station_names_RiverThames))


if __name__ == "__main__":
    print ("******** Task 1D: CUED Part IA Flood Warning System ********")
    run()
