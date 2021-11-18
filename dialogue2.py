# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogue1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import logging
import psycopg2
logger = logging.getLogger(__name__)
f_handler = logging.FileHandler('app.log')
f_handler.setLevel(logging.DEBUG)

class Ui_RegisterBox(object):
    def setupUi(self, RegisterBox):
        RegisterBox.setObjectName("RegisterBox")
        RegisterBox.resize(739, 320)
        RegisterBox.setMaximumSize(QtCore.QSize(739, 320))

        icon=QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Athrved3.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        RegisterBox.setWindowIcon(icon)
        
        self.centralwidget = QtWidgets.QWidget(RegisterBox)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 130, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.logbutton = QtWidgets.QPushButton(self.centralwidget)
        self.logbutton.setGeometry(QtCore.QRect(210, 200, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.logbutton.setFont(font)
        self.logbutton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.logbutton.setObjectName("logbutton")
        self.logbutton.clicked.connect(self.signin)
        self.closebutton = QtWidgets.QPushButton(self.centralwidget)
        self.closebutton.setGeometry(QtCore.QRect(420, 200, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.closebutton.setFont(font)
        self.closebutton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.closebutton.setObjectName("closebutton")
        self.closebutton.clicked.connect(self.close)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 20, 101, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("bell.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        RegisterBox.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RegisterBox)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 739, 26))
        self.menubar.setObjectName("menubar")
        RegisterBox.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RegisterBox)
        self.statusbar.setObjectName("statusbar")
        RegisterBox.setStatusBar(self.statusbar)

        self.retranslateUi(RegisterBox)
        QtCore.QMetaObject.connectSlotsByName(RegisterBox)

    def retranslateUi(self, RegisterBox):
        _translate = QtCore.QCoreApplication.translate
        RegisterBox.setWindowTitle(_translate("RegisterBox", "Athrv-Ed LMS Productivity Tracker"))
        self.label.setText(_translate("RegisterBox", "Successfully Registered !!!!"))
        self.logbutton.setText(_translate("RegisterBox", "Log-In"))
        self.closebutton.setText(_translate("RegisterBox", "Close"))
        
    def signin(self):
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('Signin page has been accessed through dialog box')
        import subprocess
        subprocess.Popen(['login.py'],shell = True)
        
        RegisterBox.close()
        

    def close(self):
    
         RegisterBox.close()
        


if __name__ == "__main__":
    from getmac import get_mac_address as gma
    a=gma()
    conn=psycopg2.connect('')       #PSQL Database link
    cur=conn.cursor()
    cur.execute( 'select * from mac_address')
    data=cur.fetchall()
    zzz=[0]

    for x in data:
        
            if a==x[1]:
                zzz.clear()
                zzz.append(1)
                try:
                    import sys
                    app = QtWidgets.QApplication(sys.argv)
                    RegisterBox = QtWidgets.QMainWindow()
                    ui = Ui_RegisterBox()
                    ui.setupUi(RegisterBox)
                    RegisterBox.show()
                    f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                    f_handler.setFormatter(f_format)
                    logger.addHandler(f_handler)
                    logger.warning('Dialog box has been displayed')
                    sys.exit(app.exec_())
                except Exception as e:
                    f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                    f_handler.setFormatter(f_format)
                    logger.addHandler(f_handler)
                    logger.critical('Dialog box has been crashed')

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
            
