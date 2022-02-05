# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data. You must have the "haversine" and "utils" modules installed to run this module"""

from pickle import APPEND
from .utils import sorted_by_key  # noqa

# Task 1B:
def stations_by_distance(stations, p):
    """Calculates the distance (in km) of every station in a list of station objects from a Lat/Long coordinate specified by the user
    and returns this information as a list of tuples in the form (station, distance) in order of distance"""

    from haversine import haversine, Unit
    from .utils import sorted_by_key
    
    # creates empty list
    sd_list = []

    # fills the list
    for i in range(len(stations)):
        station_entry = stations[i]
        s_name = station_entry.name
        s_coord = station_entry.coord

        s_distance = haversine(s_coord, p)

        sd = (s_name, s_distance)
        sd_list.append(sd)

    #sorts the list
    output_list = sorted_by_key(sd_list, 1)

    return output_list



#Task 1C:
def stations_within_radius(stations, centre, r):
    """Returns an alphabetically-ordered list of the names of all the stations (in a list of stations objects) within a radius r
    (in km) of a central point (a Lat/Long coordinate)"""

    from haversine import haversine, Unit
    
    # creates empty list
    name_list = []

    # extracts the necessary data from the list of stations
    for i in range(len(stations)):
        station_entry = stations[i]

        s_coord = station_entry.coord
        s_distance = haversine(s_coord, centre)

        # Determines if the station is within the radius
        if s_distance <= r:
            s_name = station_entry.name
            name_list.append(s_name)

    #sorts the list
    name_list.sort()

    return name_list


#Task 1D:
#part 1- developing a function to return a set of rivers with monitoring stations

def rivers_with_stations(stations):
    #creates a list of rivers with monitoring stations- without duplicates
   
    rivers = set() #creates an empty set for the list- using a set to avoid duplicates
    for station in stations: #applys function to every station
        rivers.add(station.river) #adds the river name to the station object in the set
    
    return rivers #returns the set
    #this part works

#part 2- developing a function that returns a dictionary that maps river names to station objects on a given river

def stations_by_river(stations):
    #dictionary mapping river names to stations on a given river

    river_stations = {} #creates empty dictionary

    for station in stations: #goes through each station in stations list
        
        if station.river in river_stations: #checks to see if there is a key for the river already
            river_stations[station.river].append(station) #append = adds station to dictionary as an object- key is the river name

        else: 
            river_stations.setdefault(station.river, []) #creates a new river key- correction: had list.setdefault needed dictionary.setdefault
            river_stations[station.river].append(station) #append adds the station to the key for that river 

    return river_stations #returns the dictionary 
            

#Task 1E:
#developing a function that returns a list of the N rivers with the most monitoring stations

def rivers_by_station_number(stations, N):
    #determines the N rivers with most monitoring stations

    river_stations = stations_by_river(stations) #creates a dictionary using function (from 1D) of rivers with station names

    river_stationfreq = [] #creates an empty list for rivers and number of stations

    for river in river_stations: #cycles through each of the river keys in the dictionary...
        river_stationfreq.append((river, len(river_stations[river]))) #adds the river name and the number of stations for the given river to the list

        #sorting function for the tuples, sorts based on number of stations (descending order)
        def sort_by_second(tup): 
            return tup[1] #picks out the number of stations Note-!!! python counts from zero so [0] is river name and [1] is the number of stations

    river_stationfreq.sort(key = sort_by_second, reverse=True) #sorts the list of rivers and number of stations by the second part of the tuple (number of stations), in descending order

    #incase the Nth river has the same number of monitoring stations as rivers further down the list.
    while True:
        if   river_stationfreq[N-1][1] == river_stationfreq[N][1]:  #checks to see if more rivers have same number of stations as Nth

            N += 1 #adds increment so that it includes the river with the same value

        else:
            break #breaks the loop as no other rivers have an equal number of stations


    return river_stationfreq[:N] #returns ordered list up to N entries 



