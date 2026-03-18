import pandas as pd
import matplotlib.pyplot as plt

    # Limites de segurança
temp_max = 80
vib_max = 3
press_max = 10

plt.ion()
fig, axes = plt.subplots(3, 1, figsize=(10,12))  # Creates figure wit 3 subplots (3 lines, 1 row)

def plot_data():
    df = pd.read_csv("myenv_python\Industrial_Monitor\data\sensor_data.csv")
     
    # Clear each plot as plt.clf() doesnt work in this case
    for ax in axes:
        ax.clear()  
       # -------------------
    # Plot 1: Temperature
    axes[0].plot(df.index, df["Temperature"], color="red", marker="o", linewidth=2, label="Temperature")
    axes[0].axhline(temp_max, color="orange", linestyle="--", label="Max")
    axes[0].set_title("Machine Temperature")
    axes[0].set_ylabel("°C")
    axes[0].grid(True)
    axes[0].legend()

    # Show point beyond max
    for t, temp in zip(df.index, df["Temperature"]):
        if temp > temp_max:
            axes[0].scatter(t, temp, color="red", s=100)

    # -------------------
    # Plot 2: Pressure
    axes[1].plot(df.index,df["Pressure"], color="blue", marker="x", linewidth=2, label="Vibrtion")
    axes[1].axhline(press_max, color="orange", linestyle="--", label="Max")
    axes[1].set_title("Machine Pressure")
    axes[1].set_ylabel("bar")
    axes[1].grid(True)
    axes[1].legend()

    # Show point beyond max
    for t, vib in zip(df.index,df["Pressure"]):
        if vib > press_max:
            axes[1].scatter(t, vib, color="red", s=100)

    # -------------------
    # Plot 3: Vibration
    axes[2].plot(df.index, df["Vibration"], color="green", marker="s", linewidth=2, label="Vibration")
    axes[2].axhline(vib_max, color="orange", linestyle="--", label="Max")
    axes[2].set_title("Machine Vibration")
    axes[2].set_xlabel("Time")
    axes[2].set_ylabel("mm/s")
    axes[2].grid(True)
    axes[2].legend()

    # Show point beyond max
    for t, p in zip(df.index, df["Vibration"]):
        if p > vib_max:
            axes[2].scatter(t, p, color="red", s=100)

    # adjust gaps between graphs
    plt.tight_layout()
    # show image
    plt.pause(0.5)