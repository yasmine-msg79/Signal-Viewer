import sys

from PyQt5 import uic
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QVBoxLayout, QFrame, QPushButton
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import pandas as pd


def plot_polar(signal, polar_ax, polar_canvas):
    theta = np.linspace(0, 2 * np.pi, len(signal['x']))
    r = signal['y']

    polar_ax.clear()  # Clear previous plots
    polar_ax.set_ylim(-2, 2)  # Keep the plot range normalized
    polar_ax.plot(theta, r, marker='o', color='g', linewidth=2)  # Plot the signal
    polar_canvas.draw()


def create_polar_plot():
    figure = Figure()
    figure.patch.set_facecolor('black')
    ax = figure.add_subplot(111, polar=True)  # Polar axis
    ax.set_facecolor('black')
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


class NonRectangularPlot(QWidget):
    def __init__(self):
        super(NonRectangularPlot, self).__init__()
        uic.loadUi(r"..\UI\Non_rectangular.ui", self)
        self.polar_canvas, self.polar_ax = create_polar_plot()
        self.polar_graph = self.findChild(QWidget, "polar_widget")  # Get the widget
        self.polar_graph.setLayout(QVBoxLayout())
        self.polar_graph.layout().addWidget(self.polar_canvas)  # Add canvas to the layout
        self.timer = QTimer()
        self.play_button = self.findChild(QPushButton, "polar_toggle_button")
        self.browse_button =self.findChild(QPushButton, "polar_upload_button")
        self.clear_button = self.findChild(QPushButton, "polar_clear_button")
        self.browse_button.clicked.connect(self.upload_file)

    def upload_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select File", "",
                                                   "CSV Files (*.csv);;Excel Files (*.xls *.xlsx);;Text Files ("
                                                   "*.txt);;All Files (*)",
                                                   options=options)
        if file_name:
            signal = extract_signal_data(file_name)
            if signal:
                self.display_polar_signal(signal)

    def display_polar_signal(self, signal):
        self.timer.stop()  # Stop any existing timer
        plot_polar(signal, self.polar_ax, self.polar_canvas)  # Plot the signal

        # Optional: Restart timer if you want dynamic updates
        self.timer.timeout.connect(lambda: plot_polar(signal, self.polar_ax, self.polar_canvas))
        self.timer.start(100)


if __name__ == "__main__":
    app = QApplication([])
    window = NonRectangularPlot()
    window.setWindowTitle("Non-rectangular Plot")
    window.show()
    sys.exit(app.exec_())
