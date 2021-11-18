# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Appin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from aboutapp import Ui_MainWindow2
from reportissue import Ui_MainWindow1
import logging
from pymongo import MongoClient
from getmac import get_mac_address as gma
import psycopg2
from PyQt5.QtWidgets import QMessageBox
logger = logging.getLogger(__name__)
f_handler = logging.FileHandler('app.log')
f_handler.setLevel(logging.DEBUG)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setMaximumSize(QtCore.QSize(1366, 768))
        MainWindow.setStyleSheet("")

        icon=QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Athrved3.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1366, 768))
        self.label.setMaximumSize(QtCore.QSize(1366, 768))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Appinfo.png"))
        self.label.setScaledContents(True)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(680, 490, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(960, 40, 351, 211))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Athrved.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.buttonup = QtWidgets.QPushButton(self.centralwidget)
        self.buttonup.setGeometry(QtCore.QRect(810, 470, 170, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.buttonup.setFont(font)
        self.buttonup.setMouseTracking(False)
        self.buttonup.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color:white;")
        self.buttonup.setObjectName("buttonup")
        self.buttonup.clicked.connect(self.signup)

        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 330, 1171, 131))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(40)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.buttonin = QtWidgets.QPushButton(self.centralwidget)
        self.buttonin.setGeometry(QtCore.QRect(420, 470, 170, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.buttonin.setFont(font)
        self.buttonin.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color:white;")
        self.buttonin.setObjectName("buttonin")
        self.buttonin.clicked.connect(self.signin)
        self.buttonabout = QtWidgets.QPushButton(self.centralwidget)
        self.buttonabout.setGeometry(QtCore.QRect(560, 660, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.buttonabout.setFont(font)
        self.buttonabout.setStyleSheet("background-color: rgb(185, 167, 167);\n"
"border-radius:5px;\n"
"")
        self.buttonabout.setObjectName("buttonabout")
        self.buttonabout.clicked.connect(self.app_info)
        global name1
        
        name2="Login as "+name1
        
        if name1 !=" ":
            self.buttonabout_5 = QtWidgets.QPushButton(self.centralwidget)
            self.buttonabout_5.setText(name2)
            
            if len(name2)<=10:
                
                self.buttonabout_5.setGeometry(QtCore.QRect(651, 583, 171, 71))

            elif (10<len(name2)<=14):
                
                self.buttonabout_5.setGeometry(QtCore.QRect(635, 583, 171, 71))

            elif (14<len(name2)<=17):
                
                self.buttonabout_5.setGeometry(QtCore.QRect(609, 583, 171, 71))
            elif (17<len(name2)<=22):
                
                self.buttonabout_5.setGeometry(QtCore.QRect(585, 583, 171, 71))



            else:
                
                self.buttonabout_5.setGeometry(QtCore.QRect(552, 583, 171, 71)) 


            
            self.buttonabout_5.setStyleSheet("background-color: rgb(185, 167, 167);\n"
    
    "")
            font = QtGui.QFont()
            font.setFamily("Segoe UI Semibold")
            font.setPointSize(14)
            font.setBold(True)
            
            font.setWeight(75)
            self.buttonabout_5.setFont(font)
            self.buttonabout_5.adjustSize()
            self.buttonabout_5.setStyleSheet("background-color: rgb(85, 170, 255);\n"
    
    "")
            

    
            self.buttonabout_5.setObjectName("buttonabout_5")
            self.buttonabout_5.clicked.connect(self.login_as)
        
        self.buttonabout_2 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonabout_2.setGeometry(QtCore.QRect(730, 660, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.buttonabout_2.setFont(font)
        self.buttonabout_2.setStyleSheet("background-color: rgb(185, 167, 167);\n"
"border-radius:5px;\n"
"")
        self.buttonabout_2.setObjectName("buttonabout_2")
        self.buttonabout_2.clicked.connect(self.reportIssue)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        
        MainWindow.setWindowTitle(_translate("MainWindow", "Athrv-Ed Productivity Tracker"))
        self.label_3.setText(_translate("MainWindow", "OR"))
        self.label_4.setStatusTip(_translate("MainWindow", "Athrv-EdTech"))
        self.buttonup.setStatusTip(_translate("MainWindow", "Click to Register"))
        self.buttonup.setText(_translate("MainWindow", "Sign-Up"))
        self.label_2.setText(_translate("MainWindow", "Athrv-Ed LMS Productivity Tracker"))
        self.buttonin.setStatusTip(_translate("MainWindow", "Click to Sign-in"))
        self.buttonin.setText(_translate("MainWindow", "Sign-In"))
        self.buttonabout.setStatusTip(_translate("MainWindow", "Appinfo"))
        self.buttonabout.setText(_translate("MainWindow", "About App"))
        
        self.buttonabout_2.setStatusTip(_translate("MainWindow", "If any issues occur regarding application,Report it here"))
        self.buttonabout_2.setText(_translate("MainWindow", "Report Issue"))
       


    def signup(self):
        
        f_format = logging.Formatter('%(asctime)s - %(levelname)s  - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('signup page has been opened')
        import subprocess
        subprocess.Popen(['Signup.py'],shell=True)
    
        MainWindow.close()
        
        
    def reportIssue(self):
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('user reported an issue')
        self.window6=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow1()
        self.ui.setupUi(self.window6)
        MainWindow.show()
        self.window6.show()

    def signin(self):
        
        
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('Signin page has been opened')
        import subprocess
        subprocess.Popen(['login.py'],shell=True)
        MainWindow.close() 
        
    def app_info(self):
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('user checked app info')
        self.window5=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow2()
        self.ui.setupUi(self.window5)
        MainWindow.show()
        self.window5.show()
    def login_successfu(self):
        
        import subprocess
        subprocess.Popen(['TTESTING.py'],shell=True)
        
    def login_as(self):
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.critical('Welcome page has beeen crashed  11')
                
                

                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.critical('Welcome page has beeen crashed  22')

                if yes[0] == 0:               

                    import subprocess
                    f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                    f_handler.setFormatter(f_format)
                    logger.addHandler(f_handler)
                    logger.critical('Welcome page has beeen crashed 33')

                    subprocess.Popen(['final_operation_page.py'],shell=True)
                    
                    f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                    f_handler.setFormatter(f_format)
                    logger.addHandler(f_handler)
                    logger.critical('Welcome page has beeen crashed 44')

                    import threading
                    t=threading.Thread(target=self.login_successfu)
                    t.start()

                    import time
                    time.sleep(1)

                    self.MainWindow.close()

                    f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                    f_handler.setFormatter(f_format)
                    logger.addHandler(f_handler)
                    logger.critical('Welcome page has beeen crashed 55')


                else :
                    print(65)
                    msg = QMessageBox()
                    msg.setWindowTitle("Warning")
                    msg.setText("you have Already opened the operation page")
                    msg.setIcon(QMessageBox.Information)
                    msg.exec_()
            


if __name__ == "__main__":
    yes =[0]
    import wmi
    f=wmi.WMI()
    def check(str_):
                if f.Win32_Process(name=str_):
                    yes.clear()
                    yes.append(1)

                    import tkinter,tkinter.messagebox
                    root=tkinter.Tk()
                    root.withdraw()
                    tkinter.messagebox.showinfo("UNSUCCESSFULL","The app is already running in the background \n If no, execute REFRESH.exe .\n Then try again")
                    root.mainloop()
                    
                    
                else:
                    print("nooo")
                    
    
    if (yes[0]) == 0 :
        
        global a
        a=gma()
        conn=psycopg2.connect('')           #PSQL Database link
        cur=conn.cursor()
        cur.execute( 'select * from mac_address')
        data=cur.fetchall()
        zzz=[0]

        for x in data:
            
                if a==x[1]:
                    cur.execute( 'select * from login_mac')
                    data2 =cur.fetchall()
                    list1=[1]
                    for m in data2:
                        if a==m[1]:
                            list1.clear()
                            list1.append(3)
                            
                            Id=m[0]
                            cur.execute( 'select name1 from member1 where member_id =(%d)'%(Id))
                            data1 =cur.fetchall()
                            #print(data1)
                        
                            name =data1[0]
                            name1=name[0]
                        #print(name1)
                    if list1[0]==1:
                        name1=" "
                    
                    zzz.clear()
                    zzz.append(1)
                    try:
                        import sys
                        app = QtWidgets.QApplication(sys.argv)
                        MainWindow = QtWidgets.QMainWindow()
                        ui = Ui_MainWindow()
                        ui.setupUi(MainWindow)
                        MainWindow.show()
                        f_format = logging.Formatter('%(asctime)s- %(levelname)s - %(message)s')
                        f_handler.setFormatter(f_format)
                        logger.addHandler(f_handler)
                        logger.warning('Welcome page has opened')
                        sys.exit(app.exec_())
                    except Exception as e:
                        
                        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                        f_handler.setFormatter(f_format)
                        logger.addHandler(f_handler)
                        logger.critical('Welcome page has been crashed'+str(e))


        if zzz[0]==0:
                f_format = logging.Formatter('%(asctime)s- %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('the mac adress is not exist')

                import tkinter,tkinter.messagebox
                root=tkinter.Tk()
                root.withdraw()
                tkinter.messagebox.showinfo("NOT REGISTERED","YOU ARE NOT A VALID USER")
                root.mainloop()
     
            
            
