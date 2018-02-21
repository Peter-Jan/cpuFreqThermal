# This file defines strings as sysfs paths for various
# 'dials and control knobs' available in Debian.
# Frequency reading/control, thermals, and voltages are accessible using these paths.
# C0_ prefix indicates that the string should be formatted with a
# core number. For cluster paths, use 0 for the little core cluster (0 will map to the 0th core)
# and 4 for the big core cluster (4 will map to the 1st big core).

# To control frequency use scaling_setspeed
# Note that the selected governor must be 'userspace' to change
# frequency settings from these files.
# Use scaling_cur_frequency to read the current frequency.
# Comments above apply to core and cluster paths below.

def sysfs():
	# For each cpu core
	C0_cpu_core_base = "/sys/devices/system/cpu/cpu0/cpufreq/"
	C0_cpu_cluster = C0_cpu_core_base+"related_cpus"
	C0_cpu_max_freq = C0_cpu_core_base+"cpuinfo_max_freq"
	C0_cpu_min_freq = C0_cpu_core_base+"cpuinfo_min_freq"
	C0_cpu_freq_read = C0_cpu_core_base+"scaling_cur_freq"
	C0_cpu_governor = C0_cpu_core_base+"scaling_governor"
	C0_cpu_max_freq_set = C0_cpu_core_base+"scaling_max_freq"
	C0_cpu_min_freq_set = C0_cpu_core_base+"scaling_min_freq"
	C0_cpu_freq_set = C0_cpu_core_base+"scaling_setspeed"

	C1_cpu_core_base = "/sys/devices/system/cpu/cpu1/cpufreq/"
	C1_cpu_cluster = C1_cpu_core_base+"related_cpus"
	C1_cpu_max_freq = C1_cpu_core_base+"cpuinfo_max_freq"
	C1_cpu_min_freq = C1_cpu_core_base+"cpuinfo_min_freq"
	C1_cpu_freq_read = C1_cpu_core_base+"scaling_cur_freq"
	C1_cpu_governor = C1_cpu_core_base+"scaling_governor"
	C1_cpu_max_freq_set = C1_cpu_core_base+"scaling_max_freq"
	C1_cpu_min_freq_set = C1_cpu_core_base+"scaling_min_freq"
	C1_cpu_freq_set = C1_cpu_core_base+"scaling_setspeed"

	c2_cpu_core_base = "/sys/devices/system/cpu/cpu2/cpufreq/"
	c2_cpu_cluster = C2_cpu_core_base+"related_cpus"
	c2_cpu_max_freq = C2_cpu_core_base+"cpuinfo_max_freq"
	c2_cpu_min_freq = C2_cpu_core_base+"cpuinfo_min_freq"
	c2_cpu_freq_read = C2_cpu_core_base+"scaling_cur_freq"
	c2_cpu_governor = C2_cpu_core_base+"scaling_governor"
	c2_cpu_max_freq_set = C2_cpu_core_base+"scaling_max_freq"
	c2_cpu_min_freq_set = C2_cpu_core_base+"scaling_min_freq"
	c2_cpu_freq_set = C2_cpu_core_base+"scaling_setspeed"

	C3_cpu_core_base = "/sys/devices/system/cpu/cpu3/cpufreq/"
	C3_cpu_cluster = C3_cpu_core_base+"related_cpus"
	C3_cpu_max_freq = C3_cpu_core_base+"cpuinfo_max_freq"
	C3_cpu_min_freq = C3_cpu_core_base+"cpuinfo_min_freq"
	C3_cpu_freq_read = C3_cpu_core_base+"scaling_cur_freq"
	C3_cpu_governor = C3_cpu_core_base+"scaling_governor"
	C3_cpu_max_freq_set = C3_cpu_core_base+"scaling_max_freq"
	C3_cpu_min_freq_set = C3_cpu_core_base+"scaling_min_freq"
	C3_cpu_freq_set = C3_cpu_core_base+"scaling_setspeed"

	C4_cpu_core_base = "/sys/devices/system/cpu/cpu4/cpufreq/"
	C4_cpu_cluster = C4_cpu_core_base+"related_cpus"
	C4_cpu_max_freq = C4_cpu_core_base+"cpuinfo_max_freq"
	C4_cpu_min_freq = C4_cpu_core_base+"cpuinfo_min_freq"
	C4_cpu_freq_read = C4_cpu_core_base+"scaling_cur_freq"
	C4_cpu_governor = C4_cpu_core_base+"scaling_governor"
	C4_cpu_max_freq_set = C4_cpu_core_base+"scaling_max_freq"
	C4_cpu_min_freq_set = C4_cpu_core_base+"scaling_min_freq"
	C4_cpu_freq_set = C4_cpu_core_base+"scaling_setspeed"

	C5_cpu_core_base = "/sys/devices/system/cpu/cpu5/cpufreq/"
	C5_cpu_cluster = C5_cpu_core_base+"related_cpus"
	C5_cpu_max_freq = C5_cpu_core_base+"cpuinfo_max_freq"
	C5_cpu_min_freq = C5_cpu_core_base+"cpuinfo_min_freq"
	C5_cpu_freq_read = C5_cpu_core_base+"scaling_cur_freq"
	C5_cpu_governor = C5_cpu_core_base+"scaling_governor"
	C5_cpu_max_freq_set = C5_cpu_core_base+"scaling_max_freq"
	C5_cpu_min_freq_set = C5_cpu_core_base+"scaling_min_freq"
	C5_cpu_freq_set = C5_cpu_core_base+"scaling_setspeed"

	C6_cpu_core_base = "/sys/devices/system/cpu/cpu6/cpufreq/"
	C6_cpu_cluster = C6_cpu_core_base+"related_cpus"
	C6_cpu_max_freq = C6_cpu_core_base+"cpuinfo_max_freq"
	C6_cpu_min_freq = C6_cpu_core_base+"cpuinfo_min_freq"
	C6_cpu_freq_read = C6_cpu_core_base+"scaling_cur_freq"
	C6_cpu_governor = C6_cpu_core_base+"scaling_governor"
	C6_cpu_max_freq_set = C6_cpu_core_base+"scaling_max_freq"
	C6_cpu_min_freq_set = C6_cpu_core_base+"scaling_min_freq"
	C6_cpu_freq_set = C6_cpu_core_base+"scaling_setspeed"

	C7_cpu_core_base = "/sys/devices/system/cpu/cpu7/cpufreq/"
	C7_cpu_cluster = C7_cpu_core_base+"related_cpus"
	C7_cpu_max_freq = C7_cpu_core_base+"cpuinfo_max_freq"
	C7_cpu_min_freq = C7_cpu_core_base+"cpuinfo_min_freq"
	C7_cpu_freq_read = C7_cpu_core_base+"scaling_cur_freq"
	C7_cpu_governor = C7_cpu_core_base+"scaling_governor"
	C7_cpu_max_freq_set = C7_cpu_core_base+"scaling_max_freq"
	C7_cpu_min_freq_set = C7_cpu_core_base+"scaling_min_freq"
	C7_cpu_freq_set = C7_cpu_core_base+"scaling_setspeed"

	# online can be used to turn cores on and off. 
	# There may be some risks to system stability with this.
	C0_core_enabled = C0_cpu_core_base[:-8]+"online"
	C1_core_enabled = C1_cpu_core_base[:-8]+"online"
	C2_core_enabled = C2_cpu_core_base[:-8]+"online"
	C3_core_enabled = C3_cpu_core_base[:-8]+"online"
	C4_core_enabled = C4_cpu_core_base[:-8]+"online"
	C5_core_enabled = C5_cpu_core_base[:-8]+"online"
	C6_core_enabled = C6_cpu_core_base[:-8]+"online"
	C7_core_enabled = C7_cpu_core_base[:-8]+"online"



	# for clusters (e.g. policies on whole clusters):
	# Generally you should use cluster to set and read frequency rather than core paths.
	P0_cluster_base = "/sys/devices/system/cpu/cpufreq/policy0/"
	P0_cluster_max_read = C0_cluster_base+"cpuinfo_max_freq"
	P0_cluster_min_read = C0_cluster_base+"cpuinfo_min_freq"
	P0_cluster_freq_range = C0_cluster_base+"scaling_available_frequencies"
	P0_cluster_cpus = C0_cluster_base+"affected_cpus"
	P0_cluster_gov = C0_cluster_base+"scaling_governor"
	P0_cluster_freq_read = C0_cluster_base+"scaling_cur_freq"
	P0_cluster_freq_set = C0_cluster_base+"scaling_setspeed"
	P0_cluster_max_set = C0_cluster_base+"scaling_max_freq"
	P0_cluster_min_set = C0_cluster_base+"scaling_min_freq"
	P4_cluster_base = "/sys/devices/system/cpu/cpufreq/policy0/"
	P4_cluster_max_read = C0_cluster_base+"cpuinfo_max_freq"
	P4_cluster_min_read = C0_cluster_base+"cpuinfo_min_freq"
	P4_cluster_freq_range = C0_cluster_base+"scaling_available_frequencies"
	P4_cluster_cpus = C0_cluster_base+"affected_cpus"
	P4_cluster_gov = C0_cluster_base+"scaling_governor"
	P4_cluster_freq_read = C0_cluster_base+"scaling_cur_freq"
	P4_cluster_freq_set = C0_cluster_base+"scaling_setspeed"
	P4_cluster_max_set = C0_cluster_base+"scaling_max_freq"
	P4_cluster_min_set = C0_cluster_base+"scaling_min_freq"

	# for temperatures:
	# zones are 0 through 4, with 0-3 being the big cores and 4 being the GPU
	# Note as stated in HW2 document that cores 5 and 7 (thermal zones 1 and 3)
	# have swapped thermal values in sysfs, so be sure to swap them back.
	C0_thermal_base = "/sys/devices/virtual/thermal/thermal_zone{}/"
	C0_thermal_sensor = C0_thermal_base+"temp"
	C0_thermal_type = C0_thermal_base+"type"

	# For voltages:
	little_cluster_voltage_base = "/sys/devices/platform/pwrseq/subsystem/devices/s2mps11-regulator/regulator/regulator.44/"
	little_micro_volts = little_cluster_voltage_base+"microvolts"
	little_max_micro_volts = little_cluster_voltage_base+"max_microvolts"
	little_min_micro_volts = little_cluster_voltage_base+"min_microvolts"

	big_cluster_voltage_base = "/sys/devices/platform/pwrseq/subsystem/devices/s2mps11-regulator/regulator/regulator.40/"
	big_micro_volts = big_cluster_voltage_base+"microvolts"
	big_max_micro_volts = big_cluster_voltage_base+"max_microvolts"
	big_min_micro_volts = big_cluster_voltage_base+"min_microvolts"


	# Paths for GPU stats:
	gpu_base  =  "/sys/devices/platform/11800000.mali/devfreq/devfreq0/device/devfreq/devfreq0/"
	gpu_freq  =  gpu_base + "cur_freq"
	# GPU voltage:
	gpu_voltage_base = "/sys/devices/platform/pwrseq/subsystem/devices/s2mps11-regulator/regulator/regulator.42/"
	gpu_micro_volts  =  gpu_voltage_base + 'microvolts'


	# Paths for memory stats:
	# Memory runs at default frequency of 750000 kHz
	# mem_freq_base  =  "/sys/class/devfreq/exynos5-devfreq-mif/"
	# mem_freq  =  mem_freq_base + 
	mem_voltage_base = "/sys/devices/platform/pwrseq/subsystem/devices/s2mps11-regulator/regulator/regulator.43/"
	mem_micro_volts  =  gpu_voltage_base + 'microvolts'
