import os


C0_temp  = '/sys/devices/virtual/thermal/thermal_zone0/'
#0_cpu_cluster = 0_cpu_core_base + "related_cpus"


os.chdir(C0_temp)
name = "temp"
file1 = open(name,"r")
print file1.read()
file1.close

