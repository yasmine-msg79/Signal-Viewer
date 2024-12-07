# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Non_rectangular.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

class Ui_polar_window(object):
    def setupUi(self, polar_window):
        if not polar_window.objectName():
            polar_window.setObjectName(u"polar_window")
        polar_window.resize(574, 431)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(polar_window.sizePolicy().hasHeightForWidth())
        polar_window.setSizePolicy(sizePolicy)
        polar_window.setAutoFillBackground(False)
        polar_window.setStyleSheet(u"\n"
"background-color: #242526;\n"
"color:rgb(255, 255, 255);\n"
"")
        self.polar_upload_button = QPushButton(polar_window)
        self.polar_upload_button.setObjectName(u"polar_upload_button")
        self.polar_upload_button.setGeometry(QRect(10, 10, 161, 51))
        font = QFont()
        font.setFamilies([u"-apple-system"])
        font.setPointSize(16)
        font.setBold(True)
        self.polar_upload_button.setFont(font)
        self.polar_upload_button.setStyleSheet(u"QPushButton{\n"
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
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"../../../../../0-MostafaMousaControl_PanelTask/Vital-Signals-Multichannel-Viewer/Vital-Signals-Multichannel-Viewer-main/ui/Icons/upload-.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.polar_upload_button.setIcon(icon)
        self.polar_upload_button.setIconSize(QSize(25, 25))
        self.polar_widget = QWidget(polar_window)
        self.polar_widget.setObjectName(u"polar_widget")
        self.polar_widget.setGeometry(QRect(110, 70, 350, 300))
        self.polar_toggle_button = QPushButton(polar_window)
        self.polar_toggle_button.setObjectName(u"polar_toggle_button")
        self.polar_toggle_button.setGeometry(QRect(20, 370, 131, 51))
        self.polar_toggle_button.setFont(font)
        self.polar_toggle_button.setAutoFillBackground(False)
        self.polar_toggle_button.setStyleSheet(u"QPushButton{\n"
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
        self.polar_clear_button = QPushButton(polar_window)
        self.polar_clear_button.setObjectName(u"polar_clear_button")
        self.polar_clear_button.setGeometry(QRect(420, 370, 131, 51))
        self.polar_clear_button.setFont(font)
        self.polar_clear_button.setAutoFillBackground(False)
        self.polar_clear_button.setStyleSheet(u"QPushButton{\n"
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

        self.retranslateUi(polar_window)

        QMetaObject.connectSlotsByName(polar_window)
    # setupUi

    def retranslateUi(self, polar_window):
        polar_window.setWindowTitle(QCoreApplication.translate("polar_window", u"Non-rectangular Plot", None))
        self.polar_upload_button.setText(QCoreApplication.translate("polar_window", u"Upload", None))
        self.polar_toggle_button.setText(QCoreApplication.translate("polar_window", u"Play", None))
        self.polar_clear_button.setText(QCoreApplication.translate("polar_window", u"Clear", None))
    # retranslateUi

