from floodsystem.analysis import polyfit
from datetime import datetime, timedelta
import numpy as np

dates = [datetime(2016, 12, 30), datetime(2016, 12, 31), datetime(2017, 1, 1),
     datetime(2017, 1, 2), datetime(2017, 1, 3), datetime(2017, 1, 4),
     datetime(2017, 1, 5)]

levels = [1, 3, 5, 8, 9, 10, 1]
x, b = polyfit(dates, levels, 6)
#y = x - 16000
print(x)
print(b)