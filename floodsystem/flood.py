from floodsystem.station import MonitoringStation

#2B (2)

def stations_level_over_threshold(stations, tol):
    """a function that returns a list of tuples containing stations eith water levels over threshold and their relative water level """
    
    stations_over = [] #creates empty list fot stations over threshold
    station_level_tup = () #creates empty station - water level tuple

    for station in stations: #cycles through every station in the list of stations
        if station.relative_water_level() != None and station.relative_water_level() < 50: #won't run if no data or if weird data
            if station.typical_range[1] > station.typical_range[0]: #only runs if data is consistent 
                if station.relative_water_level() > tol: #compares to tolerance 
                    station_level_tup = (station, station.relative_water_level()) #creates a tuple for the station
                    stations_over.append(station_level_tup) #adds tuple to list

    def sortsecond(tup):
        return tup[1] 

    stations_over.sort(key= sortsecond, reverse = True)
    #sorts list in descending order

    return stations_over #returns list of sorted tuples

    #-------------------------------------------------------------------------------------------
    #Task 2C
def stations_highest_rel_level(stations, N):
    """function that returns a list of the N stations at which the water level, relative to typical range,is highest"""

    consistent_stations = [] #creates an empty list for station, relative water level tuples
    station_level_tup = () #creates an empty station, water level tuple
    N_highest_stations = [] #creates an empty list for the N stations with highest relative water level

    for station in stations: #cycles through each station
        if station.relative_water_level() != None and station.relative_water_level() < 50: #only applies if data is consistent (there is a relative water level)
            # added a <50 to remove weird stations like Letcome Bassett
            station_level_tup = (station, station.relative_water_level()) #makes tuple with station and relative water level
            consistent_stations.append(station_level_tup) #adds tuple to the list

    def sortsecond(tup): #sorting fuction- sort by second entry of tuple
        return tup[1]

    consistent_stations.sort(key = sortsecond, reverse=True) #sorts by relative water level in descending order 

    for i in range(N):
        N_highest_stations.append(consistent_stations[i][0]) #adds N highest relative water levels to the list


    return N_highest_stations #returns the list





