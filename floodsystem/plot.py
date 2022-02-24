"""Contains functions related to plotting data from the stations"""

def plot_water_levels(station, dates, levels):
    """When given a station object, a set of dates and a set of levels, plots a graph of level vs time with the typical
    high/low levels."""
    # Imports necessary stuff
    import matplotlib.pyplot as plt
    import datetime

    # Plots the levels and times found above
    plt.plot(dates, levels, label="Actual level")

    # Gets typical highs and lows
    tr = station.typical_range
    tr_low = tr[0]
    tr_high = tr[1]

    # turns them into a list with correct length
    low_list = []
    for i in range(len(dates)):
        low_list.append(tr_low)

    high_list = []
    for i in range(len(dates)):
        high_list.append(tr_high)

    #... and plots them
    plt.plot(dates, low_list, label="Typical low level")
    plt.plot(dates, high_list, label="Typical high level")


    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('Date')
    plt.ylabel('Water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Adds legend
    plt.legend()

    #   Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

# ------------------------------------------------------

def plot_water_levels_with_fit(station, dates, levels, p):
    """When given a station object, a set of dates and a set of levels, plots a graph of level vs time with the typical
    high/low levels AND a matching polynomial of degree p"""
    # Imports necessary stuff
    import matplotlib.pyplot as plt
    import matplotlib
    import datetime
    from floodsystem.analysis import polyfit
    import numpy as np

    # Plots the levels and times found above
    plt.plot(dates, levels, label="Actual level")

    # Gets typical highs and lows
    tr = station.typical_range
    tr_low = tr[0]
    tr_high = tr[1]

    # turns them into a list with correct length
    low_list = []
    for i in range(len(dates)):
        low_list.append(tr_low)

    high_list = []
    for i in range(len(dates)):
        high_list.append(tr_high)

    #... and plots them
    plt.plot(dates, low_list, label="Typical low level")
    plt.plot(dates, high_list, label="Typical high level")


    #NEW PART, DIFFERENT FROM THE ABOVE FUNCTION!
    poly, shift = polyfit(dates, levels, p)

    # Creates an y list of the correct length using the dates list
    last_date = matplotlib.dates.date2num(dates[0]) - shift

    y_list = np.linspace(last_date, poly(0), len(dates))

    # plots the polynomial
    plt.plot(dates, poly(y_list), label = "best-fit polynomial")


    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('Date')
    plt.ylabel('Water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Adds legend
    plt.legend()

    #   Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()