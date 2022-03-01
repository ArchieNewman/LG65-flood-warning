#importing all relevant modules
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.analysis import polyfit, fit_latest_gradient
import numpy as np

#assessing flood risk for all the stations can be done by comparing the relative water level to the higher of the typical levels.
# i have estimated the danger for a given relative water level to be;
# I changed these slightly
# Very_Low < 0.5 < Low < 0.9 < Moderate < 1.2 < High < 2.0 < Severe 
# I've added something to tell if water levels at stations are increasing or decreasing
# Also, all moderate stations with increasing risk are printed. 

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
initial_moderate_list = stations_level_over_threshold(stations ,0.9) #list of all stations with a relative water level >0.9 but <1.2
moderate_list=[]
for station in initial_moderate_list :
    if station in initial_high_list:    #ignores if in the moderate list (includes the high ones (before they are removed))
        pass
    else: 
        moderate_list.append(station[0])

#generating a list of low flood risk
initial_low_list = stations_level_over_threshold(stations ,0.9) #list of all stations with a relative water level >0.9 but <1.2
low_list=[]
for station in initial_low_list :
    if station in initial_moderate_list:    #ignores if in the moderate list (includes the high ones (before they are removed))
        pass
    else: 
        low_list.append(station[0])

#generating a list of very low flood risk
very_low_list=[]
for station in stations : # Repeat for low risk
    if station in initial_low_list:
        pass
    else: 
        very_low_list.append(station)

#only necessary to print the severe and high risk towns
print('The towns with severe risk of flooding are:')
for i in severe_list:
    if i.town == None:
        print(i.name)       # Some stations don't have towns, so instead the station names gets printed.
    else:
        print(i.town)

    dates, levels = fetch_measure_levels(i.measure_id, datetime.timedelta(days=2))
    gradient = fit_latest_gradient(dates, levels, 4)
    if gradient > 0:
        print("--> Increasing risk")
    else:
        print("--> Decreasing risk")
    print("")

print('')
print('The towns with high risk of flooding are:')
for i in high_list:
    if i.town == None:
        print(i.name)       # Some stations don't have towns, so instead the station names gets printed.
    else:
        print(i.town)

    dates, levels = fetch_measure_levels(i.measure_id, datetime.timedelta(days=2))
    gradient = fit_latest_gradient(dates, levels, 4)
    if gradient > 0:
        print("--> Increasing risk")
    else:
        print("--> Decreasing risk")
    print("")

print("")

# I thought it would be a good idea to include the towns that could soon be at risk of flooding; i.e. they are in the
# moderate list and their levels are increasing

print("The towns with moderate, but increasing, risk of flooding are:")
for i in moderate_list:
    dates, levels = fetch_measure_levels(i.measure_id, datetime.timedelta(days=2))
    gradient = fit_latest_gradient(dates, levels, 4)
    if gradient > 0:
        if i.town == None:
            print(i.name)       # Some stations don't have towns, so instead the station names gets printed.
        else:
            print(i.town)