"""Tests the fit_latest_gradient function developed in the first part of task 2F"""

from floodsystem.analysis import fit_latest_gradient
from datetime import datetime, timedelta
import numpy as np

# Creates a polynomial of the form 2x**2 + x + 3
# Derivative = 4x + 1
a = 2
b = 1
c = 3
poly_test = np.poly1d([a, b, c])

# Makes lists of dates and y values from it, going backwards from January 1st 2022 (as the dates go backwards)
dates = []
y = []
for i in range(20):
    x = datetime(2022, 1, 20-i)
    dates.append(x)
    point = poly_test(19 - i)           # makes sure the y-values also go backwards!
    y.append(point)


output_p = fit_latest_gradient(dates, y, 2)
print(output_p)

assert round(output_p, 5) == 4*19 + 1           # Checks output is what it should be

# This test works.