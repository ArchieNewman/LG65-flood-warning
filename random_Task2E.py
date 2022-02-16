from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
stations = build_station_list()

# Station name to find (for some reason some don't work, such as Cambridge Jesus Lock???)
station_name = "Gwithian"

# Find station
input_station_object = None
for station in stations:
    if station.name == station_name:
        input_station_object = station
        break


output = plot_water_levels(input_station_object, 7)
print(output)