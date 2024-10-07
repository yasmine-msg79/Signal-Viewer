import PyQt5
import pyqtgraph as pg
from PyQt5 import uic, QtWidgets
import numpy as np


class ChannelViewer(PyQt5.QtWidgets.QWidget):
    def __init__(self):
        super(ChannelViewer, self).__init__()
        uic.loadUi(r"..\UI\channel_viewer.ui", self)
        self.Cine_1 = pg.PlotWidget(self)
        self.Cine_1.setBackground('w')
        self.Cine_2 = pg.PlotWidget(self)
        self.Cine_2.setBackground('w')
        self.Cine_glue = pg.PlotWidget(self)
        self.Cine_glue.setBackground('w')
        self.Cine_polar = pg.PlotWidget(self)
        self.Cine_polar.setBackground('w')

        self.cine_1 = self.findChild(QtWidgets.QFrame, "cine_1")
        self.cine_2 = self.findChild(QtWidgets.QFrame, "cine_2")
        self.cine_glue = self.findChild(QtWidgets.QFrame, "cine_glue")
        self.cine_polar = self.findChild(QtWidgets.QFrame, "cine_polar")

        self.cine_1.setLayout(QtWidgets.QVBoxLayout())
        self.cine_2.setLayout(QtWidgets.QVBoxLayout())
        self.cine_glue.setLayout(QtWidgets.QVBoxLayout())
        self.cine_polar.setLayout(QtWidgets.QVBoxLayout())

        self.cine_1.layout().addWidget(self.Cine_1)
        self.cine_2.layout().addWidget(self.Cine_2)
        self.cine_glue.layout().addWidget(self.Cine_glue)
        self.cine_polar.layout().addWidget(self.Cine_polar)

        self.Cine_1.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.Cine_2.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.Cine_glue.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.Cine_polar.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        # sample signals to test ui
        self.signal1 = np.random.randn(160)
        self.signal2 = np.random.randn(340)
        self.signal3 = np.random.randn(190)

        self.display_signal(self.signal1, self.Cine_1)
        self.display_signal(self.signal2, self.Cine_2)
        self.display_signal(self.signal3, self.Cine_glue)

    def display_signal(self, signal, viewer):
        viewer.clear()
        viewer.plot(signal, pen='r')
