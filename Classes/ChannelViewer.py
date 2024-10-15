import sys
from PyQt5 import uic
import numpy as np
from PyQt5.QtGui import QPixmap, QPainter
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QListWidget, QPushButton, QFrame, QApplication, QDialog)
import pyqtgraph as pg
from matplotlib.figure import Figure
from scipy.interpolate import interp1d

from Classes.URL_Dialog import UrlDialog


def create_polar_plot():
    figure = Figure()
    ax = figure.add_subplot(111, polar=True)  # Polar axis
    canvas = FigureCanvas(figure)
    return canvas, ax


def plot_rect(signal, rect_plot):
    rect_plot.clear()
    rect_plot.plot(signal['x'], signal['y'], pen='b')
    rect_plot.setTitle("Cartesian Cine")
    rect_plot.setLabel('left', 'Amplitude')
    rect_plot.setLabel('bottom', 'Time')
    rect_plot.showGrid(x=True, y=True)


def plot_polar(signal, polar_ax, polar_canvas):
    polar_ax.clear()

    theta = np.linspace(0, 2 * np.pi, len(signal['y']))
    r = (signal['y'] - np.min(signal['y'])) / (np.max(signal['y']) - np.min(signal['y']))

    polar_ax.scatter(theta, r, color='g', s=20)
    polar_canvas.draw()


def generate_signal(length):
    x = np.linspace(0, 1000, length)
    y = np.sin(x) + 0.5 * np.random.randn(length)
    return {'x': x, 'y': y}


def display_polar_signal(signal, polar_canvas, polar_ax):
    plot_polar(signal, polar_ax, polar_canvas)


def display_rect_signal(signal, viewer):
    viewer.plot(signal, pen='b')
    viewer.signal = signal


class ChannelViewer(QWidget):
    def __init__(self):
        super(ChannelViewer, self).__init__()
        uic.loadUi(r"..\UI\channel_viewer.ui", self)

        self.graph1 = pg.PlotWidget(self)
        self.graph1.setBackground('w')

        self.graph2 = pg.PlotWidget(self)
        self.graph2.setBackground('w')

        self.Glue_Editor = pg.PlotWidget(self)
        self.Glue_Editor.setBackground('w')

        self.polar1_canvas, self.polar1_ax = create_polar_plot()
        self.polar2_canvas, self.polar2_ax = create_polar_plot()

        self.graph_1 = self.findChild(QFrame, "graph1")
        self.graph_2 = self.findChild(QFrame, "graph2")
        self.glue_editor = self.findChild(QFrame, "GlueEditor")
        self.polar_1 = self.findChild(QFrame, "polar1")
        self.polar_2 = self.findChild(QFrame, "polar2")
        self.clear_button = self.findChild(QPushButton, "Clear")
        self.glue_button = self.findChild(QPushButton, "toggle_glue")
        self.snapshot_button = self.findChild(QPushButton, "Snapshot")
        self.action_glue_button = self.findChild(QPushButton, "action_glue")
        self.browse_local_button = self.findChild(QPushButton, "browse_local_button")
        self.browse_remote_button = self.findChild(QPushButton, "browse_remote_button")
        self.signal_block = self.findChild(QWidget, "signal_block")
        self.signal_list = self.findChild(QListWidget, "listWidget")

        self.graph_1.setLayout(QVBoxLayout())
        self.graph_2.setLayout(QVBoxLayout())
        self.glue_editor.setLayout(QVBoxLayout())
        self.polar_1.setLayout(QVBoxLayout())
        self.polar_2.setLayout(QVBoxLayout())

        self.graph_1.layout().addWidget(self.graph1)
        self.graph_2.layout().addWidget(self.graph2)
        self.glue_editor.layout().addWidget(self.Glue_Editor)
        self.polar_1.layout().addWidget(self.polar1_canvas)
        self.polar_2.layout().addWidget(self.polar2_canvas)

        self.signals = {}
        self.Gap_value = 0
        self.active_signals = []
        self.snapshots = []
        self.selected_segments = []
        self.start_line1 = None
        self.end_line1 = None
        self.start_line2 = None
        self.end_line2 = None

        # sample signals to test ui
        self.signal1 = generate_signal(200)
        self.signal2 = generate_signal(200)
        self.signal3 = generate_signal(190)

        display_rect_signal(self.signal1, self.graph1)
        display_rect_signal(self.signal2, self.graph2)
        display_polar_signal(self.signal1, self.polar1_canvas, self.polar1_ax)
        display_polar_signal(self.signal2, self.polar2_canvas, self.polar2_ax)
        # self.display_signal(self.signal3, self.Glue_Editor)

        self.clear_button.hide()
        self.snapshot_button.hide()
        self.action_glue_button.hide()
        self.glue_editor.hide()
        self.clear_button.clicked.connect(self.clear_glue_editor)
        self.glue_button.clicked.connect(self.toggle_glue_editor)
        self.snapshot_button.clicked.connect(self.take_snapshot)
        self.action_glue_button.clicked.connect(self.glue_action)
        self.browse_remote_button.clicked.connect(self.open_url_dialog())

        self.ActiveSignals = [self.signal1, self.signal2, self.signal3]

    def clear_glue_editor(self):
        self.Glue_Editor.clear()
        self.selected_segments.clear()
        if self.start_line1:
            self.graph1.removeItem(self.start_line1)
            self.graph1.removeItem(self.end_line1)
            self.graph2.removeItem(self.start_line2)
            self.graph2.removeItem(self.end_line2)
            self.start_line1 = None
            self.end_line1 = None
            self.start_line2 = None
            self.end_line2 = None
            self.add_segment_selection_lines()
            self.clear_snapshots()
            print("editor cleared")

    def add_segment_selection_lines(self):
        if self.start_line1 is None and self.end_line1 is None and self.start_line2 is None and self.end_line2 is None:
            self.start_line1 = pg.InfiniteLine(pos=10, angle=90, movable=True, pen=pg.mkPen(color='r', width=2))
            self.end_line1 = pg.InfiniteLine(pos=50, angle=90, movable=True, pen=pg.mkPen(color='g', width=2))
            self.start_line2 = pg.InfiniteLine(pos=10, angle=90, movable=True, pen=pg.mkPen(color='r', width=2))
            self.end_line2 = pg.InfiniteLine(pos=50, angle=90, movable=True, pen=pg.mkPen(color='g', width=2))

            self.graph1.addItem(self.start_line1)
            self.graph1.addItem(self.end_line1)
            self.graph2.addItem(self.start_line2)
            self.graph2.addItem(self.end_line2)

    def glue_action(self):
        signal1 = self.graph1.signal
        signal2 = self.graph2.signal
        self.select_segments(signal1, signal2)
        self.glue_segments()

    def toggle_glue_editor(self):
        if self.glue_button.isChecked():
            self.glue_editor.show()
            self.add_segment_selection_lines()
            self.clear_button.show()
            self.snapshot_button.show()
            self.action_glue_button.show()
        else:
            self.clear_glue_editor()
            self.clear_button.hide()
            self.snapshot_button.hide()
            self.action_glue_button.hide()
            self.glue_editor.hide()
            self.graph1.removeItem(self.start_line1)
            self.graph1.removeItem(self.end_line1)
            self.graph2.removeItem(self.start_line2)
            self.graph2.removeItem(self.end_line2)

    def select_segments(self, signal1, signal2):
        start_index1 = np.searchsorted(signal1['x'], self.start_line1.value())
        end_index1 = np.searchsorted(signal1['x'], self.end_line1.value())
        start_index2 = np.searchsorted(signal2['x'], self.start_line2.value())
        end_index2 = np.searchsorted(signal2['x'], self.end_line2.value())

        segment1 = {'x': signal1['x'][start_index1:end_index1], 'y': signal1['y'][start_index1:end_index1]}
        segment2 = {'x': signal2['x'][start_index2:end_index2], 'y': signal2['y'][start_index2:end_index2]}

        self.selected_segments.append(segment1)
        self.selected_segments.append(segment2)

    def glue_segments(self):
        seg1, seg2 = self.selected_segments

        def_gap = seg2['x'][0] - seg1['x'][-1]

        if self.Gap_value != 0:
            actual_gap = self.Gap_value
        else:
            actual_gap = def_gap

        # print(f"default gap: {def_gap}, slider adjusted gap: {actual_gap}")

        if actual_gap > 0:
            interp_x = np.linspace(seg1['x'][-1], seg2['x'][0], 50)
            f = interp1d([seg1['x'][-1], seg2['x'][0]], [seg1['y'][-1], seg2['y'][0]], kind='linear')
            interp_y = f(interp_x)

            glued_x = np.concatenate((seg1['x'], interp_x, seg2['x']))
            glued_y = np.concatenate((seg1['y'], interp_y, seg2['y']))

        elif actual_gap < 0:
            overlap_start = np.searchsorted(seg2['x'], seg1['x'][-1])
            glued_x = np.concatenate((seg1['x'], seg2['x'][overlap_start:]))
            glued_y = np.concatenate((seg1['y'], seg2['y'][overlap_start:]))

        else:
            glued_x = np.concatenate((seg1['x'], seg2['x']))
            glued_y = np.concatenate((seg1['y'], seg2['y']))

        self.Glue_Editor.clear()
        self.Glue_Editor.plot(glued_x, glued_y, pen='g')
        # print("glued and plotted.")

    @staticmethod
    def calc_statistics(signal):
        mean_val = np.mean(signal['y'])
        std_val = np.std(signal['y'])
        max_val = np.max(signal['y'])
        min_val = np.min(signal['y'])
        duration = signal['x'][-1] - signal['x'][0]
        return {"mean": mean_val, "std": std_val, "max": max_val, "min": min_val, "duration": duration}

    def get_signal_stat(self, signal):
        return self.calc_statistics(signal)

    def take_snapshot(self):
        pixmap = QPixmap(self.Glue_Editor.size())
        painter = QPainter(pixmap)
        self.Glue_Editor.render(painter)
        painter.end()

        snapshot_name = f"snapshot_{len(self.snapshots) + 1}.png"
        pixmap.save(snapshot_name)
        self.snapshots.append({'name': snapshot_name, 'image': pixmap})
        print(f"Snapshot saved: {snapshot_name}")
        print(f"snapshots:{self.snapshots}")

    @staticmethod
    def get_snapshots():
        return ChannelViewer().snapshots

    def clear_snapshots(self):
        self.snapshots.clear()
        print("snapshots cleared")

    ##signal fetching
   


if __name__ == "__main__":
    app = QApplication([])
    window = ChannelViewer()
    window.setWindowTitle("Viewers and Signals")
    window.show()
    sys.exit(app.exec_())
