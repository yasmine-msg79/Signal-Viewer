import PyQt5
from PyQt5 import uic


class ChannelViewer(PyQt5.QtWidgets.QWidget):
    def __init__(self):
        super(ChannelViewer, self).__init__()
        uic.loadUi(r"..\UI\channel_viewer.UI", self)

