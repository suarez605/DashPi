import csv
from ..syslib import syslib
import threading
from time import time, sleep
import pandas as pd

class DataGathering:

    async def __init__(self, refresh_freq: float):
        self.temp_list = []
        self.ram_list = []
        self.refresh_freq = refresh_freq

    async def retrieve_data(self):
        while True:
            sleep(self.refresh_freq)
            temp = syslib.get_cpu_temperature()
            ram = syslib.get_ram()
            print (f'CPU: {temp} C  |  MEM: {ram}')
            if len(self.temp_list) > 100:
                self.temp_list.pop(0)
            if len(self.ram_list) > 100:
                self.ram_list.pop(0)
            self.temp_list.append(temp)
            self.ram_list.append(ram)



