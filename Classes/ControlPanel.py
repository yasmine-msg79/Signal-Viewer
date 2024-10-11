
import sys
import os
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QWidget
import pyqtgraph as pg
import PyQt5
from PyQt5 import uic, QtWidgets
   

class ControlPanel(QtWidgets.QMainWindow):
    def __init__(self):
        super(ControlPanel, self).__init__()
        uic.loadUi(r"..\UI\control_panel.ui", self)
        # Button connections for Graph 1
        self.zoom_in_graph1.clicked.connect(lambda: self.zoom_in(self, self.linkedSignals, 1))
        self.zoom_out_graph1.clicked.connect(lambda: self.zoom_out(self, self.linkedSignals, 1))
        self.show_graph_1.clicked.connect(lambda: self.show_graph(self, self.linkedSignals, 1))
        self.hide_graph_1.clicked.connect(lambda: self.hide_graph(self, self.linkedSignals, 1))
        self.high_speed_1.clicked.connect(lambda: self.increase_speed(self, self.linkedSignals, 1))
        self.slow_speed_1.clicked.connect(lambda: self.decrease_speed(self, self.linkedSignals, 1))
        self.start_graph_1.clicked.connect(lambda: self.start_simulation(self, self.linkedSignals, 1))
        self.stop_graph_1.clicked.connect(lambda: self.stop_simulation(self, self.linkedSignals, 1))
        self.rewind_graph1.clicked.connect(lambda: self.rewind(self, self.linkedSignals , 1))
        self.Change_color_1.clicked.connect(lambda: self.change_color(self, self.linkedSignals, 1))

        # Button connections for Graph 2
        self.zoom_in_graph2.clicked.connect(lambda: self.zoom_in(self, self.linkedSignals, 2))
        self.zoom_out_graph2.clicked.connect(lambda: self.zoom_out(self, self.linkedSignals, 2))
        self.show_graph_2.clicked.connect(lambda: self.show_graph(self, self.linkedSignals, 2))
        self.hide_graph_2.clicked.connect(lambda: self.hide_graph(self, self.linkedSignals, 2))
        self.high_speed_2.clicked.connect(lambda: self.increase_speed(self, self.linkedSignals, 2))
        self.slow_speed_2.clicked.connect(lambda: self.decrease_speed(self, self.linkedSignals, 2))
        self.start_graph_2.clicked.connect(lambda: self.start_simulation(self, self.linkedSignals, 2))
        self.stop_graph_2.clicked.connect(lambda: self.stop_simulation(self, self.linkedSignals, 2))
        self.rewind_graph2.clicked.connect(lambda: self.rewind(self, self.linkedSignals, 2))
        self.Change_color_2.clicked.connect(lambda: self.change_color(self, self.linkedSignals, 2))

        # Button connections for Linked Graphs (Graph 1 and Graph 2) 
        self.change_to_graph_1.clicked.connect(self.move_to_graph_2_to_1)
        self.change_to_graph_2.clicked.connect(self.move_to_graph_1_to_2)
        
        # # to show the window uncomment ths code
        # self.show()

  

    def zoom_in(UI_MainWindow, isLinked, graphNum):
     if isLinked :
        viewRangeGraph1 = UI_MainWindow.graph1.viewRange()
        UI_MainWindow.graph1.setXRange(viewRangeGraph1[0][0] + 1, viewRangeGraph1[0][1] - 1, padding=0)
        UI_MainWindow.graph1.setYRange(viewRangeGraph1[1][0] + 1, viewRangeGraph1[1][1] - 1, padding=0)

        viewRangeGraph2 = UI_MainWindow.graph2.viewRange()
        UI_MainWindow.graph2.setXRange(viewRangeGraph2[0][0] + 1, viewRangeGraph2[0][1] - 1, padding=0)
        UI_MainWindow.graph2.setYRange(viewRangeGraph2[1][0] + 1, viewRangeGraph2[1][1] - 1, padding=0)
     else:
        if graphNum == 1: 
            viewRangeGraph1 = UI_MainWindow.graph1.viewRange()
            UI_MainWindow.graph1.setXRange(viewRangeGraph1[0][0] + 1, viewRangeGraph1[0][1] - 1, padding=0)
            UI_MainWindow.graph1.setYRange(viewRangeGraph1[1][0] + 1, viewRangeGraph1[1][1] - 1, padding=0)
        else:
            viewRangeGraph2 = UI_MainWindow.graph2.viewRange()
            UI_MainWindow.graph2.setXRange(viewRangeGraph2[0][0] + 1, viewRangeGraph2[0][1] - 1, padding=0)
            UI_MainWindow.graph2.setYRange(viewRangeGraph2[1][0] + 1, viewRangeGraph2[1][1] - 1, padding=0)


    def zoom_out(UI_MainWindow, isLinked, graphNum):
     if isLinked :
        viewRangeGraph1 = UI_MainWindow.graph1.viewRange()
        UI_MainWindow.graph1.setXRange(viewRangeGraph1[0][0] - 1, viewRangeGraph1[0][1] + 1, padding=0)
        UI_MainWindow.graph1.setYRange(viewRangeGraph1[1][0] - 1, viewRangeGraph1[1][1] + 1, padding=0)

        viewRangeGraph2 = UI_MainWindow.graph2.viewRange()
        UI_MainWindow.graph2.setXRange(viewRangeGraph2[0][0] - 1, viewRangeGraph2[0][1] + 1, padding=0)
        UI_MainWindow.graph2.setYRange(viewRangeGraph2[1][0] - 1, viewRangeGraph2[1][1] + 1, padding=0)
     else:
        if graphNum == 1: 
            viewRangeGraph1 = UI_MainWindow.graph1.viewRange()
            UI_MainWindow.graph1.setXRange(viewRangeGraph1[0][0] - 1, viewRangeGraph1[0][1] + 1, padding=0)
            UI_MainWindow.graph1.setYRange(viewRangeGraph1[1][0] - 1, viewRangeGraph1[1][1] + 1, padding=0)
        else:
            viewRangeGraph2 = UI_MainWindow.graph2.viewRange()
            UI_MainWindow.graph2.setXRange(viewRangeGraph2[0][0] - 1, viewRangeGraph2[0][1] + 1, padding=0)
            UI_MainWindow.graph2.setYRange(viewRangeGraph2[1][0] - 1, viewRangeGraph2[1][1] + 1, padding=0)

    def show_graph(UI_MainWindow, isLinked, graphNum):
     if isLinked:
        UI_MainWindow.Graph1.show()
        UI_MainWindow.Graph2.show()
     else:
        if graphNum == 1:
            UI_MainWindow.Graph1.show()
        else:
            UI_MainWindow.Graph2.show()


    def hide_graph(UI_MainWindow, isLinked, graphNum):
     if isLinked:
        UI_MainWindow.Graph1.hide()
        UI_MainWindow.Graph2.hide()
     else:
        if graphNum == 1:
            UI_MainWindow.Graph1.hide()
        else:
            UI_MainWindow.Graph2.hide()
    
    def increase_speed(UI_MainWindow, isLinked, graphNum):
     if isLinked:
        current_interval = UI_MainWindow.timer_linked_graphs.interval()  # Get the current interval in milliseconds
        if current_interval > 100:  # Prevent it from going too fast
            new_interval = max(100, current_interval - 100)  # Decrease the interval to make it faster
            UI_MainWindow.timer_linked_graphs.setInterval(new_interval)
            print(f"Speed increased. New interval: {new_interval} ms")
     else:
        if graphNum == 1:
            current_interval = UI_MainWindow.timer_graph_1.interval()  # Get the current interval in milliseconds
            if current_interval > 100:  # Prevent it from going too fast
                new_interval = max(100, current_interval - 100)  # Decrease the interval to make it faster
                UI_MainWindow.timer_graph_1.setInterval(new_interval)
                print(f"Speed increased. New interval: {new_interval} ms")
        else:
            current_interval = UI_MainWindow.timer_graph_2.interval()  # Get the current interval in milliseconds
            if current_interval > 100:  # Prevent it from going too fast
                new_interval = max(100, current_interval - 100)  # Decrease the interval to make it faster
                UI_MainWindow.timer_graph_2.setInterval(new_interval)
                print(f"Speed increased. New interval: {new_interval} ms")

    def decrease_speed(UI_MainWindow, isLinked, graphNum):
     if isLinked:
        current_interval = UI_MainWindow.timer_linked_graphs.interval()  # Get the current interval in milliseconds
        new_interval = current_interval + 100  # Increase the interval to make it slower
        UI_MainWindow.timer_linked_graphs.setInterval(new_interval)
        print(f"Speed decreased. New interval: {new_interval} ms")
     else:
        if graphNum == 1:
            current_interval = UI_MainWindow.timer_graph_1.interval()  # Get the current interval in milliseconds
            new_interval = current_interval + 100  # Increase the interval to make it slower
            UI_MainWindow.timer_graph_1.setInterval(new_interval)
            print(f"Speed decreased. New interval: {new_interval} ms")
        else:
            current_interval = UI_MainWindow.timer_graph_2.interval()  # Get the current interval in milliseconds
            new_interval = current_interval + 100  # Increase the interval to make it slower
            UI_MainWindow.timer_graph_2.setInterval(new_interval)
            print(f"Speed decreased. New interval: {new_interval} ms")

    def start_simulation(UI_MainWindow, isLinked, graphNum):
     if isLinked:
        if not UI_MainWindow.timer_linked_graphs.isActive():
            UI_MainWindow.timer_linked_graphs.start()
            UI_MainWindow.timer_graph_1.start()
            UI_MainWindow.timer_graph_2.start()
            # Update limits for linked graphs (if needed)
            # adjust_graph_1_slider_max(UI_MainWindow)
            # adjust_graph_2_slider_max(UI_MainWindow)
     else:
        if graphNum == 1:
            if not UI_MainWindow.timer_graph_1.isActive():
                UI_MainWindow.timer_graph_1.start()
                # adjust_graph_1_slider_max(UI_MainWindow)
        else:
            if not UI_MainWindow.timer_graph_2.isActive():
                UI_MainWindow.timer_graph_2.start()
                # adjust_graph_2_slider_max(UI_MainWindow)


    def stop_simulation(UI_MainWindow, isLinked, graphNum):
     if isLinked:
        if  UI_MainWindow.timer_linked_graphs.isActive():
            print("linked timer is active")
            UI_MainWindow.timer_graph_1.stop()
            UI_MainWindow.timer_graph_2.stop()
            UI_MainWindow.timer_linked_graphs.stop()
            # adjust_graph_1_slider_max(UI_MainWindow)
        else:
         if graphNum == 1:
            if  UI_MainWindow.timer_graph_1.isActive():
                print("graph1 timer is active")
                UI_MainWindow.timer_graph_1.stop()
                # adjust_graph_1_slider_max(UI_MainWindow)
         else:
            if  UI_MainWindow.timer_graph_2.isActive():
                print("graph2 timer is active")
                UI_MainWindow.timer_graph_2.stop()


    def rewind(UI_MainWindow, isLinked , graphNum):
    # clear the graph
     if isLinked:
        UI_MainWindow.graph1.clear()
        UI_MainWindow.graph2.clear()
        if UI_MainWindow.timer_linked_graphs.isActive():
            UI_MainWindow.timer_linked_graphs.stop()  # Stop the timer if it's running
        UI_MainWindow.time_index_linked_graphs = 0  # Reset the time index to the beginning

        # Start the simulation again from the beginning
        UI_MainWindow.timer_linked_graphs.start()
     else:
        if graphNum == 1:
            UI_MainWindow.graph1.clear()
            if UI_MainWindow.timer_graph_1.isActive():
                UI_MainWindow.timer_graph_1.stop()
            UI_MainWindow.time_index_graph_1 = 0
            UI_MainWindow.timer_graph_1.start()     
        else:
            UI_MainWindow.graph2.clear()
            if UI_MainWindow.timer_graph_2.isActive():
                UI_MainWindow.timer_graph_2.stop()
            UI_MainWindow.time_index_graph_2 = 0
            UI_MainWindow.timer_graph_2.start()     

    def change_color(UI_MainWindow, isLinked ,graphNum):
    # open a color dialog to choose a color
     color = UI_MainWindow.QColorDialog.getColor()
     if isLinked:
        if color.isValid():
            UI_MainWindow.linked_graphs_color = color.name()
     else:

        if color.isValid():
            if graphNum == 1:
                UI_MainWindow.graph1_color  = color.name()
            else:
                UI_MainWindow.graph2_color = color.name()

    def move_to_graph_1_to_2(self):
        if len(self.graph_1_files) > 0:
            # Move the last signal from graph 1 to graph 2
            self.graph_2_files.append(self.graph_1_files.pop())  # Move file from graph 1 to graph 2

            self.timer_graph_1.stop()  # Stop timer for graph 1
            self.graph1.clear()  # Clear graph 1
            self.graph2.clear()  # Clear graph 2

            # Plot new data for graph 1 if available
            if len(self.graph_1_files) > 0:
                graph1Data = self.loadSignalData(self.graph_1_files[-1])  # Load new data for graph 1
                self.signalPlotting(self.graph1, graph1Data, 1)  # Plot the new data on graph 1

            # Load and plot data for graph 2 (the one just moved)
            if len(self.graph_2_files) > 0:
                graph2Data = self.loadSignalData(self.graph_2_files[-1])  # Load data for graph 2
                self.signalPlotting(self.graph2, graph2Data, 2)  # Plot the data on graph 2
        else:
            print("No Signals to Move")


    def move_to_graph_2_to_1(self):
        if len(self.graph_2_files) > 0:
            # Move the last signal from graph 2 to graph 1
            self.graph_1_files.append(self.graph_2_files.pop())  # Move file from graph 2 to graph 1

            self.timer_graph_2.stop()  # Stop timer for graph 2
            self.graph1.clear()  # Clear graph 1
            self.graph2.clear()  # Clear graph 2

            # Plot new data for graph 2 if available
            if len(self.graph_2_files) > 0:
                graph2Data = self.loadSignalData(self.graph_2_files[-1])  # Load new data for graph 2
                self.signalPlotting(self.graph2, graph2Data, 2)  # Plot the new data on graph 2

            # Load and plot data for graph 1 (the one just moved)
            if len(self.graph_1_files) > 0:
                graph1Data = self.loadSignalData(self.graph_1_files[-1])  # Load data for graph 1
                self.signalPlotting(self.graph1, graph1Data, 1)  # Plot the data on graph 1
        else:
            print("No Signals to Move")


# # to show the window uncomment ths code
# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     window = ControlPanel()
#     window.show()
#     sys.exit(app.exec_())
