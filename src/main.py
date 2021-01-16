#!/usr/bin/env 
from src.lib import gathering as dg
import sys
import threading
from flask import Flask


freq = sys.argv[1]
data_recovery_object = dg.DataGathering(freq)


def data_recovery(freq: float):
    global data_recovery_object
    data_recovery_object.retrieve_data()


app = Flask()


@app.route('/', )
def get_data():
    return f'CPU: {str(data_recovery_object.temp_list)} C  |  MEM: {str(data_recovery_object.ram_list)}'

if __name__ == "__main__":
    x = threading.Thread(target=data_recovery, args=(freq,), daemon=True)
    x.start()
    app.run(host='127.0.0.1', port=80)


