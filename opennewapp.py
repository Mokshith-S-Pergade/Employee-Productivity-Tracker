# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newapp.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from pymongo import MongoClient
from PyQt5.QtWidgets import QMessageBox
import subprocess
import threading
import logging
logger = logging.getLogger(__name__)
f_handler = logging.FileHandler('app.log')
f_handler.setLevel(logging.DEBUG)
f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)
logger.warning('Open app page is opened')



class Ui_appwindow(object):
    def __init__(self, i_d):
        self.i_d=i_d
        

    def setupUi(self, appwindow):
        #self.i_d = 25
        appwindow.setObjectName("appwindow")
        appwindow.resize(713, 426)
        appwindow.setStyleSheet("\n"
"background-color: rgb(233, 255, 239);")
        icon=QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Athrved3.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        appwindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(appwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 130, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 246, 248);")
        self.label.setObjectName("label")
        cluster = MongoClient("")           #MongoDB Database link
            #print("Location_of_app")
        db = cluster["test"]#  test is the Database name
            #print("done")
        
        collection2 = db["Time_tracking"]
            
          

        
        myquery={"_id":self.i_d}
            #my = {"_id":25}
        y2=collection2.find_one(myquery)
        global list1
        list1 = y2["name"]
        print(list1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(350, 130, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(255, 246, 248);\n"
"border-color: rgb(255, 234, 253);")
        self.comboBox.setObjectName("comboBox")
        
        #self.comboBox.setEditable(True)
        self.comboBox.addItems(list1)
        self.comboBox.setStyleSheet("background-color: white");
       
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 260, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 216, 230);")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 20, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        appwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(appwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 713, 26))
        self.menubar.setObjectName("menubar")
        appwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(appwindow)
        self.statusbar.setObjectName("statusbar")
        appwindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.click)

        self.retranslateUi(appwindow)
        QtCore.QMetaObject.connectSlotsByName(appwindow)
    def click (self):
        
        print(88)
        if list1 !=[]:
            t = threading.Thread(target=self.log12)
            t.start()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("Can't open")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
        

    def log12(self):
      try:
            app_name=self.comboBox.currentText()
            print(app_name)
        
            print(88)
           
            cluster = MongoClient("")       #MongoDB Database link
            print("a")
            db = cluster["test"]
            print("b")
            collection=db["Time_Tracking"]
            print("d")
            #collection2=db["Time tracking"]
            
            #Id= i_d
            myquery={"_id":self.i_d}
            print(1)
            x=collection.find_one(myquery)
            print(2)
            f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            f_handler.setFormatter(f_format)
            logger.addHandler(f_handler)
            logger.warning('user opened '+app_name)
            #self.Github_desktop.setStyleSheet("background-color: transparent;")

            # do your work here
            path = "path_of_"+app_name
            print(path)
            print(3)
            subprocess.call([x[path]],shell=True)
            
            
            

        
      except Exception as e:
        print(e)
        msg = QMessageBox()
               
        msg.setWindowTitle("Warning")
        msg.setText("Something went wrong")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

        

    def retranslateUi(self, appwindow):
        _translate = QtCore.QCoreApplication.translate
        appwindow.setWindowTitle(_translate("appwindow", "Opennewapps"))
        self.label.setText(_translate("appwindow", "Select the name of app  :"))
        self.pushButton.setText(_translate("appwindow", "Open"))
        self.label_2.setText(_translate("appwindow", "Welcome to this page"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    appwindow = QtWidgets.QMainWindow()
    ui = Ui_appwindow()
    ui.setupUi(appwindow)
    appwindow.show()
    sys.exit(app.exec_())
