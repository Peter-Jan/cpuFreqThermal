import os
from sysfs_paths import *
import psutil
import telnetlib
import sys
import string
import time

#connect to telenet
tn = telnetlib.Telnet('192.168.4.1')

#set frequency of cluster
file = open(P0_cluster_gov,"w")
file.write("userspace")
file.close

file = open(P4_cluster_gov,"w")
file.write("userspace")
file.close

#Max Temp
TEMP_LIM = 70
USAGE_THRESHOLD = 80
FREQ_AVAIL = [200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000,
	      1000000, 1100000, 1200000, 1300000, 1400000, 1500000, 1600000, 1700000,
	      1800000, 1900000, 2000000]
#Record Data

while(1):

	usage = psutil.cpu_percent(interval=1,percpu=True)
	C4_usage = usage[4]
	C5_usage = usage[5]
	C6_usage = usage[6]
	C7_usage = usage[7]
	print "Usage: ",C4_usage," ",C5_usage," ",C6_usage," ",C7_usage

	# ps1 = pstemp
	# powerOut =  tn.read_until("\n")
	# power = powerOut[12:17]
	# psOut = psOut[0]

	file1 = open(C4_thermal_sensor,"r")
	file2 = open(C5_thermal_sensor,"r")
	file3 = open(C6_thermal_sensor,"r")
	file4 = open(C7_thermal_sensor,"r")

	C4temp = file1.read()
	C5temp = file2.read()
	C6temp = file3.read()
	C7temp = file4.read()
	C4temp = float(C4temp.replace('\n',''))/1000
	C5temp = float(C5temp.replace('\n',''))/1000
	C6temp = float(C6temp.replace('\n',''))/1000
	C7temp = float(C7temp.replace('\n',''))/1000
	file1.close
	file2.close
	file3.close
	file4.close

	print "Temp: ",C4temp," ",C5temp," ",C6temp," ",C7temp
	
	maxUsage = max([C4_usage,C5_usage,C6_usage,C7_usage])
	maxTemp = max([C4temp,C5temp,C6temp,C7temp])
	headroom = TEMP_LIM-maxTemp

	if headroom <= 0:
#		file = open(P4_cluster_freq_set,"w")
#		file.write(freq)
#		file.close
#		headroom_integral = 0
	else:
		steps = floor(headroom*P+headroom_integral*I)
#		max_allowed += steps

	if maxUsage > USAGE_THRESHOLD:
#		file = open(P4_cluster_freq_set,"w")
#		file.write(max_allowed)
#		file.close
	else:
#		file = open(P4_cluster_freq_set,"w")
#		file.write(freq)
#		file.close

	print "maxTemp: ",maxTemp
	print "test: ", FREQ_AVAIL[3]
