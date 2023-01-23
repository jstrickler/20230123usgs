import numpy as np
import matplotlib.pyplot as plt

dt = np.dtype([('Month', 'int8'), ('Day', 'int8'), ('Year', 'int16'), ('Temp', 'float64')])  # define custom numpy datatype
data = np.loadtxt('../DATA/weather/NYNEWYOR.txt', dtype=dt)  # read flat-file data into numpy array

print(data['Temp'])

temps = data['Temp']  # get data from 'Temp' column

plt.plot(temps)  # plot days against temps
plt.show()  # display plot
plt.cla()  # clear first axis but not the whole figure

normalized_data = data[data['Temp'] > -50]  # remove readings < -50, which seem to be default N/A values
temps = normalized_data['Temp']  # grab temps again
plt.plot(temps)  # replot
plt.show()
