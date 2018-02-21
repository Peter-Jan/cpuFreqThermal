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

freq = "".join(sys.argv[1])
file = open(P0_cluster_freq_set,"w")
file.write(freq)
file.close()

freq = "".join(sys.argv[2])
file = open(P4_cluster_freq_set,"w")
file.write(freq)
file.close

#run testbench
#os.system('./TPBench.exe')

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

#test read
while(ps1-ps0<120):
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
		print "Temp C4: ", C4temp
		print "Temp C5: ", C5temp
		print "Temp C6: ", C6temp
		print "Temp C7: ", C7temp
		print "Power: ", power

		file5.write(C4temp.replace('\n','')+",")
		file6.write(C5temp.replace('\n','')+",")
		file7.write(C6temp.replace('\n','')+",")
		file8.write(C7temp.replace('\n','')+",")
		file9.write(power+",")		 

		file = open(P0_cluster_freq_read,"r")
		print "P0_Cluster_freq: ",file.read()
		file.close
		file = open(little_micro_volts,"r")
		print "P0_Cluster_volt: ",file.read()
		file.close
		file = open(P4_cluster_freq_read,"r")
		print "P4_cluster_freq: ",file.read()
		file.close
		file = open(big_micro_volts,"r")
		print "P4_cluster volt: ",file.read()
		file.close
		print "Time: ",psOut,"\n"
file1.close
file2.close
file3.close
file4.close
file5.close
file6.close
file7.close
file8.close
file9.close


