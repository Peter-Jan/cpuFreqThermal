import os
from sysfs_paths import *
import psutil
import telnetlib
import sys
import string

#connect to telenet
tn = telnetlib.Telnet('192.168.4.1')

#set frequency of cluster
file = open(P0_cluster_gov,"w")
file.write("userspace")
file.close

file = open(P4_cluster_gov,"w")
file.write("userspace")
file.close

freq1 = "".join(sys.argv[1])
file = open(P0_cluster_freq_set,"w")
file.write(freq)
file.close()

freq = "".join(sys.argv[2])
file = open(P4_cluster_freq_set,"w")
file.write(freq1)
file.close

duration = sys.argv[3]

#start timer
psOut = psutil.cpu_times()
ps0 = psOut[0]
ps1 = ps0


file1 = open(C4_thermal_sensor,"r")
file2 = open(C5_thermal_sensor,"r")
file3 = open(C6_thermal_sensor,"r")
file4 = open(C7_thermal_sensor,"r")
file5 = open("data_log/C4_temp_"+freq+".txt","a")
file6 = open("data_log/C5_temp_"+freq+".txt","a")
file7 = open("data_log/C6_temp_"+freq+".txt","a")
file8 = open("data_log/C7_temp_"+freq+".txt","a")
file9 = open("data_log/Power_"+freq+".txt","a")
file10 = open(P0_cluster_freq_read,"r")
file11 = open(little_micro_volts,"r")
file12 = open(P4_cluster_freq_read,"r")
file13 = open(big_micro_volts,"r")
file14 = open("data_log/little_freq.txt","a")
file15 = open("data_log/little_volt.txt","a")
file16 = open("data_log/big_freq.txt","a")
file17 = open("data_log/big_volt.txt","a")

#Record Data
while(ps1-ps0<duration):
	psOut = psutil.cpu_times()
	pstemp = psOut[0]

	if(pstemp-ps1>=0.2):
		ps1 = pstemp
		powerOut =  tn.read_until("\n")
		power = powerOut[12:17]
		psOut = psutil.cpu_times()

		C4temp = file1.read()	 
		C5temp = file2.read()	 
		C6temp = file3.read()	 
		C7temp = file4.read()
		P0freq = file10.read()
		P0volt = file11.read()
		P4freq = file12.read()
		P4volt = file13.read()	 
		print "Temp C4: ", C4temp
		print "Temp C5: ", C5temp
		print "Temp C6: ", C6temp
		print "Temp C7: ", C7temp
		print "Power: ", power
		print "P0_Cluster_freq: ", P0freq
		print "P0_Cluster_volt: ", P0volt
		print "P4_cluster_freq: ", P4freq
		print "P4_cluster volt: ", P4volt
		print "Time: ",psOut,"\n"

		file5.write(C4temp.replace('\n','')+",")
		file6.write(C5temp.replace('\n','')+",")
		file7.write(C6temp.replace('\n','')+",")
		file8.write(C7temp.replace('\n','')+",")
		file9.write(power+",")
		file14.write(P0freq.replace('\n','')+",")
		file15.write(P0volt.replace('\n','')+",")
		file16.write(P4freq.replace('\n','')+",")
		file17.write(P0volt.replace('\n','')+",")



file1.close
file2.close
file3.close
file4.close
file5.close
file6.close
file7.close
file8.close
file9.close
file10.close
file11.close
file12.close
file13.close
file14.close
file15.close
file16.close
file17.close


