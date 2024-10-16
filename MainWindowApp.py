# Task 1 – Multi-Port, Multi-Channel Signal Viewer 
# Introduction: Monitoring the vital signals is a crucial aim in any ICU room.  
# Description: Using Python and Qt, develop a desktop application that illustrates multi-port, multi-channel signal viewer 
# that has the following features: - The user can browse his PC to open any signal file. Each group will need to provide samples from any three different 
# medical signals (e.g. ECG, EMG, EEG,…etc). Each signal type should have an example for normal signal and abnormal 
# signal. The user should also be able to connect to some website that emits a signal in real time, read the emitted signal 
# and plot it. Each group is responsible for searching and connecting at least one of these websites. The websites are not 
# to be repeated among the different groups and will be allocated for the group based on “first-to-deliver first
# allocated”. - Your application should contain two main identical graphs. The user can open different signals in each graph. i.e. each 
# graph has to have its own controls. The user can run each graph independently or link both graphs via a button in the 
# UI. When the graphs are linked (i.e. linked option is ON), the two graphs must display the same time frames, signal 
# speed, and same viewport if zoomed or panned (i.e. if the user zoom on one graph, the other graph should apply the 
# same exact zoom as well). If the link of the two graphs is disabled, then each graph can run its signals independently. - Your application should also provide a non-rectangle graph. Pick any non-rectangle graph of your own and be ready to 
# open a suitable signal that can be displayed on this graph in cine mode (Please, think in how this signal should be 
# displayed in the cine mode. This is not a trivial feature!). - In any of the three graphs, when the user opens a signal file, the signal should show up in the cine mode (i.e. a running 
# signal through time, similar to the one you see in the ICU monitors). Do NOT open a signal in a static mode. If the 
# signal ends, there should be a rewind option to either stop the signal or start running it again from the beginning. - The user can manipulate the running signals through UI elements that provide the below function: 
# • Change color, 
# • Add a label/title for each signal, 
# • Show/hide, 
# • Control/customize the cine speed, 
# • Zoom in/out, 
# • Pause/play/rewind(on/off),
#  • Scroll/Pan the signal in any direction (left, top, right, bottom). Scroll is performed through sliders, and pan is 
# performed through the mouse movements. 
# • Move any signal from one graph to the other. 
# During these manipulations, you need to take care of the boundary conditions! Intuitively, no scroll/pan should be 
# allowed before your signal starts or after it ends or above its maximum values or below its minimum values. No user 
# expects to see an empty graph coz he scrolled the signal too much to the top for example. Note: Ofcourse, all 
# manipulations will be applied on all the opened signals (viewed or hidden). - Signal Glue: The user should be able to cut any two parts of any two signals, each displayed in one of the two 
# rectangular graphs and glue them in a third graph using signal interpolation. The different parameters of the glue 
# operation should be customizable by the user. These glue parameters are window start and size of each signal, signals 
# gap (positive distance between the two signals) or overlap (negative distance between the two signals), and 
# interpolation order.  - Exporting & Reporting: For the sake of reporting the results of the glue operation, the user can construct a report of 
# one or more snapshots for the glue graph sent to the report along with some data statistics on the glued signal to a 
# pdf file. You need to generate the pdf contents via the code. i.e. Do NOT take a snapshot image and convert it to a pdf 
# file! 
# • Data statistics can be mean, std, duration, min and max values for each signal. These numbers should be 
# organized in a nice table in the pdf file. The report itself should be organized to have a nice layout. The report can 
# be single or multi-page. Prepare samples of your reports for different number of signals and snapshots. 
# Code Practice: - Use proper variable and function names. If I do not understand what your variable is roughly doing without asking for 
# your explanation, then this is NOT a proper name! Examples for non-proper names: x, y, counter, ss, ii, s_i,…etc. Each 
# non-proper variable or function name will be penalized with -10% of the whole task grade. 
# General Notes: - This is a task for an engineer who has had reasonable experience with software programs. And thus, s/he is expected 
# to provide convenient, user-friendly software. Do NOT invent a feature or a user-interaction that you had never seen 
# before in another software. Do NOT INVENT but rather IMMITAE what you have experienced before with software. If 
# you feel you are very smart that your feature is completely new and no one thought about or saw it before, then we 
# do NOT want to see it either! During delivery, you will always be asked this question “where did you see this feature 
# before?” either for features related to signal viewers or related to dealing with the computer or software in general. - If you are new to signal viewers, try to download a couple and experience them. There are tons of free downloadable 
# viewers on the internet. Not seeing a viewer before is NOT an excuse for the previous note. - Any feature in your program should have a default value. Never ask the user to provide you with an initial value for 
# any of your parameters. - Any “or” for the user means “and” for the developer. If the user can do X or Y, then the developer is expected to 
# provide the user with the full functionality of features X and Y. - You can use any toolbox to read or process the signal underneath but you have to do your own UI and not use any UI 
# elements from any library or toolkit. - Please, note that the number of opened signals in any graph is not fixed/limited. i.e. Don't assume you will open 5 
# signals at maximum and prepare their controls accordingly.

 













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
import pyqtgraph.exporters
from pyqtgraph import PlotWidget
import random
from PyQt6.QtCore import Qt
# Added new libraries
from PyQt6.QtWidgets import QInputDialog
import requests
from PyQt6.QtWidgets import QInputDialog, QMessageBox



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

        # # Connect tab change event to handler
        # # Declare the tab widget
        # self.tab = self.findChild(QtWidgets.QTabWidget, 'tab')
        # self.tab3 = self.findChild(QtWidgets.QTabWidget, 'tab_3')

        # # # Connect tab change event to handler
        # self.tab.currentIndex().connect(lambda index: self.on_tab_change(index))
        # self.tab3.currentIndex().connect(lambda index: self.on_tab_change(index))




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
        self.signal_Link_Label.returnPressed.connect(self.signal_Link)


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

        # Create shortcuts for actions
    #     self.create_shortcuts()

    # def create_shortcuts(self):
    #     # Create a shortcut for the Import button
    #     import_shortcut = QShortcut(QKeySequence('Ctrl+O'), self)
    #     import_shortcut.activated.connect(self.browse)

    #     # Create a shortcut for the snapshoot button
    #     report_shortcut = QShortcut(QKeySequence('Ctrl+S'), self)
    #     report_shortcut.activated.connect(self.take_snapshot)

    #     # Create a shortcut for the REPORT button
    #     report_shortcut = QShortcut(QKeySequence('Ctrl+P'), self)
    #     report_shortcut.activated.connect(self.generate_signal_report)

    #     # Create a shortcut for the play button
    #     paly_shortcut = QShortcut(Qt.Key.Key_Space, self)
    #     paly_shortcut.activated.connect(self.toggle_play_pause)

    #     # Create a shortcut for the rewind button
    #     rewind_shortcut = QShortcut(QKeySequence('Ctrl+R'), self)
    #     rewind_shortcut.activated.connect(self.rewind_graph)

    #     # Create a shortcut for the link button
    #     link_shortcut = QShortcut(QKeySequence('Ctrl+L'), self)
    #     link_shortcut.activated.connect(self.link_graphs)

    #     # Create a shortcut for the clear button
    #     clear_shortcut = QShortcut(QKeySequence('Ctrl+C'), self)
    #     clear_shortcut.activated.connect(self.hide_Show_graph)


                
                
                        
                


                




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
        unchecked_indexes_list1 = self.get_unchecked_indexes(self.hideList1)
        for index in unchecked_indexes_list1:
            self.signals_lines['graph1'][index].setPen((0, 0, 0))
        unchecked_indexes_list2 = self.get_unchecked_indexes(self.hideList2)
        for index in unchecked_indexes_list2:
            self.signals_lines['graph2'][index].setPen((0, 0, 0))

    def on_item_checked(self):
        checked_indexes_list1 = self.get_checked_indexes(self.hideList1)
        for index in checked_indexes_list1:
            self.signals_lines['graph1'][index].setPen(
                self.channels_color['graph1'][index])
        checked_indexes_list2 = self.get_checked_indexes(self.hideList2)
        for index in checked_indexes_list2:
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
            file_filter = "Raw Data (*.csv *.txt *.xls *.hea *.dat *.rec)"
            self.file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
                None, 'Open Signal File', './', filter=file_filter)

            if self.current_graph == self.graph1 and self.file_path:
                self.graph1_signals_paths.append(self.file_path)
                self.channelsGraph1.addItem(
                    f"Channel{len(self.signals['graph1']) + 1}")
                self.fill_list1()
                self.signals_info["graph1"].append([True, None, None])

            elif self.current_graph == self.graph2 and self.file_path:
                self.graph2_signals_paths.append(self.file_path)
                self.channelsGraph2.addItem(
                    f"Channel{len(self.signals['graph2']) + 1}")
                self.fill_list2()
                self.signals_info["graph2"].append([True, None, None])

            elif self.current_graph == [self.graph1, self.graph2] and self.file_path:
                self.graph1_signals_paths.append(self.file_path)
                self.graph2_signals_paths.append(self.file_path)
                self.channelsGraph1.addItem(
                    f"Channel{len(self.signals['graph1']) + 1}")
                self.fill_list1()
                self.channelsGraph2.addItem(
                    f"Channel{len(self.signals['graph2']) + 1}")
                self.fill_list2()
                self.signals_info["graph1"].append([True, None, None])
                self.signals_info["graph2"].append([True, None, None])

            if self.file_path:
                self.open_file(self.file_path)

# I Want to Add a Feature that if The user want to clicked to connectButton ask him to add the link of the signal from website that emits a signal in real time, in the signal_Link_Label and after read the emitted signal and plot it as the browse button.
# Q i want example for some api emit signals !
# A     
    
    def signal_Link(self):
        """
        Prompts the user to enter the link of the signal from a website that emits a signal in real time.
        """
        link, ok = QInputDialog.getText(self, 'Enter Signal Link', 'Enter the link of the signal:')
        if ok and link:
            self.signal_Link_Label.setText(link)
            return link
        return None

    def connectFunction(self):
        """
        Connects to the signal source from the provided link, reads the emitted signal, and plots it.
        """
        link = self.signal_Link()
        if not link:
            return

        try:
            # Read the signal from the link
            response = requests.get(link, stream=True)
            response.raise_for_status()
        except requests.RequestException as e:
            QMessageBox.critical(self, "Connection Error", f"Failed to connect to the signal source: {e}")
            return

        time_data = []
        amplitude_data = []

        for line in response.iter_lines():
            if line:
                data = line.decode('utf-8')
                try:
                    value = float(data)
                    amplitude_data.append(value)
                    time_data.append(len(time_data) * 0.01)  # Simulate time data
                except ValueError:
                    continue

        # Plot the signal on graph1
        pen = pg.mkPen(color=(255, 0, 0), width=2)
        self.plot_signal(self.graph1, (time_data, amplitude_data), pen)

        # Update the signals data structure
        self.signals["graph1"].append(((time_data, amplitude_data), len(time_data)))
        self.signals_lines["graph1"].append(None)
        self.signals_info["graph1"].append({'label': 'Real-time Signal', 'color': (255, 0, 0)})

        # Update the channel selection combo box
        self.channelsGraph1.addItem(f"Channel {len(self.signals['graph1'])}")

        # Update the play/pause state
        self.is_playing[0]["is_playing"] = True
        self.playButton.setText('Pause')
        self.set_icon("Icons/pause.svg")

        if not self.timer.isActive():
            self.timer.start(50) 
    



    def open_file(self, path: str):
        self.time = []
        self.data = []
        self.fsampling = 1
        filetype = path[-3:]

        if filetype in ["hea", "rec", "dat"]:
            self.record = wfdb.rdrecord(path[:-4], channels=[0])
            self.data = np.concatenate(self.record.p_signal)
            self.fsampling = self.record.fs
            self.time = np.arange(len(self.data)) / self.fsampling

        if filetype in ["csv", "txt", "xls"]:
            with open(path, 'r') as data_file:
                data_reader = csv.reader(data_file, delimiter=',')
                for row in data_reader:
                    time_value = float(row[0])
                    amplitude_value = float(row[1])
                    self.time.append(time_value)
                    self.data.append(amplitude_value)

        self.data_x = []
        self.data_y = []

        if self.current_graph == self.graph1:
            self.signals["graph1"].append(
                [(self.time, self.data), 50])
            self.is_playing[0]["is_playing"] = True
            self.playButton.setText('Pause')
            self.set_icon("Icons/pause.svg")
            self.plot_graph_signal()

        elif self.current_graph == self.graph2:
            self.signals["graph2"].append(
                [(self.time, self.data), 50])
            self.is_playing[1]["is_playing"] = True
            self.playButton.setText('Pause')
            self.set_icon("Icons/pause.svg")
            self.plot_graph_signal()

        else:
            if self.sourceGraph == "both":
                self.signals["graph1"].append(
                    [(self.time, self.data), 50])
                self.is_playing[0]["is_playing"] = True
                self.signals["graph2"].append(
                    [(self.time, self.data), 50])
                self.is_playing[1]["is_playing"] = True
                self.playButton.setText('Pause')
                self.set_icon("Icons/pause.svg")
                self.plot_common_linked_signal()

            elif self.sourceGraph == "graph1":
                self.signals["graph1"].append(
                    [(self.time, self.data), 50])
                self.is_playing[0]["is_playing"] = True
                self.playButton.setText('Pause')
                self.set_icon("Icons/pause.svg")
                self.plot_unique_linked_signal()

            elif self.sourceGraph == "graph2":
                self.signals["graph2"].append(
                    [(self.time, self.data), 50])
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

    #  Glue Signals
    def glue_graphs(self):
        # Retrieve signals from the two graphs
        signal1 = self.graph1.signal
        signal2 = self.graph2.signal

        # Select segments from each signal based on user-defined start and end points
        start_index1 = np.searchsorted(signal1['x'], self.start_line1.value())
        end_index1 = np.searchsorted(signal1['x'], self.end_line1.value())
        start_index2 = np.searchsorted(signal2['x'], self.start_line2.value())
        end_index2 = np.searchsorted(signal2['x'], self.end_line2.value())

        segment1 = {'x': signal1['x'][start_index1:end_index1], 'y': signal1['y'][start_index1:end_index1]}
        segment2 = {'x': signal2['x'][start_index2:end_index2], 'y': signal2['y'][start_index2:end_index2]}

        # Glue the selected segments together
        def_gap = segment2['x'][0] - segment1['x'][-1]
        actual_gap = self.Gap_value if self.Gap_value != 0 else def_gap

        if actual_gap > 0:
            glued_x = np.concatenate((segment1['x'], segment1['x'][-1] + np.arange(1, actual_gap + 1), segment2['x']))
            glued_y = np.concatenate((segment1['y'], np.zeros(actual_gap), segment2['y']))
        elif actual_gap < 0:
            glued_x = np.concatenate((segment1['x'], segment2['x'] - actual_gap))
            glued_y = np.concatenate((segment1['y'], segment2['y']))
        else:
            glued_x = np.concatenate((segment1['x'], segment2['x']))
            glued_y = np.concatenate((segment1['y'], segment2['y']))

        # Plot the glued signal in a designated plot area
        self.Glue_Editor.clear()
        self.Glue_Editor.plot(glued_x, glued_y, pen='g')



# ************************************** Snapshot and PDF Report **************************************
       
    # Snapshot 


    from PyQt6.QtWidgets import QFileDialog
    import pyqtgraph.exporters

    def take_snapshot(self):
        # Retrieve the current state of the graphs
        graph1_state = self.graph1.plotItem
        graph2_state = self.graph2.plotItem

        # Use the pyqtgraph library to export the graphs as images
        exporter1 = pyqtgraph.exporters.ImageExporter(graph1_state)
        exporter2 = pyqtgraph.exporters.ImageExporter(graph2_state)

        # Open a file dialog to specify the save location
        file_dialog = QFileDialog()
        file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
        file_dialog.setNameFilter("Images (*.png *.jpg *.bmp)")
        file_dialog.setDefaultSuffix("png")

        if file_dialog.exec():
            file_paths = file_dialog.selectedFiles()
            if len(file_paths) == 2:
                # Save the images to the specified location
                exporter1.export(file_paths[0])
                exporter2.export(file_paths[1])
                print("SnapShot Done")
            else:
                print("Please select two file paths to save the snapshots.")
        else:
            print("Snapshot canceled.")


    # Report Generation
    def generate_report(self):
        self.folder_path, _ = QFileDialog.getSaveFileName(
            None, 'Save the signal file', None, 'PDF Files (*.pdf)')
        if self.folder_path:
            self.pdf = FPDF()
            self.pdf.add_page()
            self.add_page_border()
            self.add_title("Signal Report")
            self.add_logos()
            self.add_snapshots_to_pdf(self.pdf)
            self.add_statistics_tables()
            self.save_pdf()

    def generate_signal_report(self):
        if isinstance(self.current_graph, list):
            # If in link mode, generate reports for both graphs
            for graph in self.current_graph:
                self.create_report(graph)
        else:
            # Generate a report for the current graph
            self.create_report(self.current_graph)
        self.snapshoot_data = []
        self.stat_lst = []

    def add_page_border(self):
        self.pdf.set_draw_color(0, 0, 0)  # Set line color to black
        # Draw a border around the entire page
        self.pdf.rect(1, 1, self.pdf.w - 2, self.pdf.h - 2)

    def add_title(self, title):
        self.pdf.set_font("times", "B", size=25)
        self.pdf.cell(200, 10, txt=title, ln=True, align="C")
        # Reset the font to the previous settings
        self.pdf.set_font("times", size=12)

    def add_logos(self):
        pass
        # self.pdf.image('LOGO/asset-cairo.png', 2, 3, 40, 40)
        # self.pdf.image('LOGO/Asset-SBE.png', 160, 3, 40, 40)
        # self.pdf.ln(30)

    def add_snapshots_to_pdf(self, pdf):
        # Capture the snapshots
        snap_data = self.snapshoot_data

        # Iterate over each snapshot
        for graph_image in snap_data:
            # Add the graph name to the PDF
            # Extract the image file name
            image_name = os.path.basename(graph_image[:12])

            pdf.cell(200, 10, text=image_name)
            pdf.ln(10)

            pdf.image(graph_image, x=10, w=190)
            pdf.ln(10)

    def add_statistics_tables(self):
        graph_names = ["graph1", "graph2"]

        for graph_name in graph_names:
            statistics = self.get_signal_statistics(graph_name)

            if statistics:
                self.pdf.cell(200, 10, text=f"Statistics for {graph_name}")
                self.pdf.ln(10)  # Move to the next line

                mean, std, maximum, minimum = self.access_nested_list_items(
                    statistics)

                self.create_statistics_table(mean, std, maximum, minimum)

    def create_statistics_table(self, mean, std, maximum, minimum):
        self.pdf.ln(10)  # Move to the next line
        col_width = 25
        num_plots = len(mean)

        self.pdf.set_fill_color(211, 211, 211)  # Set a light gray fill color

        # Add headers
        self.pdf.cell(col_width, 10, "Metric", border=1, fill=True)
        for i in range(num_plots):
            self.pdf.cell(col_width, 10, f"Plot {i + 1}", border=1, fill=True)
        self.pdf.ln()

        metrics = ["Mean", "Std", "Maximum", "Minimum"]
        data_lists = [mean, std, maximum, minimum]

        for metric, data_list in zip(metrics, data_lists):
            self.pdf.cell(col_width, 10, metric, border=1)
            for value in data_list:
                self.pdf.cell(col_width, 10, f"{value: .4f}", border=1)
            self.pdf.ln(10)

    def get_signal_statistics(self, graph_widget: str):
        statistics = []
        for signal in self.signals[graph_widget]:
            _, data = signal[0]
            mean = np.mean(data)
            std = np.std(data)
            maximum = np.max(data)
            minimum = np.min(data)
            statistics.append([mean, std, maximum, minimum])
        return statistics

    def access_nested_list_items(self, nested_list):
        mean_list, std_list, max_list, min_list = [], [], [], []

        for sublist in nested_list:
            if len(sublist) == 4:
                mean_list.append(sublist[0])
                std_list.append(sublist[1])
                max_list.append(sublist[2])
                min_list.append(sublist[3])

        return mean_list, std_list, max_list, min_list

    def save_pdf(self):
        self.pdf.output(str(self.folder_path))
        # This message appears when the PDF is EXPORTED
        QMessageBox.information(self, 'Done', 'PDF has been created')
        for i in range(len(self.snapshoot_data)):
            os.remove(f"Screenshot_{i}.png")

    def create_report(self, graph_widget, pdf_title="Signal_Report.pdf"):
        self.folder_path, _ = QFileDialog.getSaveFileName(
            None, 'Save the signal file', None, 'PDF Files (*.pdf)')
        if self.folder_path:
            self.pdf = FPDF()
            self.pdf.add_page()
            self.add_page_border()
            self.add_title("Signal Report")
            self.add_logos()
            self.add_snapshots_to_pdf(self.pdf)
            self.add_statistics_tables()
            self.save_pdf()





# UnUsed Functions


    # def take_snapshot(self):
    #     pass
    #     # index = self.graphSelection.currentIndex()
    #     # graph_items = {
    #     #     0: self.graph1.plotItem,
    #     #     1: self.graph2.plotItem
    #     # }

    #     # if index in graph_items:
    #     #     graph_item = graph_items[index]
    #     #     screenshot = ImageExporter(graph_item)
    #     #     screenshot.parameters()['width'] = 640
    #     #     screenshot.parameters()['height'] = 480
    #     #     screenshot_path = f"Screenshot_{len(self.snapshoot_data)}.png"
    #     #     screenshot.export(screenshot_path)
    #     #     self.snapshoot_data.append(screenshot_path)
    #     # else:
    #     #     QtWidgets.QMessageBox.warning(
    #     #         self, 'Warning', 'Please select a graph')

    # def add_snapshots_to_pdf(self, pdf):
    #     # Capture the snapshots
    #     snap_data = self.snapshoot_data

    #     # Iterate over each snapshot
    #     for graph_image in snap_data:
    #         # Add the graph name to the PDF
    #         # Extract the image file name
    #         image_name = os.path.basename(graph_image[:12])

    #         pdf.cell(200, 10, text=image_name)
    #         pdf.ln(10)

    #         pdf.image(graph_image, x=10, w=190)
    #         pdf.ln(10)

    # def create_report(self, graph_widget, pdf_title="Signal_Report.pdf"):
    #     self.folder_path, _ = QFileDialog.getSaveFileName(
    #         None, 'Save the signal file', None, 'PDF Files (*.pdf)')
    #     if self.folder_path:
    #         self.pdf = FPDF()
    #         self.pdf.add_page()
    #         self.add_page_border()
    #         self.add_title("Signal Report")
    #         self.add_logos()
    #         self.add_snapshots_to_pdf(self.pdf)
    #         self.add_statistics_tables()
    #         self.save_pdf()

    # def add_page_border(self):
    #     self.pdf.set_draw_color(0, 0, 0)  # Set line color to black
    #     # Draw a border around the entire page
    #     self.pdf.rect(1, 1, self.pdf.w, self.pdf.h)

    # def add_title(self, title):
    #     self.pdf.set_font("times", "B", size=25)
    #     self.pdf.cell(200, 5, txt=title, align="C")
    #     # Reset the font to the previous settings
    #     self.pdf.set_font("times", size=12)

    # def add_logos(self):
    #     pass
    #     # self.pdf.image('LOGO/asset-cairo.png', 2, 3, 40, 40)
    #     # self.pdf.image('LOGO/Asset-SBE.png', 160, 3, 40, 40)
    #     # self.pdf.ln(30)

    # def add_statistics_tables(self):
    #     graph_names = ["graph1", "graph2"]

    #     for graph_name in graph_names:
    #         statistics = self.get_signal_statistics(graph_name)

    #         if statistics:
    #             self.pdf.cell(200, 10, text=f"Statistics for {graph_name}")
    #             self.pdf.ln(10)  # Move to the next line

    #             mean, std, maximum, minimum = self.access_nested_list_items(
    #                 statistics)

    #             self.create_statistics_table(mean, std, maximum, minimum)

    # def create_statistics_table(self, mean, std, maximum, minimum):
    #     self.pdf.ln(10)  # Move to the next line
    #     col_width = 25
    #     num_plots = len(mean)

    #     self.pdf.set_fill_color(211, 211, 211)  # Set a light gray fill color

    #     # Add headers
    #     self.pdf.cell(col_width, 10, "Metric", border=1, fill=True)
    #     for i in range(num_plots):
    #         self.pdf.cell(col_width, 10, f"Plot {i + 1}", border=1, fill=True)
    #     self.pdf.ln()

    #     metrics = ["Mean", "Std", "Maximum", "Minimum"]
    #     data_lists = [mean, std, maximum, minimum]

    #     for metric, data_list in zip(metrics, data_lists):
    #         self.pdf.cell(col_width, 10, metric, border=1)
    #         for value in data_list:
    #             self.pdf.cell(col_width, 10, f"{value: .4f}", border=1)
    #         self.pdf.ln(10)

    # def get_signal_statistics(self, graph_widget: str):
    #     statistics = []
    #     for signal in self.signals[graph_widget]:
    #         _, data = signal[0]
    #         mean = np.mean(data)
    #         std = np.std(data)
    #         maximum = np.max(data)
    #         minimum = np.min(data)
    #         statistics.append([mean, std, maximum, minimum])
    #     return statistics

    # def access_nested_list_items(self, nested_list):
    #     mean_list, std_list, max_list, min_list = [], [], [], []

    #     for sublist in nested_list:
    #         if len(sublist) == 4:
    #             mean_list.append(sublist[0])
    #             std_list.append(sublist[1])
    #             max_list.append(sublist[2])
    #             min_list.append(sublist[3])

    #     return mean_list, std_list, max_list, min_list

    # def save_pdf(self):
    #     self.pdf.output(str(self.folder_path))
    #     # This message appears when the PDF is EXPORTED
    #     QMessageBox.information(self, 'Done', 'PDF has been created')
    #     for i in range(len(self.snapshoot_data)):
    #         os.remove(f"Screenshot_{i}.png")

    # def generate_signal_report(self):
    #     if isinstance(self.current_graph, list):
    #         # If in link mode, generate reports for both graphs
    #         for graph in self.current_graph:
    #             self.create_report(graph)
    #     else:
    #         # Generate a report for the current graph
    #         self.create_report(self.current_graph)
    #     self.snapshoot_data = []
    #     self.stat_lst = []


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt6())
    main = MainWindow()
    main.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
    
