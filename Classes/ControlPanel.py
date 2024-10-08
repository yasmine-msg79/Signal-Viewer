
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

  

    def toggle_play_pause(self):
        if self.current_graph == self.graph1:
            if self.is_playing[0]["is_playing"]:
                self.is_playing[0]["is_playing"] = False
                self.playButton.setText('Play')
                self.set_icon("Icons/play-svgrepo-com.svg")
                last_data = self.get_last_data_point("graph1")[0]
                self.graph1.setLimits(xMin=0)
                self.graph1.setLimits(yMin=-0.5, yMax=1)
            else:
                self.is_playing[0]["is_playing"] = True
                self.playButton.setText('Pause')
                self.set_icon("Icons/pause.svg")

        elif self.current_graph == self.graph2:
            if self.is_playing[1]["is_playing"]:
                self.is_playing[1]["is_playing"] = False
                self.playButton.setText('Play')
                self.set_icon("Icons/play-svgrepo-com.svg")
                last_data = self.get_last_data_point("graph2")[0]
                self.graph2.setLimits(xMin=0, xMax=last_data)
                self.graph2.setLimits(yMin=-0.5, yMax=1)

            else:
                self.is_playing[1]["is_playing"] = True
                self.playButton.setText('Pause')
                self.set_icon("Icons/pause.svg")
                # Allow free panning when playing
                # self.set_panning_limits(self.graph2, False)

        else:  # link mode
            for graph in self.is_playing:
                if graph["is_playing"]:
                    graph["is_playing"] = False
                    self.playButton.setText('Play')
                    self.set_icon("Icons/play-svgrepo-com.svg")
                    # Restrict panning beyond the last data point when pausing
                    # self.set_panning_limits(self.current_graph, True)
                    self.graph1.setLimits(xMin=0, xMax=last_data)
                    self.graph2.setLimits(xMin=0, xMax=last_data)
                    self.graph1.setLimits(yMin=-0.5, yMax=1)
                    self.graph2.setLimits(yMin=-0.5, yMax=1)
                else:
                    graph["is_playing"] = True
                    self.playButton.setText('Pause')
                    self.set_icon("Icons/pause.svg")
                    # Allow free panning when playing
                    # self.set_panning_limits(self.current_graph, False)

    def rewind_graph(self):
        if (self.current_graph == self.graph1):
            self.initialize_data()
            self.current_graph.clear()
            self.assign_colors(self.get_graph_name())
        elif (self.current_graph == self.graph2):
            self.initialize_data()
            self.current_graph.clear()
            self.assign_colors(self.get_graph_name())
        else:  # link mode
            self.initialize_data()
            self.current_graph[0].clear()
            self.current_graph[1].clear()

            for signal_path in self.graph1_signals_paths:
                # so that the plot appears only on its corresponding graph
                self.sourceGraph = "graph1"
                self.assign_colors(self.sourceGraph)
            for signal_path in self.graph2_signals_paths:
                self.sourceGraph = "graph2"
                self.assign_colors(self.sourceGraph)
            self.sourceGraph = "both"  # so that the controls apply to both graphs

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
