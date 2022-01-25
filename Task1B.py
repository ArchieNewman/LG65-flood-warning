# Runs the code from Geo needed by task 1B

# imports the required function from geo
from floodsystem.geo import stations_by_distance 

# creates the list of stations (for testing purposes)
from floodsystem.stationdata import build_station_list
test_stations = build_station_list()

cam_centre = (52.2053, 0.1218)

# uses the function required for Task 1B to create a complete list of stations and their distance from cam_centre
full_list = stations_by_distance(test_stations, cam_centre)




# now for the fancy demonstration program bits:

# Since stations_by_distance is required to ONLY have (name, distance) in each tuple,
# I had to make the following function below to add the corresponding town to each entry in an list from stations_by_distance
# to meet the demonstration requirements while also having stations_by_distance meeting its requirements. 
# This took a very long time!

# Extracts the first 10 entries in full_list
closest_10 = full_list[:10]

#extracts the last 10 entries in full_list
furthest_10 = full_list[-10:]


def name_inserter (stations, small_list):
    """Inserts the town name into each tuple in a smaller list of (name, distance) tuples"""
    output_list = []
    from floodsystem.utils import sorted_by_key

    # gets name of each station from the stations list
    for i in range(len(stations)):
        station_entry = stations[i]
        s_name = station_entry.name

        # attempts to match the current name to a name in the closest_10 list
        for n in range(len(small_list)):
            tuple_n = small_list[n]
            name_n = tuple_n[0]

            if s_name == name_n:
                s_town = station_entry.town
                distance_n = tuple_n[1]
    
                # yes, I am aware of the name of this variable
                std = (name_n, s_town, distance_n)
                output_list.append(std)
                break           # stops further iteration over small_list

        #stops the function running after all towns have been found
        if len(output_list) == len(small_list):
            break

    # sorts the list by distance again
    output_list = sorted_by_key(output_list, 2)
    return output_list

#FINALLY gives you the required lists for Task 1B.
demo1 = name_inserter(test_stations, closest_10)
print("Closest 10:")
print(demo1)

print("")
print("")

print("Furthest 10:")
demo2 = name_inserter(test_stations, furthest_10)
print(demo2)
