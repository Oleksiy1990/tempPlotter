import re
import time
import numpy as np
import sys
import datetime

filename_ovensettings = 'OvenControl3Cooldown25062016.dat'

with open(filename_ovensettings,"r") as f:
    lines = f.readlines() #with statement automatically closes file


thermocouple_num = []
min_Tlimit = []
max_Tlimit = []
percent_permin = []



for num,q in enumerate(lines):
	m = re.match("\d{1,2}[c ]",q)

	if m is not None:
		m = m.group()
		#print(type(m))
		m = re.sub("c","",m)
		thermocouple_num.append(int(m))
		min_Tlimit.append(float(lines[num+5]))
		max_Tlimit.append(float(lines[num+6]))
		percent_permin.append(float(lines[num+9]))
		
print(thermocouple_num)
print(min_Tlimit)
print(max_Tlimit)
print(percent_permin)
print(datetime.datetime.now().strftime("%H:%M:%S"))	
# for u in lines:
# 	u.find

newarr = np.column_stack([thermocouple_num,percent_permin])
print(newarr)
#sys.exit(0)
i=1
while i<10: 
	fo = open("test.txt","a")
	tm = datetime.datetime.now().strftime("%H:%M:%S") 
	dt = datetime.datetime.now().date()
	fo.write("%s %s %.i %.5f"%(dt,tm,newarr[i,0],newarr[i,1])+"\n")
	fo.close()
	i+=1
	time.sleep(1)
	
#print(lines)