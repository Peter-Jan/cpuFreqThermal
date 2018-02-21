import os
from sysfs_paths import *

name = C0_cpu_freq_set
file1 = open(name,"w")
print file1.write(200000)
file1.close

