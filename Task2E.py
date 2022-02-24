# Imports
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import datetime
all_stations = build_station_list()


# need to find which stations have the current relative highest water level
# this is part of task 2C - so I will use the function from 2C to get a list of 5 the station objects needed.
from floodsystem.flood import stations_highest_rel_level
risky_stations = stations_highest_rel_level(all_stations, 5)



# Uses fetch_water_levels to get the dates, levels for the risky_stations for the past 10 days
for i in range(len(risky_stations)):
    new_name = risky_stations[i].measure_id
    dates, levels = fetch_measure_levels(new_name, datetime.timedelta(days=10))
    # And then uses my function to plot them
    plot_water_levels(risky_stations[i], dates, levels)