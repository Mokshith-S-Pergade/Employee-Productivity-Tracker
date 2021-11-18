# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymongo
from PyQt5.QtWidgets import QMessageBox
from reset import Ui_ResetWindow
from pymongo import MongoClient
import logging
import psycopg2
from getmac import get_mac_address as gma

logger = logging.getLogger(__name__)
f_handler = logging.FileHandler('app.log')
f_handler.setLevel(logging.DEBUG)

class Ui_SigninWindow(object):
    def setupUi(self, SigninWindow):
        SigninWindow.setObjectName("SigninWindow")
        SigninWindow.resize(1061, 766)
        SigninWindow.setMaximumSize(QtCore.QSize(1061, 766))

        
        icon=QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Athrved3.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        SigninWindow.setWindowIcon(icon)
        
        self.centralwidget = QtWidgets.QWidget(SigninWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Back2 = QtWidgets.QLabel(self.centralwidget)
        self.Back2.setGeometry(QtCore.QRect(0, -20, 1061, 761))
        self.Back2.setStyleSheet("background-color: rgb(156, 209, 255);")
        self.Back2.setText("")
        self.Back2.setScaledContents(True)
        self.Back2.setObjectName("Back2")
        self.resetbutton = QtWidgets.QPushButton(self.centralwidget)
        self.resetbutton.setGeometry(QtCore.QRect(460, 630, 121, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.resetbutton.setFont(font)
        self.resetbutton.setStyleSheet("background-color: rgb(156, 209, 255);\n""border-radius:2px;")
        self.resetbutton.setObjectName("resetbutton")
        self.resetbutton.clicked.connect(self.reset)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 560, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(23, 162, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.check)
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(490, 400, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.email.setFont(font)
        self.email.setAutoFillBackground(False)
        self.email.setStyleSheet("border-radius:10px;\n""")
        self.email.setInputMask("")
        self.email.setText("")
        self.email.setCursorPosition(0)
        self.email.setObjectName("email")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 400, 190, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 470, 161, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(490, 470, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.password.setFont(font)
        self.password.setStyleSheet("border-radius:10px;")
        self.password.setInputMask("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440, 140, 161, 161))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Login.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(460, 300, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.showpass1 = QtWidgets.QCheckBox(self.centralwidget)
        self.showpass1.setGeometry(QtCore.QRect(750, 520, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(True)
        self.showpass1.setFont(font)
        self.showpass1.setObjectName("showpass1")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(-6, -25, 1071, 121))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -20, 221, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Athrved.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(690, 10, 351, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(26)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        SigninWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SigninWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1061, 26))
        self.menubar.setObjectName("menubar")
        SigninWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SigninWindow)
        self.statusbar.setObjectName("statusbar")
        SigninWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SigninWindow)
        QtCore.QMetaObject.connectSlotsByName(SigninWindow)
        self.showpass1.stateChanged.connect(self.pass_view)

    def retranslateUi(self, SigninWindow):
        _translate = QtCore.QCoreApplication.translate
        SigninWindow.setWindowTitle(_translate("SigninWindow", "Athrv-Ed Productivity Tracker"))
        self.resetbutton.setStatusTip(_translate("SigninWindow", "Click to Reset Password"))
        self.resetbutton.setText(_translate("SigninWindow", "Forgot Password?"))
        self.pushButton.setStatusTip(_translate("SigninWindow", "Click to Login"))
        self.pushButton.setText(_translate("SigninWindow", "Log-In"))
        self.email.setStatusTip(_translate("SigninWindow", "Enter User Id"))
        self.label_2.setText(_translate("SigninWindow", "User Id"))
        self.label_3.setText(_translate("SigninWindow", "Password"))
        self.password.setStatusTip(_translate("SigninWindow", "Enter Password"))
        self.label_5.setText(_translate("SigninWindow", "Sign-In"))
        self.showpass1.setStatusTip(_translate("SigninWindow", "Check to Unhide"))
        self.showpass1.setText(_translate("SigninWindow", "Show Password"))
        self.label_6.setText(_translate("SigninWindow", "Productivity Tracker"))

    def pass_view(self, SigninWindow):
        
        if self.showpass1.isChecked():
            self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.password.setEchoMode(QtWidgets.QLineEdit.Password)
    
    def login_successfu(self):
        import subprocess
        subprocess.Popen(['TTESTING.py'],shell=True)
        
        
    def check(self):
        
            global mainIDD
            mainIDD = int(self.email.text())
            passw = self.password.text()
            
            try:
                cluster = MongoClient("")           #MongoDB Database link
                db = cluster["test"]
                collection = db["test"]
                data = {'_id': mainIDD, 'Password': passw}
                import psycopg2 
                conn=psycopg2.connect('')           #PSQL Database link
                cur=conn.cursor()
            except Exception as e :
                msg = QMessageBox()
                msg.setWindowTitle("Warning")
                msg.setText("Please check your internet connection \n and try again")
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()
                
                f_format = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.critical('login details not received by database')
            #print(78)
            
            
            yes =[0]
            import wmi
            f=wmi.WMI()
            def check(str_):
                if f.Win32_Process(name=str_):
                    yes.clear()
                    yes.append(1)
                   
                else:
                    print("nooo")
            
            if yes[0] ==0:
             if collection.find_one({'_id':{'$eq': mainIDD},'Password':{'$eq':passw}},{'Email':0,'Username':0,"Mac adress":0})==data:
                    
                    f_format = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
                    f_handler.setFormatter(f_format)
                    logger.addHandler(f_handler)
                    logger.warning('Login to operation page successful with mail id: %s',mainIDD)
                    
                    import os
                    import psycopg2
                    from getmac import get_mac_address as gma
                    b=str(gma())
                   
                    conn=psycopg2.connect('')       #PSQL Database link
                    cur=conn.cursor()
                    
                    cur.execute("delete from login_mac where mac = '%s'"%(b))
                   
                    conn.commit()
                    cur.execute("insert into login_mac (user_id,mac) VALUES (%d,'%s')"%(mainIDD,b))
                    conn.commit()

                    import os
                    os.system("taskkill /f /im final_operation_page.exe") 

                    



                    msg = QMessageBox()
                    msg.setWindowTitle("Info")
                    msg.setText("Login successful \n Please wait...")
                    msg.setIcon(QMessageBox.Information)
                    msg.exec_()
                    #print(23)
                    
                    
                    

                    

                    #print("ddonne")
                    

                    import subprocess
                    subprocess.Popen(['final_operation_page.py'],shell=True)
                    
                    import threading
                    t=threading.Thread(target=self.login_successfu)
                    t.start()

                    import time
                    time.sleep(1)
                    self.SigninWindow.close()
                   

             else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Warning")
                    msg.setText("Invalid Credentials""\n""Try again")
                    msg.setIcon(QMessageBox.Warning)
                    msg.exec_()
                    
                    f_format = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
                    f_handler.setFormatter(f_format)
                    logger.addHandler(f_handler)
                    logger.error('Invalid credentials in login page')

            else:
                msg = QMessageBox()
                msg.setWindowTitle("Warning")
                msg.setText("Multiple login not permitted.\n If not contact admins.")
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()


            
    
        
            
            
    def reset(self):

        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Please contact Admin")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

       
        

            
                
            

if __name__ == "__main__":

                try:
                    import sys
                    app = QtWidgets.QApplication(sys.argv)
                    SigninWindow = QtWidgets.QMainWindow()
                    ui = Ui_SigninWindow()
                    ui.setupUi(SigninWindow)
                    SigninWindow.show()
                    f_format = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
                    f_handler.setFormatter(f_format)
                    logger.addHandler(f_handler)
                    logger.critical('Login page has been opened by User')
                    sys.exit(app.exec_())
                    
                except Exception as e:
                    f_format = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
                    f_handler.setFormatter(f_format)
                    logger.addHandler(f_handler)
                    logger.critical('Login page has been crashed'+str(e))

    
