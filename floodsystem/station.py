# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    # Task 1F, part 1:
    def typical_range_consistent(self):
        """A method that determines if an individual station's high/low range data is consistent (True) or not (False)"""
        # Checks if no data is availalve for high/low ranges
        if self.typical_range == None:
            return False

        # Had to move this below the no-data check as "None" would cause an error
        tr = self.typical_range
        tr_low = tr[0]
        tr_high = tr[1]
        
        #Checks if typical high > typical low
        if tr_high < tr_low:
            return False

        else:
            return True


#Task 1F, part 2:
def inconsistent_typical_range_stations(stations):
    """Applies typical_range_consistent to a list of station objects and returns an alphabetical list of the names of all stations
    which have inconsistent data"""
    
    # Creates empty list
    output_list = []

    # Iterates over stations to find all stations with inconsistent range data 
    for i in range(len(stations)):
        station_entry = stations[i]
        if station_entry.typical_range_consistent() == False:
            s_name = station_entry.name
            output_list.append(s_name)

    # Orders list
    output_list.sort()

    return output_list

        

