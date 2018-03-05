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

# #start timer
# psOut = psutil.cpu_times()
# ps0 = psOut[0]
# ps1 = ps0


#Record Data
while(1):

	usage = psutil.cpu_percent(interval=None)
	print usage
	# ps1 = pstemp
	# powerOut =  tn.read_until("\n")
	# power = powerOut[12:17]
	# psOut = psOut[0]
	# file1 = open(C4_thermal_sensor,"r")
	# file2 = open(C5_thermal_sensor,"r")
	# file3 = open(C6_thermal_sensor,"r")
	# file4 = open(C7_thermal_sensor,"r")

	# C4temp = file1.read()
	# C5temp = file2.read()
	# C6temp = file3.read()
	# C7temp = file4.read()

	# file1.close
	# file2.close
	# file3.close
	# file4.close



