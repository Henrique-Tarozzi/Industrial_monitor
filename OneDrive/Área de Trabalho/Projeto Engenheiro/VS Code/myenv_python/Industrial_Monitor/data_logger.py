import pandas as pd
import datetime

def save_data(data): # data to be defined in the main file, it'll come from reading the sensor function
    #Create a dataframe to manipulate values and store it in the csv file
    #([{..,}]) --> Creates an list with Dictionary → it becomes an line in pandas.
    sv = pd.DataFrame([{"Time stamp": datetime.datetime.now(),
                       "Temperature": data["Temperature"],
                       "Pressure": data["Pressure"],
                       "Vibration": data["Vibration"]}])
    # save sensors reading in the csv file, using the to_csv() pandas funtion 
    sv.to_csv("myenv_python\Industrial_Monitor\data\sensor_data.csv",mode="a",header = False, index=False) # mode="a" will create a new file, adding(append) a new line to the exist csv file