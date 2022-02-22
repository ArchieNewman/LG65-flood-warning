from floodsystem.analysis import polyfit
from datetime import datetime, timedelta
import numpy as np

# Creates a polynomial of the form ax**2 + bx + c
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
    point = poly_test(19 - i)           # make sure the y-values also go backwards!
    y.append(point)

# Confirms that polyfit retuns the input polynomial
output_p, shift = polyfit(dates, y, 2)
print(output_p)
print(output_p[0])
print(output_p[1])
print(output_p[2])

# Checks that the values are the same to 5 dp
assert round(output_p[2], 5) == a
assert round(output_p[1], 5) == b
assert round(output_p[0], 5) == c

# This test works.