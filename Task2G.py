#importing all relevant modules
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_level_over_threshold

#assessing flood risk for all the stations can be done by comparing therelative water level to the higher of the typical levels.
# i have estimated the danger for a given relative water level to be;
# Low < 0.5 < Moderate < 1.2 < High < 2.0 < Severe 

stations = build_station_list() #builds list of stations
update_water_levels(stations) #updates water levels

#generating a list of severe flood risk
initial_severe_list = stations_level_over_threshold(stations, 2) #list of all stations with a relative water level > 2
severe_list = [] #creates empty list
for k in initial_severe_list:
    severe_list.append(k[0]) #adds only the first entry of the tuple- this is the name of the station.

#generating a list of high flood risk 
initial_high_list = stations_level_over_threshold(stations, 1.5) #list of all stations with a relative water level > 1.2 but <2
high_list = [] #creates empty list
for station in initial_high_list:
    if station in initial_severe_list: #ignores if relative water level in severe catagory
        pass
    else:
        high_list.append(station[0]) #adds only the first entry of the tuple- this is the name of the station.

#generating a list of moderate flood risk
initial_moderate_list = stations_level_over_threshold(stations ,0.5) #list of all stations with a relative water level >0.5 but <1.5
moderate_list=[]
for station in initial_moderate_list :
    if station in initial_high_list:    #ignores if in the moderate list (includes the high ones (before they are removed))
        pass
    else: 
        moderate_list.append(station[0])

#generating a list of low flood risk
low_list=[]
for station in stations : # Repeat for low risk
    if station in initial_moderate_list:
        pass
    else: 
        low_list.append(station)

#only necessary to print the severe and high risk towns
print('The towns with severe risk of flooding are:')
for i in severe_list:
    print(i.town)
print('')
print('The towns with high risk of flooding are:')
for i in high_list:
    print(i.town)