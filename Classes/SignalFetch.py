from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class SignalFetch(QWidget):
    def __init__(self):
        super().__init__()

        self.imported_signal = QVBoxLayout()
        # Widgets
        self.signal_label = QLabel("signal-1", self)
        self.signal_name = QLineEdit(self)
        self.update_signal_label = QPushButton("Update Label", self)
        self.set_signal_color = QPushButton("Select Color", self)
        self.channel_one = QCheckBox("Channel 1", self)
        self.channel_two = QCheckBox("Channel 2", self)
        self.initUI()

    def initUI(self):
        # Add widgets to the layout
        self.imported_signal.addWidget(self.signal_label)
        self.imported_signal.addWidget(self.signal_name)
        self.imported_signal.addWidget(self.update_signal_label)
        self.imported_signal.addWidget(self.set_signal_color)
        self.imported_signal.addWidget(self.channel_one)
        self.imported_signal.addWidget(self.channel_two)

        # Set layout to the widget
        self.setLayout(self.imported_signal)

        # Apply UI settings
        self.imported_signal.setContentsMargins(20, 20, 20, 20)
        self.imported_signal.setSpacing(30)
        self.signal_name.setPlaceholderText("update label")
        self.signal_name.setMaximumWidth(200)  
        self.set_signal_color.setMaximumWidth(200)
        self.update_signal_label.setMaximumWidth(200) 
        self.signal_name.setStyleSheet("padding:5px;") 
        self.signal_label.setStyleSheet("font-size:15px;")

        self.update_signal_label.setStyleSheet("""
            color: white;
            background-color: #0077c0;
            border-radius: 5px;
            font-weight: bold;
            height: 30px;
        """)
        self.set_signal_color.setStyleSheet("""
            color: white;
            background-color: #0077c0;
            border-radius: 5px;
            font-weight: bold;
            height: 30px;
        """)
        
