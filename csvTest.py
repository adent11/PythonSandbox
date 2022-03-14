import os 
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"

import csv
import matplotlib.pyplot as plt
import matplotlib.dates
import numpy as np
from datetime import datetime as dt
from datetime import timedelta as td

td = []
a = []

with open('testCsv.csv') as csvfile:
  data = csv.reader(csvfile, delimiter = ',')
  fields = next(data)
  for row in data:
    print(row[0] + " " + row[2])
    td.append(float(row[1]))
    a.append(float(row[2]))

# dates = matplotlib.dates.date2num(x)
# print(dates)
plt.figure(figsize=(3, 3))
plt.plot(td, a, color='red', label='Altitude')
plt.xlabel("Time since start (seconds)")
plt.ylabel("Number input by user")
plt.axis([0, 11, 50, 100])
plt.show()