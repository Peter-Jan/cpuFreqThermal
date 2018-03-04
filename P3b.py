import os
from sysfs_paths import *
import psutil
import telnetlib
import sys
import string
import time

#connect to telnet
tn = telnetlib.Telnet('192.168.4.1')

#set frequency of clusters
file = open(P0_cluster_gov,"w")
file.write("userspace")
file.close

file = open(P4_cluster_gov,"w")
file.write("userspace")
file.close

freq1 = "".join(sys.argv[1])
file = open(P0
