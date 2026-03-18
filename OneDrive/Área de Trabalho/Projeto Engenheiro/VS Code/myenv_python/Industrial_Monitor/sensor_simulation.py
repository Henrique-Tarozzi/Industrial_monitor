import numpy as np

#Temperature simulator
def temp_sim():
    return np.random.normal(60,15) # overral temperature of 60 celcius degrees, standar devision of 2

#Pressure simulator
def press_sim():
    return np.random.normal(8,0.8) # ovelrral pressure of 8 bar, sd of 5 bar

#Vibration simulator
def vib_sim():
    return np.random.normal(2,1) # overral vibration of 2 mm/s, sd of 3 mm/s

# Read sensors
def read_sensor():
    return  {"Temperature":round(temp_sim(),2),
            "Pressure":round(press_sim(),2),
            "Vibration":round(vib_sim(),2)
            }
