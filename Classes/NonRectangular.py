import sys
import numpy as np
import pandas as pd

from PyQt6 import uic
from PyQt6.QtCore import QTimer
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QFileDialog, QVBoxLayout, QDialog, QMainWindow
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class NonRectangularPlot(QDialog):
    def __init__(self, *args, **kwargs):
        super(NonRectangularPlot, self).__init__(*args, **kwargs)
        uic.loadUi(r"UI\Non_rectangular.ui", self)
        self.signal_data = None
        self.current_index = 0
        self.is_playing = False

        self.polar_canvas, self.polar_ax = self.create_polar_plot()
        self.polar_graph = self.findChild(QWidget, "polar_widget")
        layout = QVBoxLayout()
        # Changed alignment syntax for PyQt6
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.polar_graph.setLayout(layout)
        self.polar_graph.layout().addWidget(self.polar_canvas)

        # Connect buttons
        self.polar_upload_button.clicked.connect(self.upload_signal)
        self.polar_toggle_button.clicked.connect(self.toggle_play_pause)
        self.polar_clear_button.clicked.connect(self.clear_signal)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_signal)

    def upload_signal(self):
        # Updated QFileDialog syntax for PyQt6
        file_name, _ = QFileDialog.getOpenFileName(
            parent=self,
            caption="Select Signal File",
            directory="",
            filter="CSV Files (*.csv);;All Files (*)"
        )
        if file_name:
            self.load_signal_data(file_name)

    # Rest of the methods remain the same as they don't require PyQt6-specific changes
    def create_polar_plot(self):
        figure = Figure()
        figure.patch.set_facecolor('black')
        ax = figure.add_subplot(111, polar=True)
        ax.set_facecolor('black')
        ax.set_ylim(0, 0.7)
        ax.tick_params(colors='white')
        ax.grid(color='gray', linestyle='--', linewidth=0.5)
        canvas = FigureCanvas(figure)
        return canvas, ax

    def load_signal_data(self, file_name):
        try:
            data = pd.read_csv(file_name)
            self.signal_data = (data.iloc[:, 0].values, data.iloc[:, 1].values)
            self.current_index = 0
            self.polar_toggle_button.setEnabled(True)
            self.polar_clear_button.setEnabled(True)
            self.start_signal()
        except Exception as e:
            print(f"Error loading signal data: {e}")

    # ... [rest of the methods remain the same]
    def toggle_play_pause(self):
        if self.is_playing:
            self.stop_signal()
        else:
            self.start_signal()

    def start_signal(self):
        self.is_playing = True
        self.polar_toggle_button.setText("Pause")
        self.timer.start(100)

    def stop_signal(self):
        self.is_playing = False
        self.polar_toggle_button.setText("Play")
        self.timer.stop()

    def clear_signal(self):
        self.stop_signal()
        self.signal_data = None
        self.current_index = 0
        self.polar_ax.clear()
        self.polar_canvas.draw()
        self.polar_toggle_button.setEnabled(False)
        self.polar_clear_button.setEnabled(False)

    def update_signal(self):
        if self.signal_data:
            time_data, voltage_data = self.signal_data
            self.polar_ax.clear()
            if self.current_index < len(time_data):
                theta = (time_data[self.current_index] - time_data[0]) / (time_data[-1] - time_data[0]) * 2 * np.pi
                self.polar_ax.plot(theta, voltage_data[self.current_index], 'o', color='#FF0000')
                if self.current_index > 0:
                    self.polar_ax.plot(np.linspace(0, 2 * np.pi, self.current_index + 1), voltage_data[:self.current_index + 1], color='#00FF00')
                self.current_index += 1
            self.polar_ax.set_title("ECG Signals in Polar Coordinates")
            self.polar_ax.set_ylim([np.min(voltage_data), np.max(voltage_data)])
            self.polar_canvas.draw()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Radar Signal Viewer")
        self.setFixedSize(570, 450)
        self.radar_viewer = NonRectangularPlot()
        self.setCentralWidget(self.radar_viewer)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())  # Note: in PyQt6, exec() doesn't need parentheses
