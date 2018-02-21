import os
from sysfs_paths import *
import psutil
import telnetlib

#connect to telenet
tn = telnetlib.Telnet('192.168.4.1')

#run testbench
os.system('./TPBench.exe')

#test read
print tn.read_some()
name = C0_cpu_freq_read
file1 = open(name,"r")
print file1.read()
file1.close

#test write
file1 = open(C0_cpu_freq_set,"w")
#file1.write("200000")
file1.close()
