import random
import sys
import pandas as pd
import requests
import numpy as np
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QApplication, QMainWindow)
import pyqtgraph as pg
from flask import Flask, jsonify
from threading import Thread

# Define a class for the real-time satellite signal plot
class RealTimeSatellitePlot(QMainWindow):
    def __init__(self):
        super().__init__()
        self.active_signals = []  # Initialize an empty list to store satellite signals
        self.initUI()  # Call the method to initialize the UI
        self.fetch_real_time_signal()  # Fetch the real-time signal immediately

    # Method to initialize the user interface
    def initUI(self):
        self.setWindowTitle('Real-Time Satellite Signal')  # Set the window title
        self.setGeometry(100, 100, 800, 600)  # Set the window size and position
        
        main_widget = QWidget(self)  # Create a main widget
        self.setCentralWidget(main_widget)  # Set the main widget as the central widget
        
        self.layout = QVBoxLayout(main_widget)  # Create a vertical box layout for the main widget

    def display_rect_signal(self, signal, viewer):
        """Display a signal on the given graph with random color."""
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        pen_color = QColor(red, green, blue)
        viewer.plot(signal['x'], signal['y'], pen=pen_color)
        viewer.signal = signal

    def add_new_graph(self, signal):
        """Add a new graph to the layout with labels and display the signal."""
        new_graph = pg.PlotWidget(self)
        new_graph.setLabel('left', 'Latitude')
        new_graph.setLabel('bottom', 'Timestamp')
        self.layout.addWidget(new_graph)
        self.display_rect_signal(signal, new_graph)

    def fetch_real_time_signal(self):
        """Fetch real-time signal data (satellite positions) from an API and update the graphs."""
        try:
            base_url = "https://api.n2yo.com/rest/v1/satellite/positions"
            satellite_id = "25544"
            observer_lat = "41.702"
            observer_lon = "-76.014"
            observer_alt = "0"
            seconds = "300"
            api_key = "PECZAW-Y3BFYT-4TJFVE-5CUH"

            api_url = f"{base_url}/{satellite_id}/{observer_lat}/{observer_lon}/{observer_alt}/{seconds}/&apiKey={api_key}"

            response = requests.get(api_url)

            if response.status_code != 200:
                raise Exception(f"Failed to fetch data: {response.status_code} {response.reason}")

            data = response.json()

            if 'positions' not in data:
                raise KeyError("Response is missing 'positions' data")

            time_points = [pos['timestamp'] for pos in data['positions']]
            signal_values = [pos['satlatitude'] for pos in data['positions']]

            real_time_signal = {
                'x': np.array(time_points, dtype=float),
                'y': np.array(signal_values, dtype=float)
            }

            self.active_signals.append(real_time_signal)

            self.add_new_graph(real_time_signal)

        except requests.exceptions.RequestException as e:
            print(f"Network error: {str(e)}")
        except KeyError as e:
            print(f"Missing data in response: {str(e)}")
        except ValueError as e:
            print(f"Value error: {str(e)}")
        except Exception as e:
            print(f"Failed to fetch real-time signal: {str(e)}")

# simulate real-time emitter
app = Flask(__name__)
current_signal = {'x': [], 'y': []}
running = True

@app.route('/')
def index():
    return "test"

@app.route('/api/signal', methods=['GET'])
def get_signal():
    return jsonify(current_signal)

@app.route('/stop', methods=['POST'])
def stop_signal():
    global running
    running = False
    return jsonify({"status": "Signal generation stopped."})

def run_flask():
    app.run(debug=True, use_reloader=False)

if __name__ == '__main__':
    flask_thread = Thread(target=run_flask)
    flask_thread.start()

    app = QApplication(sys.argv)
    real_time_plot = RealTimeSatellitePlot()  # Create an instance of the RealTimeSatellitePlot class
    real_time_plot.show()  # Show the real-time plot window
    sys.exit(app.exec_())  # Execute the application
