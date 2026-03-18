from data_logger import save_data
from sensor_simulation import read_sensor
from alarm_system import check_alarms
from visualization import plot_data
import matplotlib.pyplot as plt
import time
import os
import keyboard
os.system('cls')

while True:
    os.system('cls')
    data = read_sensor()
    save_data(data)
    check_alarms(data)
    plot_data()
    print("Sensors Reading:\n",data)
    print("\n")
    print("Alarm:\n",check_alarms(data))
    print("\n\nPress and hold 'SPACE' on key board to stop ")
    time.sleep(1)
    if keyboard.is_pressed("space"):
        os.system("cls")
        print("End of execution.")
        break          