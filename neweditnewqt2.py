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
import logging
logger = logging.getLogger(__name__)
f_handler = logging.FileHandler('app.log')
f_handler.setLevel(logging.DEBUG)
f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)
logger.warning('Add location page opened')


class Ui_openwindow(object):
    
    def __init__(self, i_d):
        self.i_d=i_d
       


    def idle(self):
       
        try:
            Location_of_app=self.lineEdit.text()
            #mail = self.lineEdit_2.text()
            app_name=self.comboBox.currentText()
            
            cluster = MongoClient("")       #MongoDB Database link
            #print("Location_of_app")
            db = cluster["test"]#  test is the Database name
            #print("done")
            collection = db["Locations"]
            

        
            
        
            if app_name=="Android studio":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_Android studio":Location_of_app }}
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
                logger.warning('Android studio location added')

            elif app_name=="Visual studio":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_Visual studio":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Visual Studio location added')

            elif app_name=="Figma":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_Figma":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
               
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Figma location added')

            elif app_name=="Proteus":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_Proteus":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
               
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Proteus location added')

            elif app_name=="Tableau":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_Tableau":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Tableau location added')

            elif app_name=="Arduino illustrator":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_Arduino illustrator":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Arduino illustrator location added')

            elif app_name=="Solid works":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_Solid works":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Solidworks location added')

            elif app_name=="Photoshop":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_Photoshop":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Adobe Photoshop location added')

            elif app_name=="Premier pro":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_Premier pro":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Adobe Primier Pro location added')

            elif app_name=="After effects":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_After effects":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Adobe Aftereffects location added')

            elif app_name=="Solid work visualize":
                myquery={"_id":self.i_d}
                
                new={"$set":{"Solid work visualize":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Solid work visualize location added')

            elif app_name=="Pycharm":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_Phycharm":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Pycharm location added')
                

            elif app_name=="Idle":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_Idle":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Python Idle location added')

            elif app_name=="Qt designer":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_Qt designer":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('QT Designer location added')

            elif app_name=="Code blocks":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_Code blocks":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('CodeBlocks location added')

            elif app_name=="Wps_office":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_Wps_office":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('WPS location added')


            elif app_name=="word":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path _of_word":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Word location added')


                




            elif app_name=="MS_Excel":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_excel":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Excel location added')


            elif app_name=="MS_Powerpoint":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_powerpoint":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Powerpoint location added')


            elif app_name=="Microsoft_Edge":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_edge":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Microsoft_Edge location added')


            elif app_name=="Team_viewer":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_team_viewer":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Team_viewer location added')

            elif app_name=="Jio_meet":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_jio_meet":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Jio_meet location added')


            elif app_name=="Discord":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_discord":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Discord location added')


            elif app_name=="Whatsapp":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_whatsapp":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Whatsapp location added')



            elif app_name=="Solidwork_visualize":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_solidwork_visualize":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('solidwork_visualize location added')



            elif app_name=="Spyder":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_Spyder":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Spyder location added')



            elif app_name=="Any_desk":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_Any_desk":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Any_desk location added')



            elif app_name=="Postman":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_Postman":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Postman location added')



            elif app_name=="Blender":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_Blender":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Blender location added')




            elif app_name=="Ui_UX":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_Ui_UX":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Ui_UX location added')




            elif app_name=="Cnc_viewer":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_Cnc_viewer":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Cnc_viewer location added')




            elif app_name=="Mongodb_compass":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_Mongodb_compass":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Mongodb_compass location added')




            elif app_name=="Google_meet":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_Google_meet":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Google_meet location added')




            elif app_name=="CMD":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_cmd":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('CMD location added')



            elif app_name=="Github_desktop":
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_Github_desktop":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Github_desktop location added')

                


            else :
                myquery={"_id":self.i_d}
                
                new={"$set":{"path_of_Adobe illustrator":Location_of_app }}
                collection.update_one(myquery,new)
                msg = QMessageBox()
                #for bla in post:
                #print(post["path_of_idle"] )
                msg.setWindowTitle("confirmation")
                msg.setText("sucessfully added")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('Adobe illustrator location added')

        except:
            msg = QMessageBox()
            msg.setWindowTitle("Pause")
            msg.setText("This Email is not exists")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

      

    def setupUi(self, openwindow):
        openwindow.setObjectName("openwindow")
        openwindow.resize(1047, 600)
        openwindow.setStyleSheet("background-color:lightyellow;")
        self.centralwidget = QtWidgets.QWidget(openwindow)
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
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(920, 240, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("background-color:white;")
       # self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        #self.lineEdit_2.setGeometry(QtCore.QRect(350, 130, 531, 31))
        #s#elf.lineEdit_2.setObjectName("lineEdit_2")
        #self.lineEdit_2.setFont(font)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(350, 130, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        #self.lineEdit_2.setValidator(QIntValidator)
        list1=["Android studio","Visual studio","Figma","Proteus","Tableau","Arduino illustrator","Solid works","Photoshop","Premier pro","After effects","Adobe illustrator","Pycharm","Idle","Qt designer","Code blocks","Wps_office","word","MS_Excel","MS_Powerpoint","Microsoft_Edge","Team_viewer","Jio_meet","Discord","Whatsapp","Solidwork_visualize","Spyder","Any_desk","Postman","Blender","Ui_UX","Cnc_viewer","Mongodb_compass","Google_meet","CMD","Github_desktop"]
        self.comboBox.addItems(list1)
        openwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(openwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1047, 26))
        self.menubar.setObjectName("menubar")
        openwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(openwindow)
        self.statusbar.setObjectName("statusbar")
        openwindow.setStatusBar(self.statusbar)
        openwindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.idle)
        self.pushButton_2.clicked.connect(self.click)
        self.pushButton.setStyleSheet("background-color: skyblue");
        self.pushButton_2.setStyleSheet("background-color: skyblue");
        self.comboBox.setStyleSheet("background-color: white");

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, -20, 221, 131))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(r"C:\Users\hp\Desktop\operationpage1/Athrved.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(690, 10, 351, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(26)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet("background-color:white;")
        #self.pushButton.clicked.connect(self.)
        self.retranslateUi(openwindow)
        QtCore.QMetaObject.connectSlotsByName(openwindow)
        
       

  

#use to hide tkinter window

    def click(self):
        #print("clicked")
        self.open_dialog_box()
        
    def open_dialog_box(self):
        filename=QFileDialog.getOpenFileName()
        path=filename[0]
        self.lineEdit.setText(path)

    def retranslateUi(self, openwindow):
        _translate = QtCore.QCoreApplication.translate
        openwindow.setWindowTitle(_translate("openwindow", "Add location"))
        self.label.setText(_translate("openwindow", "Please enter the location of this app"))
        self.pushButton.setText(_translate("openwindow", "submit"))
        self.pushButton_2.setText(_translate("openwindow", "Browse"))
        self.label_2.setText(_translate("openwindow", "select the name of the app"))
        self.label_6.setText(_translate("SigninWindow", "Productivity Tracker"))

if __name__ == "__main__":
    try:
        import sys
        app = QtWidgets.QApplication(sys.argv)
        openwindow = QtWidgets.QMainWindow()
        ui= Ui_openwindow()
        ui.setupUi(openwindow)
        openwindow.show()
        sys.exit(app.exec_())
    except:
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.critical('Add location Page crashed')

