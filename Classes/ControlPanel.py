
import sys
import os
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import QMainWindow, QFileDialog
import pyqtgraph as pg

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
ui, _ = loadUiType("D:/3SBME26/3-Third Year/1-First Term/1-DSP/Tasks/0-MostafaMousaControl_PanelTask/Signal-Viewer/UI/ControlsPanels.ui")

class MainApp(QMainWindow, ui):
    def __init__(self):
        super(MainApp, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Control Panel')
        
        # Connect buttons to their respective methods
        self.link_channels.clicked.connect(self.link_graphs)
        self.channel_1_pause_btn.clicked.connect(self.pause_play_channel_1)
        self.channel_1_rewind.clicked.connect(self.rewind_channel_1)
        self.channel_1_zoom_in.clicked.connect(self.zoom_in_channel_1)
        self.channel_1_zoom_out.clicked.connect(self.zoom_out_channel_1)
        self.channel_1_reset_zoom.clicked.connect(self.reset_zoom_channel_1)
        self.channel_1_auto_pan.clicked.connect(self.auto_pan_channel_1)
        self.channel_1_speed_slider.valueChanged.connect(self.change_speed_channel_1)
        self.channel_1_horizontal_scroll_slider.valueChanged.connect(self.scroll_channel_1)
        
        self.channel_2_pause_btn.clicked.connect(self.pause_play_channel_2)
        self.channel_2_rewind.clicked.connect(self.rewind_channel_2)
        self.channel_2_zoom_in.clicked.connect(self.zoom_in_channel_2)
        self.channel_2_zoom_out.clicked.connect(self.zoom_out_channel_2)
        self.channel_2_reset_zoom.clicked.connect(self.reset_zoom_channel_2)
        self.channel_2_auto_pan.clicked.connect(self.auto_pan_channel_2)
        self.channel_2_speed_slider.valueChanged.connect(self.change_speed_channel_2)
        self.channel_2_horizontal_scroll_slider.valueChanged.connect(self.scroll_channel_2)
        
        self.show()

    def browse_signal_file(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Signal File", "", "All Files (*);;Signal Files (*.sig)", options=options)
        if fileName:
            print(f"File selected: {fileName}")
            # Load and display the signal file
            self.load_signal(fileName)

    def load_signal(self, file_path):
        # Implement the logic to load and display the signal from the file
        pass

    def link_graphs(self):
        # Implement the logic to link/unlink the graphs
        pass

    def pause_play_channel_1(self):
        # Implement the logic to pause/play the signal for channel 1
        pass

    def rewind_channel_1(self):
        # Implement the logic to rewind the signal for channel 1
        pass

    def zoom_in_channel_1(self):
        # Implement the logic to zoom in the signal for channel 1
        pass

    def zoom_out_channel_1(self):
        # Implement the logic to zoom out the signal for channel 1
        pass

    def reset_zoom_channel_1(self):
        # Implement the logic to reset zoom for channel 1
        pass

    def auto_pan_channel_1(self):
        # Implement the logic to auto pan the signal for channel 1
        pass

    def change_speed_channel_1(self):
        # Implement the logic to change speed for channel 1
        pass

    def scroll_channel_1(self):
        # Implement the logic to scroll the signal for channel 1
        pass

    def pause_play_channel_2(self):
        # Implement the logic to pause/play the signal for channel 2
        pass

    def rewind_channel_2(self):
        # Implement the logic to rewind the signal for channel 2
        pass

    def zoom_in_channel_2(self):
        # Implement the logic to zoom in the signal for channel 2
        pass

    def zoom_out_channel_2(self):
        # Implement the logic to zoom out the signal for channel 2
        pass

    def reset_zoom_channel_2(self):
        # Implement the logic to reset zoom for channel 2
        pass

    def auto_pan_channel_2(self):
        # Implement the logic to auto pan the signal for channel 2
        pass

    def change_speed_channel_2(self):
        # Implement the logic to change speed for channel 2
        pass

    def scroll_channel_2(self):
        # Implement the logic to scroll the signal for channel 2
        pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    sys.exit(app.exec_())
