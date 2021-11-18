# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newqt2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import tkinter
from tkinter import filedialog
import os
from pymongo import MongoClient
from PyQt5.QtWidgets import QMessageBox
from getmac import get_mac_address as gma
import psycopg2
import logging
logger = logging.getLogger(__name__)
f_handler = logging.FileHandler('app.log')
f_handler.setLevel(logging.DEBUG)
f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)
logger.warning('Add location page opened')

conn=psycopg2.connect('')       #PSQL Database link
cur=conn.cursor()

mac_a=str(gma())

cur.execute("select user_id from login_mac where mac ='%s'"%(mac_a))
mac_aaa = cur.fetchall()
mac_aaa1=mac_aaa[0]
mac_aaa2=mac_aaa1[0]


global mainID
mainID= mac_aaa2

class Ui_addopenwindow(object):
    
    '''def __init__(self, i_d):
        self.i_d=i_d
        #print(self.app_name)
        #self.mail=mail'''
       


    def idle(self):
        
        try:
          Location_of_app=self.lineEdit.text()
            #mail = self.lineEdit_2.text()
          app_name=self.lineEdit_2.text()
          if app_name == "":
                #print("yes")
                msg = QMessageBox()
                msg.setWindowTitle("Pause")
                msg.setText("please enter a valid app name")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
          else:

            
            cluster = MongoClient("")           #MongoDB Database link
            #print("Location_of_app")
            db = cluster["test"]#  test is the Database name
            #print("done")
            collection = db["Time_Tracking"]
            collection2 = db["Time_tracking"]
            
           
        
            myquery={"_id":mainID}#self.i_d}
            #my = {"_id":25}
            y2=collection2.find_one(myquery)
            list1 = y2["name"]
            #print(list1)
            if app_name not in list1:
                #print("yes")
                list1.append(app_name)
                #print(list1)
                collection2.update_one(myquery,{"$set":{"name":list1}})
            #print("no")
            path = "path_of_"+app_name  
            new={"$set":{path:Location_of_app }}
            collection.update_one(myquery,new)
            msg = QMessageBox()
                
            msg.setWindowTitle("confirmation")
            msg.setText("sucessfully added")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
                #openwindow.close()
            f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            f_handler.setFormatter(f_format)
            logger.addHandler(f_handler)
            logger.warning(' location added for '+app_name)
        
            

        except :
            msg = QMessageBox()
            msg.setWindowTitle("Pause")
            msg.setText("Something went wrong")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

      

    def setupUi(self, addopenwindow):
        #print(1)
        addopenwindow.setObjectName("addopenwindow")
        addopenwindow.resize(1047, 600)
        addopenwindow.setStyleSheet("background-color:lightyellow;")
        icon=QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Athrved3.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        addopenwindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(addopenwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 240, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("background-color:white;\nborder-color:green;")
        #self.label.setStyleSheet("border-color:green;")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(350, 240, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("background-color:white;")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 400, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        #print(2)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(920, 240, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        #print(3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("background-color:white;")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 130, 541, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:white;")

        
        #print(4)
        addopenwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(addopenwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1047, 26))
        self.menubar.setObjectName("menubar")
        addopenwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(addopenwindow)
        self.statusbar.setObjectName("statusbar")
        addopenwindow.setStatusBar(self.statusbar)
        addopenwindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.idle)
        self.pushButton_2.clicked.connect(self.click)
        self.pushButton.setStyleSheet("background-color: skyblue");
        self.pushButton_2.setStyleSheet("background-color: skyblue");
        # self.comboBox.setStyleSheet("background-color: white");

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, -20, 221, 131))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(r"C:\Users\hp\Desktop\operationpage1/Athrved.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        #print(5)

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(690, 10, 351, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(26)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet("background-color:white;")
        #self.pushButton.clicked.connect(self.)
        self.retranslateUi(addopenwindow)
        QtCore.QMetaObject.connectSlotsByName(addopenwindow)
        
       

  


    def click(self):
        #print("clicked")
        self.open_dialog_box()
        
    def open_dialog_box(self):
        filename=QFileDialog.getOpenFileName()
        path=filename[0]
        self.lineEdit.setText(path)

    def retranslateUi(self, addopenwindow):
        #print(6)
        _translate = QtCore.QCoreApplication.translate
        addopenwindow.setWindowTitle(_translate("addopenwindow", "Add Apps"))
        self.label.setText(_translate("addopenwindow", "Please enter the location of this app"))
        self.pushButton.setText(_translate("addopenwindow", "submit"))
        self.pushButton_2.setText(_translate("addopenwindow", "Browse"))
        self.label_2.setText(_translate("addopenwindow", "Enter the name of the app"))
        self.label_6.setText(_translate("SigninWindow", "Productivity Tracker"))

if __name__ == "__main__":
    try:
        import sys
        
        app = QtWidgets.QApplication(sys.argv)
        addopenwindow = QtWidgets.QMainWindow()
        ui= Ui_addopenwindow()
        ui.setupUi(addopenwindow)
        addopenwindow.show()
        sys.exit(app.exec_())
    except Exception as e:
        msg = QMessageBox()
        msg.setWindowTitle("Pause")
        msg.setText("Something went wrong")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

        #print(e)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.critical('Add newapp Page crashed')

