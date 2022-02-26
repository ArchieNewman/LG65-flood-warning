from floodsystem.station import MonitoringStation

#2B (2)

def stations_level_over_threshold(stations, tol):
    """a function that returns a list of tuples containing stations eith water levels over threshold and their relative water level """
    
    stations_over = [] #creates empty list fot stations over threshold
    station_level_tup = () #creates empty station - water level tuple

    for station in stations: #cycles through every station in the list of stations
        if station.relative_water_level() != None: #wont run if no data
            if station.typical_range[1] > station.typical_range[0]: 
                if station.relative_water_level() > tol: #compares to tolerance 
                    station_level_tup = (station, station.relative_water_level()) #creates a tuple for the station
                    stations_over.append(station_level_tup) #adds tuple to list

    def sortsecond(tup):
        return tup[1] 

    stations_over.sort(key= sortsecond, reverse = True)
    #sorts list in descending order

    return stations_over #returns list of sorted tuples
