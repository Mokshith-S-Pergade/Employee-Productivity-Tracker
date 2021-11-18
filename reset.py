# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reset.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymongo
from pymongo import MongoClient
from PyQt5.QtWidgets import QMessageBox
import logging
logger = logging.getLogger(__name__)
f_handler = logging.FileHandler('app.log')
f_handler.setLevel(logging.DEBUG)

class Ui_ResetWindow(object):
    def setupUi(self, ResetWindow):
        ResetWindow.setObjectName("ResetWindow")
        ResetWindow.resize(992, 759)
        ResetWindow.setMaximumSize(QtCore.QSize(992, 759))

        
        icon=QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Athrved3.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        ResetWindow.setWindowIcon(icon)
        
        self.centralwidget = QtWidgets.QWidget(ResetWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Back4 = QtWidgets.QLabel(self.centralwidget)
        self.Back4.setGeometry(QtCore.QRect(-10, 0, 1001, 731))
        self.Back4.setStyleSheet("background-color: rgb(171, 171, 171);")
        self.Back4.setText("")
        self.Back4.setObjectName("Back4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 280, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(220, 460, 221, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 560, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(23, 162, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.update)
        self.newpass1 = QtWidgets.QLineEdit(self.centralwidget)
        self.newpass1.setGeometry(QtCore.QRect(480, 460, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.newpass1.setFont(font)
        self.newpass1.setAutoFillBackground(False)
        self.newpass1.setStyleSheet("border-radius:10px;\n""")
        self.newpass1.setInputMask("")
        self.newpass1.setText("")
        self.newpass1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newpass1.setCursorPosition(0)
        self.newpass1.setObjectName("newpass1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 120, 161, 161))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("reset.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(-30, -20, 1071, 121))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(610, 20, 351, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(26)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -20, 221, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Athrved.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.showpass4 = QtWidgets.QCheckBox(self.centralwidget)
        self.showpass4.setGeometry(QtCore.QRect(730, 520, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(True)
        self.showpass4.setFont(font)
        self.showpass4.setObjectName("showpass4")
        self.userid = QtWidgets.QLineEdit(self.centralwidget)
        self.userid.setGeometry(QtCore.QRect(480, 390, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.userid.setFont(font)
        self.userid.setAutoFillBackground(False)
        self.userid.setStyleSheet("border-radius:10px;\n""")
        self.userid.setInputMask("")
        self.userid.setText("")
        self.userid.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.userid.setCursorPosition(0)
        self.userid.setObjectName("userid")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(310, 390, 131, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        ResetWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ResetWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 992, 26))
        self.menubar.setObjectName("menubar")
        ResetWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ResetWindow)
        self.statusbar.setObjectName("statusbar")
        ResetWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ResetWindow)
        QtCore.QMetaObject.connectSlotsByName(ResetWindow)
        self.showpass4.stateChanged.connect(self.pass_view3)

    def retranslateUi(self, ResetWindow):
        _translate = QtCore.QCoreApplication.translate
        ResetWindow.setWindowTitle(_translate("ResetWindow", "Athrv-Ed LMS Productivity Tracker"))
        self.label_5.setText(_translate("ResetWindow", "Reset Password"))
        self.label_6.setText(_translate("ResetWindow", "New Password "))
        self.pushButton.setStatusTip(_translate("ResetWindow", "Click to Reset"))
        self.pushButton.setText(_translate("ResetWindow", "Reset"))
        self.newpass1.setStatusTip(_translate("ResetWindow", "Enter a New Password"))
        self.label_8.setText(_translate("ResetWindow", "Productivity Tracker"))
        self.showpass4.setStatusTip(_translate("ResetWindow", "Check to Unhide"))
        self.showpass4.setText(_translate("ResetWindow", "Show Password"))
        self.userid.setStatusTip(_translate("ResetWindow", "Enter UserId"))
        self.label_9.setText(_translate("ResetWindow", "User Id"))

    def pass_view3(self, ResetWindow):
        
        if self.showpass4.isChecked():
            self.newpass1.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.newpass1.setEchoMode(QtWidgets.QLineEdit.Password)

    def update(self):
        idi1 = int(self.userid.text())
        newpassw = self.newpass1.text()
        cluster = MongoClient("")           #MongoDB Database link
        db = cluster["test"]
        collection = db["test"]
        myquery = { "_id" : idi1 }
        newvalues = { "$set": { "Password": newpassw } }

        collection.update_one(myquery, newvalues)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s  - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('userid: %s has changed password successfully',idi1)
        msg = QMessageBox()
        msg.setWindowTitle("Successfull")
        msg.setText("New password has been saved")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

if __name__ == "__main__":
    try:
        import sys
        app = QtWidgets.QApplication(sys.argv)
        ResetWindow = QtWidgets.QMainWindow()
        ui = Ui_ResetWindow()
        ui.setupUi(ResetWindow)
        ResetWindow.show()
        sys.exit(app.exec_())
    except:
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.critical('Reset password page has beeen crashed')
