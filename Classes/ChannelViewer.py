import random
import sys
from PyQt6 import uic
import numpy as np
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QPainter, QPen, QColor
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QListWidget, QPushButton, QFrame, QApplication, QDialog, QMessageBox,
                             QFileDialog, QGroupBox, QHBoxLayout, QCheckBox, QLineEdit, QListWidgetItem, QSizePolicy,
                             QSlider, QLabel, QComboBox)
import pyqtgraph as pg
from scipy.interpolate import interp1d
import MainWindowApp
from Classes import ReportGenerate





def display_rect_signal(signal, viewer):
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    pen_color = QColor(red, green, blue)
    viewer.plot(signal, pen=pen_color)
    viewer.signal = signal


def get_signal_stat():
    return ChannelViewer(MainWindowApp.get_glued_data()).pass_data()


class ChannelViewer(QDialog):
    
    def __init__(self, glue_items, *args, **kwargs):
        super(ChannelViewer, self).__init__(*args, **kwargs)
        # self.limit_graph2 = None
        # self.limit_graph1 = None
        # self.signal2 = None
        # self.signal1 = None
        # self.glue_data = MainWindowApp.get_glued_data()
        # self.main_window = main_instance
        uic.loadUi(r"UI\channel_viewer.ui", self)
        # signal1 = None
        # signal2 = None

        # limit_1, limit_2, signal1, signal2 = MainWindowApp.get_glued_data()
        # self.limit_1 = glue_items[0]
        # self.limit_2 = glue_items[1]
        self.signal1 = glue_items[2]
        self.signal2 = glue_items[3]

        self.graph1 = pg.PlotWidget(self)
        self.graph1.setBackground('black')
        self.graph1.signal = self.signal1

        self.graph2 = pg.PlotWidget(self)
        self.graph2.setBackground('black')
        self.graph2.signal = self.signal2

        self.Glue_Editor = pg.PlotWidget(self)
        self.Glue_Editor.setBackground('black')

        self.graph_1 = self.findChild(QWidget, "graph1")
        self.graph_2 = self.findChild(QWidget, "graph2")
        self.glue_editor = self.findChild(QWidget, "GlueEditor")
        self.clear_button = self.findChild(QPushButton, "Clear")
        self.glue_button = self.findChild(QPushButton, "toggle_glue")
        self.snapshot_button = self.findChild(QPushButton, "Snapshot")
        self.action_glue_button = self.findChild(QPushButton, "action_glue")
        self.report_generate_button = self.findChild(QPushButton, "report_button")
        self.gap_slider = self.findChild(QSlider, "gap_slider")
        self.gap_label = self.findChild(QLabel, "Gap_label")

        self.graph_1.setLayout(QVBoxLayout())
        self.graph_2.setLayout(QVBoxLayout())
        self.glue_editor.setLayout(QVBoxLayout())

        self.graph_1.layout().addWidget(self.graph1)
        self.graph_2.layout().addWidget(self.graph2)
        self.glue_editor.layout().addWidget(self.Glue_Editor)

        self.signals = {}
        self.Gap_value = 0
        self.active_signals = []
        self.glued_statistics = []
        self.snapshots = []
        self.selected_segments = []
        self.report_window = None
        self.start_line1 = None
        self.end_line1 = None
        self.start_line2 = None
        self.end_line2 = None
        self.graph1.setObjectName("graph1")
        self.graph2.setObjectName("graph2")

        # Add fixed colors for signals
        self.signal1_color = pg.mkPen(color='g', width=2)  # Green for signal 1
        self.signal2_color = pg.mkPen(color='b', width=2)  # Blue for signal 2
        
        if self.signal1 and self.signal2:
            self.plot_rect(self.signal1, self.graph1, self.signal1_color)
            self.plot_rect(self.signal2, self.graph2, self.signal2_color)

        # display_rect_signal(self.signal1, self.graph1)
        # display_rect_signal(self.signal2, self.graph2)

        self.clear_button.hide()
        self.snapshot_button.hide()
        self.action_glue_button.hide()
        self.report_generate_button.hide()
        self.gap_slider.hide()
        self.gap_label.hide()
        self.glue_editor.hide()
        self.clear_button.clicked.connect(self.clear_glue_editor)
        self.glue_button.clicked.connect(self.toggle_glue_editor)
        self.snapshot_button.clicked.connect(self.take_snapshot)
        self.action_glue_button.clicked.connect(self.glue_action)
        self.report_generate_button.clicked.connect(self.report_generate)
        self.gap_slider.valueChanged.connect(self.update_gap)

        # Add interpolation combo box
        self.interp_combo = QComboBox()
        self.interp_combo.addItems(['linear', 'quadratic', 'cubic'])
        self.interp_combo.setCurrentText('linear')
        # Connect combo box change signal to update method
        self.interp_combo.currentTextChanged.connect(self.update_interpolation)
        
        # Add to UI layout
        interp_layout = QHBoxLayout()
        interp_layout.addWidget(QLabel("Interpolation:"))
        interp_layout.addWidget(self.interp_combo)
        self.glue_editor.layout().addLayout(interp_layout)

    # Fetch and update glue data.
    def plot_rect(self, signal, rect_plot, pen_color):
        rect_plot.clear()
        rect_plot.plot(signal['x'], signal['y'], pen=pen_color)
        rect_plot.setTitle(f"{rect_plot}")
        rect_plot.setLabel('left', 'Amplitude')
        rect_plot.setLabel('bottom', 'Time')
        rect_plot.showGrid(x=True, y=True)

        rect_plot.signal = signal
    
        self.glue_segments()

    # Button logic: clear, show/hide glue editor, and glue.
    def clear_glue_editor(self):
        self.Glue_Editor.clear()
        self.selected_segments.clear()
        self.graph1.removeItem(self.start_line1)
        self.graph1.removeItem(self.end_line1)
        self.graph2.removeItem(self.start_line2)
        self.graph2.removeItem(self.end_line2)
        self.start_line1 = None
        self.end_line1 = None
        self.start_line2 = None
        self.end_line2 = None
        self.gap_slider.setValue(0)
        self.Gap_value = 0
        self.add_segment_selection_lines()
        self.clear_snapshots()

    def glue_action(self):
        # signal1 = self.graph1.signal
        # signal2 = self.graph2.signal
        self.select_segments(self.signal1, self.signal2)
        self.glue_segments()
        self.graph1.removeItem(self.start_line1)
        self.graph1.removeItem(self.end_line1)
        self.graph2.removeItem(self.start_line2)
        self.graph2.removeItem(self.end_line2)
        self.start_line1 = None
        self.end_line1 = None
        self.start_line2 = None
        self.end_line2 = None

    def toggle_glue_editor(self):
        if self.glue_button.isChecked():
            self.glue_button.setText("Hide Glue Editor")
            self.glue_editor.show()
            self.add_segment_selection_lines()
            self.clear_button.show()
            self.snapshot_button.show()
            self.action_glue_button.show()
            self.report_generate_button.show()
            self.gap_slider.show()
            self.gap_label.show()
        else:
            self.glue_button.setText("Show Glue Editor")
            self.clear_glue_editor()
            self.clear_button.hide()
            self.snapshot_button.hide()
            self.action_glue_button.hide()
            self.report_generate_button.hide()
            self.glue_editor.hide()
            self.gap_slider.hide()
            self.gap_label.hide()
            self.graph1.removeItem(self.start_line1)
            self.graph1.removeItem(self.end_line1)
            self.graph2.removeItem(self.start_line2)
            self.graph2.removeItem(self.end_line2)

    # Glue Logic Implementation.

    def add_segment_selection_lines(self):
        if self.start_line1 is None and self.end_line1 is None and self.start_line2 is None and self.end_line2 is None:
            self.start_line1 = pg.InfiniteLine(pos=self.signal1['x'][0], angle=90, movable=True,
                                               pen=pg.mkPen(color='r', width=2))
            self.end_line1 = pg.InfiniteLine(pos=self.signal1['x'][-1], angle=90, movable=True,
                                             pen=pg.mkPen(color='g', width=2))
            self.start_line2 = pg.InfiniteLine(pos=self.signal2['x'][0], angle=90, movable=True,
                                               pen=pg.mkPen(color='r', width=2))
            self.end_line2 = pg.InfiniteLine(pos=self.signal2['x'][-1], angle=90, movable=True,
                                             pen=pg.mkPen(color='g', width=2))

        self.graph1.addItem(self.start_line1)
        self.graph1.addItem(self.end_line1)
        self.graph2.addItem(self.start_line2)
        self.graph2.addItem(self.end_line2)



    def select_segments(self, signal1, signal2):
        start_index1 = np.searchsorted(signal1['x'], self.start_line1.value())
        end_index1 = np.searchsorted(signal1['x'], self.end_line1.value())
        start_index2 = np.searchsorted(signal2['x'], self.start_line2.value())
        end_index2 = np.searchsorted(signal2['x'], self.end_line2.value())

        segment1 = {'x': signal1['x'][start_index1:end_index1], 'y': signal1['y'][start_index1:end_index1]}
        segment2 = {'x': signal2['x'][start_index2:end_index2], 'y': signal2['y'][start_index2:end_index2]}

        self.selected_segments.append(segment1)
        self.selected_segments.append(segment2)
    
    
    def update_gap(self, value):
        self.Gap_value = value
        if self.selected_segments:
            self.glue_segments()

    def glue_segments(self):
        if len(self.selected_segments) < 2:
            return

        try:
            seg1, seg2 = self.selected_segments

            def_gap = seg2['x'][0] - seg1['x'][-1]
            actual_gap = def_gap + self.Gap_value if self.Gap_value != 0 else def_gap

            if actual_gap > 0:
                # Get interpolation method
                interp_method = self.interp_combo.currentText()
                
                # Create more points for higher order interpolation
                if interp_method in ['quadratic', 'cubic']:
                    # Use more points from the ends of segments for higher order interpolation
                    x_points = [
                        seg1['x'][-2], seg1['x'][-1],  # Two points from end of first segment
                        (seg1['x'][-1] + seg2['x'][0])/2,  # Midpoint
                        seg2['x'][0], seg2['x'][1]  # Two points from start of second segment
                    ]
                    y_points = [
                        seg1['y'][-2], seg1['y'][-1],
                        (seg1['y'][-1] + seg2['y'][0])/2,
                        seg2['y'][0], seg2['y'][1]
                    ]
                else:  # linear interpolation
                    x_points = [seg1['x'][-1], seg2['x'][0]]
                    y_points = [seg1['y'][-1], seg2['y'][0]]

                # Create interpolation points
                num_interp_points = 50
                interp_x = np.linspace(seg1['x'][-1], seg2['x'][0], num_interp_points)
                
                try:
                    # Create interpolation function
                    f = interp1d(x_points, y_points, kind=interp_method)
                    interp_y = f(interp_x)
                except ValueError as e:
                    print(f"Interpolation error: {e}. Falling back to linear interpolation.")
                    # Fallback to linear interpolation
                    f = interp1d([seg1['x'][-1], seg2['x'][0]], 
                               [seg1['y'][-1], seg2['y'][0]], 
                               kind='linear')
                    interp_y = f(interp_x)

                # Combine segments with interpolated points
                glued_x = np.concatenate((seg1['x'], interp_x[1:-1], seg2['x']))
                glued_y = np.concatenate((seg1['y'], interp_y[1:-1], seg2['y']))

            elif actual_gap < 0:
                overlap_start = np.searchsorted(seg2['x'], seg1['x'][-1])
                glued_x = np.concatenate((seg1['x'], seg2['x'][overlap_start:]))
                glued_y = np.concatenate((seg1['y'], seg2['y'][overlap_start:]))

            else:
                glued_x = np.concatenate((seg1['x'], seg2['x']))
                glued_y = np.concatenate((seg1['y'], seg2['y']))

            # Ensure arrays have same length
            min_len = min(len(glued_x), len(glued_y))
            glued_x = glued_x[:min_len]
            glued_y = glued_y[:min_len]

            signal_glued = {'x': glued_x, 'y': glued_y}

            # Update plot with consistent colors
            self.Glue_Editor.clear()
            self.Glue_Editor.plot(seg1['x'], seg1['y'], pen=self.signal1_color)  # Green
            self.Glue_Editor.plot(seg2['x'], seg2['y'], pen=self.signal2_color)  # Blue
            
            # Plot glued sections with their original colors
            glue_start = len(seg1['x'])
            glue_end = glue_start + len(interp_x) - 2
            
            # Plot first segment in green
            self.Glue_Editor.plot(glued_x[:glue_start], glued_y[:glue_start], 
                                 pen=self.signal1_color)
            
            # Plot interpolated section in gray
            if actual_gap > 0:
                self.Glue_Editor.plot(glued_x[glue_start:glue_end], 
                                    glued_y[glue_start:glue_end],
                                    pen=pg.mkPen(color='gray', width=2))
            
            # Plot second segment in blue
            self.Glue_Editor.plot(glued_x[glue_end:], glued_y[glue_end:], 
                                 pen=self.signal2_color)

            self.calc_statistics(signal_glued)
            return signal_glued

        except Exception as e:
            print(f"Error in glue operation: {str(e)}")
            return None

    def calc_statistics(self, signal):
        mean_val = np.mean(signal['y'])
        std_val = np.std(signal['y'])
        max_val = np.max(signal['y'])
        min_val = np.min(signal['y'])
        duration = signal['x'][-1] - signal['x'][0]
        self.glued_statistics = {"Mean": mean_val, "Std": std_val, "Max": max_val, "Min": min_val, "Duration": duration}

    def pass_data(self):
        return self.glued_statistics

    def take_snapshot(self):
        pixmap = QPixmap(self.Glue_Editor.size())
        painter = QPainter(pixmap)
        self.Glue_Editor.render(painter)
        painter.end()

        snapshot_name = f"snapshot_{len(self.snapshots) + 1}.png"
        pixmap.save(snapshot_name)        
        QMessageBox.information(self, "Snapshot Saved", f"Snapshot saved: {snapshot_name}")
        print(f"Snapshot saved: {snapshot_name}")
        print(f"snapshots:{self.snapshots}")
        self.snapshots.append({'name': snapshot_name, 'image': pixmap})


   
    def clear_snapshots(self):
        self.snapshots.clear()
        print("snapshots cleared")

    def report_generate(self):
        self.report_window = ReportGenerate.SignalReportGenerator(self.snapshots)
        self.report_window.show()

    # Add new method to handle interpolation changes
    def update_interpolation(self):
        """Update the glue operation when interpolation method changes"""
        if self.selected_segments:
            self.glue_segments()


def generate_signal(length):
    x = np.linspace(0, 100, length)
    y = np.sin(x) + 0.5 * np.random.randn(length)
    return {'x': x, 'y': y}

if __name__ == "__main__":
    app = QApplication([])
    window = ChannelViewer(glue_items=(10,10,[1,2,3,4,5],[1,2,3,4,5]))
    window.setWindowTitle("Glue Editor")
    window.show()
    sys.exit(app.exec())
