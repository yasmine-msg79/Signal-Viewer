import sys

from PyQt6 import uic
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QWidget, QApplication, QFileDialog, QVBoxLayout, QPushButton, QDialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import pandas as pd


def plot_polar(signal, polar_ax, polar_canvas):
    if signal is None:
        return
    theta = np.linspace(0, 2 * np.pi, len(signal['x']))
    r = signal['y']

    polar_ax.clear()  # Clear previous plots
    polar_ax.set_ylim(-1.5, 1.5)  # Keep the plot range normalized
    polar_ax.plot(theta, r, marker='o', color='g', linewidth=1)  # Plot the signal
    polar_canvas.draw()


def create_polar_plot():
    figure = Figure()
    figure.patch.set_facecolor('black')
    ax = figure.add_subplot(111, polar=True)  # Polar axis
    ax.set_facecolor('black')
    ax.set_ylim(0, 0.7)
    ax.tick_params(colors='white')  # White tick labels
    ax.grid(color='gray', linestyle='--', linewidth=0.5)  # Grid in gray
    canvas = FigureCanvas(figure)  # Embed in canvas
    return canvas, ax


def extract_signal_data(source):
    try:
        if source.endswith('.csv'):
            df = pd.read_csv(source)
            signal = {
                'x': df.iloc[:, 0].values,  # First column (e.g., Time)
                'y': df.iloc[:, 1].values  # Second column (e.g., Amplitude)
            }
            # print(self.active_signals)
            return signal
    except Exception as e:
        print(f"Error extracting signal data: {e}")
        return None


class NonRectangularPlot(QDialog):
    def __init__(self, *args, **kwargs):
        super(NonRectangularPlot, self).__init__(*args, **kwargs)
        uic.loadUi(r"UI\Non_rectangular.ui", self)
        self.signal = None
        self.is_playing = False
        self.current_index = 0
        self.polar_canvas, self.polar_ax = create_polar_plot()
        self.polar_graph = self.findChild(QWidget, "polar_widget")  # Get the widget
        self.polar_graph.setLayout(QVBoxLayout())
        self.polar_graph.layout().addWidget(self.polar_canvas)  # Add canvas to the layout
        self.timer = QTimer()
        self.timer.timeout.connect(self.plot_next_point)
        self.play_button = self.findChild(QPushButton, "polar_toggle_button")
        self.browse_button = self.findChild(QPushButton, "polar_upload_button")
        self.clear_button = self.findChild(QPushButton, "polar_clear_button")
        self.browse_button.clicked.connect(self.upload_file)
        self.clear_button.clicked.connect(self.clear_plot)
        self.play_button.clicked.connect(self.toggle_play_pause)

    def clear_plot(self):
        self.polar_ax.clear()
        self.polar_canvas.draw()  # Refresh the canvas
        self.current_index = 0
        self.signal = None

    def plot_next_point(self):
        """Plot the next point in the signal incrementally."""
        if self.signal and self.current_index < len(self.signal['x']):
            # Get the next point's coordinates
            x = self.signal['x'][self.current_index]
            y = self.signal['y'][self.current_index]

            normalized_y = (y - np.min(self.signal['y'])) / (np.max(self.signal['y']) - np.min(self.signal['y']))
            self.polar_ax.plot([0, x], [0, normalized_y], color='g', linestyle='-')
            self.polar_canvas.draw()
            self.current_index += 5
        else:
            self.timer.stop()

    def toggle_play_pause(self):
        """Toggle between play and pause states."""
        if self.timer.isActive():
            self.timer.stop()  # Pause the timer
        else:
            self.current_index = 0  # Restart plotting from the beginning
            self.timer.start(1)

    def upload_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select File", "",
                                                   "CSV Files (*.csv);;Excel Files (*.xls *.xlsx);;Text Files ("
                                                   "*.txt);;All Files (*)",
                                                   options=options)
        if file_name:
            self.signal = extract_signal_data(file_name)
            # if signal:
            #     self.display_polar_signal(signal)

    def display_polar_signal(self, signal):
        self.signal = signal  # Store the signal for updates
        plot_polar(signal, self.polar_ax, self.polar_canvas)


if __name__ == "__main__":
    app = QApplication([])
    window = NonRectangularPlot()
    window.setWindowTitle("Non-rectangular Plot")
    window.show()
    sys.exit(app.exec())
