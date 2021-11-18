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
import psycopg2
import logging
logger = logging.getLogger(__name__)
f_handler = logging.FileHandler('app.log')
f_handler.setLevel(logging.DEBUG)
f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)
logger.warning('Remove app page is opened')
from getmac import get_mac_address as gma
conn=psycopg2.connect('')       #PSQL Database link
cur=conn.cursor()
mac_a=str(gma())

cur.execute("select user_id from login_mac where mac ='%s'"%(mac_a))
mac_aaa = cur.fetchall()
mac_aaa1=mac_aaa[0]
mac_aaa2=mac_aaa1[0]


global mainID
mainID= mac_aaa2

class Ui_appwindow2(object):
    '''def __init__(self, i_d):
        self.i_d=i_d
        #print(self.app_name)
        #self.mail=mail'''
       



    def setupUi(self, appwindow2):
        self.i_d = mainID
        appwindow2.setObjectName("appwindow2")
        appwindow2.resize(713, 426)
        appwindow2.setStyleSheet("\n"
"background-color: rgb(233, 255, 239);")
        icon=QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Athrved3.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        appwindow2.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(appwindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 130, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 246, 248);")
        self.label.setObjectName("label")
        cluster = MongoClient("")               #MongoDB Database link
            #print("Location_of_app")
        db = cluster["test"]#  test is the Database name
            #print("done")
        
        collection2 = db["Time_tracking"]
            
           

        
        myquery={"_id":self.i_d}
            #my = {"_id":25}
        y2=collection2.find_one(myquery)
        global list1
        list1 = y2["name"]
        #print(list1)
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
        self.label_2.setGeometry(QtCore.QRect(210, 20, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        appwindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(appwindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 713, 26))
        self.menubar.setObjectName("menubar")
        appwindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(appwindow2)
        self.statusbar.setObjectName("statusbar")
        appwindow2.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.click)

        self.retranslateUi(appwindow2)
        QtCore.QMetaObject.connectSlotsByName(appwindow2)
    def click (self):
        
        try:
            app_name=self.comboBox.currentText()
            #print(app_name)
            path = "path_of_"+app_name
            
            cluster = MongoClient("")       #MongoDB Database link
            #print("a")
            db = cluster["test"]
            #print("b")
            collection=db["Time_Tracking"]
            #print("d")
            myquery={"_id":self.i_d}
            collection2=db["Time_tracking"]
            collection.update_one(myquery,{"$set":{path:""}})
            collection.update_one(myquery,{"$unset":{path:""}})
            #Id= i_d
            myquery={"_id":self.i_d}
            #print(1)
            x=collection2.find_one(myquery)
            #print(2)
            list1 = x["name"]
            #print(list1)
            list1.remove(app_name)
            #print(list1)
            collection2.update_one(myquery,{"$set":{"name":list1}})
            msg = QMessageBox()
            msg.setWindowTitle("Information")
            msg.setText("Successfully removed")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
            f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            f_handler.setFormatter(f_format)
            logger.addHandler(f_handler)
            logger.warning('user removed '+app_name)
            #self.Github_desktop.setStyleSheet("background-color: transparent;")

                    
            
            

            
        except Exception as e:
            #print(e)
            msg = QMessageBox()
                    
            msg.setWindowTitle("Warning")
            msg.setText("Something went wrong")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

        

    def retranslateUi(self, appwindow2):
        _translate = QtCore.QCoreApplication.translate
        appwindow2.setWindowTitle(_translate("appwindow2", "Removeapps"))
        self.label.setText(_translate("appwindow2", "Select the name of app  :"))
        self.pushButton.setText(_translate("appwindow2", "Remove"))
        self.label_2.setText(_translate("appwindow2", "Remove app"))


if __name__ == "__main__":
   try:
    import sys
    app = QtWidgets.QApplication(sys.argv)
    appwindow2 = QtWidgets.QMainWindow()
    ui = Ui_appwindow2()
    ui.setupUi(appwindow2)
    appwindow2.show()
    sys.exit(app.exec_())
   except Exception as e:
    f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    f_handler.setFormatter(f_format)
    logger.addHandler(f_handler)
    logger.critical('Remove app Page crashed'+str(e))
    
    msg = QMessageBox()
    msg.setWindowTitle("Warning")
    msg.setText("Something went wrong")
    msg.setIcon(QMessageBox.Information)
    msg.exec_()
    
       
