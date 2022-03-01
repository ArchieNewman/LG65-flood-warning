from floodsystem.stationdata import build_station_list
stations = build_station_list()
import datetime
from floodsystem.datafetcher import fetch_measure_levels

for i in range(len(stations)):
    if stations[i].name == "Letcombe Bassett":
        print(stations[i].typical_range)
        url = (stations[i].measure_id)
        dates, levels = fetch_measure_levels(url, dt=datetime.timedelta(days=10))
        print(dates)
        print(levels)
        # Seems that the dates and levels are both just []
        # So I will add something to fix that to the inconsistent range function
        # And also make task 2C run inconsistent range.
