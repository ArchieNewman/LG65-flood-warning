# imports the required function from geo
from floodsystem.geo import stations_by_distance 

# creates the list of stations (for testing purposes)
from floodsystem.stationdata import build_station_list
stations = build_station_list()

#for i in range(len(stations)):
#    a = stations[i].typical_range
#    print(a)
#    if a == None:
#        print("please can this work")

#for i in range(len(stations)):
#    a = stations[i].typical_range_consistent()
#    print(a)



#Task 1F, part 2:
# Creates empty list
output_list = []

# Iterates over stations to find all stations with inconsistent range data 
for i in range(len(stations)):
    station_entry = stations[i]
    if station_entry.typical_range_consistent() == False:
        print("I am so confused")
        s_name = station_entry.name
        print(s_name)
        output_list.append(s_name)

# Orders list
output_list.sort()

print(output_list)
