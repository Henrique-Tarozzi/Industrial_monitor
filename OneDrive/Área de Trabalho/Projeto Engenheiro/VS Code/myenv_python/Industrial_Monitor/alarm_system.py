import pandas as pd
import datetime

#limits
temp_limit = 80
press_limit = 12
vib_limit = 4

def check_alarms(data):
    alarms = []
    if data["Temperature"] > temp_limit:
       alarms.append(("Temperature",data["Temperature"]))
    if data["Pressure"] > press_limit:
        alarms.append(("Pressure",data["Pressure"]))
    if data["Vibration"] > vib_limit:
        alarms.append(("Vibration",data["Vibration"]))
        
    for sensor,values in alarms:
        ca=pd.DataFrame([{"Time Stamp":datetime.datetime.now(),
                          "Sensor":sensor,
                          "Reading":values}])
        ca.to_csv("myenv_python\Industrial_Monitor\data\sensor_alerts.csv", mode="a",header=False,index=False)
    return alarms