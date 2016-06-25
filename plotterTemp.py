# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 02:18:13 2016

@author: Oleksiy
"""

import pandas as pd 
#import numpy as np
import time 
import matplotlib.pyplot as plt
#import matplotlib.dates as mdates
from thermocoupledict import tdict
import settingsfile as sf



"""
Initial setting for what to plot
NOTE: imported from settingsfile.py
There must also be the dictionary provided for the names to 
    use in the plot and the correspondence to the names 
    in the data file
"""
filepath_toimport = sf.file_toplot
names_thermocouples = sf.names_thermocouples
thermocouples_filelabel = [tdict[name] for name in names_thermocouples]

"""
Time interval in real time which we want to plot
"""
initial_hr = sf.start_hr
initial_min = sf.start_min

final_hr = sf.finish_hr
final_min = sf.finish_min



def time_and_data(filepath,init_hour,init_min,fin_hr,fin_min,thermocouple_col,sep=" "):
    
    raw_df = pd.read_csv(filepath,sep) #this produces a DataFrame object
        #in Pandas
    #v = np.genfromtxt("20160622_OvenTemp.dat")
    init_sec = 3600*init_hour + 60*init_min
    final_sec = 3600*fin_hr + 60*fin_min
    
    selected_timedata = raw_df[(raw_df['Seconds'] > init_sec) & (raw_df['Seconds'] < final_sec)]
    temp_toplot = pd.to_numeric(selected_timedata[thermocouple_col])
    #temp_tolplot2 = pd.to_numeric(selected_timedata[thermocouple2])
    datetime = pd.to_datetime(selected_timedata["Time"],format="%H:%M:%S")
    #date = datetime.map(pd.Timestamp.date)
    tm = datetime.map(pd.Timestamp.time)
    return (tm,temp_toplot,init_sec,final_sec)



#u = time.strptime(q[7], "%H:%M:%S") 


fig = plt.figure()

ax = fig.add_subplot(111)



data = [time_and_data(filepath_toimport,initial_hr,initial_min,final_hr,final_min,therm) for therm in thermocouples_filelabel]

[ax.plot(d[0],d[1],"o") for d in data]
#ax.plot(tm,temp_tolplot1,"ro")
fig.autofmt_xdate()
ax.set_ylabel("Temperature [C]")
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.65, box.height])

ax.legend(names_thermocouples, bbox_to_anchor=(1,0.5),loc='center left')
#ax.set_title(thermocouple1)
plt.show()
