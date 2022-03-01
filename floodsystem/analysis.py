"""Creates a least-squares polynomial of the desired degree for given dates and water levels"""

def polyfit(dates, levels, p):
    """Creates a least-squares polynomial of degree p for given dates and water levels lists.
    Returns a tuple of the numpy.poly1d object created, and any shift used in the date axis."""

    # Imports
    import numpy as np
    from datetime import datetime, timedelta
    import matplotlib

    # Turns list of dates into times
    times = matplotlib.dates.date2num(dates)

    # Turns the times into shifted times relative to the longest-ago time (aka the last one in the list)
    shift = times[-1]
    s_times = times - shift
    
    #uses numpy polynomial maker to make the polynomial object
    p_coeff = np.polyfit(s_times, levels, p)
    poly = np.poly1d(p_coeff)

    return poly, shift

# --------------------------------------------------------------------

def fit_latest_gradient(dates, levels, p):
    """Creates a least-squares polynomial of degree p for given dates and water levels lists.
    Then finds the gradient at the latest date"""

    # Imports
    import numpy as np
    from datetime import datetime, timedelta
    import matplotlib

    if dates == [] or levels == []:     #removes weird stations
        return 0

    # Turns list of dates into times
    times = matplotlib.dates.date2num(dates)

    # Turns the times into shifted times relative to the longest-ago time (aka the last one in the list)
    shift = times[-1]
    s_times = times - shift
    
    #uses numpy polynomial maker to make the polynomial object
    p_coeff = np.polyfit(s_times, levels, p)
    poly = np.poly1d(p_coeff)

    dydx = poly.deriv()        # finds the derivative function
    
    gradient = dydx(s_times[0])

    return gradient


