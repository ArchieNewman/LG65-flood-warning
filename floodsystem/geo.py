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

#part 2- developing a function that returns a dictionary that maps river names to station objects on a given river

def stations_by_river(stations):
    #dictionary mapping river names stations on a given river

    river_stations = {} #creates empty dictionary

    for station in stations #goes through each station in stations list
        
        if station.river in river_stations: #checks to see if there is a key for the river already
            river_stations[station.river].append(station) #append = adds station to dictionary as an object- key is the river name

        else: 
            station.setdefault(station.river, []) #creates a new river key
            river_stations[station.river].append(station) #append adds the station to the key for that river 

    return river_stations #returns the dictionary 
            