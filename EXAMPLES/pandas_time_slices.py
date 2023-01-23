import pandas as pd
import numpy as np

hourly = pd.date_range('1/1/2013 00:00:00', '1/3/2013 23:59:59', freq='H')  # make time series -- every hour for 3 days
print("Number of periods: ", len(hourly))

seconds = pd.date_range('1/1/2013 12:00:00', freq='S', periods=(60 * 60 * 18))  # make time series -- every second for 18 hours
print("Number of periods: ", len(seconds))
print("Last second: ", seconds[-1])

monthly = pd.date_range('1/1/2013', '12/31/2013', freq='M')  # every month for 1 year
print("Number of periods: {0} Seventh element: {1}".format(
    len(monthly),
    monthly[6]
))

NUM_DATA_POINTS = 1441  # number of minutes in a day

dates = pd.date_range('4/1/2013 00:00:00', periods=NUM_DATA_POINTS, freq='T')  # create range from starting point with specified number of points -- one day's worth of minutes

data = np.random.random(NUM_DATA_POINTS)  # a day's worth of data

series = pd.Series(data, index=dates)  # series indexed by minutes

time_slice = series['4/1/2013 10:00:00':'4/1/2013 10:30:00']  # select the half hour of data from 10:00 to 10:30
print(time_slice)  # 31 values
