# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 02:18:13 2016

@author: Oleksiy
"""

import pandas as pd 
#import numpy as np
#import time 
import matplotlib.pyplot as plt
#import matplotlib.dates as mdates
from thermocoupledict import tdict

filepath_toimport = "20160624_OvenTemp.dat"

names_thermocouples = ["Ion pump 2 flange","Left TC tube","Ti-sub 2 vert tube"]

thermocouples = [tdict[name] for name in names_thermocouples]

"""
Write the time interval in real time which we want to plot
"""
initial_hr = 15
initial_min = 0

final_hr = 20
final_min = 0




raw_df = pd.read_csv(filepath_toimport,sep=" ") #this produces a DataFrame object
    #in Pandas
#v = np.genfromtxt("20160622_OvenTemp.dat")
init_sec = 3600*initial_hr + 60*initial_min
final_sec = 3600*final_hr + 60*final_min

selected_timedata = raw_df[(raw_df['Seconds'] > init_sec) & (raw_df['Seconds'] < final_sec)]




temp_tolplot = [pd.to_numeric(selected_timedata[th]) for th in thermocouples]
#temp_tolplot2 = pd.to_numeric(selected_timedata[thermocouple2])
datetime = pd.to_datetime(selected_timedata["Time"],format="%H:%M:%S")


date = datetime.map(pd.Timestamp.date)
tm = datetime.map(pd.Timestamp.time)



#u = time.strptime(q[7], "%H:%M:%S") 


fig = plt.figure()
fig2 = plt.figure()
ax = fig.add_subplot(111)

[ax.plot(tm,tplt,"o") for tplt in temp_tolplot]
#ax.plot(tm,temp_tolplot1,"ro")
fig.autofmt_xdate()
ax.set_ylabel("Temperature [C]")
ax.legend(names_thermocouples)
#ax.set_title(thermocouple1)

ax2 = fig2.add_subplot(111)

plt.show()