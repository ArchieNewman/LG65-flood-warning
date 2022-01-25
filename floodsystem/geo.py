# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data. You must have the "haversine" and "utils" modules installed to run this module"""

from .utils import sorted_by_key  # noqa

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