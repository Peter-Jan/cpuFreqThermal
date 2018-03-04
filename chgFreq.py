#usage chgFreq <LITTLE_freq> <big_freq>

import os
from sysfs_paths import *
import psutil
import telnetlib
import sys
import string
import time

#set frequency of cluster
file = open(P0_cluster_gov,"w")
file.write("userspace")
file.close

file = open(P4_cluster_gov,"w")
file.write("userspace")
file.close

freq1 = "".join(sys.argv[1])
file = open(P0_cluster_freq_set,"w")
file.write(freq1)
file.close()

freq = "".join(sys.argv[2])
file = open(P4_cluster_freq_set,"w")
file.write(freq)
file.close

