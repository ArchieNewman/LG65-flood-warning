# Build list of stations (for testing purposes)
from floodsystem.stationdata import build_station_list
test_stations = build_station_list()


def stations_within_radius(stations, centre, r):
    """Returns an alphabetically-ordered list of the names of all the stations (in a list of stations objects) within a radius r (in km) of a central point 
    (which must be a Lat/Long coordinate)"""

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


#centre = (52.4, 0.3)        # 1dp of Ely, my home town
centre = (52.2053, 0.1218)

please_work = stations_within_radius(test_stations, centre, 10)
print(please_work)
