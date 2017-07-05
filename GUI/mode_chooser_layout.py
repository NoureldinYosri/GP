# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mode_chooser.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.general_img_btn = QtGui.QPushButton(self.centralwidget)
        self.general_img_btn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.general_img_btn.setFont(font)
        self.general_img_btn.setObjectName(_fromUtf8("general_img_btn"))
        self.gridLayout_2.addWidget(self.general_img_btn, 3, 0, 1, 1)
        self.separate_video_btn = QtGui.QPushButton(self.centralwidget)
        self.separate_video_btn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.separate_video_btn.setFont(font)
        self.separate_video_btn.setObjectName(_fromUtf8("separate_video_btn"))
        self.gridLayout_2.addWidget(self.separate_video_btn, 2, 1, 1, 1)
        self.separate_img_btn = QtGui.QPushButton(self.centralwidget)
        self.separate_img_btn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.separate_img_btn.setFont(font)
        self.separate_img_btn.setObjectName(_fromUtf8("separate_img_btn"))
        self.gridLayout_2.addWidget(self.separate_img_btn, 3, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setItalic(False)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.general_video_btn = QtGui.QPushButton(self.centralwidget)
        self.general_video_btn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.general_video_btn.setFont(font)
        self.general_video_btn.setObjectName(_fromUtf8("general_video_btn"))
        self.gridLayout_2.addWidget(self.general_video_btn, 2, 0, 1, 1)
        self.track_players_btn = QtGui.QPushButton(self.centralwidget)
        self.track_players_btn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(10)
        self.track_players_btn.setFont(font)
        self.track_players_btn.setObjectName(_fromUtf8("track_players_btn"))
        self.gridLayout_2.addWidget(self.track_players_btn, 4, 0, 1, 1)
        self.track_ball_btn = QtGui.QPushButton(self.centralwidget)
        self.track_ball_btn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(10)
        self.track_ball_btn.setFont(font)
        self.track_ball_btn.setObjectName(_fromUtf8("track_ball_btn"))
        self.gridLayout_2.addWidget(self.track_ball_btn, 4, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.general_img_btn.setText(_translate("MainWindow", "General Image Model", None))
        self.separate_video_btn.setText(_translate("MainWindow", "Seperate Video Model", None))
        self.separate_img_btn.setText(_translate("MainWindow", "Seperate Image Model", None))
        self.label.setText(_translate("MainWindow", "Choose one of the below modes of operation:", None))
        self.general_video_btn.setText(_translate("MainWindow", "General Video Model", None))
        self.track_players_btn.setText(_translate("MainWindow", "Track Players", None))
        self.track_ball_btn.setText(_translate("MainWindow", "Track Ball", None))

