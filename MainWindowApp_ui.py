# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowApp.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)

from pyqtgraph import PlotWidget

class Ui_RealTimeMontoring(object):
    def setupUi(self, RealTimeMontoring):
        if not RealTimeMontoring.objectName():
            RealTimeMontoring.setObjectName(u"RealTimeMontoring")
        RealTimeMontoring.resize(1480, 749)
        font = QFont()
        font.setFamilies([u"Adobe Gothic Std B"])
        font.setPointSize(16)
        font.setBold(True)
        RealTimeMontoring.setFont(font)
        RealTimeMontoring.setStyleSheet(u"\n"
"background-color: #242526;\n"
"color:rgb(255, 255, 255);\n"
"")
        self.centralwidget = QWidget(RealTimeMontoring)
        self.centralwidget.setObjectName(u"centralwidget")
        font1 = QFont()
        font1.setPointSize(12)
        self.centralwidget.setFont(font1)
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, -1, -1, -1)
        self.rightwidget = QWidget(self.centralwidget)
        self.rightwidget.setObjectName(u"rightwidget")
        self.verticalLayout_2 = QVBoxLayout(self.rightwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.importButton = QPushButton(self.rightwidget)
        self.importButton.setObjectName(u"importButton")
        font2 = QFont()
        font2.setFamilies([u"-apple-system"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.importButton.setFont(font2)
        self.importButton.setStyleSheet(u"QPushButton{\n"
"  appearance: button;\n"
"  backface-visibility: hidden;\n"
"  background-color: rgb(0, 154, 231);\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  font-size: 100%;\n"
"  height: 44px;\n"
"  line-height: 1.15;\n"
"  margin: 12px 0 0;\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 10px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-transform: none;\n"
"  transform: translateZ(0);\n"
"  transition: all .2s,box-shadow .08s ease-in;\n"
"  touch-action: manipulation;\n"
"  width: 100%;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 115, 173);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:  rgb(0, 115, 173);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"../../../0-MostafaMousaControl_PanelTask/Vital-Signals-Multichannel-Viewer/Vital-Signals-Multichannel-Viewer-main/ui/Icons/upload-.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.importButton.setIcon(icon)
        self.importButton.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.importButton)

        self.connectButton = QPushButton(self.rightwidget)
        self.connectButton.setObjectName(u"connectButton")
        self.connectButton.setFont(font2)
        self.connectButton.setStyleSheet(u"QPushButton{\n"
"  appearance: button;\n"
"  backface-visibility: hidden;\n"
"  background-color: rgb(0, 154, 231);\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  font-size: 100%;\n"
"  height: 44px;\n"
"  line-height: 1.15;\n"
"  margin: 12px 0 0;\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 10px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-transform: none;\n"
"  transform: translateZ(0);\n"
"  transition: all .2s,box-shadow .08s ease-in;\n"
"  touch-action: manipulation;\n"
"  width: 100%;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 115, 173);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:  rgb(0, 115, 173);\n"
"}\n"
"")
        self.connectButton.setIcon(icon)
        self.connectButton.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.connectButton)

        self.line_8 = QFrame(self.rightwidget)
        self.line_8.setObjectName(u"line_8")
        font3 = QFont()
        font3.setPointSize(100)
        font3.setBold(False)
        self.line_8.setFont(font3)
        self.line_8.setStyleSheet(u"/* Line style */\n"
"\n"
"  /* Set the width of the line */\n"
"  width: 20px;\n"
"\n"
"  /* Set the height of the line */\n"
"  height: 5px;\n"
"\n"
"  /* Set the background color of the line */\n"
"  background-color: #3a3b3c;\n"
"\n"
"  /* Set the border of the line */\n"
"  border: 10px;\n"
"\n"
"  /* Set the border radius of the line */\n"
"  border-radius:5px;\n"
"\n"
"\n"
"\n"
"")
        self.line_8.setLineWidth(50)
        self.line_8.setMidLineWidth(100)
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_8)

        self.hideList1 = QListWidget(self.rightwidget)
        self.hideList1.setObjectName(u"hideList1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hideList1.sizePolicy().hasHeightForWidth())
        self.hideList1.setSizePolicy(sizePolicy)
        self.hideList1.setStyleSheet(u"QListWidget {\n"
"    background-color: #4a4a4a; /* Background color of the list widget */\n"
"    /*border: 1px solid #c0c0c0; /* Border color and width */\n"
"    padding: 5px; /* Padding around the list items */\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    background-color: #4a4a4a; /* Background color of each list item */\n"
"    padding: 5px; /* Padding inside each list item */\n"
"    border-bottom: 1px solid #c0c0c0; /* Separator between list items */\n"
"    border-radius: 15px; /* Border radius for rounded corners */\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #3399ff; /* Background color of selected item */\n"
"    color: #ffffff; /* Text color of selected item */\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: rgb(39, 120, 163); /* Background color when hovering over an item */\n"
"}\n"
"")
        self.hideList1.setAutoScrollMargin(50)

        self.verticalLayout_2.addWidget(self.hideList1)

        self.verticalSpacer_2 = QSpacerItem(180, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.hideList2 = QListWidget(self.rightwidget)
        self.hideList2.setObjectName(u"hideList2")
        sizePolicy.setHeightForWidth(self.hideList2.sizePolicy().hasHeightForWidth())
        self.hideList2.setSizePolicy(sizePolicy)
        self.hideList2.setStyleSheet(u"QListWidget {\n"
"    background-color: #4a4a4a; /* Background color of the list widget */\n"
"    /*border: 1px solid #c0c0c0; /* Border color and width */\n"
"    padding: 5px; /* Padding around the list items */\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    background-color: #4a4a4a; /* Background color of each list item */\n"
"    padding: 5px; /* Padding inside each list item */\n"
"    border-bottom: 1px solid #c0c0c0; /* Separator between list items */\n"
"    border-radius: 15px; /* Border radius for rounded corners */\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #3399ff; /* Background color of selected item */\n"
"    color: #ffffff; /* Text color of selected item */\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: rgb(39, 120, 163); /* Background color when hovering over an item */\n"
"}\n"
"")
        self.hideList2.setAutoScrollMargin(50)

        self.verticalLayout_2.addWidget(self.hideList2)


        self.horizontalLayout_2.addWidget(self.rightwidget)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        font4 = QFont()
        font4.setPointSize(40)
        font4.setBold(False)
        self.line_3.setFont(font4)
        self.line_3.setStyleSheet(u"/* Line style */\n"
"\n"
"  /* Set the width of the line */\n"
"  width: 20px;\n"
"\n"
"  /* Set the height of the line */\n"
"  height: 5px;\n"
"\n"
"  /* Set the background color of the line */\n"
"  background-color: #3a3b3c;\n"
"\n"
"   opacity: 20%;\n"
"\n"
"  /* Set the border of the line */\n"
"  border: 10px;\n"
"\n"
"  /* Set the border radius of the line */\n"
"  border-radius:2px;\n"
"\n"
"\n"
"\n"
"")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_3)

        self.centerwidget = QWidget(self.centralwidget)
        self.centerwidget.setObjectName(u"centerwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centerwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_13 = QLabel(self.centerwidget)
        self.label_13.setObjectName(u"label_13")
        font5 = QFont()
        font5.setFamilies([u"Gabarito"])
        font5.setBold(True)
        self.label_13.setFont(font5)
        self.label_13.setStyleSheet(u"font-family: 'Gabarito', cursive;\n"
"font-size: 20px;\n"
"color: #fff;")

        self.verticalLayout_7.addWidget(self.label_13, 0, Qt.AlignHCenter)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.tabWidget = QTabWidget(self.centerwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        self.tabWidget.setFont(font6)
        self.tabWidget.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.graph1 = PlotWidget(self.tab)
        self.graph1.setObjectName(u"graph1")
        self.graph1.setGeometry(QRect(0, 0, 881, 251))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_8.addWidget(self.tabWidget)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.channelsGraph1 = QComboBox(self.centerwidget)
        self.channelsGraph1.setObjectName(u"channelsGraph1")
        self.channelsGraph1.setMinimumSize(QSize(180, 30))
        self.channelsGraph1.setStyleSheet(u"")
        self.channelsGraph1.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_10.addWidget(self.channelsGraph1)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_10)

        self.deleteButtonGraph1 = QPushButton(self.centerwidget)
        self.deleteButtonGraph1.setObjectName(u"deleteButtonGraph1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.deleteButtonGraph1.sizePolicy().hasHeightForWidth())
        self.deleteButtonGraph1.setSizePolicy(sizePolicy1)
        self.deleteButtonGraph1.setMaximumSize(QSize(150, 16777215))
        self.deleteButtonGraph1.setFont(font2)
        self.deleteButtonGraph1.setStyleSheet(u"QPushButton{\n"
"appearance: button;\n"
"backface-visibility: hidden;\n"
"background-color:  rgb(0, 154, 231);\n"
"border-radius: 6px;\n"
"border-width: 0;\n"
"box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"box-sizing: border-box;\n"
"color: #fff;\n"
"cursor: pointer;\n"
"font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"font-size: 100%;\n"
"height: 30px;\n"
"line-height: 1.15;\n"
"outline: none;\n"
"overflow: hidden;\n"
"padding: 3 10px;\n"
"position: relative;\n"
"text-align: center;\n"
"text-transform: none;\n"
"transform: translateZ(0);\n"
"transition: all .2s,box-shadow .08s ease-in;\n"
"user-select: none;\n"
"-webkit-user-select: none;\n"
"touch-action: manipulation;\n"
"width: 100%; /* Reduced width to 200 pixels */\n"
"}\n"
"QPushButton:hover{\n"
"background-color:  rgb(0, 115, 173);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:  rgb(0, 115, 173);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../../../0-MostafaMousaControl_PanelTask/Vital-Signals-Multichannel-Viewer/Vital-Signals-Multichannel-Viewer-main/ui/Icons/delete-svgrepo-com.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.deleteButtonGraph1.setIcon(icon1)
        self.deleteButtonGraph1.setIconSize(QSize(25, 25))
        self.deleteButtonGraph1.setCheckable(False)
        self.deleteButtonGraph1.setAutoDefault(False)
        self.deleteButtonGraph1.setFlat(True)

        self.horizontalLayout_9.addWidget(self.deleteButtonGraph1)

        self.transferButtonGraph1_2 = QPushButton(self.centerwidget)
        self.transferButtonGraph1_2.setObjectName(u"transferButtonGraph1_2")
        sizePolicy1.setHeightForWidth(self.transferButtonGraph1_2.sizePolicy().hasHeightForWidth())
        self.transferButtonGraph1_2.setSizePolicy(sizePolicy1)
        self.transferButtonGraph1_2.setMaximumSize(QSize(150, 16777215))
        self.transferButtonGraph1_2.setFont(font2)
        self.transferButtonGraph1_2.setStyleSheet(u"QPushButton{\n"
"appearance: button;\n"
"backface-visibility: hidden;\n"
"background-color: rgb(0, 154, 231) ;\n"
"border-radius: 6px;\n"
"border-width: 0;\n"
"box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"box-sizing: border-box;\n"
"color: #fff;\n"
"cursor: pointer;\n"
"font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"font-size: 100%;\n"
"height: 30px;\n"
"line-height: 1.15;\n"
"outline: none;\n"
"overflow: hidden;\n"
"padding: 3 10px;\n"
"position: relative;\n"
"text-align: center;\n"
"text-transform: none;\n"
"transform: translateZ(0);\n"
"transition: all .2s,box-shadow .08s ease-in;\n"
"user-select: none;\n"
"-webkit-user-select: none;\n"
"touch-action: manipulation;\n"
"width: 100%; /* Reduced width to 200 pixels */\n"
"}\n"
"QPushButton:hover{\n"
"background-color:  rgb(0, 115, 173);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:  rgb(0, 115, 173);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Icons/transfer-vertical-svgrepo-com.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.transferButtonGraph1_2.setIcon(icon2)
        self.transferButtonGraph1_2.setIconSize(QSize(25, 25))
        self.transferButtonGraph1_2.setCheckable(False)
        self.transferButtonGraph1_2.setAutoDefault(False)
        self.transferButtonGraph1_2.setFlat(True)

        self.horizontalLayout_9.addWidget(self.transferButtonGraph1_2)

        self.colorButtonGraph1 = QPushButton(self.centerwidget)
        self.colorButtonGraph1.setObjectName(u"colorButtonGraph1")
        sizePolicy1.setHeightForWidth(self.colorButtonGraph1.sizePolicy().hasHeightForWidth())
        self.colorButtonGraph1.setSizePolicy(sizePolicy1)
        self.colorButtonGraph1.setMaximumSize(QSize(150, 16777215))
        self.colorButtonGraph1.setFont(font2)
        self.colorButtonGraph1.setStyleSheet(u"QPushButton{\n"
"appearance: button;\n"
"backface-visibility: hidden;\n"
"background-color:  rgb(0, 154, 231);\n"
"border-radius: 6px;\n"
"border-width: 0;\n"
"box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"box-sizing: border-box;\n"
"color: #fff;\n"
"cursor: pointer;\n"
"font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"font-size: 100%;\n"
"height: 30px;\n"
"line-height: 1.15;\n"
"margin: 0 0 0;\n"
"outline: none;\n"
"overflow: hidden;\n"
"padding: 3 8px;\n"
"position: relative;\n"
"text-align: center;\n"
"text-transform: none;\n"
"transform: translateZ(0);\n"
"transition: all .2s,box-shadow .08s ease-in;\n"
"user-select: none;\n"
"-webkit-user-select: none;\n"
"touch-action: manipulation;\n"
"width: 100%; /* Reduced width to 200 pixels */\n"
"}\n"
"QPushButton:hover{\n"
"background-color:  rgb(0, 115, 173);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:  rgb(0, 115, 173);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../../../0-MostafaMousaControl_PanelTask/Vital-Signals-Multichannel-Viewer/Vital-Signals-Multichannel-Viewer-main/ui/Icons/color-palette-svgrepo-com.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.colorButtonGraph1.setIcon(icon3)
        self.colorButtonGraph1.setIconSize(QSize(22, 22))

        self.horizontalLayout_9.addWidget(self.colorButtonGraph1)

        self.addLabelGraph1 = QLineEdit(self.centerwidget)
        self.addLabelGraph1.setObjectName(u"addLabelGraph1")
        font7 = QFont()
        font7.setPointSize(10)
        self.addLabelGraph1.setFont(font7)
        self.addLabelGraph1.setStyleSheet(u"  position: relative;\n"
"  display: inline-block;\n"
"  height: 32px;\n"
"  width: 210px;\n"
"  margin: 0;\n"
"  padding: 0;\n"
"  background-color: #fff;\n"
"  border: none;\n"
"  border-radius: 10px;\n"
"  color:#0d0d0d;")
        self.addLabelGraph1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.addLabelGraph1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_11)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)


        self.verticalLayout_4.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 5, 0, 0)
        self.line = QFrame(self.centerwidget)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"/* Line style */\n"
"\n"
"  /* Set the width of the line */\n"
"  width: 20px;\n"
"\n"
"  /* Set the height of the line */\n"
"  height: 5px;\n"
"\n"
"  /* Set the background color of the line */\n"
"  background-color: #3a3b3c;\n"
"\n"
"  /* Set the border of the line */\n"
"  border: 10px;\n"
"\n"
"  /* Set the border radius of the line */\n"
"  border-radius:5px;\n"
"\n"
"\n"
"\n"
"")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_7.addWidget(self.line)

        self.line_2 = QFrame(self.centerwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"/* Line style */\n"
"\n"
"  /* Set the width of the line */\n"
"  width: 20px;\n"
"\n"
"  /* Set the height of the line */\n"
"  height: 5px;\n"
"\n"
"  /* Set the background color of the line */\n"
"  background-color: #3a3b3c;\n"
"\n"
"  /* Set the border of the line */\n"
"  border: 10px;\n"
"\n"
"  /* Set the border radius of the line */\n"
"  border-radius:5px;\n"
"\n"
"\n"
"\n"
"")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_7.addWidget(self.line_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.label_10 = QLabel(self.centerwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font5)
        self.label_10.setStyleSheet(u"font-family: 'Gabarito', cursive;\n"
"font-size: 20px;\n"
"color: #fff;")
        self.label_10.setMargin(2)

        self.verticalLayout_6.addWidget(self.label_10, 0, Qt.AlignHCenter)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tabWidget_2 = QTabWidget(self.centerwidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setFont(font6)
        self.tabWidget_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.graph2 = PlotWidget(self.tab_3)
        self.graph2.setObjectName(u"graph2")
        self.graph2.setGeometry(QRect(0, 0, 881, 231))
        self.graph2.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")

        self.horizontalLayout_4.addWidget(self.tabWidget_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.channelsGraph2 = QComboBox(self.centerwidget)
        self.channelsGraph2.setObjectName(u"channelsGraph2")
        self.channelsGraph2.setMinimumSize(QSize(180, 30))
        self.channelsGraph2.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.channelsGraph2)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.deleteButtonGraph2 = QPushButton(self.centerwidget)
        self.deleteButtonGraph2.setObjectName(u"deleteButtonGraph2")
        self.deleteButtonGraph2.setFont(font2)
        self.deleteButtonGraph2.setStyleSheet(u"QPushButton{\n"
"appearance: button;\n"
"backface-visibility: hidden;\n"
"background-color:  rgb(0, 154, 231);\n"
"border-radius: 6px;\n"
"border-width: 0;\n"
"box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"box-sizing: border-box;\n"
"color: #fff;\n"
"cursor: pointer;\n"
"font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"font-size: 100%;\n"
"height: 30px;\n"
"line-height: 1.15;\n"
"outline: none;\n"
"overflow: hidden;\n"
"padding: 3 10px;\n"
"position: relative;\n"
"text-align: center;\n"
"text-transform: none;\n"
"transform: translateZ(0);\n"
"transition: all .2s,box-shadow .08s ease-in;\n"
"user-select: none;\n"
"-webkit-user-select: none;\n"
"touch-action: manipulation;\n"
"width: 100%; /* Reduced width to 200 pixels */\n"
"}\n"
"QPushButton:hover{\n"
"background-color:   rgb(0, 115, 173);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 115, 173);\n"
"}")
        self.deleteButtonGraph2.setIcon(icon1)
        self.deleteButtonGraph2.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.deleteButtonGraph2)

        self.transferButtonGraph2_1 = QPushButton(self.centerwidget)
        self.transferButtonGraph2_1.setObjectName(u"transferButtonGraph2_1")
        self.transferButtonGraph2_1.setFont(font2)
        self.transferButtonGraph2_1.setStyleSheet(u"QPushButton{\n"
"appearance: button;\n"
"backface-visibility: hidden;\n"
"background-color:  rgb(0, 154, 231);\n"
"border-radius: 6px;\n"
"border-width: 0;\n"
"box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"box-sizing: border-box;\n"
"color: #fff;\n"
"cursor: pointer;\n"
"font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"font-size: 100%;\n"
"height: 30px;\n"
"line-height: 1.15;\n"
"outline: none;\n"
"overflow: hidden;\n"
"padding: 3 10px;\n"
"position: relative;\n"
"text-align: center;\n"
"text-transform: none;\n"
"transform: translateZ(0);\n"
"transition: all .2s,box-shadow .08s ease-in;\n"
"user-select: none;\n"
"-webkit-user-select: none;\n"
"touch-action: manipulation;\n"
"width: 100%; /* Reduced width to 200 pixels */\n"
"}\n"
"QPushButton:hover{\n"
"background-color:  rgb(0, 115, 173);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:  rgb(0, 115, 173);\n"
"}")
        self.transferButtonGraph2_1.setIcon(icon2)
        self.transferButtonGraph2_1.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.transferButtonGraph2_1)

        self.colorButtonGraph2 = QPushButton(self.centerwidget)
        self.colorButtonGraph2.setObjectName(u"colorButtonGraph2")
        self.colorButtonGraph2.setFont(font2)
        self.colorButtonGraph2.setStyleSheet(u"QPushButton{\n"
"appearance: button;\n"
"backface-visibility: hidden;\n"
"background-color:  rgb(0, 154, 231);\n"
"border-radius: 6px;\n"
"border-width: 0;\n"
"box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"box-sizing: border-box;\n"
"color: #fff;\n"
"cursor: pointer;\n"
"font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"font-size: 100%;\n"
"height: 30px;\n"
"line-height: 1.15;\n"
"outline: none;\n"
"overflow: hidden;\n"
"padding: 3 8px;\n"
"position: relative;\n"
"text-align: center;\n"
"text-transform: none;\n"
"transform: translateZ(0);\n"
"transition: all .2s,box-shadow .08s ease-in;\n"
"user-select: none;\n"
"-webkit-user-select: none;\n"
"touch-action: manipulation;\n"
"width: 100%; /* Reduced width to 200 pixels */\n"
"}\n"
"QPushButton:hover{\n"
"background-color:   rgb(0, 115, 173);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:   rgb(0, 115, 173);\n"
"}")
        self.colorButtonGraph2.setIcon(icon3)
        self.colorButtonGraph2.setIconSize(QSize(22, 22))

        self.horizontalLayout_6.addWidget(self.colorButtonGraph2)

        self.addLabelGraph2 = QLineEdit(self.centerwidget)
        self.addLabelGraph2.setObjectName(u"addLabelGraph2")
        self.addLabelGraph2.setFont(font7)
        self.addLabelGraph2.setStyleSheet(u"  position: relative;\n"
"  display: inline-block;\n"
"  height: 32px;\n"
"  width: 210px;\n"
"  margin: 0;\n"
"  padding: 0;\n"
"  background-color: #fff;\n"
"  border: none;\n"
"  border-radius: 10px;\n"
"color:#0d0d0d;")
        self.addLabelGraph2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.addLabelGraph2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)


        self.verticalLayout_4.addLayout(self.verticalLayout_6)


        self.horizontalLayout_2.addWidget(self.centerwidget)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        font8 = QFont()
        font8.setPointSize(40)
        self.line_4.setFont(font8)
        self.line_4.setStyleSheet(u"/* Line style */\n"
"\n"
"  /* Set the width of the line */\n"
"  width: 20px;\n"
"\n"
"  /* Set the height of the line */\n"
"  height: 5px;\n"
"\n"
"  /* Set the background color of the line */\n"
"  background-color:#3a3b3c;\n"
"\n"
"  /* Set the border of the line */\n"
"  border: 10px;\n"
"\n"
"  /* Set the border radius of the line */\n"
"  border-radius:5px;\n"
"\n"
"\n"
"\n"
"")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_4)

        self.leftwidget = QWidget(self.centralwidget)
        self.leftwidget.setObjectName(u"leftwidget")
        self.leftwidget.setEnabled(True)
        self.verticalLayout = QVBoxLayout(self.leftwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.graphSelection = QComboBox(self.leftwidget)
        self.graphSelection.addItem("")
        self.graphSelection.addItem("")
        self.graphSelection.addItem("")
        self.graphSelection.setObjectName(u"graphSelection")
        font9 = QFont()
        font9.setFamilies([u"MS Shell Dlg 2"])
        font9.setPointSize(18)
        font9.setBold(False)
        font9.setItalic(False)
        self.graphSelection.setFont(font9)
        self.graphSelection.setStyleSheet(u"font: 75 18pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.graphSelection)

        self.line_5 = QFrame(self.leftwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"/* Line style */\n"
"\n"
"  /* Set the width of the line */\n"
"  width: 20px;\n"
"\n"
"  /* Set the height of the line */\n"
"  height: 5px;\n"
"\n"
"  /* Set the background color of the line */\n"
"  background-color: #3a3b3c;\n"
"\n"
"  /* Set the border of the line */\n"
"  border: 10px;\n"
"\n"
"  /* Set the border radius of the line */\n"
"  border-radius:5px;\n"
"\n"
"\n"
"\n"
"")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_5)

        self.linkButton = QPushButton(self.leftwidget)
        self.linkButton.setObjectName(u"linkButton")
        self.linkButton.setFont(font2)
        self.linkButton.setStyleSheet(u"QPushButton{\n"
"  appearance: button;\n"
"  backface-visibility: hidden;\n"
"  background-color: rgb(0, 181, 133);\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  font-size: 100%;\n"
"  height: 44px;\n"
"  line-height: 1.15;\n"
"  margin: 12px 0 0;\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 10px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-transform: none;\n"
"  transform: translateZ(0);\n"
"  transition: all .2s,box-shadow .08s ease-in;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  width: 100%;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 118, 86);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 118, "
                        "86);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../../../0-MostafaMousaControl_PanelTask/Vital-Signals-Multichannel-Viewer/Vital-Signals-Multichannel-Viewer-main/ui/Icons/play-svgrepo-com.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.linkButton.setIcon(icon4)
        self.linkButton.setIconSize(QSize(22, 22))

        self.verticalLayout.addWidget(self.linkButton)

        self.playButton = QPushButton(self.leftwidget)
        self.playButton.setObjectName(u"playButton")
        self.playButton.setFont(font2)
        self.playButton.setStyleSheet(u"QPushButton{\n"
"  appearance: button;\n"
"  backface-visibility: hidden;\n"
"  background-color:  rgb(0, 154, 231);\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  font-size: 100%;\n"
"  height: 44px;\n"
"  line-height: 1.15;\n"
"  margin: 12px 0 0;\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 10px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-transform: none;\n"
"  transform: translateZ(0);\n"
"  transition: all .2s,box-shadow .08s ease-in;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  width: 100%;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:  rgb(0, 115, 173);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:  rgb(0, 1"
                        "15, 173);\n"
"}")
        self.playButton.setIcon(icon4)
        self.playButton.setIconSize(QSize(22, 22))

        self.verticalLayout.addWidget(self.playButton)

        self.rewindButton = QPushButton(self.leftwidget)
        self.rewindButton.setObjectName(u"rewindButton")
        self.rewindButton.setFont(font2)
        self.rewindButton.setStyleSheet(u"QPushButton{\n"
"  appearance: button;\n"
"  backface-visibility: hidden;\n"
"  background-color:  rgb(0, 154, 231);\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  font-size: 100%;\n"
"  height: 44px;\n"
"  line-height: 1.15;\n"
"  margin: 12px 0 0;\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 25px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-transform: none;\n"
"  transform: translateZ(0);\n"
"  transition: all .2s,box-shadow .08s ease-in;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  width: 100%;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:  rgb(0, 115, 173);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:  rgb(0, 1"
                        "15, 173);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"../../../0-MostafaMousaControl_PanelTask/Vital-Signals-Multichannel-Viewer/Vital-Signals-Multichannel-Viewer-main/ui/Icons/rewind-forward-svgrepo-com.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.rewindButton.setIcon(icon5)
        self.rewindButton.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.rewindButton)

        self.line_6 = QFrame(self.leftwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"/* Line style */\n"
"\n"
"  /* Set the width of the line */\n"
"  width: 20px;\n"
"\n"
"  /* Set the height of the line */\n"
"  height: 5px;\n"
"\n"
"  /* Set the background color of the line */\n"
"  background-color: #3a3b3c;\n"
"\n"
"  /* Set the border of the line */\n"
"  border: 10px;\n"
"\n"
"  /* Set the border radius of the line */\n"
"  border-radius:5px;\n"
"\n"
"\n"
"\n"
"")
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.line_6.setLineWidth(30)
        self.line_6.setMidLineWidth(16)
        self.line_6.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout.addWidget(self.line_6)

        self.hideButton = QPushButton(self.leftwidget)
        self.hideButton.setObjectName(u"hideButton")
        self.hideButton.setFont(font2)
        self.hideButton.setStyleSheet(u"QPushButton{\n"
"  appearance: button;\n"
"  backface-visibility: hidden;\n"
"  background-color:  rgb(0, 154, 231);\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  font-size: 100%;\n"
"  height: 44px;\n"
"  line-height: 1.15;\n"
"  margin: 12px 0 0;\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 25px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-transform: none;\n"
"  transform: translateZ(0);\n"
"  transition: all .2s,box-shadow .08s ease-in;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  width: 100%;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:  rgb(0, 115, 173);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:  rgb(0, 1"
                        "15, 173);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"../../../0-MostafaMousaControl_PanelTask/Vital-Signals-Multichannel-Viewer/Vital-Signals-Multichannel-Viewer-main/ui/Icons/clear-svgrepo-com.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.hideButton.setIcon(icon6)
        self.hideButton.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.hideButton)

        self.zoomIn = QPushButton(self.leftwidget)
        self.zoomIn.setObjectName(u"zoomIn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.zoomIn.sizePolicy().hasHeightForWidth())
        self.zoomIn.setSizePolicy(sizePolicy2)
        self.zoomIn.setMinimumSize(QSize(0, 0))
        self.zoomIn.setFont(font2)
        self.zoomIn.setStyleSheet(u"QPushButton{\n"
"  appearance: button;\n"
"  backface-visibility: hidden;\n"
"  background-color:  rgb(0, 154, 231);\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  font-size: 100%;\n"
"  height: 44px;\n"
"  line-height: 1.15;\n"
"  margin: 12px 0 0;\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 25px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-transform: none;\n"
"  transform: translateZ(0);\n"
"  transition: all .2s,box-shadow .08s ease-in;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  width: 100%;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:  rgb(0, 115, 173);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:  rgb(0, 1"
                        "15, 173);\n"
"}")
        self.zoomIn.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.zoomIn)

        self.zoomOut = QPushButton(self.leftwidget)
        self.zoomOut.setObjectName(u"zoomOut")
        self.zoomOut.setFont(font2)
        self.zoomOut.setStyleSheet(u"QPushButton{\n"
"  appearance: button;\n"
"  backface-visibility: hidden;\n"
"  background-color:  rgb(0, 154, 231);\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  font-size: 100%;\n"
"  height: 44px;\n"
"  line-height: 1.15;\n"
"  margin: 12px 0 0;\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 15px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-transform: none;\n"
"  transform: translateZ(0);\n"
"  transition: all .2s,box-shadow .08s ease-in;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  width: 100%;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:  rgb(0, 115, 173);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:  rgb(0, 1"
                        "15, 173);\n"
"}")
        self.zoomOut.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.zoomOut)

        self.speedLabel = QLabel(self.leftwidget)
        self.speedLabel.setObjectName(u"speedLabel")
        sizePolicy2.setHeightForWidth(self.speedLabel.sizePolicy().hasHeightForWidth())
        self.speedLabel.setSizePolicy(sizePolicy2)
        font10 = QFont()
        font10.setFamilies([u"MS Shell Dlg 2"])
        font10.setPointSize(16)
        font10.setBold(False)
        font10.setItalic(False)
        self.speedLabel.setFont(font10)
        self.speedLabel.setStyleSheet(u"font-family: 'Gabarito', cursive;\n"
"font-size: ;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: #fff;")
        self.speedLabel.setAlignment(Qt.AlignCenter)
        self.speedLabel.setMargin(28)

        self.verticalLayout.addWidget(self.speedLabel)

        self.speedSlider = QSlider(self.leftwidget)
        self.speedSlider.setObjectName(u"speedSlider")
        self.speedSlider.setStyleSheet(u"/* Style for the QSlider */\n"
"\n"
"/* Background of the slider track */\n"
"QSlider {\n"
"    background-color: transparent;\n"
"    height: 16px; /* Set the height of the track */\n"
"\n"
"}\n"
"\n"
"/* Style for the groove (track) */\n"
"QSlider::groove {\n"
"    background: #595a5c; /* Color of the track */\n"
"    border: 0px solid #999; /* Border of the track */\n"
"    height: 10px; /* Set the height of the track */\n"
"    border-radius: 4px; /* Round the corners of the track */\n"
"}\n"
"\n"
"/* Style for the slider handle (thumb) */\n"
"QSlider::handle {\n"
"    background: rgb(0, 170, 127); /* Color of the handle */\n"
"    border: 1px solid ; /* Border of the handle */\n"
"    width: 20px; /* Width of the handle */\n"
"    height: 30px; /* Height of the handle */\n"
"    margin: -5px 0; /* Negative margin to center the handle vertically */\n"
"    border-radius: 2px; /* Round the corners of the handle */\n"
"}\n"
"\n"
"/* Style for the slider handle when pressed */\n"
"QSlider::handle:pressed {\n"
""
                        "    background: rgb(0, 138, 101); /* Color of the handle when pressed */\n"
"    border: 1px solid #3498db; /* Border of the handle when pressed */\n"
"}\n"
"")
        self.speedSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.speedSlider)

        self.verticalSpacer = QSpacerItem(250, 11, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.glue_Button = QPushButton(self.leftwidget)
        self.glue_Button.setObjectName(u"glue_Button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.glue_Button.sizePolicy().hasHeightForWidth())
        self.glue_Button.setSizePolicy(sizePolicy3)
        self.glue_Button.setFont(font2)
        self.glue_Button.setStyleSheet(u"QPushButton{\n"
"  appearance: button;\n"
"  backface-visibility: hidden;\n"
"  background-color:  rgb(0, 154, 231);\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  font-size: 100%;\n"
"  height: 44px;\n"
"  line-height: 1.15;\n"
"  margin: 12px 0 0;\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 25px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-transform: none;\n"
"  transform: translateZ(0);\n"
"  transition: all .2s,box-shadow .08s ease-in;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  width: 100%;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:  rgb(0, 115, 173);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:  rgb(0, 1"
                        "15, 173);\n"
"}")
        self.glue_Button.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.glue_Button)

        self.nonRectangular_Button = QPushButton(self.leftwidget)
        self.nonRectangular_Button.setObjectName(u"nonRectangular_Button")
        sizePolicy3.setHeightForWidth(self.nonRectangular_Button.sizePolicy().hasHeightForWidth())
        self.nonRectangular_Button.setSizePolicy(sizePolicy3)
        self.nonRectangular_Button.setMinimumSize(QSize(270, 55))
        self.nonRectangular_Button.setFont(font2)
        self.nonRectangular_Button.setStyleSheet(u"QPushButton{\n"
"  appearance: button;\n"
"  backface-visibility: hidden;\n"
"  background-color:  rgb(0, 154, 231);\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  box-sizing: border-box;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  font-size: 100%;\n"
"  height: 44px;\n"
"  line-height: 1.15;\n"
"  margin: 12px 0 0;\n"
"  outline: none;\n"
"  overflow: hidden;\n"
"  padding: 0 25px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-transform: none;\n"
"  transform: translateZ(0);\n"
"  transition: all .2s,box-shadow .08s ease-in;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  width: 100%;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:  rgb(0, 115, 173);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:  rgb(0, 1"
                        "15, 173);\n"
"}")
        self.nonRectangular_Button.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.nonRectangular_Button)


        self.horizontalLayout_2.addWidget(self.leftwidget)

        RealTimeMontoring.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(RealTimeMontoring)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1480, 26))
        RealTimeMontoring.setMenuBar(self.menubar)

        self.retranslateUi(RealTimeMontoring)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(RealTimeMontoring)
    # setupUi

    def retranslateUi(self, RealTimeMontoring):
        RealTimeMontoring.setWindowTitle(QCoreApplication.translate("RealTimeMontoring", u"MainWindow", None))
        self.importButton.setText(QCoreApplication.translate("RealTimeMontoring", u"Upload", None))
        self.connectButton.setText(QCoreApplication.translate("RealTimeMontoring", u"Connect", None))
        self.label_13.setText(QCoreApplication.translate("RealTimeMontoring", u"Graph 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("RealTimeMontoring", u"Graph 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("RealTimeMontoring", u"-", None))
        self.deleteButtonGraph1.setText(QCoreApplication.translate("RealTimeMontoring", u"Delete", None))
        self.transferButtonGraph1_2.setText(QCoreApplication.translate("RealTimeMontoring", u"Down", None))
        self.colorButtonGraph1.setText(QCoreApplication.translate("RealTimeMontoring", u" Color", None))
        self.addLabelGraph1.setPlaceholderText(QCoreApplication.translate("RealTimeMontoring", u"Channel Name ", None))
        self.label_10.setText(QCoreApplication.translate("RealTimeMontoring", u"Graph 2", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("RealTimeMontoring", u"Graph 2", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("RealTimeMontoring", u"-", None))
        self.deleteButtonGraph2.setText(QCoreApplication.translate("RealTimeMontoring", u"Delete", None))
        self.transferButtonGraph2_1.setText(QCoreApplication.translate("RealTimeMontoring", u"Up", None))
        self.colorButtonGraph2.setText(QCoreApplication.translate("RealTimeMontoring", u" Color", None))
        self.addLabelGraph2.setPlaceholderText(QCoreApplication.translate("RealTimeMontoring", u"Channel Name", None))
        self.graphSelection.setItemText(0, QCoreApplication.translate("RealTimeMontoring", u"Graph 1", None))
        self.graphSelection.setItemText(1, QCoreApplication.translate("RealTimeMontoring", u"Graph 2", None))
        self.graphSelection.setItemText(2, QCoreApplication.translate("RealTimeMontoring", u"Linked", None))

        self.linkButton.setText(QCoreApplication.translate("RealTimeMontoring", u"Link", None))
        self.playButton.setText(QCoreApplication.translate("RealTimeMontoring", u"Play", None))
        self.rewindButton.setText(QCoreApplication.translate("RealTimeMontoring", u"Rewind", None))
        self.hideButton.setText(QCoreApplication.translate("RealTimeMontoring", u"Hide", None))
        self.zoomIn.setText(QCoreApplication.translate("RealTimeMontoring", u"Zoom In", None))
        self.zoomOut.setText(QCoreApplication.translate("RealTimeMontoring", u"Zoom Out", None))
        self.speedLabel.setText(QCoreApplication.translate("RealTimeMontoring", u"Speed", None))
        self.glue_Button.setText(QCoreApplication.translate("RealTimeMontoring", u"Glue", None))
        self.nonRectangular_Button.setText(QCoreApplication.translate("RealTimeMontoring", u"Non Rectangular", None))
    # retranslateUi

