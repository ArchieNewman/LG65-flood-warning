# Build list of stations (for testing purposes)
from floodsystem.stationdata import build_station_list
test_stations = build_station_list()

# For geo:
def stations_by_distance(stations, p):
    """Calculates the distance (in km) of every station in a list of station objects from a Lat/Long coordinate specified by the user
    and returns this information as a list of tuples in the form (station, town, distance)"""
    # note: was unsure whether the function needed to return the town or not, as the demonstration had the town
    # but the reqiurements didn't? I decided to include the town.

    from haversine import haversine, Unit
    
    sd_list = []

    for i in range(len(stations)):
        station_entry = stations[i]
        s_name = station_entry.name
        s_town = station_entry.town
        s_coord = station_entry.coord

        s_distance = haversine(s_coord, p)
        #s_distance = "placeholder"

        sd = (s_name, s_town, s_distance)
        sd_list.append(sd)

    return sd_list

a_place = (45, 9)           #checked on Google maps, my random numbers are a town in Northern Italy
testlist = stations_by_distance(test_stations, a_place)
print(testlist)

for n in range(10):
    print(n)

