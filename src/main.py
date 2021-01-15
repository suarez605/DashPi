from src.lib.gathering import DataGathering as dg
import sys
import threading


def data_recovery(freq: float):
    data_recovery_object = dg(freq)
    data_recovery_object.retrieve_data()
   

if __name__ == "__main__":
    freq = sys.argv[1]
    x = threading.Thread(target=data_recovery, args=(freq,))
    x.start()
