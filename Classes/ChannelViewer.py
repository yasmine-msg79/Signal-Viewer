from PyQt5 import uic
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QFrame)
import pyqtgraph as pg


def create_polar_plot():
    figure = plt.figure()
    ax = figure.add_subplot(111, polar=True)
    canvas = FigureCanvas(figure)
    return canvas


def plot_rect(signal, rect_plot):
    rect_plot.plot(signal['x'], signal['y'], pen='b')


def plot_polar(signal, polar_plot):
    theta = np.linspace(0, 2 * np.pi, len(signal['x']))
    radius = signal['y']

    ax = polar_plot.figure.gca(polar=True)
    #ax.clear()
    ax.plot(theta, radius)
    polar_plot.draw()


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

        self.Polar1 = create_polar_plot()
        self.Polar2 = create_polar_plot()

        self.graph_1 = self.findChild(QFrame, "graph1")
        self.graph_2 = self.findChild(QFrame, "graph2")
        self.glue_editor = self.findChild(QFrame, "GlueEditor")
        self.polar_1 = self.findChild(QFrame, "polar1")
        self.polar_2 = self.findChild(QFrame, "polar2")
        self.clear_button = self.findChild(QPushButton, "Clear")
        self.glue_button = self.findChild(QPushButton, "toggle_glue")
        self.snapshot_button = self.findChild(QPushButton, "Snapshot")

        self.graph_1.setLayout(QVBoxLayout())
        self.graph_2.setLayout(QVBoxLayout())
        self.glue_editor.setLayout(QVBoxLayout())
        self.polar_1.setLayout(QVBoxLayout())
        self.polar_2.setLayout(QVBoxLayout())

        self.graph_1.layout().addWidget(self.graph1)
        self.graph_2.layout().addWidget(self.graph2)
        self.glue_editor.layout().addWidget(self.Glue_Editor)
        self.polar_1.layout().addWidget(self.Polar1)
        self.polar_2.layout().addWidget(self.Polar2)

        self.signals = {}
        self.active_signals = []
        self.snapshots = []
        self.selected_segments = []
        self.start_line = None
        self.end_line = None

        # sample signals to test ui
        self.signal1 = np.random.randn(160)
        self.signal2 = np.random.randn(340)
        self.signal3 = np.random.randn(190)

        self.display_signal(self.signal1, self.graph1)
        self.display_signal(self.signal2, self.graph2)
        self.display_signal(self.signal3, self.Glue_Editor)

        self.clear_button.hide()
        self.snapshot_button.hide()
        self.glue_editor.hide()
        self.clear_button.clicked.connect(self.clear_glue_editor)
        self.glue_button.clicked.connect(self.toggle_glue_editor)

        self.ActiveSignals = [self.signal1, self.signal2, self.signal3]

    def display_signal(self, signal, viewer):
        viewer.plot(signal, pen='r')

        if viewer == 'graph_1':
            self.graph_1.plot(signal['x'], signal['y'], pen='b')
        elif viewer == 'graph_2':
            self.graph_2.plot(signal['x'], signal['y'], pen='r')
        elif viewer == 'polar_1':
            plot_polar(signal, self.polar_1)
        elif viewer == 'polar_2':
            plot_polar(signal, self.polar_2)

    def clear_glue_editor(self):
        self.Glue_Editor.clear()
        self.selected_segments.clear()
        if self.start_line:
            self.Glue_Editor.removeItem(self.start_line)
            self.Glue_Editor.removeItem(self.end_line)
            self.start_line = None
            self.end_line = None
            print("editor cleared")

    def add_segment_selection_lines(self):
        if self.start_line is None and self.end_line is None:
            self.start_line = pg.InfiniteLine(pos=10, angle=90, movable=True)
            self.start_line.isVisible()
            self.end_line = pg.InfiniteLine(pos=50, angle=90, movable=True)
            self.end_line.isVisible()
            self.graph1.addItem(self.start_line)
            self.graph1.addItem(self.end_line)
            self.graph2.addItem(self.start_line)
            self.graph2.addItem(self.end_line)

    def toggle_glue_editor(self):
        if self.glue_button.isChecked():
            self.glue_editor.show()
            self.add_segment_selection_lines()
            self.clear_button.show()
            self.snapshot_button.show()
        else:
            self.clear_glue_editor()
            self.clear_button.hide()
            self.snapshot_button.hide()
            self.glue_editor.hide()
            self.start_line = None
            self.end_line = None
            self.graph1.removeItem(self.start_line)
            self.graph1.removeItem(self.end_line)
            self.graph2.removeItem(self.start_line)
            self.graph2.removeItem(self.end_line)

    def select_segments(self, signal, start, end):
        pass

    def glue_segments(self):
        pass

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

    def take_snapshot(self, glue_edit):
        pass

    def get_snapshots(self):
        return self.snapshots

    def clear_snapshots(self):
        self.snapshots.clear()
