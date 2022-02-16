"""This module contains a function that allows you to plot water level against time for a station of your choice.
You must have matplotlib and datetime installed to use this module. Dates = how many days back you want to go."""

def plot_water_levels(station, dates):
    # Imports necessary stuff
    import matplotlib.pyplot as plt
    import datetime
    from floodsystem.datafetcher import fetch_measure_levels

    # gets the id needed to use fetch_measure_levels
    new_name = station.measure_id

    #uses fetch_measure_levels to get the levels for the desired dates
    t, l = fetch_measure_levels(new_name, datetime.timedelta(days=dates))

    #Creates the lists for the x and y axes
    times = []
    levels = []

    # I thought that I was getting a weird format and spent ages trying to fix it, but it looks like it works
    # And that the weird time format was just Python's special way of handling dates
    for time, level in zip(t, l):           #copied from Task 2D, I don't really know what it does but I got it working
        times.append(time)
        levels.append(level)

    # Plots the levels and times found above
    plt.plot(times, levels, label="Actual level")

    # Gets typical highs and lows
    tr = station.typical_range
    tr_low = tr[0]
    tr_high = tr[1]

    # turns them into a list with correct length
    low_list = []
    for i in range(len(times)):
        low_list.append(tr_low)

    high_list = []
    for i in range(len(times)):
        high_list.append(tr_high)

    #... and plots them
    plt.plot(times, low_list, label="Typical low level")
    plt.plot(times, high_list, label="Typical high level")

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