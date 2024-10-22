import random
import sys
from PyQt6 import uic
import numpy as np
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QPainter, QPen, QColor
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QListWidget, QPushButton, QFrame, QApplication, QDialog, QMessageBox,
                             QFileDialog, QGroupBox, QHBoxLayout, QCheckBox, QLineEdit, QListWidgetItem, QSizePolicy,
                             QSlider, QLabel)
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

        # sample signals to test ui
        # self.signal1 = generate_signal(50)
        # self.signal2 = generate_signal(50)
        if self.signal1 and self.signal2:
            self.plot_rect(self.signal1, self.graph1)
            self.plot_rect(self.signal2, self.graph2)

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

    # Fetch and update glue data.
    def plot_rect(self, signal, rect_plot):
        rect_plot.clear()
        rect_plot.plot(signal['x'], signal['y'], pen='b')
        rect_plot.setTitle(f"{rect_plot}")
        rect_plot.setLabel('left', 'Amplitude')
        rect_plot.setLabel('bottom', 'Time')
        rect_plot.showGrid(x=True, y=True)

        rect_plot.signal = signal
    def update_gap(self, value):
        self.Gap_value = value

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
            print(self.start_line2)
            self.glue_editor.show()
            self.add_segment_selection_lines()
            print(self.end_line2)
            self.clear_button.show()
            self.snapshot_button.show()
            self.action_glue_button.show()
            self.report_generate_button.show()
            self.gap_slider.show()
            self.gap_label.show()
        else:
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
            # self.start_line1 = None
            # self.end_line1 = None
            # self.start_line2 = None
            # self.end_line2 = None

    # Glue Logic Implementation.

    def add_segment_selection_lines(self):
        if self.start_line1 is None and self.end_line1 is None and self.start_line2 is None and self.end_line2 is None:
            self.start_line1 = pg.InfiniteLine(pos=10, angle=90, movable=True,
                                               pen=pg.mkPen(color='r', width=2))
            self.end_line1 = pg.InfiniteLine(pos=50, angle=90, movable=True,
                                             pen=pg.mkPen(color='g', width=2))
            self.start_line2 = pg.InfiniteLine(pos=10, angle=90, movable=True,
                                               pen=pg.mkPen(color='r', width=2))
            self.end_line2 = pg.InfiniteLine(pos=50, angle=90, movable=True,
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

    def glue_segments(self):
        seg1, seg2 = self.selected_segments

        def_gap = seg2['x'][0] - seg1['x'][-1]

        if self.Gap_value != 0:
            actual_gap = def_gap + self.Gap_value
        else:
            actual_gap = def_gap

        if actual_gap > 0:
            interp_x = np.linspace(seg1['x'][-1], seg2['x'][0], 50)
            f = interp1d([seg1['x'][-1], (seg2['x'][0] + seg1['x'][-1]) // 2, seg2['x'][0]],
                         [seg1['y'][-1], (seg2['y'][0] + seg1['y'][-1]) // 2, seg2['y'][0]], kind='quadratic')
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
        signal_glued = {
            'x': glued_x,
            'y': glued_y
        }
        # self.Glue_Editor.plot(glued_x, glued_y, pen='g')
        self.plot_rect(signal_glued, self.Glue_Editor)
        self.calc_statistics(signal_glued)

    # Report Related functions: statistics, snapshots and report window launch.

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
        self.snapshots.append({'name': snapshot_name, 'image': pixmap})
        print(f"Snapshot saved: {snapshot_name}")
        print(f"snapshots:{self.snapshots}")

    # @staticmethod
    # def get_snapshots():
    #     return ChannelViewer().snapshots

    def clear_snapshots(self):
        self.snapshots.clear()
        print("snapshots cleared")

    def report_generate(self):
        self.report_window = ReportGenerate.SignalReportGenerator(self.snapshots)
        self.report_window.show()

    #  browsing
    # def create_signal_widget(self, index):
    #
    #     signal_widget = QGroupBox(f'Signal_{index + 1}')
    #     signal_widget.setStyleSheet("background-color: white;")
    #     signal_layout = QHBoxLayout()
    #     viewer1_checkbox = QCheckBox("Viewer1")
    #     viewer2_checkbox = QCheckBox("Viewer2")
    #     signal_layout.addWidget(viewer1_checkbox)
    #     signal_layout.addWidget(viewer2_checkbox)
    #     viewer1_checkbox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
    #     viewer2_checkbox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
    #
    #     viewer1_checkbox.stateChanged.connect(lambda state: self.handle_viewer_checkbox(state, index, self.graph1))
    #     viewer2_checkbox.stateChanged.connect(lambda state: self.handle_viewer_checkbox(state, index, self.graph2))
    #
    #     signal_widget.setMinimumWidth(200)
    #     signal_widget.setMinimumHeight(100)
    #     signal_widget.setLayout(signal_layout)
    #    return signal_widget

    # def add_signal_to_list(self, index):
    #     item = QListWidgetItem(f"Signal_{index + 1}")
    #     item_widget = self.create_signal_widget(index)
    #     self.signal_block.addItem(item)
    #     self.signal_block.setItemWidget(item, item_widget)
    #     self.hidden_layout.setSpacing(20)
    #
    #
    # def handle_viewer_checkbox(self, state, index, viewer):
    #     if state == 2:  # Checked
    #         self.plot_signal(index, viewer)

    # def plot_signal(self, index, viewer):
    #     signal = self.active_signals[index]
    #
    #     if viewer.objectName() == "graph1":
    #         display_rect_signal(signal, self.graph1)
    #     else:
    #         display_rect_signal(signal, self.graph2)


#     def extract_signal_data(self, source):
#         try:
#             if source.endswith('.csv'):
#                 df = pd.read_csv(source)
#                 signal = {
#                     'x': df.iloc[:, 0].values,  # First column (e.g., Time)
#                     'y': df.iloc[:, 1].values  # Second column (e.g., Amplitude)
#                 }
#                 print(self.active_signals)
#                 return signal
#         except Exception as e:
#             print(f"Error extracting signal data: {e}")
#             return None
#
#     # API handling
#     def fetch_real_time_signal(self):
#         """Fetch real-time signal data (satellite positions) from an API and update the graphs."""
#         try:
#
#             base_url = "https://api.n2yo.com/rest/v1/satellite/positions"
#             satellite_id = "25544"
#             observer_lat = "41.702"
#             observer_lon = "-76.014"
#             observer_alt = "0"
#             seconds = "300"
#             api_key = "PECZAW-Y3BFYT-4TJFVE-5CUH"
#
# api_url = f"{base_url}/{satellite_id}/{observer_lat}/{observer_lon}/{observer_alt}/{seconds}/&apiKey={api_key}"
#
#             response = requests.get(api_url)
#
#             if response.status_code != 200:
#                 raise Exception(f"Failed to fetch data: {response.status_code} {response.reason}")
#
#             data = response.json()
#
#             if 'positions' not in data:
#                 raise KeyError("Response is missing 'positions' data")
#
#             time_points = [pos['timestamp'] for pos in data['positions']]
#             signal_values = [pos['satlatitude'] for pos in data['positions']]
#
#             real_time_signal = {
#                 'x': np.array(time_points, dtype=float),
#                 'y': np.array(signal_values, dtype=float)  #
#             }
#
#             self.active_signals.append(real_time_signal)
#             # self.add_signal_to_list(len(self.active_signals) - 1)
#
#             display_rect_signal(real_time_signal, self.graph1)
#             display_rect_signal(real_time_signal, self.graph2)
#
#         except requests.exceptions.RequestException as e:
#             QMessageBox.critical(self, "Error", f"Network error: {str(e)}")
#         except KeyError as e:
#             QMessageBox.critical(self, "Error", f"Missing data in response: {str(e)}")
#         except ValueError as e:
#             QMessageBox.critical(self, "Error", f"Value error: {str(e)}")
#         except Exception as e:
#             QMessageBox.critical(self, "Error", f"Failed to fetch real-time signal: {str(e)}")
#
#
# # simulate real time emitter
# app = Flask(__name__)
# current_signal = {'x': [], 'y': []}
# running = True
#
#
# @app.route('/')
# def index():
#     return "test"
#
#
# @app.route('/api/signal', methods=['GET'])
# def get_signal():
#     return jsonify(current_signal)
#
#
# @app.route('/stop', methods=['POST'])
# def stop_signal():
#     global running
#     running = False
#     return jsonify({"status": "Signal generation stopped."})
#
#
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
