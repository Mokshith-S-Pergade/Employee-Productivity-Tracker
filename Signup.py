# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Signup.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymongo
from terms import Ui_Terms_conditions
from pymongo import MongoClient
from PyQt5.QtWidgets import QMessageBox
import subprocess
import psycopg2
import logging

logger = logging.getLogger(__name__)
f_handler = logging.FileHandler('app.log')
f_handler.setLevel(logging.DEBUG)
class Ui_SignupWindow(object):
    def setupUi(self, SignupWindow):
        SignupWindow.setObjectName("SignupWindow")
        SignupWindow.resize(1228, 740)
        SignupWindow.setMaximumSize(QtCore.QSize(1228, 740))

        
        icon=QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Athrved3.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        SignupWindow.setWindowIcon(icon)
        
        self.centralwidget = QtWidgets.QWidget(SignupWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.back3 = QtWidgets.QLabel(self.centralwidget)
        self.back3.setGeometry(QtCore.QRect(-40, 0, 1271, 821))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.back3.setFont(font)
        self.back3.setStyleSheet("background-color: rgb(162, 187, 255);")
        self.back3.setText("")
        self.back3.setScaledContents(True)
        self.back3.setObjectName("back3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 320, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 380, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(460, 250, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 500, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 620, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(23, 162, 255);\n""border-radius:20px")
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(360, 440, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(550, 120, 141, 141))
        self.label_8.setStyleSheet("")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("signup.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.userid = QtWidgets.QLineEdit(self.centralwidget)
        self.userid.setGeometry(QtCore.QRect(500, 320, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.userid.setFont(font)
        self.userid.setStyleSheet("border-radius:10px;")
        self.userid.setObjectName("userid")
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(500, 380, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name.setFont(font)
        self.name.setStyleSheet("border-radius:10px;")
        self.name.setObjectName("name")
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(500, 440, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.email.setFont(font)
        self.email.setStyleSheet("border-radius:10px;")
        self.email.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.email.setObjectName("email")
        self.newpass = QtWidgets.QLineEdit(self.centralwidget)
        self.newpass.setGeometry(QtCore.QRect(500, 500, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.newpass.setFont(font)
        self.newpass.setStyleSheet("border-radius:10px;")
        self.newpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newpass.setObjectName("newpass")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(-50, -20, 1281, 121))
        self.label_9.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -20, 221, 121))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Athrved.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(870, 20, 338, 52))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(26)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.showpass3 = QtWidgets.QCheckBox(self.centralwidget)
        self.showpass3.setGeometry(QtCore.QRect(890, 510, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(True)
        self.showpass3.setFont(font)
        self.showpass3.setObjectName("showpass3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(510, 560, 21, 31))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 560, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(23, 162, 255);\n""border-radius:10px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.terms__conditions)
        
        SignupWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SignupWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1228, 26))
        self.menubar.setObjectName("menubar")
        SignupWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SignupWindow)
        self.statusbar.setObjectName("statusbar")
        SignupWindow.setStatusBar(self.statusbar)
        self.showpass3.stateChanged.connect(self.pass_view1)

        self.pushButton.clicked.connect(self.checkbox)
        
        self.retranslateUi(SignupWindow)
        QtCore.QMetaObject.connectSlotsByName(SignupWindow)
        
    def checkbox(self):
        
        if self.checkBox.isChecked():
            self.register_user()
            
        else:
            
            f_format = logging.Formatter('%(asctime)sv- %(levelname)s - %(message)s')
            f_handler.setFormatter(f_format)
            logger.addHandler(f_handler)
            logger.error('user didnt accept the terms and conditions')
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Accept the terms and conditions before registering")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            
        
    def register_user(self):
        idi = int(self.userid.text())
        Name = self.name.text()
        Email = self.email.text()
        Pass = self.newpass.text()
        import psycopg2
        conn=psycopg2.connect('')       #PSQL Database link
        cur=conn.cursor()
        Mail= "select * from member1 where member_id=  {} ".format(idi)
        cur.execute(Mail)
        records= cur.fetchall()
        for row in records:
            ID= row[0]
            EMAIL=row[2]
            
        cur.close()
        conn.close()
        if Email== EMAIL:
        
           try:
                print(78)
                cluster = MongoClient("")       #MongoDB Database link
                db = cluster["test"]   #  test is the Database name
                collection = db["test"]# test is the collection name
                post = {"_id" : idi,"Username":Name,"Email":Email,"Password":Pass}
                collection.insert_one(post)
                
                collection4 = db["Locations"]   # screenshots is the collection name
                collection2=db["screenshots"]
                collection3=db["Time tracking"]
                collection6=db["Time_tracking"]
                collection7=db["Time_Tracking"]
                
                post1= {"_id":idi,"path_of_Adobe illustrator":"" "","path_of_Android studio":"" "","path_of_Visual studio":"" "","path_of_Figma":"" "","path_of_Vs code":"" "","path_of_Proteus":"" "","path_of_Tableau":"" "","path_of_Arduino illustrator":"" ""
        ,"path_of_Solid works":"" "","path_of_Photoshop":"" "","path_of_Premier pro":"" "","path_of_After effects":"" "","path_of_Phycharm":"" "",
              "path_of_Qt designer":"" "","path_of_Idle":"" "","path_of_Code blocks":"" "","path_of_Wps_office":"" "","path _of_word":"" "","path_of_excel":"" "","path_of_powerpoint":"" "","path_of_edge":"" "","path_of_team_viewer":"" "","path_of_jio_meet":"" "","path_of_discord":"" "","path_of_whatsapp":"" "","path_of_solidwork_visualize":"" "","path_of_Spyder":"" "","path_of_Any_desk":"" "","path_of_Postman":"" "","path_of_Blender":"" "","path_of_Ui_UX":"" "","path_of_Cnc_viewer":"" "","path_of_Mongodb_compass":"" "","path_of_Google_meet":"" "","path_of_cmd":"" "","path_of_Github_desktop":"" ""}
                collection4.insert_one(post1)

                myquery={"_id":idi}
                collection2.insert_one(myquery)
                collection3.insert_one(myquery)
                collection7.insert_one(myquery)
                collection6.insert_one(myquery)
                list111 = []
                collection6.update_one(myquery,{"$set":{"name":list111}})
                

                msg = QMessageBox()
                msg.setWindowTitle("Please Wait")
                msg.setText("Saving Your Credentials""\n""click on OK to Continue")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()

                
                subprocess.Popen(['dialogue2.py'],shell=True)
                
                self.SignupWindow.close()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('%s has accepted T&Cs and sucessfully registered to application',Name)
                #self.SignupWindow.close()
               

           except :
                msg = QMessageBox()
                msg.setWindowTitle("Please Wait")
                msg.setText("You have already registered")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                
                subprocess.Popen(['dialogue2.py'],shell=True)
                self.SignupWindow.close()
                
                f_format = logging.Formatter('%(asctime)sv- %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.error('%s credentials not saved to database from signup page',Name)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Please Wait")
            msg.setText("Email is not matching with LMS Signup Email")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            
    def retranslateUi(self, SignupWindow):
        _translate = QtCore.QCoreApplication.translate
        SignupWindow.setWindowTitle(_translate("SignupWindow", "Athrv-Ed Productivity Tracker"))
        self.label_2.setText(_translate("SignupWindow", "User ID"))
        self.label_3.setText(_translate("SignupWindow", "Name"))
        self.label_5.setText(_translate("SignupWindow", "Create An Account"))
        self.label_4.setText(_translate("SignupWindow", " Password"))
        self.pushButton.setStatusTip(_translate("SignupWindow", "Click to Register"))
        self.pushButton.setText(_translate("SignupWindow", "Sign-Up"))
        self.label_6.setText(_translate("SignupWindow", "Email"))
        self.userid.setStatusTip(_translate("SignupWindow", "Enter the your UserId"))
        self.name.setStatusTip(_translate("SignupWindow", "Enter the Name"))
        self.email.setStatusTip(_translate("SignupWindow", "Enter a your Email"))
        self.newpass.setStatusTip(_translate("SignupWindow", "Enter your New Password"))
        self.label_10.setText(_translate("SignupWindow", "Productivity Tracker"))
        self.showpass3.setStatusTip(_translate("SignupWindow", "Check to Unhide"))
        self.showpass3.setText(_translate("SignupWindow", "Show Password"))
        self.checkBox.setStatusTip(_translate("SignupWindow", "I accept the terms and conditions"))
        self.pushButton_2.setStatusTip(_translate("SignupWindow", "View terms and condition"))
        self.pushButton_2.setText(_translate("SignupWindow", "TERMS AND CONDITIONS"))

    def pass_view1(self, SignupWindow):       
        if self.showpass3.isChecked():
            self.newpass.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.newpass .setEchoMode(QtWidgets.QLineEdit.Password)
            
    def terms__conditions(self):
        self.window3=QtWidgets.QMainWindow()
        self.ui=Ui_Terms_conditions()
        self.ui.setupUi(self.window3)
        #SignupWindow.show()
        self.window3.show()
        f_format = logging.Formatter('%(asctime)sv- %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.error('User has viewed the T&Cs page')
        
if __name__ == "__main__":
    
                try:
                    import sys
                    app = QtWidgets.QApplication(sys.argv)
                    SignupWindow = QtWidgets.QMainWindow()
                    ui = Ui_SignupWindow()
                    ui.setupUi(SignupWindow)
                    SignupWindow.show()
                    sys.exit(app.exec_())
                except Exception as e:
                    f_format = logging.Formatter('%(asctime)s - %(levelname)s -  %(message)s')
                    f_handler.setFormatter(f_format)
                    logger.addHandler(f_handler)
                    logger.critical('SignUp page has beeen crashed'+str(e))
  
