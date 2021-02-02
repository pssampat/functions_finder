# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'FunctionsFinder.ui'
#
# Created by: Qt User Interface Compiler version 5.15.0
#
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
                            QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient,
                           QPalette, QPainter,
                           QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from src.ui import files_rc


class MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(814, 941)
        MainWindow.setMinimumSize(QSize(600, 900))
        MainWindow.setMaximumSize(QSize(10000, 10000))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
                                 "QToolTip {\n"
                                 "	color: #ffffff;\n"
                                 "	background-color: rgba(27, 29, 35, 160);\n"
                                 "	border: 1px solid rgb(40, 40, 40);\n"
                                 "	border-radius: 2px;\n"
                                 "}")
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(10000, 10000))
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
                                         "color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
                                      "QLineEdit {\n"
                                      "	background-color: rgb(27, 29, 35);\n"
                                      "	border-radius: 5px;\n"
                                      "	border: 2px solid rgb(27, 29, 35);\n"
                                      "	padding-left: 10px;\n"
                                      "}\n"
                                      "QLineEdit:hover {\n"
                                      "	border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QLineEdit:focus {\n"
                                      "	border: 2px solid rgb(91, 101, 124);\n"
                                      "}\n"
                                      "\n"
                                      "/* SCROLL BARS */\n"
                                      "QScrollBar:horizontal {\n"
                                      "    border: none;\n"
                                      "    background: rgb(52, 59, 72);\n"
                                      "    height: 14px;\n"
                                      "    margin: 0px 21px 0 21px;\n"
                                      "	border-radius: 0px;\n"
                                      "}\n"
                                      "QScrollBar::handle:horizontal {\n"
                                      "    background: rgb(85, 170, 255);\n"
                                      "    min-width: 25px;\n"
                                      "	border-radius: 7px\n"
                                      "}\n"
                                      "QScrollBar::add-line:horizontal {\n"
                                      "    border: none;\n"
                                      "    background: rgb(55, 63, 77);\n"
                                      "    width: 20px;\n"
                                      "	border-top-right-radius: 7px;\n"
                                      "    border-bottom-right-radius: 7px;\n"
                                      "    subcontrol-position: right;\n"
                                      "    subcontrol-origin: margin;\n"
                                      "}\n"
                                      "QScrollBar::sub-line:horizontal {\n"
                                      "    border: none;\n"
                                      "    background: rgb(55, 63, 77);\n"
                                      "    width: 20px;\n"
                                      ""
                                      "	border-top-left-radius: 7px;\n"
                                      "    border-bottom-left-radius: 7px;\n"
                                      "    subcontrol-position: left;\n"
                                      "    subcontrol-origin: margin;\n"
                                      "}\n"
                                      "QScrollBar::up-arrow:horizontal, "
                                      "QScrollBar::down-arrow:horizontal\n"
                                      "{\n"
                                      "     background: none;\n"
                                      "}\n"
                                      "QScrollBar::add-page:horizontal, "
                                      "QScrollBar::sub-page:horizontal\n"
                                      "{\n"
                                      "     background: none;\n"
                                      "}\n"
                                      " QScrollBar:vertical {\n"
                                      "	border: none;\n"
                                      "    background: rgb(52, 59, 72);\n"
                                      "    width: 14px;\n"
                                      "    margin: 21px 0 21px 0;\n"
                                      "	border-radius: 0px;\n"
                                      " }\n"
                                      " QScrollBar::handle:vertical {	\n"
                                      "	background: rgb(85, 170, 255);\n"
                                      "    min-height: 25px;\n"
                                      "	border-radius: 7px\n"
                                      " }\n"
                                      " QScrollBar::add-line:vertical {\n"
                                      "     border: none;\n"
                                      "    background: rgb(55, 63, 77);\n"
                                      "     height: 20px;\n"
                                      "	border-bottom-left-radius: 7px;\n"
                                      "    border-bottom-right-radius: 7px;\n"
                                      "     subcontrol-position: bottom;\n"
                                      "     subcontrol-origin: margin;\n"
                                      " }\n"
                                      " QScrollBar::sub-line:vertical {\n"
                                      "	border: none;\n"
                                      "    background: rgb(55, 63"
                                      ", 77);\n"
                                      "     height: 20px;\n"
                                      "	border-top-left-radius: 7px;\n"
                                      "    border-top-right-radius: 7px;\n"
                                      "     subcontrol-position: top;\n"
                                      "     subcontrol-origin: margin;\n"
                                      " }\n"
                                      " QScrollBar::up-arrow:vertical, "
                                      "QScrollBar::down-arrow:vertical {\n"
                                      "     background: none;\n"
                                      " }\n"
                                      "\n"
                                      " QScrollBar::add-page:vertical, "
                                      "QScrollBar::sub-page:vertical {\n"
                                      "     background: none;\n"
                                      " }\n"
                                      "\n"
                                      "/* CHECKBOX */\n"
                                      "QCheckBox::indicator {\n"
                                      "    border: 3px solid rgb(52, 59, 72);\n"
                                      "	width: 15px;\n"
                                      "	height: 15px;\n"
                                      "	border-radius: 10px;\n"
                                      "    background: rgb(44, 49, 60);\n"
                                      "}\n"
                                      "QCheckBox::indicator:hover {\n"
                                      "    border: 3px solid rgb(58, 66, 81);\n"
                                      "}\n"
                                      "QCheckBox::indicator:checked {\n"
                                      "background: 3px solid rgb(52, 59, 72);\n"
                                      "border: 3px solid rgb(52, 59, 72);	\n"
                                      "background-image: "
                                      "url(:/16x16/icons/16x16/"
                                      "cil-check-alt.png);\n"
                                      "}\n"
                                      "\n"
                                      "/* RADIO BUTTON */\n"
                                      "QRadioButton::indicator {\n"
                                      "    border: 3px solid rgb(52, 59, 72);\n"
                                      "	width: 15px;\n"
                                      "	height: 15px;\n"
                                      "	border-radius"
                                      ": 10px;\n"
                                      "    background: rgb(44, 49, 60);\n"
                                      "}\n"
                                      "QRadioButton::indicator:hover {\n"
                                      "    border: 3px solid rgb(58, 66, 81);\n"
                                      "}\n"
                                      "QRadioButton::indicator:checked {\n"
                                      "background: 3px solid rgb(94, 106, 130);\n"
                                      "border: 3px solid rgb(52, 59, 72);	\n"
                                      "}\n"
                                      "\n"
                                      "/* COMBOBOX */\n"
                                      "QComboBox{\n"
                                      "	background-color: rgb(27, 29, 35);\n"
                                      "	border-radius: 5px;\n"
                                      "	border: 2px solid rgb(27, 29, 35);\n"
                                      "	padding: 5px;\n"
                                      "	padding-left: 10px;\n"
                                      "}\n"
                                      "QComboBox:hover{\n"
                                      "	border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QComboBox::drop-down {\n"
                                      "	subcontrol-origin: padding;\n"
                                      "	subcontrol-position: top right;\n"
                                      "	width: 25px; \n"
                                      "	border-left-width: 3px;\n"
                                      "	border-left-color: rgba(39, 44, 54, 150);\n"
                                      "	border-left-style: solid;\n"
                                      "	border-top-right-radius: 3px;\n"
                                      "	border-bottom-right-radius: 3px;	\n"
                                      "	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
                                      "	background-position: center;\n"
                                      "	background-repeat: no-reperat;\n"
                                      " }\n"
                                      "QComboBox QAbstractItemView {\n"
                                      "	color: rgb("
                                      "85, 170, 255);	\n"
                                      "	background-color: rgb(27, 29, 35);\n"
                                      "	padding: 10px;\n"
                                      "	selection-background-color: rgb(39, 44, 54);\n"
                                      "}\n"
                                      "\n"
                                      "/* SLIDERS */\n"
                                      "QSlider::groove:horizontal {\n"
                                      "    border-radius: 9px;\n"
                                      "    height: 18px;\n"
                                      "	margin: 0px;\n"
                                      "	background-color: rgb(52, 59, 72);\n"
                                      "}\n"
                                      "QSlider::groove:horizontal:hover {\n"
                                      "	background-color: rgb(55, 62, 76);\n"
                                      "}\n"
                                      "QSlider::handle:horizontal {\n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "    border: none;\n"
                                      "    height: 18px;\n"
                                      "    width: 18px;\n"
                                      "    margin: 0px;\n"
                                      "	border-radius: 9px;\n"
                                      "}\n"
                                      "QSlider::handle:horizontal:hover {\n"
                                      "    background-color: rgb(105, 180, 255);\n"
                                      "}\n"
                                      "QSlider::handle:horizontal:pressed {\n"
                                      "    background-color: rgb(65, 130, 195);\n"
                                      "}\n"
                                      "\n"
                                      "QSlider::groove:vertical {\n"
                                      "    border-radius: 9px;\n"
                                      "    width: 18px;\n"
                                      "    margin: 0px;\n"
                                      "	background-color: rgb(52, 59, 72);\n"
                                      "}\n"
                                      "QSlider::groove:vertical:hover {\n"
                                      "	background-color: rgb(55, 62, 76);\n"
                                      "}\n"
                                      "QSlider::handle:verti"
                                      "cal {\n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "	border: none;\n"
                                      "    height: 18px;\n"
                                      "    width: 18px;\n"
                                      "    margin: 0px;\n"
                                      "	border-radius: 9px;\n"
                                      "}\n"
                                      "QSlider::handle:vertical:hover {\n"
                                      "    background-color: rgb(105, 180, 255);\n"
                                      "}\n"
                                      "QSlider::handle:vertical:pressed {\n"
                                      "    background-color: rgb(65, 130, 195);\n"
                                      "}\n"
                                      "\n"
                                      "")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 40))
        self.frame_top.setMaximumSize(QSize(16777215, 40))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(
            u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(
                u"background: transparent;\n"
                "background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
                "background-position: center;\n"
                "background-repeat: no-repeat;\n"
                "")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)
        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
                                               "color: rgb(100, 100, 100)")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)

        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy.setHeightForWidth(
            self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy1)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(
                u"QPushButton {	\n"
                "	border: none;\n"
                "	background-color: transparent;\n"
                "}\n"
                "QPushButton:hover {\n"
                "	background-color: rgb(52, 59, 72);\n"
                "}\n"
                "QPushButton:pressed {	\n"
                "	background-color: rgb(85, 170, 255);\n"
                "}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(),
                     QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy1.setHeightForWidth(
            self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy1)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(
                u"QPushButton {	\n"
                "	border: none;\n"
                "	background-color: transparent;\n"
                "}\n"
                "QPushButton:hover {\n"
                "	background-color: rgb(52, 59, 72);\n"
                "}\n"
                "QPushButton:pressed {	\n"
                "	background-color: rgb(85, 170, 255);\n"
                "}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(),
                      QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy1.setHeightForWidth(
            self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy1)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
                                     "	border: none;\n"
                                     "	background-color: transparent;\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "	background-color: rgb(52, 59, 72);\n"
                                     "}\n"
                                     "QPushButton:pressed {	\n"
                                     "	background-color: rgb(85, 170, 255);\n"
                                     "}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal,
                      QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)

        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0,
                                          Qt.AlignRight)

        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.horizontalLayout_3.addWidget(self.frame_top_right)

        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy2)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(
            u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(self.frame_content)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"background: transparent;")
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frameB = QFrame(self.frame)
        self.frameB.setObjectName(u"frameB")
        self.frameB.setStyleSheet(u"border-radius: 5px;")
        self.frameB.setFrameShape(QFrame.StyledPanel)
        self.frameB.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frameB)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.frameB)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setStyleSheet(
            u"background-color: rgb(41, 45, 56);\n"
            "border-radius: 5px;\n"
            "")
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setStyleSheet(
            u"background-color: rgb(39, 44, 54); border-radius: 5px;")
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(
            u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font1)
        self.labelBoxBlenderInstalation.setStyleSheet(
            u"color: rgb(100, 100, 100)")

        self.verticalLayout_8.addWidget(self.labelBoxBlenderInstalation)

        self.verticalLayout_7.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.textBoxA = QLineEdit(self.frame_content_wid_1)
        self.textBoxA.setObjectName(u"textBoxA")
        self.textBoxA.setMinimumSize(QSize(0, 30))
        self.textBoxA.setStyleSheet(u"QLineEdit {\n"
                                    "	background-color: rgb(27, 29, 35);\n"
                                    "	border-radius: 5px;\n"
                                    "	border: 2px solid rgb(27, 29, 35);\n"
                                    "	padding-left: 10px;\n"
                                    "}\n"
                                    "QLineEdit:hover {\n"
                                    "	border: 2px solid rgb(64, 71, 88);\n"
                                    "}\n"
                                    "QLineEdit:focus {\n"
                                    "	border: 2px solid rgb(91, 101, 124);\n"
                                    "}")

        self.gridLayout.addWidget(self.textBoxA, 0, 0, 1, 1)

        self.backBtn = QPushButton(self.frame_content_wid_1)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setMinimumSize(QSize(64, 32))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(9)
        self.backBtn.setFont(font2)
        self.backBtn.setStyleSheet(u"QPushButton {\n"
                                   "	border: 2px solid rgb(52, 59, 72);\n"
                                   "	border-radius: 16px;	\n"
                                   "	background-color: rgb(52, 59, 72);\n"
                                   "}\n"
                                   "QPushButton:hover {\n"
                                   "	background-color: rgb(57, 65, 80);\n"
                                   "	border: 2px solid rgb(61, 70, 86);\n"
                                   "}\n"
                                   "QPushButton:pressed {	\n"
                                   "	background-color: rgb(35, 40, 49);\n"
                                   "	border: 2px solid rgb(43, 50, 61);\n"
                                   "}")
        icon3 = QIcon()
        icon3.addFile(u":/20x20/icons/20x20/cil-arrow-circle-left.png", QSize(),
                      QIcon.Normal, QIcon.Off)
        self.backBtn.setIcon(icon3)

        self.gridLayout.addWidget(self.backBtn, 0, 1, 1, 1)

        self.horizontalLayout_9.addLayout(self.gridLayout)

        self.verticalLayout_7.addWidget(self.frame_content_wid_1)

        self.verticalLayout_15.addWidget(self.frame_div_content_1)

        self.frame_2 = QFrame(self.frameB)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 150))
        self.frame_2.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
                                   "border-radius: 5px;\n"
                                   "color:  rgb(70, 100, 130);\n"
                                   "")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setContentsMargins(6, 6, 6, 6)
        self.list_widget = QListWidget(self.frame_2)
        self.list_widget.setObjectName(u"list_widget")
        self.list_widget.setMaximumSize(QSize(300, 16777215))
        self.list_widget.setMouseTracking(True)
        self.list_widget.setToolTipDuration(3)
        self.list_widget.setStyleSheet(u"")
        self.list_widget.setSortingEnabled(False)

        self.gridLayout_2.addWidget(self.list_widget, 0, 0, 1, 1)

        self.help_display_text_box = QPlainTextEdit(self.frame_2)
        self.help_display_text_box.setObjectName(u"help_display_text_box")
        self.help_display_text_box.setMinimumSize(QSize(200, 200))
        self.help_display_text_box.viewport().setProperty("cursor", QCursor(
            Qt.IBeamCursor))
        self.help_display_text_box.setMouseTracking(False)
        self.help_display_text_box.setStyleSheet(
                u"QPlainTextEdit {\n"
                "	background-color: rgb(27, 29, 35);\n"
                "	border-radius: 5px;\n"
                "	padding: 10px;\n"
                "}\n"
                "QPlainTextEdit:hover {\n"
                "	border: 2px solid rgb(64, 71, 88);\n"
                "}\n"
                "QPlainTextEdit:focus {\n"
                "	border: 2px solid rgb(91, 101, 124);\n"
                "}")
        self.help_display_text_box.setReadOnly(True)
        self.help_display_text_box.setOverwriteMode(False)
        self.help_display_text_box.setBackgroundVisible(False)

        self.gridLayout_2.addWidget(self.help_display_text_box, 0, 2, 1, 1)

        self.help_button = QPushButton(self.frame_2)
        self.help_button.setObjectName(u"help_button")
        self.help_button.setMinimumSize(QSize(32, 64))
        self.help_button.setFont(font2)
        self.help_button.setStyleSheet(
                u"QPushButton {\n"
                "	border: 2px solid rgb(52, 59, 72);\n"
                "	border-radius: 16px;	\n"
                "	background-color: rgb(52, 59, 72);\n"
                "}\n"
                "QPushButton:hover {\n"
                "	background-color: rgb(57, 65, 80);\n"
                "	border: 2px solid rgb(61, 70, 86);\n"
                "}\n"
                "QPushButton:pressed {	\n"
                "	background-color: rgb(35, 40, 49);\n"
                "	border: 2px solid rgb(43, 50, 61);\n"
                "}")
        icon4 = QIcon()
        icon4.addFile(u":/20x20/icons/20x20/cil-arrow-circle-right.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.help_button.setIcon(icon4)

        self.gridLayout_2.addWidget(self.help_button, 0, 1, 1, 1)

        self.verticalLayout_11.addLayout(self.gridLayout_2)

        self.verticalLayout_15.addWidget(self.frame_2)

        self.verticalLayout_6.addWidget(self.frameB)

        self.frame_title_wid_3 = QFrame(self.frame)
        self.frame_title_wid_3.setObjectName(u"frame_title_wid_3")
        self.frame_title_wid_3.setMaximumSize(QSize(16777215, 64))
        self.frame_title_wid_3.setStyleSheet(
            u"background-color: rgb(39, 44, 54);\n"
            "border-radius: 5px")
        self.frame_title_wid_3.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_title_wid_3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, -1, -1)
        self.searchTextBox = QLineEdit(self.frame_title_wid_3)
        self.searchTextBox.setObjectName(u"searchTextBox")
        self.searchTextBox.setMinimumSize(QSize(0, 30))
        self.searchTextBox.setStyleSheet(
                u"QLineEdit {\n"
                "	background-color: rgb(27, 29, 35);\n"
                "	border-radius: 5px;\n"
                "	border: 2px solid rgb(27, 29, 35);\n"
                "	padding-left: 10px;\n"
                "}\n"
                "QLineEdit:hover {\n"
                "	border: 2px solid rgb(64, 71, 88);\n"
                "}\n"
                "QLineEdit:focus {\n"
                "	border: 2px solid rgb(91, 101, 124);\n"
                "}")

        self.gridLayout_3.addWidget(self.searchTextBox, 0, 1, 1, 1)

        self.labelBoxBlenderInstalation_3 = QLabel(self.frame_title_wid_3)
        self.labelBoxBlenderInstalation_3.setObjectName(
            u"labelBoxBlenderInstalation_3")
        self.labelBoxBlenderInstalation_3.setFont(font1)
        self.labelBoxBlenderInstalation_3.setStyleSheet(
            u"color: rgb(100, 100, 100)")
        self.gridLayout_3.addWidget(self.labelBoxBlenderInstalation_3, 0, 0, 1,
                                    1)
        self.verticalLayout_17.addLayout(self.gridLayout_3)
        self.verticalLayout_6.addWidget(self.frame_title_wid_3)
        self.verticalLayout_9.addWidget(self.frame)
        self.verticalLayout_4.addWidget(self.frame_content)
        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        self.label_credits.setFont(font3)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.horizontalLayout_7.addWidget(self.label_credits)
        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font3)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.horizontalLayout_7.addWidget(self.label_version)
        self.horizontalLayout_6.addWidget(self.frame_label_bottom)
        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(
                u"QSizeGrip {\n"
                "background-image: url"
                "(:/16x16/icons/16x16/cil-size-grip.png);\n"
                "background-position: center;\n"
                "background-repeat: no-reperat;\n"
                "}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6.addWidget(self.frame_size_grip)
        self.verticalLayout_4.addWidget(self.frame_grip)
        self.horizontalLayout_2.addWidget(self.frame_content_right)
        self.verticalLayout.addWidget(self.frame_center)
        self.horizontalLayout.addWidget(self.frame_main)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title_bar_top.setText(
            QCoreApplication.translate("MainWindow", u"Functions Finder", None))
        # if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(
            QCoreApplication.translate("MainWindow", u"Minimize", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
        # if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(
            QCoreApplication.translate("MainWindow", u"Maximize", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
        # if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(
            QCoreApplication.translate("MainWindow", u"Close", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.labelBoxBlenderInstalation.setText(
            QCoreApplication.translate("MainWindow", u"Function:", None))
        self.textBoxA.setPlaceholderText("")
        self.backBtn.setText(
            QCoreApplication.translate("MainWindow", u"&Back", None))
        # if QT_CONFIG(tooltip)
        self.list_widget.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.help_display_text_box.setDocumentTitle("")
        self.help_display_text_box.setPlainText(
            QCoreApplication.translate("MainWindow", u"<Nothing to display>",
                                       None))
        self.help_display_text_box.setPlaceholderText("")
        self.help_button.setText("")
        self.searchTextBox.setPlaceholderText("")
        self.labelBoxBlenderInstalation_3.setText(
            QCoreApplication.translate("MainWindow", u"Search:", None))
        self.label_credits.setText(
            QCoreApplication.translate("MainWindow", u"Made by Pratik Sampat",
                                       None))
        self.label_version.setText(
            QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi
