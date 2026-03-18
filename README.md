# Industrial Sensor Monitoring System

## Overview
This project simulates an industrial monitoring system similar to a basic SCADA application.

It collects sensor data in real time, logs it, detects abnormal conditions, and visualizes the process using live charts.

## Features
- Real-time sensor simulation (temperature, pressure, vibration)
- Continuous data logging (CSV)
- Alarm detection system
- Live data visualization with Matplotlib
- Highlight of abnormal values

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib

## System Architecture
Sensor → Data Logger → Alarm System → Visualization

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/Henrique-Tarozzi/Industrial_monito.git

Navigate to the folder:
cd industrial-sensor-monitor

Install dependencies:
pip install pandas numpy matplotlib keyboard

Run the system:
python main.py

Example Output:
Real-time charts updating every second
Alerts generated when limits are exceeded

Future Improvements:
Database integration (SQLite / PostgreSQL)
MQTT / Modbus communication
Web dashboard (Plotly Dash)
Multi-threading

Author
Henrique T. Coelho
