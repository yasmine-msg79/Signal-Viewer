import sys
import psutil
import datetime
import time
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.dates as mdates

# Define a class for the real-time CPU usage plot
class RealTimeCpuPlot(QMainWindow):
    def __init__(self):
        super().__init__()
        self.data = []  # Initialize an empty list to store CPU usage data
        self.initUI()  # Call the method to initialize the UI

    # Method to initialize the user interface
    def initUI(self):
        self.setWindowTitle('Real-Time CPU Usage')  # Set the window title
        self.setGeometry(100, 100, 800, 600)  # Set the window size and position
        
        main_widget = QWidget(self)  # Create a main widget
        self.setCentralWidget(main_widget)  # Set the main widget as the central widget
        
        layout = QVBoxLayout(main_widget)  # Create a vertical box layout for the main widget
        
        self.figure = Figure()  # Create a Matplotlib figure
        self.canvas = FigureCanvas(self.figure)  # Create a canvas to display the figure
        layout.addWidget(self.canvas)  # Add the canvas to the layout
        
        self.ax = self.figure.add_subplot(111)  # Add a subplot to the figure
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))  # Set the x-axis date format
        self.ax.xaxis.set_major_locator(mdates.SecondLocator(interval=5))  # Set the x-axis major locator
        
        # Start a new thread to update the data in real-time
        threading.Thread(target=self.update_data, daemon=True).start()

    # Method to update the data
    def update_data(self):
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)  # Get the current CPU usage percentage
            current_time = datetime.datetime.now()  # Get the current time
            self.data.append((current_time, cpu_usage))  # Append the time and CPU usage to the data list
            self.data = self.data[-100:]  # Keep only the last 100 data points
            self.update_plot()  # Update the plot with the new data
            time.sleep(1)  # Sleep for 1 second before getting the next data point

    # Method to update the plot
    def update_plot(self):
        times, usages = zip(*self.data)  # Unzip the data into separate lists of times and usages
        self.ax.clear()  # Clear the previous plot
        self.ax.plot(times, usages, 'r-')  # Plot the new data
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))  # Set the x-axis date format again
        self.ax.xaxis.set_major_locator(mdates.SecondLocator(interval=5))  # Set the x-axis major locator again
        self.canvas.draw()  # Redraw the canvas with the updated plot

# Main block to run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create a QApplication
    real_time_plot = RealTimeCpuPlot()  # Create an instance of the RealTimeCpuPlot class
    real_time_plot.show()  # Show the real-time plot window
    sys.exit(app.exec_())  # Execute the application
