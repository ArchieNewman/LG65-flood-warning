# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


    #------------------------------------------------------------------------------#

    #test for 2B
def test_relative_water_level():

    stations = build_station_list () #builds a list of stations 
    update_water_levels(stations) #updates to latest water levels

    for station in stations:
        if station.typical_range_consistent() == False:
            assert station.relative_water_level() == None #this checks that inconsistent data returns None

    s_id = "http://environment.data.gov.uk/flood-monitoring/id/stations/1029TH"
    m_id = "http://environment.data.gov.uk/flood-monitoring/id/measures/1029TH-level-stage-i-15_min-mASD"
    label = "Bourton Dickler"
    coord = (51.874767, -1.740083)
    river = "River Dikler"
    town = "Little Rissington"
    test_typical_range = (0, 10)
    test_station_list = [MonitoringStation(s_id, m_id, label, coord, test_typical_range, river, town)] #turns it intoo a monitoring station in the class

    update_water_levels(test_station_list)

    known_latest_level = test_station_list[0].latest_level #updates the latest water level to the test station

    test_station_list[0].typical_range = (0, known_latest_level) #sets the station's max in typical to the known latest level
    assert test_station_list[0].relative_water_level() == 1 #runs the station through the relative water level function and checks that the ratio is 1
    test_station_list[0].typical_range = (known_latest_level, 10) #sets the station's min typical to known latest level
    assert test_station_list[0].relative_water_level() == 0 #runs station through function and checks ratio is 0



