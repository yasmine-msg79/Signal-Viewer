# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'channel_viewer.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QSlider, QWidget)

class Ui_Glue_window(object):
    def setupUi(self, Glue_window):
        if not Glue_window.objectName():
            Glue_window.setObjectName(u"Glue_window")
        Glue_window.resize(773, 663)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Glue_window.sizePolicy().hasHeightForWidth())
        Glue_window.setSizePolicy(sizePolicy)
        Glue_window.setAutoFillBackground(False)
        Glue_window.setStyleSheet(u"\n"
"background-color: #242526;\n"
"color:rgb(255, 255, 255);\n"
"")
        self.GlueEditor = QWidget(Glue_window)
        self.GlueEditor.setObjectName(u"GlueEditor")
        self.GlueEditor.setGeometry(QRect(30, 430, 711, 185))
        self.Snapshot = QPushButton(Glue_window)
        self.Snapshot.setObjectName(u"Snapshot")
        self.Snapshot.setGeometry(QRect(630, 380, 111, 41))
        font = QFont()
        font.setFamilies([u"-apple-system"])
        font.setPointSize(10)
        font.setBold(True)
        self.Snapshot.setFont(font)
        self.Snapshot.setStyleSheet(u"QPushButton{\n"
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
        self.action_glue = QPushButton(Glue_window)
        self.action_glue.setObjectName(u"action_glue")
        self.action_glue.setGeometry(QRect(510, 380, 111, 41))
        self.action_glue.setFont(font)
        self.action_glue.setStyleSheet(u"QPushButton{\n"
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
        self.Clear = QPushButton(Glue_window)
        self.Clear.setObjectName(u"Clear")
        self.Clear.setGeometry(QRect(150, 380, 111, 41))
        self.Clear.setFont(font)
        self.Clear.setStyleSheet(u"QPushButton{\n"
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
        self.toggle_glue = QPushButton(Glue_window)
        self.toggle_glue.setObjectName(u"toggle_glue")
        self.toggle_glue.setGeometry(QRect(30, 380, 111, 41))
        self.toggle_glue.setFont(font)
        self.toggle_glue.setStyleSheet(u"QPushButton{\n"
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
        self.toggle_glue.setCheckable(True)
        self.graph1 = QWidget(Glue_window)
        self.graph1.setObjectName(u"graph1")
        self.graph1.setGeometry(QRect(30, 10, 711, 185))
        self.graph2 = QWidget(Glue_window)
        self.graph2.setObjectName(u"graph2")
        self.graph2.setGeometry(QRect(30, 200, 711, 185))
        self.report_button = QPushButton(Glue_window)
        self.report_button.setObjectName(u"report_button")
        self.report_button.setGeometry(QRect(580, 610, 121, 41))
        self.report_button.setFont(font)
        self.report_button.setStyleSheet(u"QPushButton{\n"
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
        self.gap_slider = QSlider(Glue_window)
        self.gap_slider.setObjectName(u"gap_slider")
        self.gap_slider.setGeometry(QRect(340, 390, 160, 31))
        font1 = QFont()
        font1.setBold(False)
        self.gap_slider.setFont(font1)
        self.gap_slider.setMinimum(-50)
        self.gap_slider.setMaximum(50)
        self.gap_slider.setOrientation(Qt.Horizontal)
        self.gap_slider.setInvertedAppearance(False)
        self.gap_slider.setTickPosition(QSlider.TicksAbove)
        self.Gap_label = QLabel(Glue_window)
        self.Gap_label.setObjectName(u"Gap_label")
        self.Gap_label.setGeometry(QRect(280, 390, 47, 31))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.Gap_label.setFont(font2)

        self.retranslateUi(Glue_window)

        QMetaObject.connectSlotsByName(Glue_window)
    # setupUi

    def retranslateUi(self, Glue_window):
        Glue_window.setWindowTitle(QCoreApplication.translate("Glue_window", u"Form", None))
        self.Snapshot.setText(QCoreApplication.translate("Glue_window", u"Snapshot", None))
        self.action_glue.setText(QCoreApplication.translate("Glue_window", u"Glue Signals", None))
        self.Clear.setText(QCoreApplication.translate("Glue_window", u"Clear", None))
        self.toggle_glue.setText(QCoreApplication.translate("Glue_window", u"Show Glue Editor", None))
        self.report_button.setText(QCoreApplication.translate("Glue_window", u"Generate Report", None))
        self.Gap_label.setText(QCoreApplication.translate("Glue_window", u"  Gap:", None))
    # retranslateUi

