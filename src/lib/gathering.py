from  .syslib import get_cpu_temperature, get_ram
from time import sleep

class DataGathering:

    def __init__(self, refresh_freq: float):
        self.temp_list = []
        self.ram_list = []
        self.refresh_freq = refresh_freq

    def retrieve_data(self):
        while True:
            sleep(int(self.refresh_freq))
            temp = get_cpu_temperature()
            ram = get_ram()
            print (f'CPU: {temp} C  |  MEM: {str(ram)}')
            if len(self.temp_list) > 100:
                self.temp_list.pop(0)
            if len(self.ram_list) > 100:
                self.ram_list.pop(0)
            self.temp_list.append(temp)
            self.ram_list.append(ram)



