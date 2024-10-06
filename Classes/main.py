
from PyQt5.QtWidgets import QApplication, QMainWindow
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
        self.setGeometry(200, 100, 900, 600)


if __name__ == "__main__":
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec_()
