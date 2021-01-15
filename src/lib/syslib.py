from subprocess import PIPE, Popen
import os

#CPU Temp
def get_cpu_temperature():
    """get cpu temperature using vcgencmd"""
    process = os.popen('vcgencmd measure_temp')
    line = process.readline()
    return line[4:]

#Memory Information
def get_ram():
    free = os.popen("free -h")
    line = free.readline()
    description = line.split()[0:7]
    line = free.readline()
    data = line.split()[1:7]
    result = {}
    count = 0 
    for desc in description:
        result[desc] = data[count]
        count += 1
    return str(result)