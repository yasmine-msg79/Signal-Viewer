
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout
import ChannelViewer
import ControlPanel
import ReportGenerate
import SignalFetch


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.channel_viewer = ChannelViewer.ChannelViewer()
        self.control_panel = ControlPanel.ControlPanel()
        self.report_generator = ReportGenerate.ReportGenerate()
        self.signal_fetcher = SignalFetch.SignalFetch()

        self.setWindowTitle("Signal Viewer")
        self.showMaximized()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout(central_widget)

        #left = QWidget()
        right = QWidget()
        layout.addWidget(self.signal_fetcher)
        layout.addWidget(self.channel_viewer)
        layout.addWidget(right)

        self.signal_fetcher.setFixedWidth(200)
        right.setFixedWidth(150)

        layout.setStretch(0, 1)
        layout.setStretch(1, 3)
        layout.setStretch(2, 1)


if __name__ == "__main__":
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec_()
