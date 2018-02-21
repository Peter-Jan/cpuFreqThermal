import os
from sysfs_paths import *
import psutil
import telnetlib

#connect to telenet
tn = telnetlib.Telnet('192.168.4.1')

#set governor to userspace
file = open(P0_cluster_gov,"w")
file.write("userspace")
file.close

file = open(P4_cluster_gov,"w")
file.write("userspace")
file.close

#run testbench
#os.system('./TPBench.exe')

psOut = psutil.cpu_times()
ps0 = psOut[0]
ps1 = ps0

file1 = open(P0_cluster_freq_read,"r")
print "P0_Cluster_freq: ",file1.read()
file1.close
file7 = open(little_micro_volts,"r")
print "P0_Cluster_volt: ",file7.read()
file7.close
file6 = open(P4_cluster_freq_read,"r")
print "P4_cluster_freq: ",file6.read()
file6.close
file8 = open(big_micro_volts,"r")
print "P4_cluster volt: ",file8.read()
file8.close

#test read
while(ps1-ps0<120):
	psOut = psutil.cpu_times()
	pstemp = psOut[0]

	if(pstemp-ps1>=0.2):
		 ps1 = pstemp
	         powerOut =  tn.read_until("\n")
		 power = powerOut[12:17]
		 psOut = psutil.cpu_times()
		 file2 = open(C4_thermal_sensor,"r")
		 file3 = open(C5_thermal_sensor,"r")
		 file4 = open(C6_thermal_sensor,"r")
		 file5 = open(C7_thermal_sensor,"r")
		 print "Temp C4: ", file2.read()
		 print "Temp C5: ", file3.read()
		 print "Temp C6: ", file4.read()
		 print "Temp C7: ", file5.read()
		 print "Power: ",power
		 file2.close
		 file3.close
		 file4.close
		 file5.close
		 print "Time: ",psOut,"\n"


#test write
file1 = open(C0_cpu_freq_set,"w")
file1.write("200000")
file1.close()
