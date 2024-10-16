
# ************************************** Importing Libraries **************************************

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QColorDialog, QListWidgetItem, QMessageBox, QDialogButtonBox
import wfdb
import numpy as np
import sys
from PyQt6.QtGui import QShortcut, QKeySequence, QIcon
from pyqtgraph.Qt import QtCore
from PyQt6 import QtWidgets, uic
import pyqtgraph as pg
import csv
from fpdf import FPDF
from pyqtgraph.exporters import ImageExporter
import os
import qdarkstyle
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtGui import QPainter
import pyqtgraph.exporters
from pyqtgraph import PlotWidget
import random
from PyQt6.QtCore import Qt
# Added new libraries
from PyQt6.QtWidgets import QInputDialog
import psutil
import requests


class RealTimeCpuPlot(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(RealTimeCpuPlot, self).__init__(*args, **kwargs)
        
        # Set window title and size
        self.setWindowTitle("Real-Time CPU Usage")
        self.setGeometry(100, 100, 800, 600)
        
        # Create layout and plot widget
        self.layout = QtWidgets.QVBoxLayout(self)
        self.plot_widget = pg.PlotWidget()
        self.layout.addWidget(self.plot_widget)
        
        # Initialize plot data
        self.plot_data = self.plot_widget.plot()
        
        # Set labels and legend for the plot
        self.plot_widget.setLabel('left', 'CPU Usage (%)')
        self.plot_widget.setLabel('bottom', 'Time (s)')
        self.plot_widget.addLegend()
        self.plot_data = self.plot_widget.plot(name="CPU Usage")
        
        # Set up a timer to update the plot every second
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)
        
        # Initialize data list to store CPU usage values
        self.data = []

    def update_plot(self):
        # Get current CPU usage
        cpu_usage = psutil.cpu_percent()
        
        # Append the CPU usage to the data list
        self.data.append(cpu_usage)
        
        # Keep only the last 100 data points
        if len(self.data) > 100:
            self.data.pop(0)
        
        # Update the plot with the new data
        self.plot_data.setData(self.data)





from PyQt6.QtWidgets import QInputDialog, QMessageBox
# from pyqtgraph import PolarPlotItem

from scipy import interpolate 

class MainWindow(QtWidgets.QMainWindow):
    
# ************************************** Start  the main  functions for our application   **************************************



    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        
        # Variabeles
        
        # Initialize signal data structures
        self.signals = {"graph1": [], "graph2": []}
        self.signals_lines = {"graph1": [], "graph2": []}
        self.signals_info = {"graph1": [], "graph2": []}
        self.channels_color = {'graph1': [], 'graph2': []}
        self.graph1_signals_paths = []
        self.graph2_signals_paths = []

        # Play/Pause State
        self.is_playing = [{"graph": "graph1", "is_playing": True}, {
            "graph": "graph2", "is_playing": False}]

        # Link Mode
        self.sourceGraph = "both"  # flag for link mode
        self.graph_mapping = {"graph1": 0, "graph2": 1, "both": 2}

        self.transfer_button1_state = False
        self.transfer_button2_state = False

        # Other Attributes
        self.data_index = {"graph1": 5, "graph2": 5}
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)

        # Initialize the UI
        self.init_ui()

    def init_ui(self):
        # Load the UI Page
        self.ui = uic.loadUi('MainWindowAppLastEND.ui', self)
        self.setWindowTitle("Multi-Channel Signal Viewer Team 1")
            # self.setWindowIcon(QIcon("Icons/ECG.png"))



        # Access the PlotWidgets created in Qt Designer
        self.graph1 = self.findChild(PlotWidget, 'graph1')
        self.graph2 = self.findChild(PlotWidget, 'graph2')
        

   


        self.lookup = {"graph1": self.graph1, "graph2": self.graph2}
        self.current_graph = self.graph1  # default value
        self.current_graph.clear()

        # Initialize channel selection
        self.channels_selected = {"graph1": 0, "graph2": 0}

        self.stat_lst = []

        self.channelsGraph1.addItem("All Channels")
        self.channelsGraph2.addItem("All Channels")

        # Set labels and grid visibility for graphs
        self.graph1.setLabel("bottom", "Time")
        self.graph1.setLabel("left", "Amplitude")
        self.graph2.setLabel("bottom", "Time")
        self.graph2.setLabel("left", "Amplitude")
        self.graph1.showGrid(x=True, y=True)
        self.graph2.showGrid(x=True, y=True)

        # Apply CSS to make fonts bold
        self.setStyleSheet("""
            QPushButton, QComboBox, QLabel {
                font-weight: bold;
            }
        """)

        # Connect signals to slots

        self.importButton.clicked.connect(self.browse)
        self.connectButton.clicked.connect(self.connectFunction)
        self.timer.timeout.connect(self.update_plot_data)
        self.playButton.clicked.connect(self.toggle_play_pause)
        self.linkButton.clicked.connect(self.link_graphs)
        self.hideButton.clicked.connect(self.hide_Show_graph)
        self.rewindButton.clicked.connect(self.rewind_graph)
        self.zoomIn.clicked.connect(self.zoom_in)
        self.zoomOut.clicked.connect(self.zoom_out)
        self.glue_Button.clicked.connect(self.glue_graphs)
        self.snapshot_Button.clicked.connect(self.take_snapshot)
        self.reportButton.clicked.connect(self.generate_signal_report)



        

        # Set speed slider properties
        self.speedSlider.setMinimum(0)
        self.speedSlider.setMaximum(100)
        self.speedSlider.setSingleStep(3)
        self.speedSlider.setValue(self.data_index[self.get_graph_name()])
        self.speedSlider.valueChanged.connect(self.change_speed)

        # Connect color buttons to channel color picking
        self.colorButtonGraph1.clicked.connect(self.pick_channel_color)
        self.colorButtonGraph2.clicked.connect(self.pick_channel_color)

        # Connect graph selection combo box to graph change
        self.graphSelection.currentIndexChanged.connect(
            self.update_selected_graph)

        # Connect channel combo boxes to channel change
        self.channelsGraph1.currentIndexChanged.connect(
            lambda i, graph="graph1": self.handle_selected_channels_change(graph, i))
        self.channelsGraph2.currentIndexChanged.connect(
            lambda i, graph="graph2": self.handle_selected_channels_change(graph, i))

        # Connect delete buttons to channel deletion
        self.deleteButtonGraph1.clicked.connect(self.delete_selected_ch)
        self.deleteButtonGraph2.clicked.connect(self.delete_selected_ch)

        # Connect label text input to channel label change
        self.addLabelGraph1.returnPressed.connect(self.change_channel_label)
        self.addLabelGraph2.returnPressed.connect(self.change_channel_label)
        # self.signal_Link_Label.returnPressed.connect(self.signal_Link)


        # Connect hide list items to item checking/unchecking
        self.hideList1.itemChanged.connect(self.on_item_checked)
        self.hideList2.itemChanged.connect(self.on_item_checked)
        self.hideList1.itemChanged.connect(self.on_item_unchecked)
        self.hideList2.itemChanged.connect(self.on_item_unchecked)

        self.transferButtonGraph1_2.clicked.connect(self.button1_clicked)
        self.transferButtonGraph2_1.clicked.connect(self.button2_clicked)
        self.transferButtonGraph1_2.clicked.connect(self.transfer_signal)
        self.transferButtonGraph2_1.clicked.connect(self.transfer_signal)

        # Connect label text input to adding legends
        self.addLabelGraph1.returnPressed.connect(
            lambda: self.add_legend("graph1"))
        self.addLabelGraph2.returnPressed.connect(
            lambda: self.add_legend("graph2"))
        



# ************************************** HELPER FUNCTIONS **************************************
    
    # Recognization
    def get_graph_name(self):
        if self.current_graph == self.graph1:
            return "graph1"
        elif self.current_graph == self.graph2:
            return "graph2"
        else:
            return self.sourceGraph
    
    # Transfer Button 
    def button1_clicked(self):
        self.transfer_button1_state = True

    def button2_clicked(self):
        self.transfer_button2_state = True

    def get_curr_graph_channels(self):
        if self.get_graph_name() == "graph1":
            return self.channelsGraph1
        else:
            return self.channelsGraph2

     # After Hide- Clear
    
    def get_curr_graph_list(self):
        if self.get_graph_name() == "graph1":
            return self.fill_list1()
        else:
            return self.fill_list2()
    
    def fill_list1(self):
        self.hideList1.clear()
        for i in range(self.channelsGraph1.count()-1):
            text = self.channelsGraph1.itemText(i+1)
            item = QListWidgetItem(text)
            item.setCheckState(Qt.CheckState.Checked)
            self.hideList1.addItem(item)
   
    def fill_list2(self):
        self.hideList2.clear()
        for i in range(self.channelsGraph2.count()-1):
            text = self.channelsGraph2.itemText(i+1)
            item = QListWidgetItem(text)
            item.setCheckState(Qt.CheckState.Checked)
            self.hideList2.addItem(item)
    #  Hide - Clear
    def clear_curr_graph_list(self):
        if self.get_graph_name() == "graph1":
            return self.hideList1.clear()
        else:
            return self.hideList2.clear()
    
    # Load
    def get_graph_paths(self):
        if self.get_graph_name() == "graph1":
            return self.graph1_signals_paths
        else:
            return self.graph2_signals_paths
    
    #  Silly Function
    def set_icon(self, icon_path):
        # Load an icon
        icon = QIcon(icon_path)
        # Set the icon for the button
        self.playButton.setIcon(icon)

    def get_unchecked_indexes(self, listWidget):
        unchecked_indexes = []
        for i in range(listWidget.count()):
            item = listWidget.item(i)
            if item.checkState() == Qt.CheckState.Unchecked:
                unchecked_indexes.append(i)
        return unchecked_indexes

    def get_checked_indexes(self, listWidget):
        checked_indexes = []
        for i in range(listWidget.count()):
            item = listWidget.item(i)
            if item.checkState() == Qt.CheckState.Checked:
                checked_indexes.append(i)
        return checked_indexes
    
    def on_item_unchecked(self):
        # Get the indexes of unchecked items in hideList1
        unchecked_indexes_list1 = self.get_unchecked_indexes(self.hideList1)
        for index in unchecked_indexes_list1:
            # Set the pen color of the corresponding signal line in graph1 to black
            self.signals_lines['graph1'][index].setPen((0, 0, 0))
        
        # Get the indexes of unchecked items in hideList2
        unchecked_indexes_list2 = self.get_unchecked_indexes(self.hideList2)
        for index in unchecked_indexes_list2:
            # Set the pen color of the corresponding signal line in graph2 to black
            self.signals_lines['graph2'][index].setPen((0, 0, 0))

    def on_item_checked(self):
        # Get the indexes of checked items in hideList1
        checked_indexes_list1 = self.get_checked_indexes(self.hideList1)
        for index in checked_indexes_list1:
            # Set the pen color of the corresponding signal line in graph1 to its original color
            self.signals_lines['graph1'][index].setPen(
                self.channels_color['graph1'][index])
        
        # Get the indexes of checked items in hideList2
        checked_indexes_list2 = self.get_checked_indexes(self.hideList2)
        for index in checked_indexes_list2:
            # Set the pen color of the corresponding signal line in graph2 to its original color
            self.signals_lines['graph2'][index].setPen(
                self.channels_color['graph2'][index])

    def show_error_message(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.exec()

    def sudden_appearing(self, graph, j):
        (time, data), end_ind = self.signals[graph][j]
        signal_line = self.signals_lines[graph][j]
        X = time[:end_ind]
        Y = data[:end_ind]
        signal_line.setData(X, Y, visible=True)

    def sudden_disappearing(self, graph, j):
        self.signals_lines[graph][j].setData([], [], visible=False)

    def handle_selected_channels_change(self, graph, i):
        self.channels_selected[graph] = i

        if self.channels_selected[graph] == 0:  #NO Channels Selected
            for j in range(len(self.signals_lines[graph])):
                self.signals_info[graph][j][0] = True
                self.sudden_appearing(graph, j)

        else:
            selected_channel_index = self.channels_selected[graph] - 1
            for j in range(len(self.signals_lines[graph])):
                if j == selected_channel_index:
                    self.signals_info[graph][j][0] = True
                    # sudden appearing
                    self.sudden_appearing(graph, j)

                else:
                    self.signals_info[graph][j][0] = False
                    # sudden disappearing
                    self.sudden_disappearing(graph, j)

    def initialize_data(self,):
        if (self.current_graph == self.graph1):
            self.signals["graph1"] = []
            self.signals_lines["graph1"] = []
        elif (self.current_graph == self.graph2):
            self.signals["graph2"] = []
            self.signals_lines["graph2"] = []
        else:
            self.signals = {"graph1": [], "graph2": []}
            self.signals_lines = {"graph1": [], "graph2": []}

    #Select Graph ComboBox
    def update_selected_graph(self, index):
        if index == 0:  # to graph1
            self.current_graph = self.graph1
            self.speedSlider.setValue(self.data_index["graph1"])
            # graph2 is playing and graph1 is not
            if self.is_playing[1]["is_playing"] and self.is_playing[0]["is_playing"] == False:
                self.playButton.setText('Play')
                self.set_icon("Icons/play-svgrepo-com.svg")
            # graph2 is not playing and graph1 is not
            elif self.is_playing[1]["is_playing"] == False and self.is_playing[0]["is_playing"] == False:
                self.playButton.setText('Play')
                # self.set_icon("Icons/play-svgrepo-com.svg")
            # graph2 is playing graph1 is playing
            elif self.is_playing[1]["is_playing"] and self.is_playing[0]["is_playing"]:
                self.playButton.setText('Pause')
                # self.set_icon("Icons/pause.svg")
            # graph2 is not playing and graph1 is playing
            elif self.is_playing[1]["is_playing"] == False and self.is_playing[0]["is_playing"]:
                self.playButton.setText('Pause')
                # self.set_icon("Icons/pause.svg")

        elif index == 1: # Graph 2
            self.current_graph = self.graph2  # to graph2
            self.speedSlider.setValue(self.data_index["graph2"])
            # graph2 is playing and graph1 is not
            if self.is_playing[1]["is_playing"] and self.is_playing[0]["is_playing"] == False:
                self.playButton.setText('Pause')
                self.set_icon("Icons/pause.svg")
            # graph2 is not playing and graph1 is not
            elif self.is_playing[1]["is_playing"] == False and self.is_playing[0]["is_playing"] == False:
                self.playButton.setText('Play')
                self.set_icon("Icons/play-svgrepo-com.svg")
            # graph2 is playing graph1 is playing
            elif self.is_playing[1]["is_playing"] and self.is_playing[0]["is_playing"]:
                self.playButton.setText('Pause')
                self.set_icon("Icons/pause.svg")
            # graph2 is not playing and graph1 is playing
            elif self.is_playing[1]["is_playing"] == False and self.is_playing[0]["is_playing"]:
                self.playButton.setText('Play')
                self.set_icon("Icons/play-svgrepo-com.svg")

        elif index == 2:
            self.current_graph = [self.graph1, self.graph2]
            self.data_index["graph2"] = 5
            self.data_index["graph1"] = 5
            self.speedSlider.setValue(self.data_index["graph1"])
            for graph in self.is_playing:
                graph["is_playing"] = True

    def get_index(self):
        index = self.channelsGraph1.currentIndex()
        return index
    
    # Colors Buttons
    def generate_random_color(self):
        while True:
            # Generate random RGB values
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)

            # Calculate brightness using a common formula
            brightness = (red * 299 + green * 587 + blue * 114) / 1000

            # Check if the color is not too light (adjust the threshold as needed)
            if brightness > 100:
                return red, green, blue



        # ************************************** Plot Graphs **************************************
    

    def browse(self):
        # Define the file filter for the file dialog
        file_filter = "Raw Data (*.csv *.txt *.xls *.hea *.dat *.rec)"
        
        # Open a file dialog to select a signal file
        self.file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, 'Open Signal File', './', filter=file_filter)

        # Check if the current graph is graph1 and a file path is selected
        if self.current_graph == self.graph1 and self.file_path:
            # Append the file path to graph1's signal paths
            self.graph1_signals_paths.append(self.file_path)
            # Add a new channel to the channels combo box for graph1
            self.channelsGraph1.addItem(
                f"Channel{len(self.signals['graph1']) + 1}")
            # Fill the hide list for graph1
            self.fill_list1()
            # Append a new signal info entry for graph1
            self.signals_info["graph1"].append([True, None, None])

        # Check if the current graph is graph2 and a file path is selected
        elif self.current_graph == self.graph2 and self.file_path:
            # Append the file path to graph2's signal paths
            self.graph2_signals_paths.append(self.file_path)
            # Add a new channel to the channels combo box for graph2
            self.channelsGraph2.addItem(
                f"Channel{len(self.signals['graph2']) + 1}")
            # Fill the hide list for graph2
            self.fill_list2()
            # Append a new signal info entry for graph2
            self.signals_info["graph2"].append([True, None, None])

        # Check if both graphs are selected and a file path is selected
        elif self.current_graph == [self.graph1, self.graph2] and self.file_path:
            # Append the file path to both graph1's and graph2's signal paths
            self.graph1_signals_paths.append(self.file_path)
            self.graph2_signals_paths.append(self.file_path)
            # Add a new channel to the channels combo box for both graphs
            self.channelsGraph1.addItem(
                f"Channel{len(self.signals['graph1']) + 1}")
            self.fill_list1()
            self.channelsGraph2.addItem(
                f"Channel{len(self.signals['graph2']) + 1}")
            self.fill_list2()
            # Append a new signal info entry for both graphs
            self.signals_info["graph1"].append([True, None, None])
            self.signals_info["graph2"].append([True, None, None])

        # If a file path is selected, open the file
        if self.file_path:
            self.open_file(self.file_path)

 
    def signal_Link(self):
        """
        Prompts the user to enter the link of the signal from a website that emits a signal in real time.
        """
        link, ok = QInputDialog.getText(self, 'Enter Signal Link', 'Enter the link of the signal:')
        if ok and link:
            self.signal_Link_Label.setText(link)
            return link
        return None

    # import psutil
    # import datetime
    # import time
    # import threading
    # from PyQt5.QtWidgets import QVBoxLayout, QWidget
    # import pyqtgraph as pg
    # import matplotlib.dates as mdates
    
    def connectFunction(self):
        # i want when i click on this buttin the new window apear and run RealTimeDataCPU_Usage python file
        
        # Create a new window for the real-time CPU usage plot
        self.real_time_cpu_plot = RealTimeCpuPlot()
        self.real_time_cpu_plot.show()

        

    def open_file(self, path: str):
        # Initialize time and data lists
        self.time = []
        self.data = []
        self.fsampling = 1  # Default sampling frequency

        # Determine the file type based on the file extension
        filetype = path[-3:]

        # Handle WFDB file types
        if filetype in ["hea", "rec", "dat"]:
            self.record = wfdb.rdrecord(path[:-4], channels=[0])
            self.data = np.concatenate(self.record.p_signal)
            self.fsampling = self.record.fs
            self.time = np.arange(len(self.data)) / self.fsampling

        # Handle CSV, TXT, and XLS file types
        if filetype in ["csv", "txt", "xls"]:
            with open(path, 'r') as data_file:
                data_reader = csv.reader(data_file, delimiter=',')
                for row in data_reader:
                    time_value = float(row[0])
                    amplitude_value = float(row[1])
                    self.time.append(time_value)
                    self.data.append(amplitude_value)

        # Initialize data_x and data_y lists
        self.data_x = []
        self.data_y = []

        # Check which graph is currently selected and update accordingly
        if self.current_graph == self.graph1:
            # Append the signal data to graph1
            self.signals["graph1"].append([(self.time, self.data), 50])
            self.is_playing[0]["is_playing"] = True
            self.playButton.setText('Pause')
            self.set_icon("Icons/pause.svg")
            self.plot_graph_signal()

        elif self.current_graph == self.graph2:
            # Append the signal data to graph2
            self.signals["graph2"].append([(self.time, self.data), 50])
            self.is_playing[1]["is_playing"] = True
            self.playButton.setText('Pause')
            self.set_icon("Icons/pause.svg")
            self.plot_graph_signal()

        else:
            # Handle the case where both graphs are linked
            if self.sourceGraph == "both":
                # Append the signal data to both graphs
                self.signals["graph1"].append([(self.time, self.data), 50])
                self.is_playing[0]["is_playing"] = True
                self.signals["graph2"].append([(self.time, self.data), 50])
                self.is_playing[1]["is_playing"] = True
                self.playButton.setText('Pause')
                self.set_icon("Icons/pause.svg")
                self.plot_common_linked_signal()

            # Handle the case where only graph1 is the source
            elif self.sourceGraph == "graph1":
                self.signals["graph1"].append([(self.time, self.data), 50])
                self.is_playing[0]["is_playing"] = True
                self.playButton.setText('Pause')
                self.set_icon("Icons/pause.svg")
                self.plot_unique_linked_signal()

            # Handle the case where only graph2 is the source
            elif self.sourceGraph == "graph2":
                self.signals["graph2"].append([(self.time, self.data), 50])
                self.is_playing[1]["is_playing"] = True
                self.playButton.setText('Pause')
                self.set_icon("Icons/pause.svg")
                self.plot_unique_linked_signal()

    def plot_graph_signal(self):
        if len(self.signals[self.get_graph_name()]) == 1:
            pen = pg.mkPen((self.generate_random_color()))
            self.data_x = self.time[:50]
            self.data_y = self.data[:50]
            curve = self.current_graph.plot(
                self.data_x, self.data_y, pen=pen)
            self.signals_lines[self.get_graph_name()].append(curve)
            self.channels_color[self.get_graph_name()].append(pen)
            self.signals_info[self.get_graph_name()][0][1] = pen
        else:
            pen = pg.mkPen((self.generate_random_color()))
            curr_index = len(self.signals[self.get_graph_name()]) - 1
            end_ind = self.signals[self.get_graph_name()][0][1]
            self.signals[self.get_graph_name()][-1] = [(self.time,
                                                        self.data), end_ind]
            self.data_x = self.time[:end_ind]
            self.data_y = self.data[:end_ind]
            curve = self.current_graph.plot(self.data_x, self.data_y, pen=pen)
            self.signals_lines[self.get_graph_name()].append(curve)
            self.channels_color[self.get_graph_name()].append(pen)
            self.signals_info[self.get_graph_name()][curr_index][1] = pen

        if not self.timer.isActive():
            self.timer.start(50)

    def plot_common_linked_signal(self):
        for i, graph_name in enumerate(["graph1", "graph2"]):
            if len(self.signals[graph_name]) == 1:
                if self.signals_info[graph_name][0][1] == None:
                    pen = pg.mkPen((self.generate_random_color()))
                    self.channels_color[graph_name].append(pen)
                    self.signals_info[graph_name][0][1] = pen
                else:
                    pen = self.channels_color[graph_name][0]

                self.data_x = self.time[:50]
                self.data_y = self.data[:50]
                curve = self.current_graph[i].plot(
                    self.data_x, self.data_y, pen=pen)
                self.signals_lines[graph_name].append(curve)

            else:
                curr_index = len(self.signals[graph_name]) - 1

                if self.signals_info[graph_name][i][1] == None:
                    pen = pg.mkPen((self.generate_random_color()))
                    self.signals_info[graph_name][curr_index][1] = pen
                    self.channels_color[graph_name].append(pen)
                else:
                    pen = self.signals_info[graph_name][curr_index][1]
                    pen = self.channels_color[graph_name][curr_index]

                end_ind = self.signals[graph_name][0][1]
                self.signals[graph_name][-1] = [(self.time,
                                                    self.data), end_ind]
                self.data_x = self.time[:end_ind]
                self.data_y = self.data[:end_ind]
                curve = self.current_graph[i].plot(
                    self.data_x, self.data_y, pen=pen)
                self.signals_lines[graph_name].append(curve)

        if not self.timer.isActive():
            self.timer.start(50)

    def plot_unique_linked_signal(self):
        if len(self.signals[self.get_graph_name()]) == 1:
            pen = self.channels_color[self.get_graph_name()][0]
            self.data_x = self.time[:50]
            self.data_y = self.data[:50]
            curve = self.lookup[self.get_graph_name()].plot(
                self.data_x, self.data_y, pen=pen)
            self.signals_lines[self.get_graph_name()].append(curve)
        else:
            curr_index = len(self.signals[self.get_graph_name()]) - 1
            pen = self.channels_color[self.get_graph_name()][curr_index]

            end_ind = self.signals[self.get_graph_name()][0][1]
            self.signals[self.get_graph_name()][-1] = [(self.time,
                                                        self.data), end_ind]
            self.data_x = self.time[:end_ind]
            self.data_y = self.data[:end_ind]
            curve = self.lookup[self.get_graph_name()].plot(
                self.data_x, self.data_y, pen=pen)
            self.signals_lines[self.get_graph_name()].append(curve)

        if not self.timer.isActive():
            self.timer.start(50)

    def update_plot_data(self):
        for item in self.is_playing:
            if item["is_playing"]:
                self.updating_graphs(item["graph"])

    def updating_graphs(self, graph: str):
        for i, signal in enumerate(self.signals[graph]):
            (time, data), end_ind = signal
            signal_line = self.signals_lines[graph][i]

            X = time[:end_ind + self.data_index[graph]]
            Y = data[:end_ind + self.data_index[graph]]
            self.signals[graph][i] = [
                (time, data), end_ind + self.data_index[graph]]
            if (X[-1] < time[-1] / 5):
                self.lookup[graph].setXRange(0, time[-1] / 5)
            else:
                self.lookup[graph].setXRange(
                    X[-1] - time[-1] / 5, X[-1])

            if self.signals_info[graph][i][0]:
                signal_line.setData(X, Y, visible=True)
                last_data = self.get_last_data_point(graph)[0]
                self.lookup[graph].setLimits(xMin=0, xMax=last_data)
            else:
                signal_line.setData([], [], visible=False)

    def link_graphs(self):
        self.update_selected_graph(2)
        self.graphSelection.setCurrentIndex(2)
        for graph in self.is_playing:
            graph["is_playing"] = True


















# ************************************** Transfer signals **************************************








    def update_after_transfer(self, curr_graph, i, item_names):
        if i == 0:
            self.get_curr_graph_channels().clear()
            self.clear_curr_graph_list()
            self.get_curr_graph_channels().addItem(item_names[0])
            self.get_curr_graph_list()
            for i in range(len(self.signals[curr_graph])):
                self.signals[curr_graph][i][1] = self.signals[curr_graph][0][1]
            for i, signal in enumerate(self.signals[curr_graph]):
                pen = self.channels_color[curr_graph][i]
                (time, data), end_ind = signal
                X = time[:end_ind]
                Y = data[:end_ind]
                curve = self.current_graph.plot(X, Y, pen=pen)
                self.signals_lines[curr_graph][i] = curve
                self.get_curr_graph_channels().addItem(
                    item_names[i+1])  # combobox refill
                self.get_curr_graph_list()
            if not self.timer.isActive():
                self.timer.start(50)
        else:
            if curr_graph == "graph1":
                self.channelsGraph1.addItem(item_names)
                self.fill_list1()
            else:
                self.channelsGraph2.addItem(item_names)
                self.fill_list2()
            for item in self.is_playing:
                if item["is_playing"]:
                    for i in range(len(self.signals[item["graph"]])):
                        self.signals[item["graph"]
                                     ][i][1] = self.signals[item["graph"]][0][1]
                    for i, signal in enumerate(self.signals[item["graph"]]):
                        pen = self.channels_color[item["graph"]][i]
                        (time, data), end_ind = signal
                        X = time[:end_ind]
                        Y = data[:end_ind]
                        curve = self.lookup[item["graph"]].plot(
                            X, Y, pen=pen)
                        self.signals_lines[item["graph"]][i] = curve
                    if not self.timer.isActive():
                        self.timer.start(50)

    def transfer_signal(self):
        if self.get_graph_name() == "graph1":  # from graph1 --> graph2
            curr_channel_ind = self.channels_selected["graph1"]
            self.transfer_data_between_globals(curr_channel_ind)
        elif self.get_graph_name() == "graph2":
            curr_channel_ind = self.channels_selected["graph2"]
            self.transfer_data_between_globals(curr_channel_ind)
        else:
            self.show_error_message("Can't transfer, specify a graph!")

    def transfer_data_between_globals(self, i): # i refer to Channel in the Specific Graph 
        if self.get_graph_name() == "graph1" and self.transfer_button1_state:
            source_graph = "graph1"
            drain_graph = "graph2"
            self.transfer_button1_state = False
        elif self.get_graph_name() == "graph2" and self.transfer_button2_state:
            source_graph = "graph2"
            drain_graph = "graph1"
            self.transfer_button2_state = False
        else:
            return
        if i == 0:
            self.signals[drain_graph] += self.signals[source_graph]
            self.signals_lines[drain_graph] += self.signals_lines[source_graph]
            self.signals_info[drain_graph] += self.signals_info[source_graph]

            if source_graph == "graph1":
                self.channels_color["graph2"] += self.channels_color["graph1"]
                temp = [self.channelsGraph1.itemText(
                    i) for i in range(len(self.graph1_signals_paths)+1)]
                if len(self.graph2_signals_paths) == 0:
                    item_names = temp
                else:
                    item_names = [self.channelsGraph2.itemText(i) for i in range(len(self.graph2_signals_paths)+1)] + temp[1:]
                self.graph2_signals_paths += self.graph1_signals_paths
                self.clear_graph1()
                self.graphSelection.setCurrentIndex(1)
                self.update_selected_graph(1)
                self.is_playing[1]["is_playing"] = True
                self.playButton.setText('Pause')
                if self.is_playing[0]["is_playing"]:
                    self.is_playing[0]["is_playing"] = False
                self.update_after_transfer("graph2", i, item_names)
            else:
                self.channels_color["graph1"] += self.channels_color["graph2"]
                temp = [self.channelsGraph2.itemText(
                    i) for i in range(len(self.graph2_signals_paths)+1)]
                if len(self.graph1_signals_paths) == 0:
                    item_names = temp
                else:
                    item_names = [self.channelsGraph1.itemText(
                        i) for i in range(len(self.graph1_signals_paths)+1)] + temp[1:]
                self.graph1_signals_paths += self.graph2_signals_paths
                self.clear_graph2()
                self.graphSelection.setCurrentIndex(0)
                self.update_selected_graph(0)  # cur graph == graph1
                self.is_playing[0]["is_playing"] = True
                self.playButton.setText('Pause')
                if self.is_playing[1]["is_playing"]:
                    self.is_playing[1]["is_playing"] = False
                self.update_after_transfer("graph1", i, item_names)

        else:
            self.signals[drain_graph].append(self.signals[source_graph][i-1])
            self.signals_info[drain_graph].append(
                self.signals_info[source_graph][i-1])
            self.signals_lines[drain_graph].append(
                self.signals_lines[source_graph][i-1])
            self.channels_color[drain_graph].append(
                self.channels_color[source_graph][i-1])

            if source_graph == "graph1":
                self.graph2_signals_paths.append(
                    self.graph1_signals_paths[i-1])
                item_name = self.channelsGraph1.itemText(i)
                self.channelsGraph1.removeItem(i)
                if len(self.signals["graph1"]) == 1:
                    self.is_playing[0]["is_playing"] = False
                    self.clear_graph1()
                    self.graphSelection.setCurrentIndex(1)
                    self.update_selected_graph(1)
                else:
                    self.is_playing[0]["is_playing"] = True
                    self.sudden_disappearing("graph1", i-1)
                    self.delete_selected_ch()
                    self.graphSelection.setCurrentIndex(2)
                    self.update_selected_graph(2)
                self.is_playing[1]["is_playing"] = True
                self.update_after_transfer("graph2", i, item_name)

            else:
                self.graph1_signals_paths.append(
                    self.graph2_signals_paths[i-1])
                item_name = self.channelsGraph2.itemText(i)
                self.channelsGraph2.removeItem(i)
                if len(self.signals["graph2"]) == 1:
                    self.clear_graph2()
                    self.is_playing[1]["is_playing"] = False
                    self.graphSelection.setCurrentIndex(0)
                    self.update_selected_graph(0)
                else:
                    self.is_playing[1]["is_playing"] = True
                    self.sudden_disappearing("graph2", i-1)
                    self.delete_selected_ch()
                    self.graphSelection.setCurrentIndex(2)
                    self.update_selected_graph(2)

                self.is_playing[0]["is_playing"] = True
                self.update_after_transfer("graph1", i, item_name)
















# ************************************** Controllers and Manipulation **************************************











    def delete_selected_ch(self): # i will delete channel
        graph_name = self.get_graph_name()
        if graph_name not in ["graph1", "graph2"]:
            self.show_error_message('Please select a graph first.')
            return

        channelsGraph = self.channelsGraph1 if graph_name == "graph1" else self.channelsGraph2

        curve_index = channelsGraph.currentIndex()
        if curve_index == 0:
            self.show_error_message("No channels selected")
            return

        curve_index_stored = curve_index - 1
        signals = self.signals[graph_name]
        signals_lines = self.signals_lines[graph_name]
        signals_info = self.signals_info[graph_name]
        signals_paths = self.graph1_signals_paths if graph_name == "graph1" else self.graph2_signals_paths
        channels_color = self.channels_color[graph_name]

        del signals[curve_index_stored]
        signals_lines[curve_index_stored].clear()
        del signals_lines[curve_index_stored]
        del signals_info[curve_index_stored]
        del signals_paths[curve_index_stored]
        del channels_color[curve_index_stored]

        channelsGraph.removeItem(len(signals_paths) + 1)
        self.fill_list1() if graph_name == "graph1" else self.fill_list2()
        channelsGraph.setCurrentIndex(0)
        self.channels_selected[graph_name] = channelsGraph.currentIndex()

        if channelsGraph.count() == 1:
            self.graph1.clear() if graph_name == "graph1" else self.graph2.clear()

    def change_speed(self):
        if self.get_graph_name() == "both":
            self.data_index["graph1"] = self.speedSlider.value()
            self.data_index["graph2"] = self.speedSlider.value()
        else:
            self.data_index[self.get_graph_name()] = self.speedSlider.value()

    def zoom_in(self):
        # Scale the viewbox around the specified center point
        if (self.current_graph == self.graph1):
            view_box = self.graph1.plotItem.getViewBox()
            view_box.scaleBy((0.5, 0.5))
        elif (self.current_graph == self.graph2):
            view_box = self.graph2.plotItem.getViewBox()
            view_box.scaleBy((0.5, 0.5))
        else:  # link mode
            for graph in self.current_graph:
                view_box = graph.plotItem.getViewBox()
                view_box.scaleBy((0.5, 0.5))

    def zoom_out(self):
        # Scale the viewbox around the specified center point
        if (self.current_graph == self.graph1):
            view_box = self.graph1.plotItem.getViewBox()
            view_box.scaleBy((1.5, 1.5))
        elif (self.current_graph == self.graph2):
            view_box = self.graph2.plotItem.getViewBox()
            view_box.scaleBy((1.5, 1.5))
        else:  # link mode
            for graph in self.current_graph:
                view_box = graph.plotItem.getViewBox()
                view_box.scaleBy((1.5, 1.5))

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
    
    
    # This function will be called when the user clicks the clear button to hide graph signals only,
    # and convert the hideButton text to Show, and then show them again when clicked on the show button and so on.
    def hide_Show_graph(self):
        graph_name = self.get_graph_name()
        
        if graph_name == "both":
            graphs = ["graph1", "graph2"]
        else:
            graphs = [graph_name]

        if self.hideButton.text() == "Hide":
            for graph in graphs:
                for i in range(len(self.signals[graph])):
                    self.signals_lines[graph][i].setVisible(False)
            self.hideButton.setText("Show")
        else:
            for graph in graphs:
                for i in range(len(self.signals[graph])):
                    self.signals_lines[graph][i].setVisible(True)
            self.hideButton.setText("Hide")

    def toggle_play_pause(self): # Play and Pause Graphs
        if self.current_graph == self.graph1:
            if self.is_playing[0]["is_playing"]: # Check if graph 1 is playing 
                self.is_playing[0]["is_playing"] = False
                self.playButton.setText('Play')
                self.set_icon("Icons/play-svgrepo-com.svg")
                last_data = self.get_last_data_point("graph1")[0]
                self.graph1.setLimits(xMin=0)
                self.graph1.setLimits(yMin=-0.5, yMax=1)
            else:                                 # Check if graph 1 is not playing
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
            last_data = min(self.get_last_data_point("graph1")[0], self.get_last_data_point("graph2")[0])
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

    def get_last_data_point(self, graph):
        if graph in self.signals and self.signals[graph]:
            last_signal = self.signals[graph][-1] # - VE Index
            (time, data), end_ind = last_signal
            if end_ind < len(time) and end_ind < len(data):
                return (time[end_ind], data[end_ind])
        return None













# ************************************** Colors, Labels, and Legends **************************************





    def change_channel_label(self):
        graph_name = self.get_graph_name()
        if graph_name == 'graph1':
            if self.channelsGraph1.currentIndex() == 0:
                self.show_error_message('Select Channel first')
            else:
                self.channelsGraph1.setItemText(
                    self.channelsGraph1.currentIndex(), self.addLabelGraph1.text())
                self.fill_list1()
        elif graph_name == 'graph2':
            if self.channelsGraph2.currentIndex() == 0:
                self.show_error_message('Select Channel first')
            else:
                self.channelsGraph2.setItemText(
                    self.channelsGraph2.currentIndex(), self.addLabelGraph2.text())
                self.fill_list2()
        else:
            self.show_error_message('Select Graph first')

    def add_legend(self, graph_name):
        channelsGraph = self.channelsGraph1 if graph_name == "graph1" else self.channelsGraph2
        addLabel = self.addLabelGraph1 if graph_name == "graph1" else self.addLabelGraph2

        index = channelsGraph.currentIndex()

        # if index == 0:
        #     self.show_error_message("No channel selected")
        #     return

        legend_text = addLabel.text()

        current_index = self.get_index()
        signals_info = self.signals_info.setdefault(graph_name, [])

        while len(signals_info) <= current_index:
            signals_info.append([True, None, None])

        signals_info[current_index][2] = legend_text

        # Initialize legends for all channels
        # self.initialize_legends(graph_name)

        addLabel.clear()

    def initialize_legends(self, graph_name):
        current_graph = getattr(self, graph_name)
        signals_info = self.signals_info.get(graph_name, [])

        if current_graph.plotItem.legend is not None:
            current_graph.plotItem.legend.clear()

        current_graph.addLegend()

        for channel_info in signals_info:
            if channel_info[2]:
                channel_index = signals_info.index(channel_info)
                channel_color = self.channels_color[graph_name][channel_index - 1].color()
                pen = pg.mkPen(color=channel_color)
                current_graph.plot(name=channel_info[2], pen=pen)

    def assign_colors(self, graph_name):
        signals_paths = self.graph1_signals_paths if graph_name == 'graph1' else self.graph2_signals_paths
        channels_color = self.channels_color[graph_name]
        signals_lines = self.signals_lines[graph_name]

        for i, signal_path in enumerate(signals_paths):
            self.open_file(signal_path)
        for j, color in enumerate(channels_color):
            if j < len(signals_lines):
                signals_lines[j].setPen(color)

    def pick_channel_color(self):
        graph = self.get_graph_name()
        channelsGraph = self.channelsGraph1 if graph == 'graph1' else self.channelsGraph2

        selected_channel_index = channelsGraph.currentIndex()

        if selected_channel_index == 0:
            self.show_error_message('Channel not selected')
        else:
            color_dialog = QColorDialog(self)
            color = color_dialog.getColor()

            if color.isValid():
                new_color = pg.mkColor(color.name())
                channels_color = self.channels_color[graph]
                signals_lines = self.signals_lines[graph]

                if selected_channel_index <= len(channels_color) and selected_channel_index <= len(signals_lines):
                    channels_color[selected_channel_index - 1] = new_color
                    signals_lines[selected_channel_index - 1].setPen(new_color)


    

    
    



# ************************************** Snapshot , Glue and PDF Report ************************************** #


    # Snapshot Function
    def take_snapshot(self):
        """
        Captures the current state of the graph and saves it as an image file.
        """
        # Prompt user to choose save location
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Snapshot", "", "PNG Image (*.png);;All Files (*)")
        
        if file_path:
            # Export the current graph to an image file
            exporter = pg.exporters.ImageExporter(self.current_graph.plotItem)
            exporter.export(file_path)
            
            # Show confirmation message
            QMessageBox.information(self, "Snapshot Saved", f"Snapshot saved at {file_path}")

     








   
    from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSlider
    import numpy as np
    from pyqtgraph import PlotWidget    
    
    # GLUIE FUNCTION                        ###################### لسه مخلصتش ####################
    
    def glue_graphs(self):
      pass
    # 
    # :
    #     # Ensure that there are at least two signals in both graphs
    #     if len(self.signals['graph1']) < 1 or len(self.signals['graph2']) < 1:
    #         self.show_error_message("Each graph must contain at least 1 signal.")
    #         return

    #     # Select signals from both graph1 and graph2
    #     signals_to_glue = [
    #         self.signals['graph1'][0][0][1],  # Example: selecting the first signal from graph1
    #         self.signals['graph2'][0][0][1]   # Example: selecting the first signal from graph2
    #     ]

    #     # Function to concatenate signals with an optional gap
    #     def concatenate_signals(signals, gap):
    #         glued_signal = signals[0]  # Start with the first signal
    #         for sig in signals[1:]:
    #             if gap > 0:
    #                 glued_signal = np.concatenate((glued_signal, np.zeros(gap), sig))  # Add gap
    #             elif gap < 0:
    #                 overlap_length = min(abs(gap), len(glued_signal), len(sig))
    #                 overlap = (glued_signal[-overlap_length:] + sig[:overlap_length]) / 2  # Overlap averaging
    #                 glued_signal = np.concatenate((glued_signal[:-overlap_length], overlap, sig[overlap_length:]))
    #             else:
    #                 glued_signal = np.concatenate((glued_signal, sig))  # No gap or overlap
    #         return glued_signal

    #     # Create a window for displaying the glued signal
    #     glued_signal_window = QWidget()
    #     glued_signal_window.setWindowTitle("Glued Signals")
    #     layout = QVBoxLayout()

    #     # Add a PlotWidget to display the glued signal
    #     plot_widget = PlotWidget()
    #     layout.addWidget(plot_widget)

    #     # Add a slider for adjusting the gap/overlap
    #     gap_slider = QSlider(QtCore.Qt.Orientation.Horizontal)
    #     gap_slider.setRange(-50, 100)  # Negative for overlap, positive for gap
    #     gap_slider.setValue(0)  # Default gap
    #     layout.addWidget(gap_slider)

    #     gap_label = QLabel("Gap: 0 samples")
    #     layout.addWidget(gap_label)

    #     # Function to update the glued signal based on the slider value
    #     def update_glued_signal():
    #         gap = gap_slider.value()
    #         glued_signal = concatenate_signals(signals_to_glue, gap)
    #         plot_widget.clear()
    #         plot_widget.plot(glued_signal, pen='g')  # Plot the glued signal
    #         gap_label.setText(f"Gap: {gap} samples")

    #     # Connect the slider to update the glued signal when the gap changes
    #     gap_slider.valueChanged.connect(update_glued_signal)

    #     # Show the initial glued signal
    #     update_glued_signal()

    #     glued_signal_window.setLayout(layout)
    #     glued_signal_window.resize(800, 600)
    #     glued_signal_window.show()

    #     # Keep a reference to prevent the window from closing
    #     self.glued_signal_window = glued_signal_window

    
         







    # REPORT FUNCTION

    from fpdf import FPDF
    import numpy as np
    import os
    import pyqtgraph as pg
    from PyQt5.QtWidgets import QFileDialog, QMessageBox

    def generate_signal_report(self):
        """
        Generate a PDF report that contains information about the signals, including 
        mean, std deviation, min/max values, and an image of the glued signal.
        """
        class PDF(FPDF):
            def header(self):
                self.set_font('Arial', 'B', 12)
                self.cell(0, 10, 'Signal Report', 0, 1, 'C')

            def footer(self):
                self.set_y(-15)
                self.set_font('Arial', 'I', 8)
                self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

        # Prompt user to choose save location for the report
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Report", "", "PDF Files (*.pdf);;All Files (*)")
        
        if file_path:
            # Initialize the PDF
            pdf = PDF()
            pdf.add_page()

            # Title Section
            pdf.set_font("Arial", 'B', 20)
            pdf.cell(0, 10, "Signal Analysis Report", ln=True, align="C")
            pdf.ln(10)

            # Add Glued Signal Snapshot Section
            pdf.set_font("Arial", 'B', 14)
            pdf.cell(0, 10, "Glued Signal Snapshot", ln=True)
            pdf.ln(5)

            # Save the current graph as an image and insert into the PDF
            glued_signal_image_path = "glued_signal_snapshot.png"
            exporter = pg.exporters.ImageExporter(self.graph1.plotItem)
            exporter.export(glued_signal_image_path)
            pdf.image(glued_signal_image_path, x=15, y=None, w=180, h=80, type='PNG')
            pdf.ln(5)
            os.remove(glued_signal_image_path)  # Clean up after export

            # Calculate signal statistics (mean, std, min, max)
            glued_signal = self.signals["graph1"][-1][0][1]  # Last glued signal in graph1
            signal_mean = np.mean(glued_signal)
            signal_std = np.std(glued_signal)
            signal_min = np.min(glued_signal)
            signal_max = np.max(glued_signal)

            # Add Signal Statistics Section
            pdf.set_font("Arial", 'B', 14)
            pdf.cell(0, 10, "Signal Statistics", ln=True)
            pdf.ln(5)

            # Create a table for the statistics
            pdf.set_font("Arial", '', 12)
            pdf.cell(50, 10, 'Statistic', 1, 0, 'C')
            pdf.cell(50, 10, 'Value', 1, 1, 'C')

            pdf.cell(50, 10, 'Mean', 1, 0, 'C')
            pdf.cell(50, 10, f"{signal_mean:.2f}", 1, 1, 'C')

            pdf.cell(50, 10, 'Std Deviation', 1, 0, 'C')
            pdf.cell(50, 10, f"{signal_std:.2f}", 1, 1, 'C')

            pdf.cell(50, 10, 'Min Value', 1, 0, 'C')
            pdf.cell(50, 10, f"{signal_min:.2f}", 1, 1, 'C')

            pdf.cell(50, 10, 'Max Value', 1, 0, 'C')
            pdf.cell(50, 10, f"{signal_max:.2f}", 1, 1, 'C')

            # Save the report as a PDF file
            pdf.output(file_path)
            QMessageBox.information(self, "Report Generated", f"Report saved at {file_path}")



# ************************************** Main Function ************************************** #

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt6())
    main = MainWindow()
    main.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
    
