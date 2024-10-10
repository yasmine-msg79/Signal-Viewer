import PyQt5
import pyqtgraph as pg
from PyQt5 import uic, QtWidgets
import numpy as np


class ChannelViewer(PyQt5.QtWidgets.QWidget):
    def __init__(self):
        super(ChannelViewer, self).__init__()
        uic.loadUi(r"..\UI\channel_viewer.ui", self)
        self.graph1 = pg.PlotWidget(self)
        self.graph1.setBackground('w')
        self.graph2 = pg.PlotWidget(self)
        self.graph2.setBackground('w')
        self.Glue_Editor = pg.PlotWidget(self)
        self.Glue_Editor.setBackground('w')
        self.Polar1 = pg.PlotWidget(self)
        self.Polar1.setBackground('w')
        self.Polar2 = pg.PlotWidget(self)
        self.Polar2.setBackground('w')

        self.graph_1 = self.findChild(QtWidgets.QFrame, "graph1")
        self.graph_2 = self.findChild(QtWidgets.QFrame, "graph2")
        self.glue_editor = self.findChild(QtWidgets.QFrame, "GlueEditor")
        self.polar_1 = self.findChild(QtWidgets.QFrame, "polar1")
        self.polar_2 = self.findChild(QtWidgets.QFrame, "polar2")

        self.graph_1.setLayout(QtWidgets.QVBoxLayout())
        self.graph_2.setLayout(QtWidgets.QVBoxLayout())
        self.glue_editor.setLayout(QtWidgets.QVBoxLayout())
        self.polar_1.setLayout(QtWidgets.QVBoxLayout())
        self.polar_2.setLayout(QtWidgets.QVBoxLayout())


        self.graph_1.layout().addWidget(self.graph1)
        self.graph_2.layout().addWidget(self.graph2)
        self.glue_editor.layout().addWidget(self.Glue_Editor)
        self.polar_1.layout().addWidget(self.Polar1)
        self.polar_2.layout().addWidget(self.Polar2)

        self.graph1.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.graph2.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.Glue_Editor.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.Polar1.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        # sample signals to test ui
        self.signal1 = np.random.randn(160)
        self.signal2 = np.random.randn(340)
        self.signal3 = np.random.randn(190)

        self.display_signal(self.signal1, self.graph1)
        self.display_signal(self.signal2, self.graph2)
        self.display_signal(self.signal3, self.Glue_Editor)




    def display_signal(self, signal, viewer):
        viewer.clear()
        viewer.plot(signal, pen='r')
