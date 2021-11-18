# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'operationnew.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
from datetime import datetime
from pymongo import MongoClient
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from neweditnewqt2 import Ui_openwindow
from view_time import Ui_userid

from opennewapp import Ui_appwindow

import subprocess
import threading
from getmac import get_mac_address as gma
from win32gui import GetForegroundWindow
import psutil
from urllib.request import urlopen
import win32process
import webbrowser
from ctypes import Structure, windll, c_uint, sizeof, byref
import time
import PIL
from PIL import Image
import base64
import psycopg2

import sys
import pyautogui
import os
import logging

import random       
import ctypes       
logger = logging.getLogger(__name__)
f_handler = logging.FileHandler('app.log')
f_handler.setLevel(logging.DEBUG)

f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)
logger.warning('operation page has been accessed')
global a,b,k 

start_time1 = datetime.now().replace(microsecond=0)
a=[0]      ##  idle time 
b=[0]      ## total idle time 
m=[]       ## pause resume time
resume_pause=[0]   ##for first time resume pause
j=[0]      ##  idle time of resume pause
k=[0]      ##  total idle time of resume pause
op=[0]     ##incase user closes the window without resuming his work(in pause mode")
reading_mode=[0]   ##ON and OFF of the reading mode
bro_screen=[0]    ##screenshot time of sleep   
global idle_in_sleep_mode
idle_in_sleep_mode=[0]

global imidle
imidle=[0]
t_w_t_lis = []
t_a_t_lis = []
p_r_t_lis = []
i_d_t_lis = []
t_w_t_lis2 = []
p_r_t_lis2 = []
i_d_t_lis2 = []
t_a_t_lis2 = []
t_date = []
global dif_v
dif_v = []
global vv
vv = []

conn=psycopg2.connect('')           #PSQL Database link
cur=conn.cursor()
#list1=[]
global mac_a
mac_a=str(gma())
#print(mac_a)
#cur.execute("select member_id from member1 where name1 ='%s'"%(l))
cur.execute("select user_id from login_mac where mac ='%s'"%(mac_a))
mac_aaa = cur.fetchall()
mac_aaa1=mac_aaa[0]
mac_aaa2=mac_aaa1[0]
#print(mac_aaa2)

global mainID
mainID= mac_aaa2



qss = """
QMenuBar {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                      stop:0 lightgray, stop:1 darkgray);
}
QMenuBar::item {
    spacing: 3px;           
    padding: 2px 10px;
    background-color: rgb(255,255,255);
    color: rgb(0,0,0);  
    border-radius: 0px;
}
QMenuBar::item:selected {    
    background-color: rgb(255,255,255);
}
QMenuBar::item:pressed {
    background: rgb(255,255,255);
}

/* +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ */  

QMenu {
    background-color: rgb(255,255,255);   
    border: 1px solid black;
    margin: 2px;
}
QMenu::item {
    background-color: rgb(255,255,255);
}
QMenu::item:selected { 
    background-color: rgb(255,255,255);
    color: rgb(0,0,0);
}
"""

conn=psycopg2.connect('')           #PSQL Database link
cur=conn.cursor()
cur.execute("select dark_or_light_mode from mac_address where users_id='%s'"%(mainID))
global dark_light_mode
dark_light_mode=cur.fetchone()
#print(dark_light_mode[0])

class Ui_operations(object):   
    def setupUi(self, operations):
        t = threading.Thread(target=self.log100)
        t.start()
        t = threading.Thread(target=self.log)
        t.start()
        operations.setObjectName("operations")
        operations.resize(1366, 768)
        operations.setMaximumSize(QtCore.QSize(1366, 768))
        
        icon=QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Athrved3.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        operations.setWindowIcon(icon)
        
        self.centralwidget = QtWidgets.QWidget(operations)
        self.centralwidget.setObjectName("centralwidget")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(-10, -20, 1561, 861))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        #self.label_21.setStyleSheet("background-color:gray;")# rgb(255, 255, 255);")   
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")


        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 220, 111, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(85, 170, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 580, 111, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(85, 170, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 340, 111, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(85, 170, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(50, 460, 111, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(85, 170, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        


        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1153, 475, 165, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
       
        self.label.setObjectName("label")

        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(1210, 580, 81, 101))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("pic.jpg"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(1250, 680, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_16.setText(load9)
        
        
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1145, 680, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        #font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        
       
        self.label_11.setObjectName("label_11")


        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        if (len(name4) >=10):
          self.label_4.setGeometry(QtCore.QRect(1144, 530, 221, 41))
        else:
          self.label_4.setGeometry(QtCore.QRect(1184, 530, 221, 41))  
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_4.setText(name4)
        

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(200, 190, 921, 521))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setStyleSheet("background-color:transparent;")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()#905
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 905, 771))
        self.scrollAreaWidgetContents.setAutoFillBackground(False)
        
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")

       
        self.vscode = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        #self.vscode.setGeometry(QtCore.QRect(660, 190, 101, 101))
        self.vscode.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.vscode.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.vscode.setText("\n\n\n\n\n\n")
        icon = QtGui.QIcon()
        #icon.addPixmap(QtGui.QPixmap("VS.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vscode.setIcon(icon)
        self.vscode.setIconSize(QtCore.QSize(100, 100))
        self.vscode.setObjectName("vscode")
        self.gridLayout.addWidget(self.vscode, 0, 4, 1, 1)
        self.androidstudio = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        #self.androidstudio.setGeometry(QtCore.QRect(100, 310, 111, 111))
        self.androidstudio.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.androidstudio.setText("\n\n\n\n\n\n")
        icon1 = QtGui.QIcon()
        #icon1.addPixmap(QtGui.QPixmap("Android.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.androidstudio.setIcon(icon1)
        self.androidstudio.setIconSize(QtCore.QSize(120, 120))
        self.androidstudio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.androidstudio.setObjectName("androidstudio")
        self.gridLayout.addWidget(self.androidstudio, 2, 0, 1, 1)
        self.premierpro = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        #self.premierpro.setGeometry(QtCore.QRect(380, 190, 101, 101))
        self.premierpro.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.premierpro.setText("\n\n\n\n\n\n")
        icon2 = QtGui.QIcon()
        #icon2.addPixmap(QtGui.QPixmap("Adobe_Premiere_Pro_Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.premierpro.setIcon(icon2)
        self.premierpro.setIconSize(QtCore.QSize(100, 100))
        self.premierpro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.premierpro.setObjectName("premierpro")
        self.gridLayout.addWidget(self.premierpro, 0, 2, 1, 1)
        self.pycharm = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        #self.pycharm.setGeometry(QtCore.QRect(380, 310, 101, 101))
        self.pycharm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pycharm.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.pycharm.setText("\n\n\n\n\n\n")
        icon3 = QtGui.QIcon()
        #icon3.addPixmap(QtGui.QPixmap("Py_Charm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pycharm.setIcon(icon3)
        self.pycharm.setIconSize(QtCore.QSize(100, 100))
        self.pycharm.setObjectName("pycharm")
        self.gridLayout.addWidget(self.pycharm, 2, 2, 1, 1)
        self.photoshop = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        #self.photoshop.setGeometry(QtCore.QRect(520, 190, 101, 101))
        self.photoshop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.photoshop.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.photoshop.setText("\n\n\n\n\n\n")
        icon4 = QtGui.QIcon()
        #icon4.addPixmap(QtGui.QPixmap("Photoshop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.photoshop.setIcon(icon4)
        self.photoshop.setIconSize(QtCore.QSize(100, 100))
        self.photoshop.setObjectName("photoshop")
        self.gridLayout.addWidget(self.photoshop, 0, 3, 1, 1)
        self.tableau = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        #self.tableau.setGeometry(QtCore.QRect(100, 440, 121, 101))
        self.tableau.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tableau.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.tableau.setText("\n\n\n\n\n\n")
        icon5 = QtGui.QIcon()
        #icon5.addPixmap(QtGui.QPixmap("Tablaeu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tableau.setIcon(icon5)
        self.tableau.setIconSize(QtCore.QSize(120, 120))
        self.tableau.setObjectName("tableau")
        self.gridLayout.addWidget(self.tableau, 4, 0, 1, 1)
        self.figma = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        #self.figma.setGeometry(QtCore.QRect(790, 310, 111, 111))
        self.figma.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.figma.setText("\n\n\n\n\n\n")
        icon6 = QtGui.QIcon()
        #icon6.addPixmap(QtGui.QPixmap("FigmaLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.figma.setIcon(icon6)
        self.figma.setIconSize(QtCore.QSize(110, 110))
        self.figma.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.figma.setObjectName("figma")
        self.gridLayout.addWidget(self.figma, 2, 5, 1, 1)
        self.idle = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        #self.idle.setGeometry(QtCore.QRect(510, 310, 121, 101))
        self.idle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.idle.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.idle.setText("\n\n\n\n\n\n")
        icon7 = QtGui.QIcon()
        #icon7.addPixmap(QtGui.QPixmap("python.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.idle.setIcon(icon7)
        self.idle.setIconSize(QtCore.QSize(100, 100))
        self.idle.setObjectName("idle")
        self.gridLayout.addWidget(self.idle, 2, 3, 1, 1)
        self.ardiuno = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
       # self.ardiuno.setGeometry(QtCore.QRect(240, 310, 101, 101))
        self.ardiuno.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ardiuno.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.ardiuno.setText("\n\n\n\n\n\n")
        icon8 = QtGui.QIcon()
        #icon8.addPixmap(QtGui.QPixmap("ardiuno.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ardiuno.setIcon(icon8)
        self.ardiuno.setIconSize(QtCore.QSize(100, 100))
        self.ardiuno.setObjectName("ardiuno")
        self.gridLayout.addWidget(self.ardiuno, 2, 1, 1, 1)
        self.illustrator = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        #self.illustrator.setGeometry(QtCore.QRect(110, 190, 101, 101))
        self.illustrator.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.illustrator.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.illustrator.setText("\n\n\n\n\n\n")
        icon9 = QtGui.QIcon()
        #icon9.addPixmap(QtGui.QPixmap("AI.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.illustrator.setIcon(icon9)
        self.illustrator.setIconSize(QtCore.QSize(100, 100))
        self.illustrator.setObjectName("illustrator")
        self.gridLayout.addWidget(self.illustrator, 0, 0, 1, 1)
        self.wps = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        #self.wps.setGeometry(QtCore.QRect(790, 190, 111, 101))
        self.wps.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.wps.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.wps.setText("\n\n\n\n\n\n")
        icon10 = QtGui.QIcon()
        #icon10.addPixmap(QtGui.QPixmap("wps.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)  ############################################################################
        self.wps.setIcon(icon10)
        self.wps.setIconSize(QtCore.QSize(110, 110))
        self.wps.setObjectName("wps")
        self.gridLayout.addWidget(self.wps, 0, 5, 1, 1)
        self.Qtdesigner = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
       # self.Qtdesigner.setGeometry(QtCore.QRect(660, 310, 101, 101))
        self.Qtdesigner.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Qtdesigner.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.Qtdesigner.setText("\n\n\n\n\n\n")
        icon11 = QtGui.QIcon()
        #icon11.addPixmap(QtGui.QPixmap("qtdesigner.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Qtdesigner.setIcon(icon11)
        self.Qtdesigner.setIconSize(QtCore.QSize(100, 100))
        self.Qtdesigner.setObjectName("Qtdesigner")
        self.gridLayout.addWidget(self.Qtdesigner, 2, 4, 1, 1)
        self.aftereffects = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        #self.aftereffects.setGeometry(QtCore.QRect(240, 190, 101, 101))
        self.aftereffects.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.aftereffects.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.aftereffects.setText("\n\n\n\n\n\n")
        icon12 = QtGui.QIcon()
        #icon12.addPixmap(QtGui.QPixmap("Adobe_After_Effects_Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aftereffects.setIcon(icon12)
        self.aftereffects.setIconSize(QtCore.QSize(100, 100))
        self.aftereffects.setObjectName("aftereffects")
        self.gridLayout.addWidget(self.aftereffects, 0, 1, 1, 1)
        self.proteus = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        #self.proteus.setGeometry(QtCore.QRect(920, 190, 131, 111))
        self.proteus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.proteus.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.proteus.setText("\n\n\n\n\n\n")
        icon13 = QtGui.QIcon()
        #icon13.addPixmap(QtGui.QPixmap("Proteus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off) ##########################################################333
        self.proteus.setIcon(icon13)
        self.proteus.setIconSize(QtCore.QSize(120, 120))
        self.proteus.setObjectName("proteus")
        self.gridLayout.addWidget(self.proteus, 0, 6, 1, 1)
        self.codeblocks = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        #self.codeblocks.setGeometry(QtCore.QRect(770, 620, 101, 101))
        
        self.codeblocks.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.codeblocks.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.codeblocks.setText("\n\n\n\n\n\n")
        icon14 = QtGui.QIcon()
        #icon14.addPixmap(QtGui.QPixmap("Code.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.codeblocks.setIcon(icon14)
        self.codeblocks.setIconSize(QtCore.QSize(120, 120))
        self.codeblocks.setObjectName("codeblocks")
        self.gridLayout.addWidget(self.codeblocks, 2, 6, 1, 1)
        
        self.solidworks = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        #self.solidworks.setGeometry(QtCore.QRect(250, 440, 111, 101))
        self.solidworks.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.solidworks.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.solidworks.setText("\n\n\n\n\n\n")
        icon15 = QtGui.QIcon()
        #icon15.addPixmap(QtGui.QPixmap("sw.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.solidworks.setIcon(icon15)
        self.solidworks.setIconSize(QtCore.QSize(100, 100))
        self.solidworks.setObjectName("solidworks")
        self.gridLayout.addWidget(self.solidworks, 4, 1, 1, 1)
        self.word = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        #self.word.setGeometry(QtCore.QRect(520, 440, 101, 101))
        self.word.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.word.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.word.setText("\n\n\n\n\n\n")
        icon16 = QtGui.QIcon()
        #icon16.addPixmap(QtGui.QPixmap("word.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.word.setIcon(icon16)
        self.word.setIconSize(QtCore.QSize(100, 100))
        self.word.setObjectName("word")
        self.gridLayout.addWidget(self.word, 4, 3, 1, 1)

        self.MS_Excel = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        #self.MS_Excel.setGeometry(QtCore.QRect(380, 440, 101, 101))
        self.MS_Excel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MS_Excel.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.MS_Excel.setText("\n\n\n\n\n\n")
        icon17 = QtGui.QIcon()
        #icon17.addPixmap(QtGui.QPixmap("Excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MS_Excel.setIcon(icon17)
        self.MS_Excel.setIconSize(QtCore.QSize(100, 100))
        self.MS_Excel.setObjectName("MS_Excel")
        self.gridLayout.addWidget(self.MS_Excel, 4, 2, 1, 1)

        self.MS_Powerpoint = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        #self.MS_Powerpoint.setGeometry(QtCore.QRect(660, 440, 101, 101))
        self.MS_Powerpoint.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MS_Powerpoint.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.MS_Powerpoint.setText("\n\n\n\n\n\n")
        icon18 = QtGui.QIcon()
        #icon18.addPixmap(QtGui.QPixmap("powerpoint.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MS_Powerpoint.setIcon(icon18)
        self.MS_Powerpoint.setIconSize(QtCore.QSize(100, 100))
        self.MS_Powerpoint.setObjectName("MS_Powerpoint")
        self.gridLayout.addWidget(self.MS_Powerpoint, 4, 4, 1, 1)

        self.Microsoft_Edge = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        #self.Microsoft_Edge.setGeometry(QtCore.QRect(790, 440, 101, 101))
        self.Microsoft_Edge.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Microsoft_Edge.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.Microsoft_Edge.setText("\n\n\n\n\n\n")
        icon19 = QtGui.QIcon()
        #icon19.addPixmap(QtGui.QPixmap("edge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)          #####################################################################3
        self.Microsoft_Edge.setIcon(icon19)
        self.Microsoft_Edge.setIconSize(QtCore.QSize(100, 100))
        self.Microsoft_Edge.setObjectName("Microsoft_Edge")
        self.gridLayout.addWidget(self.Microsoft_Edge, 4, 5, 1, 1)

        self.Team_viewer = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        #self.Team_viewer.setGeometry(QtCore.QRect(110, 560, 101, 101))
        self.Team_viewer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Team_viewer.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.Team_viewer.setText("\n\n\n\n\n\n")
        icon20 = QtGui.QIcon()
        #icon20.addPixmap(QtGui.QPixmap("teamviewer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Team_viewer.setIcon(icon20)
        self.Team_viewer.setIconSize(QtCore.QSize(100, 100))
        self.Team_viewer.setObjectName("Team_viewer")
        self.gridLayout.addWidget(self.Team_viewer, 5, 0, 1, 1)

        self.Jio_meet = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        #self.Jio_meet.setGeometry(QtCore.QRect(250, 560, 101, 101))
        self.Jio_meet.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Jio_meet.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.Jio_meet.setText("\n\n\n\n\n\n")
        icon21 = QtGui.QIcon()
        #icon21.addPixmap(QtGui.QPixmap("jio_Meet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Jio_meet.setIcon(icon21)
        self.Jio_meet.setIconSize(QtCore.QSize(100, 100))
        self.Jio_meet.setObjectName("Jio_meet")
        self.gridLayout.addWidget(self.Jio_meet, 5, 1, 1, 1)

        self.Discord = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        #self.Discord.setGeometry(QtCore.QRect(380, 560, 101, 101))
        self.Discord.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Discord.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.Discord.setText("\n\n\n\n\n\n")
        icon22 = QtGui.QIcon()
        #icon22.addPixmap(QtGui.QPixmap("Discord.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Discord.setIcon(icon22)
        self.Discord.setIconSize(QtCore.QSize(100, 100))
        self.Discord.setObjectName("Discord")
        self.gridLayout.addWidget(self.Discord, 5, 2, 1, 1)

        self.Whatsapp = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        #  self.Whatsapp.setGeometry(QtCore.QRect(930, 440, 101, 101))
        self.Whatsapp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Whatsapp.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.Whatsapp.setText("\n\n\n\n\n\n")
        icon23 = QtGui.QIcon()
        #icon23.addPixmap(QtGui.QPixmap("whatsapp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Whatsapp.setIcon(icon23)
        self.Whatsapp.setIconSize(QtCore.QSize(100, 100))
        self.Whatsapp.setObjectName("Whatsapp")
        self.gridLayout.addWidget(self.Whatsapp, 4, 6, 1, 1)


        self.Solidwork_visualize = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        #  self.Solidwork_visualize.setGeometry(QtCore.QRect(520, 560, 101, 101))
        self.Solidwork_visualize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Solidwork_visualize.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.Solidwork_visualize.setText("\n\n\n\n\n\n")
        icon24 = QtGui.QIcon()
        #icon24.addPixmap(QtGui.QPixmap("sw_vis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Solidwork_visualize.setIcon(icon24)
        self.Solidwork_visualize.setIconSize(QtCore.QSize(100, 100))
        self.Solidwork_visualize.setObjectName("Solidwork_visualize")
        self.gridLayout.addWidget(self.Solidwork_visualize, 5, 3, 1, 1)


        self.Spyder = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        # self.Solidwork_visualize.setGeometry(QtCore.QRect(520, 560, 101, 101))
        self.Spyder.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Spyder.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.Spyder.setText("\n\n\n\n\n\n")
        icon25 = QtGui.QIcon()
        #icon25.addPixmap(QtGui.QPixmap("sw_vis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Spyder.setIcon(icon25)
        self.Spyder.setIconSize(QtCore.QSize(100, 100))
        self.Spyder.setObjectName("Spyder")
        self.gridLayout.addWidget(self.Spyder, 5, 4, 1, 1)

        self.Any_desk = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        # self.Solidwork_visualize.setGeometry(QtCore.QRect(520, 560, 101, 101))
        self.Any_desk.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Any_desk.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.Any_desk.setText("\n\n\n\n\n\n")
        icon26 = QtGui.QIcon()
        #icon26.addPixmap(QtGui.QPixmap("sw_vis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Any_desk.setIcon(icon26)
        self.Any_desk.setIconSize(QtCore.QSize(100, 100))
        self.Any_desk.setObjectName("Any_desk")
        self.gridLayout.addWidget(self.Any_desk, 5, 5, 1, 1)

        self.Postman = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        # self.Solidwork_visualize.setGeometry(QtCore.QRect(520, 560, 101, 101))
        self.Postman.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Postman.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.Postman.setText("\n\n\n\n\n\n")
        icon27 = QtGui.QIcon()
        #icon27.addPixmap(QtGui.QPixmap("sw_vis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Postman.setIcon(icon27)
        self.Postman.setIconSize(QtCore.QSize(100, 100))
        self.Postman.setObjectName("Postman")
        self.gridLayout.addWidget(self.Postman, 5, 6, 1, 1)

        self.Blender = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        # self.Solidwork_visualize.setGeometry(QtCore.QRect(520, 560, 101, 101))
        self.Blender.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Blender.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.Blender.setText("\n\n\n\n\n\n")
        icon28 = QtGui.QIcon()
        #icon28.addPixmap(QtGui.QPixmap("sw_vis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Blender.setIcon(icon28)
        self.Blender.setIconSize(QtCore.QSize(100, 100))
        self.Blender.setObjectName("Blender")
        self.gridLayout.addWidget(self.Blender, 6, 0, 1, 1)

        self.Ui_UX = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        # self.Solidwork_visualize.setGeometry(QtCore.QRect(520, 560, 101, 101))
        self.Ui_UX.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Ui_UX.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.Ui_UX.setText("\n\n\n\n\n\n")
        icon29 = QtGui.QIcon()
        #icon29.addPixmap(QtGui.QPixmap("sw_vis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Ui_UX.setIcon(icon29)
        self.Ui_UX.setIconSize(QtCore.QSize(100, 100))
        self.Ui_UX.setObjectName("Ui_UX")
        self.gridLayout.addWidget(self.Ui_UX, 6, 1, 1, 1)

        self.Cnc_viewer = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        # self.Solidwork_visualize.setGeometry(QtCore.QRect(520, 560, 101, 101))
        self.Cnc_viewer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Cnc_viewer.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.Cnc_viewer.setText("\n\n\n\n\n\n")
        icon30 = QtGui.QIcon()
        #icon30.addPixmap(QtGui.QPixmap("sw_vis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Cnc_viewer.setIcon(icon30)
        self.Cnc_viewer.setIconSize(QtCore.QSize(100, 100))
        self.Cnc_viewer.setObjectName("Cnc_viewer")
        self.gridLayout.addWidget(self.Cnc_viewer, 6, 2, 1, 1)

        self.Mongodb_compass = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        # self.Solidwork_visualize.setGeometry(QtCore.QRect(520, 560, 101, 101))
        self.Mongodb_compass.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Mongodb_compass.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.Mongodb_compass.setText("\n\n\n\n\n\n")
        icon31 = QtGui.QIcon()
        #icon31.addPixmap(QtGui.QPixmap("sw_vis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Mongodb_compass.setIcon(icon31)
        self.Mongodb_compass.setIconSize(QtCore.QSize(100, 100))
        self.Mongodb_compass.setObjectName("Mongodb_compass")
        self.gridLayout.addWidget(self.Mongodb_compass, 6, 3, 1, 1)

        self.Google_meet = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        # self.Solidwork_visualize.setGeometry(QtCore.QRect(520, 560, 101, 101))
        self.Google_meet.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Google_meet.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.Google_meet.setText("\n\n\n\n\n\n")
        icon32 = QtGui.QIcon()
        #icon32.addPixmap(QtGui.QPixmap("sw_vis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)    ###########################################
        self.Google_meet.setIcon(icon32)
        self.Google_meet.setIconSize(QtCore.QSize(100, 100))
        self.Google_meet.setObjectName("Google_meet")
        self.gridLayout.addWidget(self.Google_meet, 6, 4, 1, 1)

        self.cmd = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        # self.Solidwork_visualize.setGeometry(QtCore.QRect(520, 560, 101, 101))
        self.cmd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cmd.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.cmd.setText("\n\n\n\n\n\n")
        icon33 = QtGui.QIcon()
        #icon33.addPixmap(QtGui.QPixmap("sw_vis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmd.setIcon(icon33)
        self.cmd.setIconSize(QtCore.QSize(100, 100))
        self.cmd.setObjectName("Solidwork_visualize")
        self.gridLayout.addWidget(self.cmd, 6, 5, 1, 1)

        self.Github_desktop = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        # self.Solidwork_visualize.setGeometry(QtCore.QRect(520, 560, 101, 101))
        self.Github_desktop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Github_desktop.setStyleSheet("background:none;\n""background-color:transparent;")#"border:1px solid;""border-color:red;")
        self.Github_desktop.setText("\n\n\n\n\n\n")
        icon34 = QtGui.QIcon()
        #icon34.addPixmap(QtGui.QPixmap("sw_vis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Github_desktop.setIcon(icon34)
        self.Github_desktop.setIconSize(QtCore.QSize(100, 100))
        self.Github_desktop.setObjectName("Solidwork_visualize")
        self.gridLayout.addWidget(self.Github_desktop, 6, 6, 1, 1)

        
        
                    
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(320, 110, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius:10px;\n""background-color: rgb(220, 220, 220);\n""")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        
        
            #self.buttonabout_5.move(591,560)
        if len(name1)<=10:
            #print(1)
            self.label_2.setGeometry(QtCore.QRect(430, 20, 691, 81))

        elif (10<len(name1)<=14):
            #print(5)
            self.label_2.setGeometry(QtCore.QRect(370, 20, 721, 81))

        elif (14<len(name1)<=17):
            #print(10)
            self.label_2.setGeometry(QtCore.QRect(340, 20, 751, 81))
        elif (17<len(name1)<=22):
            #print(11)
            self.label_2.setGeometry(QtCore.QRect(300, 20, 781, 81))



        else:
                #print(15)
            self.label_2.setGeometry(QtCore.QRect(200, 20, 781, 81)) 

        print(999)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(5, 10, 201, 131))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Athrved.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1000, 20, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(26)
        font.setUnderline(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")#710
        self.label_8.setStyleSheet("color: blue;")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(810, 110, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-radius:10px;\n""background-color: rgb(85, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.search_option)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1140, 399, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(85, 170, 255);")
       
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.reading_mode_idle_time)

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(1135, 370, 197, 20))#390
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(1135, 450, 197, 20))#390
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")#1170
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1185, 180, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("border-radius:10px;\n""background-color: rgb(85, 170, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.pause_window)        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1185, 290, 111, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(85, 170, 255);")
        self.pushButton_4.setStyleSheet("border-radius:10px;\n" "background-color: green;\n" "color: rgb(255, 255, 255)")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.resume_window)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)#1130
        self.label_5.setGeometry(QtCore.QRect(1150, 140, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1150, 260, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(0, 790, 1551, 21))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.scrollAreaWidgetContents.setStyleSheet("background-repeat:none;\n"
        "background-image: url(Screenshot (11751).png);\n""")
        
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        self.pushButton_5.clicked.connect(self.lms_portal_link)
        self.pushButton_6.clicked.connect(self.chat_app)
        self.pushButton_7.clicked.connect(self.youtube_link)
        self.pushButton_8.clicked.connect(self.gmail_link)
        #print(999)
        self.vscode.clicked.connect(self.vs)
        self.androidstudio.clicked.connect(self.android)
        self.premierpro.clicked.connect(self.premier)
        self.pycharm.clicked.connect(self.pych)
        self.photoshop.clicked.connect(self.photo)
        self.tableau.clicked.connect(self.tabl)
        self.figma.clicked.connect(self.fig)
        self.idle.clicked.connect(self.idl)
        self.ardiuno.clicked.connect(self.ardu)
        self.illustrator.clicked.connect(self.illus)
        self.wps.clicked.connect(self.wp)
        self.Qtdesigner.clicked.connect(self.Qtdes)
        self.proteus.clicked.connect(self.prot)
        self.aftereffects.clicked.connect(self.aftere)
        self.codeblocks.clicked.connect(self.code)
        self.solidworks.clicked.connect(self.solid)
        self.word.clicked.connect(self.wod)

        self.MS_Excel.clicked.connect(self.excel)
        self.MS_Powerpoint.clicked.connect(self.power)
        self.Microsoft_Edge.clicked.connect(self.edge)
        self.Team_viewer.clicked.connect(self.Tmv)
        self.Jio_meet.clicked.connect(self.jio)
        self.Discord.clicked.connect(self.dis)
        self.Whatsapp.clicked.connect(self.whatsapp)
        self.Solidwork_visualize.clicked.connect(self.svisual)
        
        self.Spyder.clicked.connect(self.spy)
   
        self.Any_desk.clicked.connect(self.any)
   
        self.Postman.clicked.connect(self.post)
        self.Blender.clicked.connect(self.blen)
        self.Ui_UX.clicked.connect(self.ux)
   
        self.Cnc_viewer.clicked.connect(self.cnc)

        self.Mongodb_compass.clicked.connect(self.mongo)
  
        self.Google_meet.clicked.connect(self.goo)
        
        self.cmd.clicked.connect(self.cd)
       
        self.Github_desktop.clicked.connect(self.git)
        
          
        if dark_light_mode[0]=="OFF":
            self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.label_21.setStyleSheet("background-color:rgb(255, 255, 255);")   #mmmmmmmmmmmmmm

            
            operations.setStyleSheet("background-color:rgb(255, 255, 255);")
            operations.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(operations)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 26))
            self.menubar.setObjectName("menubar")
            self.menuEdit = QtWidgets.QMenu(self.menubar)
            self.menuEdit.setObjectName("menuEdit")
            
            self.menuEdit.setStyleSheet("color: black;")
            self.menuExtra_features = QtWidgets.QMenu(self.menubar)
            self.menuExtra_features.setObjectName("menuExtra_features")
            self.menuExtra_features.setStyleSheet("color: black;")

            self.menuExtra_Apps = QtWidgets.QMenu(self.menubar)
            self.menuExtra_Apps.setObjectName("menuExtra_Apps")
            self.menuExtra_Apps.setStyleSheet("color: black;")
        
            self.menubar.setStyleSheet("color: black; background-color:white;") #mmmmmm adding colour to menubar

            
        else:
            operations.setStyleSheet("background-color:gray;")
            self.label_8.setStyleSheet("color: blue;")
            self.label_2.setStyleSheet("background-color:gray);")
            self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
            self.label.setStyleSheet("color: rgb(255, 255, 255);")
            self.label_11.setStyleSheet("color:yellow;")
            self.label_16.setStyleSheet("color: yellow;")
            self.label_4.setStyleSheet("color:yellow;")
            self.label_21.setStyleSheet("background-color:gray;")   #mmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
            self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
            self.label_6.setStyleSheet("color: rgb(255, 255, 255);")

            operations.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(operations)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 26))
            self.menubar.setObjectName("menubar")
            self.menuEdit = QtWidgets.QMenu(self.menubar)
            self.menuEdit.setObjectName("menuEdit")
            
            self.menuEdit.setStyleSheet("color: white;")
            self.menuExtra_features = QtWidgets.QMenu(self.menubar)
            self.menuExtra_features.setObjectName("menuExtra_features")
            self.menuExtra_features.setStyleSheet("color: white;")
            self.menuExtra_Apps = QtWidgets.QMenu(self.menubar)
            self.menuExtra_Apps.setObjectName("menuExtra_Apps")
            self.menuExtra_Apps.setStyleSheet("color: white;")
            self.menubar.setStyleSheet("color: white; background-color:gray;") #mmmmmm adding colour to menubar
            
            


        
        
       
        


        self.actionAdd_Location = QtWidgets.QAction(operations)
        self.actionAdd_Location.setObjectName("actionAdd_Location")
        
        self.menuEdit.addAction(self.actionAdd_Location)
        

        self.actionLogout = QtWidgets.QAction(operations)
        self.actionLogout.setObjectName("actionLogout")
        self.menuEdit.addAction(self.actionLogout)

        self.actionLogout.triggered.connect(self.see3)
        
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuExtra_features.menuAction())
        self.menubar.addAction(self.menuExtra_Apps.menuAction())

        
        self.actionview_time = QtWidgets.QAction(operations)
        self.actionview_time.setObjectName("actionview_time")
        self.menuExtra_features.addAction(self.actionview_time)

        self.actiondark_mode = QtWidgets.QAction(operations)
        self.actiondark_mode.setObjectName("actiondark_mode")
        self.menuExtra_features.addAction(self.actiondark_mode)


        self.actionaddapp = QtWidgets.QAction(operations)
        self.actionaddapp.setObjectName("actionaddapp")
        self.menuExtra_Apps.addAction(self.actionaddapp)

        self.actionopenapp = QtWidgets.QAction(operations)
        self.actionopenapp.setObjectName("actionopenapp")
        self.menuExtra_Apps.addAction(self.actionopenapp)

        self.actionchangeapp = QtWidgets.QAction(operations)
        self.actionchangeapp.setObjectName("actionchangeapp")
        self.menuExtra_Apps.addAction(self.actionchangeapp)

        self.actionremoveapp = QtWidgets.QAction(operations)
        self.actionremoveapp.setObjectName("actionchangeapp")
        self.menuExtra_Apps.addAction(self.actionremoveapp)




        #self..clicked.connect(self.dark_mode_or_light_menubar)
        self.actiondark_mode.triggered.connect(self.dark_mode_or_light_menubar)
        
        self.actionAdd_Location.triggered.connect(self.see1)
        self.actionview_time.triggered.connect(self.see2)

        self.actionopenapp.triggered.connect(self.see5)
        self.actionchangeapp.triggered.connect(self.see6)
        self.actionaddapp.triggered.connect(self.see4)
        self.actionremoveapp.triggered.connect(self.see7)

      

        
        self.statusbar = QtWidgets.QStatusBar(operations)

        
        
        
        #self.statusbar.setObjectName("statusbar")
        operations.setStatusBar(self.statusbar)
        

        
        
        print(9999)
        self.retranslateUi(operations)
        QtCore.QMetaObject.connectSlotsByName(operations)

    def log(self):       #screenshot code
            
            try: 
              if op[0]==0:
                mywidth=150
                myheight=150
                
                from datetime import datetime,time
                t=(datetime.now().strftime("%Y-%m-%d %H-%M"))
                #print(time)
                from datetime import date, timedelta
                import datetime, time
                time1 = time.strftime("%H:%M:%S", time.localtime())
                yesterday = format(date.today() - timedelta(days=1))
                today1=format(date.today())
                start = '00:00:00'
                end = '05:00:00'
               
                if time1 > start and time1 < end:
                    t1=yesterday
                
                else:
                    t1=today1
                pho=pyautogui.screenshot()
                pho=pho.resize((mywidth,myheight),PIL.Image.ANTIALIAS)

                try:
                  #print(5)
                  os.mkdir("My Screenshots")
                  pho.save("My Screenshots/"+str(t)+'.png')
                except:
                  #print("haaaaaaaa")         #os.chdir("me")
                  pho.save("My Screenshots/"+str(t)+'.png')
                #pho.save(str(t)+'.png')
                
                with open("My Screenshots/"+str(t)+'.png','rb') as imageFile:
                    z = base64.b64encode(imageFile.read())
                #x+=1
                time.sleep(1*60)                                              #######################################
                
                connection = MongoClient("")            #MongoDB Database link
                db = connection['test']
                collection = db['screenshots']
                usrid=int(mainID)
                myid={'_id':usrid}
                    
                y= collection.find_one(myid)
                
                try:
                    m=y[t1]
                    collection.update_one(myid,{"$addToSet":{t1:{"$each":[z]}}})
                    
                    
                except KeyError as error:
                    collection.update_one(myid,{"$set":{t1:[z]}})
                    
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('screen shot has been taken')
                
                import random
                random_for_screenshot=random.randint(0,10)
                rf_s=int(random_for_screenshot)+int(14)
                #time.sleep(rf_s*60)                                                  #######################################################
                bro_screen.clear()
                bro_screen.append(rf_s*60)
                #print(rf_s*60)
                
              elif op[0]==2:
                  print(op[0])
                  
              else:
                import time
                #time.sleep(10*60)                                                    ##################################################################
                bro_screen.clear()
                bro_screen.append(600)
                
            except Exception as e:
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('screen shot has not been taken '+str(e))




    def auto_save(self):
      from datetime import date, timedelta
      global b
      global start_time1,k,j,m,op,imidle
      
      global dif_v
      try:
            

            
            from datetime import datetime
            if op[0]==1:           #if the user has closed the app without resuming his work
                global resume_time,interval
                resume_time = datetime.now().replace(microsecond=0)
                global pause_time
   
                interval = format(resume_time-pause_time)
                m.append(interval)
                op.clear()
                op.append(1)
                pause_time = datetime.now().replace(microsecond=0)
          

                b0=(int(b[0]))
                k0=(int(k[0]))
                
                if k0>b0:
                   bk=0
                else:
                  bk=int(b0-k0)
                #print(b)

     
                b.clear()
                b.append(bk)
            
            Id=mainID 
            myquery={"_id":Id}
            import datetime as datetime2
            #print("ghuhjjffrdtfyg")
            bb=int(b[0])
            bb-=int(imidle[0])
            imidle.clear()
            imidle.append(b[0])
           
            from time import strftime
            from time import gmtime
            from datetime import datetime
            end_time = datetime.now().replace(microsecond=0)
       
            total = format(end_time - start_time1)
            #print("ljihhggu")
            total=str(total)
           
            total=datetime.strptime(total,"%H:%M:%S")
          
            idle_time = bb
            
            import time
        
            
            sumd=datetime2.timedelta()
            #print("sumd and m is",sumd,m)
            for i in m:
                (hh,mm,ss)=i.split(':')
                d=datetime2.timedelta(hours=int(hh),minutes=int(mm),seconds=int(ss))
                sumd +=d
            sumd=str(sumd)
            
            sumd=datetime.strptime(sumd,"%H:%M:%S")
            

            idle_time=strftime("%H:%M:%S",gmtime(idle_time))
            
            idle_time=datetime.strptime(idle_time,"%H:%M:%S")
            
            
            actual_time=format(total-sumd)#idle_time
            
            actual_time2=str(actual_time)
            actual_time2=datetime.strptime(actual_time,"%H:%M:%S")
            
            if idle_time>actual_time2:
               
                total_working_hrs="0:00:00"
            else:
                #print("ya2")
                total_working_hrs=format(actual_time2-idle_time)
            

            idle_time=str(idle_time)
            idle_time=datetime2.datetime.strptime(idle_time,"%Y-%m-%d %H:%M:%S") 
            idle_time=format(idle_time.time())
            
            sumd=str(sumd)
            sumd=datetime2.datetime.strptime(sumd,"%Y-%m-%d %H:%M:%S") 
            sumd=format(sumd.time())
            #print("new sumd is", sumd)
            
            total=str(total)
            total=datetime2.datetime.strptime(total,"%Y-%m-%d %H:%M:%S") 
            total=format(total.time())

            
            
            total_working_hrs=str(total_working_hrs)
            total_working_hrs=datetime2.datetime.strptime(total_working_hrs,"%H:%M:%S") 
            total_working_hrs=format(total_working_hrs.time())
            
            total=format(total)
            idle_time=format(idle_time)
            sumd=format(sumd)

            #global start_time1
            start_time1 = datetime.now().replace(microsecond=0)
            
            
            if op[0]==1:
                pause_time = datetime.now().replace(microsecond=0)
                
            m=[]       ## pause resume time
            #resume_pause=[0]   ##for first time resume pause
            j=[0]      ##  idle time of resume pause
            k=[0]      ##  total idle time of resume pause
            try:
                twh,twm,tws = total_working_hrs.split(':')
                twt = int(twh)*3600 + int(twm)*60 +int(tws)*1
                prh,prm,prs = sumd.split(':')
                prt = int(prh)*3600 + int(prm)*60 +int(prs)*1
                idh,idm,ids = idle_time.split(':')
                idt = int(idh)*3600 + int(idm)*60 +int(ids)*1
                tah,tam,tas = total.split(':')
                tat = int(tah)*3600 + int(tam)*60 +int(tas)*1

                if t_w_t_lis!=[]:   #checking is there any data in the list or not
                    twt+=t_w_t_lis[0]
                    #t_w_t_lis.append(twt)
                if p_r_t_lis!=[]:
                    prt+=p_r_t_lis[0]
                    #p_r_t_lis.append(prt)
                if i_d_t_lis!=[]:
                    idt+=i_d_t_lis[0]
                    #i_d_t_lis.append(idt)
                if t_a_t_lis!=[]:
                    tat+=t_a_t_lis[0]
                    #t_a_t_lis.append(tat)
                #print("tat all is",tat,prt,idt,twt)
                from datetime import date as dd
                nowwwwday = dd.today()
                
                if vv == []:
                    
                     urlopen('http://216.58.192.142', timeout=1)
                if t_w_t_lis2 != []:
                    threadst = threading.Thread(target=self.go_save)#(b,m,op,start_time1,pause_time,k,today))
                    threadst.start()
                    
                #print("next continuation")
                from datetime import date as d, timedelta as t
                #import datetime, time
                time_tt = time.strftime("%H:%M:%S", time.localtime())

                yesterday = d.today() - t(days=1)
                today1=d.today()
                global today
                start = '00:00:00'
                end = '03:00:00'
                if time_tt > start and time_tt < end:                   #work done before today morning 6am is considered as yesterdays work
                  #print("in")
                  today=yesterday

                else:
                  #print("out")
                  today=today1
                total=format(strftime("%H:%M:%S",gmtime(tat)))
                #print(8)
                sumd=format(strftime("%H:%M:%S",gmtime(prt)))
                #print(8)
                idle_time=format(strftime("%H:%M:%S",gmtime(idt)))
                #print(8)
                total_working_hrs=format(strftime("%H:%M:%S",gmtime(twt)))
                
                
                conn=psycopg2.connect('')
                cur=conn.cursor()
                cur.execute( 'select * from productivity')
                data=cur.fetchall()   
                cur.execute("select * from productivity where date='%s' AND user_id=%d"%(today,Id))
                data=cur.fetchall()
                
                for x in data:
                       
                           if x[0] == Id:
                                

                                from datetime import date            

                                idle_time1=x[3]                        #  ["Actual_Idle_time"]     #values from database      #idle_time
                                total_app_time1=x[2]                   #["Total_App_time"]                                    #total
                                pause_resume1=x[4]                     #["Pause_Resume_Interval"]                             #sumd
                                total_working_hours=x[5]               #["Total_Working_Hours"]                               #total_working_hrs

                                 
                               
                                #print("m is",m)
                                idle_time1=str(idle_time1)
                                idle_time1=datetime2.datetime.strptime(idle_time1,"%H:%M:%S") 
                                idle_time1=format(idle_time1.time())
                                
                                
                                (h1,m1,s1)=idle_time1.split(':')
                                idle_time1=(int(h1)*3600)+(int(m1)*60)+int(s1)
                                (h1,m1,s1)=idle_time.split(':')
                                idle_time=(int(h1)*3600)+(int(m1)*60)+int(s1)   
                                idle_time_final2= (idle_time1+idle_time)
                                idle_time_final=format(strftime("%H:%M:%S",gmtime(idle_time_final2))) 

                             
                                total_app_time1=str(total_app_time1)
                                total_app_time1=datetime2.datetime.strptime(total_app_time1,"%H:%M:%S")
                                total_app_time1=format(total_app_time1.time())
                                (h1,m1,s1)=total_app_time1.split(':')
                                total_app_time1=(int(h1)*3600)+(int(m1)*60)+int(s1)
                                (h1,m1,s1)=total.split(':')
                                total=(int(h1)*3600)+(int(m1)*60)+int(s1)
                                total_app_time1_final2=(total_app_time1+total)
                                total_app_time1_final=format(strftime("%H:%M:%S",gmtime(total_app_time1_final2)))
                                
                            
                                pause_resume1=str(pause_resume1)
                                pause_resume1=datetime2.datetime.strptime(pause_resume1,"%H:%M:%S")
                                pause_resume1=format(pause_resume1.time())
                                (h1,m1,s1)=pause_resume1.split(':')
                                pause_resume1=(int(h1)*3600)+(int(m1)*60)+int(s1)
                                (h1,m1,s1)=sumd.split(':')
                                sumd=(int(h1)*3600)+(int(m1)*60)+int(s1)
                                pause_resume1_final2=(pause_resume1+sumd)
                                pause_resume1_final=format(strftime("%H:%M:%S",gmtime(pause_resume1_final2)))
                                #print("values are")

                                #print(total_app_time1_final2,pause_resume1_final2,idle_time_final2)
                                woooork = int(pause_resume1_final2+idle_time_final2)
                                total_working_hours_final2=(total_app_time1_final2-woooork)
                                #print(total_working_hours_final2)
                               
                                    
                                total_working_hours_final=format(strftime("%H:%M:%S",gmtime(total_working_hours_final2)))


                                #do additions here
                                
                                cur.execute("update productivity SET total_app_time='%s',actual_idle_time='%s',pause_resume_interval='%s',total_working_hours='%s' WHERE user_id=%d AND date='%s'" %(total_app_time1_final,idle_time_final,pause_resume1_final,total_working_hours_final,Id,today))   
                                conn.commit()
        
                                
                                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                                f_handler.setFormatter(f_format)
                                logger.addHandler(f_handler)
                                logger.critical('Successfully  automatically saved to database finals--idle time'+str(idle_time_final))
                                logger.critical('Successfully automatically  saved to database finals--start time'+str(start_time1))
                                logger.critical('Successfully automatically  saved to database finals--app time'+str(total_app_time1_final))
                                logger.critical('Successfully  automatically saved to database finals--total working time'+str(total_working_hours_final))
                               

                                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                                f_handler.setFormatter(f_format)
                                logger.addHandler(f_handler)
                                logger.critical('Successfully saved to database finals')
                                #print("finALLY")
                                t_w_t_lis.clear()
                                t_a_t_lis.clear()
                                p_r_t_lis.clear()
                                i_d_t_lis.clear()
                                dif_v.clear()
                                

                                '''text="your working hours is saved successfully"
                                title="Successful"
                                ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)'''
                                #print("all parameters is",b,m,start_time1,op,pause_time)
                                
                                
                                
                            
                                break
                
                if data==[]:       #save to database if the user has used the app first time today
                             #collection3.update_one(myquery,{"$set":{today:{"Date":today,"Total_App_time":total,"Actual_Idle_time":idle_time,"Pause_Resume_Interval":sumd,"Total_Working_Hours":total_working_hrs}}})
                             cur.execute("insert into productivity (user_id,date,total_app_time,actual_idle_time,pause_resume_interval,total_working_hours) VALUES (%d,'%s','%s','%s','%s','%s')"%(Id,today,total,idle_time,sumd,total_working_hrs))
                           
                             conn.commit()
                             
                             

                             
                             f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                             f_handler.setFormatter(f_format)
                             logger.addHandler(f_handler)
                             logger.critical('Successfully  automatically saved to database finals--idle time'+str(idle_time))
                             logger.critical('Successfully  automatically saved to database finals--start time'+str(start_time1))
                             logger.critical('Successfully  automatically saved to database finals--app time'+str(total))
                             logger.critical('Successfully  automatically saved to database finals--total working time'+str(total_working_hrs))
                            
                            

                             f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                             f_handler.setFormatter(f_format)
                             logger.addHandler(f_handler)
                             logger.critical('Successfully saved to database finals')
                             #print("finALLY")
                             t_w_t_lis.clear()
                             t_a_t_lis.clear()
                             p_r_t_lis.clear()
                             i_d_t_lis.clear()
                             dif_v.clear()

                             '''text="your working hours is saved successfully"
                             title="Successful"
                             ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)'''


            except Exception as e:
                dif_v.clear()
                
                time_tt = time.strftime("%H:%M:%S", time.localtime())
                if time_tt >"3:00:00" and time_tt <"4:00:00":
                    #print("8888")
                    from datetime import date as ddd, timedelta as ttt
                    #import datetime, time
                    time_tt = time.strftime("%H:%M:%S", time.localtime())

                    yesterday = ddd.today() - ttt(days=1)
                    t_date.clear()
                    t_date.append(yesterday)
                    t_w_t_lis.clear()
                    t_a_t_lis.clear()
                    p_r_t_lis.clear()
                    i_d_t_lis.clear()
                    t_w_t_lis2.clear()
                    t_a_t_lis2.clear()
                    p_r_t_lis2.clear()
                    i_d_t_lis2.clear()
                    t_w_t_lis2.append(twt)
                    p_r_t_lis2.append(prt)
                    i_d_t_lis2.append(idt)
                    t_a_t_lis2.append(tat)
                else:
                    t_w_t_lis.clear()
                    t_a_t_lis.clear()
                    p_r_t_lis.clear()
                    i_d_t_lis.clear()
                    t_w_t_lis.append(twt)
                    p_r_t_lis.append(prt)
                    i_d_t_lis.append(idt)
                    t_a_t_lis.append(tat)
                

                        
                         
                         
                        
                       
                         

                       
      except Exception as e:
        
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.critical('Operation Page automatic saving 1 has been Crashed'+str(e))
        
        #import os
        #os.system("taskkill /f /im final_operation_page.exe")   ################# 'END TASK' of the app from task manager
 


    def go_save(self):
      global dif_v
      
      from datetime import date, timedelta
      global b,start_time1,k,j,m,op
      try:
           
            
            ##  total idle time of resume pause
            try:
                

                if t_w_t_lis2!=[]:   #checking is there any data in the list or not
                    twtt=t_w_t_lis2[0]
                    #t_w_t_lis.append(twt)
                if p_r_t_lis2!=[]:
                    prtt=p_r_t_lis2[0]
                    #p_r_t_lis.append(prt)
                if i_d_t_lis2!=[]:
                    idtt=i_d_t_lis2[0]
                    #i_d_t_lis.append(idt)
                if t_a_t_lis2!=[]:
                    tatt=t_a_t_lis2[0]
                    #t_a_t_lis.append(tat)
                #print("tat all is",tatt,prtt,idtt,twtt)
                from datetime import date as dd
                nowwwwday = dd.today()
               
                
                urlopen('http://216.58.192.142', timeout=1)
                from time import strftime
                from time import gmtime
                
                from datetime import date as ddd, timedelta as ttt
                import  time
                time_tt = time.strftime("%H:%M:%S", time.localtime())

                yesterday = ddd.today() - ttt(days=1)
                today= t_date[0]
                
                total=format(strftime("%H:%M:%S",gmtime(tatt)))
                #print(8)
                sumd=format(strftime("%H:%M:%S",gmtime(prtt)))
                #print(8)
                idle_time=format(strftime("%H:%M:%S",gmtime(idtt)))
                #print(8)
                total_working_hrs=format(strftime("%H:%M:%S",gmtime(twtt)))
               
            
                import datetime as datetime2
                conn=psycopg2.connect('')
                cur=conn.cursor()
                cur.execute( 'select * from productivity')
                data=cur.fetchall()   
                cur.execute("select * from productivity where date='%s' AND user_id=%d"%(today,Id))
                data=cur.fetchall()
                
                for ff in data:
                       
                           if ff[0] == Id:
                                

                                from datetime import date            

                                idle_time1=ff[3]                        #  ["Actual_Idle_time"]     #values from database      #idle_time
                                total_app_time1=ff[2]                   #["Total_App_time"]                                    #total
                                pause_resume1=ff[4]                     #["Pause_Resume_Interval"]                             #sumd
                                total_working_hours=ff[5]               #["Total_Working_Hours"]                               #total_working_hrs

                           
                                
                                
                                idle_time1=str(idle_time1)
                                idle_time1=datetime2.datetime.strptime(idle_time1,"%H:%M:%S") 
                                idle_time1=format(idle_time1.time())
                                
                                
                                (h1,m1,s1)=idle_time1.split(':')
                                idle_time1=(int(h1)*3600)+(int(m1)*60)+int(s1)
                                (h1,m1,s1)=idle_time.split(':')
                                idle_time=(int(h1)*3600)+(int(m1)*60)+int(s1)   
                                idle_time_final2= (idle_time1+idle_time)
                                idle_time_final=format(strftime("%H:%M:%S",gmtime(idle_time_final2))) 

                             
                                total_app_time1=str(total_app_time1)
                                total_app_time1=datetime2.datetime.strptime(total_app_time1,"%H:%M:%S")
                                total_app_time1=format(total_app_time1.time())
                                (h1,m1,s1)=total_app_time1.split(':')
                                total_app_time1=(int(h1)*3600)+(int(m1)*60)+int(s1)
                                (h1,m1,s1)=total.split(':')
                                total=(int(h1)*3600)+(int(m1)*60)+int(s1)
                                total_app_time1_final2=(total_app_time1+total)
                                total_app_time1_final=format(strftime("%H:%M:%S",gmtime(total_app_time1_final2)))
                                
                            
                                pause_resume1=str(pause_resume1)
                                pause_resume1=datetime2.datetime.strptime(pause_resume1,"%H:%M:%S")
                                pause_resume1=format(pause_resume1.time())
                                (h1,m1,s1)=pause_resume1.split(':')
                                pause_resume1=(int(h1)*3600)+(int(m1)*60)+int(s1)
                                (h1,m1,s1)=sumd.split(':')
                                sumd=(int(h1)*3600)+(int(m1)*60)+int(s1)
                                pause_resume1_final2=(pause_resume1+sumd)
                                pause_resume1_final=format(strftime("%H:%M:%S",gmtime(pause_resume1_final2)))

                                #print(total_app_time1_final2,pause_resume1_final2,idle_time_final2)
                                woooork = int(pause_resume1_final2+idle_time_final2)
                                total_working_hours_final2=(total_app_time1_final2-woooork)
                                #print("total_working_hours_final2 go save",total_working_hours_final2)
                                
                                total_working_hours_final=format(strftime("%H:%M:%S",gmtime(total_working_hours_final2)))


                                
                                cur.execute("update productivity SET total_app_time='%s',actual_idle_time='%s',pause_resume_interval='%s',total_working_hours='%s' WHERE user_id=%d AND date='%s'" %(total_app_time1_final,idle_time_final,pause_resume1_final,total_working_hours_final,Id,today))   
                                conn.commit()
        
                                
                                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                                f_handler.setFormatter(f_format)
                                logger.addHandler(f_handler)
                                logger.critical('Successfully automatically saved to database finals--idle time'+str(idle_time_final))
                                logger.critical('Successfully automatically saved to database finals--start time'+str(start_time1))
                                logger.critical('Successfully automatically saved to database finals--app time'+str(total_app_time1_final))
                                logger.critical('Successfully automatically saved to database finals--total working time'+str(total_working_hours_final))
                                

                                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                                f_handler.setFormatter(f_format)
                                logger.addHandler(f_handler)
                                logger.critical('Successfully saved to database finals')
                                #print("gosave finALLY")

                                '''text="your working hours is saved successfully"
                                title="Successful"
                                ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)'''
                                #print("all parameters is",b,m,start_time1,op,pause_time)
                                dif_v.clear()
                                t_w_t_lis2.clear()
                                t_a_t_lis2.clear()
                                p_r_t_lis2.clear()
                                i_d_t_lis2.clear()
                                            
                            
                                break
                
                if data==[]:       #save to database if the user has used the app first time today
                             cur.execute("insert into productivity (user_id,date,total_app_time,actual_idle_time,pause_resume_interval,total_working_hours) VALUES (%d,'%s','%s','%s','%s','%s')"%(Id,today,total,idle_time,sumd,total_working_hrs))
                           
                             conn.commit()
                             
                             
                             
                             f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                             f_handler.setFormatter(f_format)
                             logger.addHandler(f_handler)
                             logger.critical('Successfully automatically  saved to database finals--idle time'+str(idle_time))
                             logger.critical('Successfully  automatically saved to database finals--start time'+str(start_time1))
                             logger.critical('Successfully  automatically saved to database finals--app time'+str(total))
                             logger.critical('Successfully  automatically saved to database finals--total working time'+str(total_working_hrs))
                             
                             f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                             f_handler.setFormatter(f_format)
                             logger.addHandler(f_handler)
                             logger.critical('Successfully saved to database finals')
                             #print("finALLY")
                             dif_v.clear()
                             t_w_t_lis2.clear()
                             t_a_t_lis2.clear()
                             p_r_t_lis2.clear()
                             i_d_t_lis2.clear()

                             
                

            except Exception as e:
                #print("exception in go save1")
                #print(e)
                dif_v.clear()
                
                         
                         
                        
                       
                         

                       
      except Exception as e:
        
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.critical('Operation Page automatic saving2 has been Crashed'+str(e))
        


    def search_option(self):
                  
                tabUrl="http://google.com/search?q="
                term = self.lineEdit.text()
                webbrowser.open(tabUrl+term,new=2)
                
    def lms_portal_link(self):
        webbrowser.open("https://athrvedoperationalportal.herokuapp.com",new=2)
    def youtube_link(self):
        webbrowser.open("https://www.youtube.com/",new=2)
    def gmail_link(self):
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox",new=2)
    def chat_app(self):
        webbrowser.open("https://athrvedchattesting.herokuapp.com/",new=2)
        
        
    def dark_mode_or_light_menubar(self):
        conn=psycopg2.connect('')           #PSQL Database link
        cur=conn.cursor()
        cur.execute("select dark_or_light_mode from mac_address where users_id='%s'"%(mainID))
        dark_light_mode2=cur.fetchone()
       
   
        
        if dark_light_mode2[0]=="ON":
            
            cur.execute("update mac_address SET dark_or_light_mode='OFF' WHERE users_id='%s'"%(mainID))
            
            cur.execute("select dark_or_light_mode from mac_address where users_id='%s'"%(mainID))
            dark_light_mode2=cur.fetchone()
            conn.commit()
            #print(dark_light_mode2[0])
            
            self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.label_21.setStyleSheet("background-color:rgb(255, 255, 255);")   #mmmmmmmmmmmmmm

            self.label_5.setStyleSheet("color: black;")
            self.label_6.setStyleSheet("color: black;")
            self.label_8.setStyleSheet("color: blue;")
            self.label_11.setStyleSheet("color:blue;")
            self.label_16.setStyleSheet("color: blue;")
            self.label_2.setStyleSheet("color: black;")

            
            operations.setStyleSheet("background-color:rgb(255, 255, 255);")
            operations.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(operations)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 26))
            self.menubar.setObjectName("menubar")
            self.menuEdit = QtWidgets.QMenu(self.menubar)
            self.menuEdit.setObjectName("menuEdit")
            #print("su")
            self.menuEdit.setStyleSheet("color: black;")
            self.menuExtra_features = QtWidgets.QMenu(self.menubar)
            self.menuExtra_features.setObjectName("menuExtra_features")
            self.menuExtra_features.setStyleSheet("color: black;")
        
            self.menubar.setStyleSheet("color: black;"" background-color:white;") #mmmmmm adding colour to menubar

            
        else:
            cur.execute("update mac_address set dark_or_light_mode='ON' WHERE users_id='%s'"%(mainID))
            conn.commit()

            self.label.setStyleSheet("background-color: gray);")
            self.label_21.setStyleSheet("background-color:gray;")   #mmmmmmmmmmmmmm

            operations.setStyleSheet("background-color:gray;")
            operations.setCentralWidget(self.centralwidget)
            self.label_8.setStyleSheet("color: blue;")
            
            self.label_2.setStyleSheet("color: rgb(255, 255, 255);")#"background-color:gray;")
            
            self.label_11.setStyleSheet("color:yellow;")#"background-color:gray;")
            self.label_16.setStyleSheet("color: yellow;")#"background-color:gray;")
            
            self.label_5.setStyleSheet("color: white;")
            self.label_6.setStyleSheet("color: white;")

            operations.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(operations)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 26))
            self.menubar.setObjectName("menubar")
            self.menuEdit = QtWidgets.QMenu(self.menubar)
            self.menuEdit.setObjectName("menuEdit")
            #print("su")
            self.menuEdit.setStyleSheet("color: white;")
            self.menuExtra_features = QtWidgets.QMenu(self.menubar)
            self.menuExtra_features.setObjectName("menuExtra_features")
            self.menuExtra_features.setStyleSheet("color: white;")
            self.menubar.setStyleSheet("color: white;"" background-color:gray;") #adding colour to menubar
            
            
        
    def reading_mode_idle_time(self):
        if reading_mode[0] == 0 :            # reading mode will become ON after clicked
            f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')             
            f_handler.setFormatter(f_format)
            logger.addHandler(f_handler)
            logger.warning('user has enabled reading mode')
            
            _translate = QtCore.QCoreApplication.translate
            self.pushButton_2.setText(_translate("operations","Reading Mode ON"))
            self.pushButton_2.setStatusTip(_translate("operations","Reading mode is ON"))
            reading_mode.clear()
            reading_mode.append(1)
            self.pushButton_2.setStyleSheet("border-radius:10px;\n" "background-color: green;\n" "color: rgb(255, 255, 255)")

            msg = QMessageBox()
            msg.setWindowTitle("Reading mode")
            msg.setText("Reading Mode is ON")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

        else:                                               # reading mode will become OFF after clicked
            f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')           
            f_handler.setFormatter(f_format)
            logger.addHandler(f_handler)
            logger.warning('Reading mode turned off')
            
            _translate = QtCore.QCoreApplication.translate
            self.pushButton_2.setStatusTip(_translate("operations","Reading mode is OFF"))
            self.pushButton_2.setText(_translate("operations","Reading Mode OFF"))
            reading_mode.clear()
            reading_mode.append(0)
            self.pushButton_2.setStyleSheet("border-radius:10px;\n""background-color: rgb(85, 170, 255);")

            msg = QMessageBox()
            msg.setWindowTitle("Reading mode")
            msg.setText("Reading Mode is OFF")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
    
    def log100_chrome_idle_time(self):   # idle time is equal to chrome idle time then message box appears      
        
            try:
                text="Click OK to prove your presence"
                title="Verification"
                ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)
                
            except Exception as e:
                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')           
                f_handler.setFormatter(f_format)
                logger.addHandler(f_handler)
                logger.warning('browser was idle but unsuccessfull ,'+(str(e)))
                
            
                                       
    def log100(self):                   #idle time calculation
                
                import random
                random_for_chrome_idle_time=random.randint(0,5)
                rf_chrome=int(random_for_chrome_idle_time)+int(8)
                
                rf_chrome=rf_chrome*60
               
                
                class LASTINPUTINFO(Structure):
                                _fields_ = [
                                    ('cbSize', c_uint),
                                    ('dwTime', c_uint),
                                ]
                def get_idle_duration():
                    lastInputInfo = LASTINPUTINFO()
                    lastInputInfo.cbSize = sizeof(lastInputInfo)
                    windll.user32.GetLastInputInfo(byref(lastInputInfo))
                    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
                    return millis / 1000.0
               
                t=0
                process_time={}
                timestamp = {}
                bro_screen_no=0#mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
                global a
                a=[0]
                
                while True:
                  
                  from datetime import datetime #as datetime3
                 
                  datetimeFormat = '%Y-%m-%d %H:%M:%S'
                  date1 = str(start_time1)
                  date2 = str( datetime.now().replace(microsecond=0))
                  diff = datetime.strptime(date2, datetimeFormat)\
                    - datetime.strptime(date1, datetimeFormat)
                  
                  if str(diff) >="1:00:00" and dif_v==[]:
                    #global dif_v
                    dif_v.append(0)
                    
                    
                    tttt = threading.Thread(target=self.auto_save)#(b,m,op,start_time1,pause_time,k,today))
                    tttt.start()
                    
                  if bro_screen_no == bro_screen[0]:       #screenshot with idle time(combined)
                      
                      bro_screen_no=0
                      t_screen = threading.Thread(target=self.log)
                      t_screen.start()
                  bro_screen_no=int(bro_screen_no)+1
                  
                  
                  if op[0]==0 or op[0]==1:
                       try:
                         import time
                         current_app = psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]).name().replace(".exe", "")
                         timestamp[current_app] = int(time.time())
                         time.sleep(1)
                         if current_app not in process_time.keys():
                                     process_time[current_app] = 0
                         process_time[current_app] = process_time[current_app]+int(time.time())-timestamp[current_app]
                          
                         
                         if current_app=="explorer":    #or current_app=="ApplicationFrameHost":    #if the user is not working
                                #print("current app explorer is running")
                                GetLastInputInfo = int(get_idle_duration())
                                if GetLastInputInfo>=0:
                                        a.extend([GetLastInputInfo])
                                        #print("a is in current app 1st if ",a)
                                     
                                if  GetLastInputInfo>=0 :
                                    #print("last input info is running")
                                    y=GetLastInputInfo+1
                                    #print("b is",b)
                                    x=int(b[0])
                                    x=x+1
                                    #print("x is",x)
                                    b.clear()
                                    b.append(x)
                                    #print("this is the total idle time =="+ (str(b)))                 # total idle time save this to database 
                         
                         else:
                            
                            GetLastInputInfo = int(get_idle_duration())
                            #print("get last input info is",GetLastInputInfo)
                            if (GetLastInputInfo==0) and (a[-2]>=(int(rf_chrome)+9)) and (current_app=="chrome" or current_app =="opera" or current_app=="ApplicationFrameHost" or current_app=="msedge") :  #if last but one value is greater
                                                                                                                                    #than the chrome idle time value then it is idle time
                                          #print("inside of some chrome condition")                                                                         
                                          a.extend([GetLastInputInfo])
                                          #print("a in inside is",a)
                                          c=int(a[-2])                                                              #after final verification change it to 60   
                                          d=int(b[0])
                                          d=d+c
                                          b.clear()
                                          b.append(d)
                                          #print("b is",b)
                                         
                               
                            elif (GetLastInputInfo == rf_chrome) and (current_app=="chrome" or current_app =="opera" or current_app=="ApplicationFrameHost" or current_app=="msedge") :
                                #print("GetLastInputInfo=rf_chrome is running")
                                if GetLastInputInfo>=0:
                                        a.extend([GetLastInputInfo])
                                        #print("a after GetLastInputInfo=rf_chrome",a)
                                t6 = threading.Thread(target=self.log100_chrome_idle_time)
                                t6.start()
                                # idle time is equal to chrome idle time then message box appears                                    
                                
                            
                            elif (GetLastInputInfo >= rf_chrome ) and (current_app=="chrome" or current_app =="opera" or current_app=="ApplicationFrameHost" or current_app=="msedge") :
                                #print("GetLastInputInfo>=rf_chrome is running")
                                if GetLastInputInfo>=0:
                                        a.extend([GetLastInputInfo])

                             
                            
                                    
                                                              
                            elif op[0]==1:
                                #print("in elif part op[0]==1 is running")
                                if GetLastInputInfo>=0:
                                        a.extend([GetLastInputInfo])
                                        #print("else op[0] a is",a)

                                if  GetLastInputInfo==0 :
                                    c=int(a[-2])
                                    if c >=0:                                            #after final verification change it to 25 
                                           
                                            d=int(b[0]) 
                                            d=d+c
                                            b.clear()
                                            b.append(d)

                                      
                            elif reading_mode[0]==0 :   #reading mode off and no browser
                                
                                if GetLastInputInfo>=0:
                                       
                                        a.extend([GetLastInputInfo])
                                        

                                if  GetLastInputInfo==0 :
                                    #print("if condition of getlastinput==0")
                                    c=int(a[-2])
                                    #print("c inside of getlastinput is",c)
                                    if c >=120:                                            #after final verification change it to 25 
                                            
                                            d=int(b[0])
                                            
                                            d=d+c
                                            b.clear()
                                            b.append(d)

                               
                            else:                                                #if reading mode is on
                                 
                                if GetLastInputInfo>=0:
                                        a.extend([GetLastInputInfo])
                                        

                                if  GetLastInputInfo==0 :
                                    #print("else part of if condition of getlastinput==0")
                                    c=int(a[-2])
                                    #print("c of if of else is",c)
                                    if c >=120:                                      #after final verification change it to 120
                                        
                                            d=int(b[0])
                                            d=d+c
                                            b.clear()
                                            b.append(d)
                                            #print("b is at the last line is",b)
                                            
                            
                            if idle_in_sleep_mode[0]==1:            #sleep mode (psutil.error....).calculating the sleep time
                                from datetime import datetime
                                import datetime as datetime2
                                #import time
                                end_time_in_idle = datetime.now().replace(microsecond=0)
                                
                                
                                total_idle_in_sleep=end_time_in_idle-start_time_in_idle

                                
                                f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                                f_handler.setFormatter(f_format)
                                logger.addHandler(f_handler)
                                logger.critical('idle time except end_time_in_idle'+str(end_time_in_idle))
                                logger.critical('idle time except total_idle_in_sleep'+str(total_idle_in_sleep))
                                
                                 
                                idle_in_sleep_mode.clear()
                                idle_in_sleep_mode.append(0)

                                total_idle_in_sleep=str(total_idle_in_sleep)
                                total_idle_in_sleep=datetime2.datetime.strptime(total_idle_in_sleep,"%H:%M:%S")
                                total_idle_in_sleep=format(total_idle_in_sleep.time())
                                (h1,m1,s1)=total_idle_in_sleep.split(':')
                                total_idle_in_sleep=(int(h1)*3600)+(int(m1)*60)+int(s1)
                                
                                if total_idle_in_sleep>=0:
                                    
                                    e=int(b[0])
                                    e=e+total_idle_in_sleep
                                    b.clear()
                                    b.append(e)
                                    a.clear()
                                    a.append(0)
                                    a.append(0)
                       
                           
                       except Exception as e:
                          #print("exception of idle time",e)
                          e=str(e)
                          
                          f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                          f_handler.setFormatter(f_format)
                          logger.addHandler(f_handler)
                          logger.critical('idle time exception'+str(e))
        
                          if "list index out of range" in e:
                              print("ignore exception")
                              
                          elif idle_in_sleep_mode[0]==0:           #sleep mode (psutil.error....).calculating the sleep time
                              from datetime import datetime
                              start_time_in_idle = datetime.now().replace(microsecond=0)
                              
                              f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                              f_handler.setFormatter(f_format)
                              logger.addHandler(f_handler)
                              logger.critical('idle time except start_time_in_idle'+str(start_time_in_idle))
                              
                              if a[-1]>=120:
                                  e=int(b[0])
                                  e=e+a[0]
                                  b.clear()
                                  b.append(e)
                                  a.clear()
                                  a.append(0)
                                  a.append(0)
                              else:
                                  a.clear()
                                  a.append(0)
                                  a.append(0)
                                  
                              idle_in_sleep_mode.clear()
                              idle_in_sleep_mode.append(1)
                          else:
                              
                              a.clear()
                              a.append(0)
                              a.append(0)
                          mok=1
                       t+=1
                       
                  else:
                      break


   
    
    def vs(self):
        t = threading.Thread(target=self.log5)
        t.start()

    def log5(self):
      try:
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap("VS.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vscode.setIcon(icon25)
        #print(1)
        self.vscode.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")

        from datetime import datetime
        #self.vscode.setStyleSheet("background-color: lightgray;")
        start_time = datetime.now()
        cluster = MongoClient("")       #MongoDB Database link
        
        db = cluster["test"]
        collection2=db["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainId
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('user opened VS')

        icon25= QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vscode.setIcon(icon25)
        
        self.vscode.setStyleSheet("background:none;""background-color: transparent;")
        from datetime import datetime
        # do your work here
        try:
           subprocess.call([x["path_of_Visual studio"]],shell=True)
        except:
                text="Check the location added and Try again"
                title="Verification"
                ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)
                
           
        end_time = datetime.now()
        vscode=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"VS_code":vscode}}})
      except:
        self.vscode.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)


    def android(self):
        t = threading.Thread(target=self.log6)
        t.start()

    def log6(self):
      try:
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap("Android.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.androidstudio.setIcon(icon26)
        #print(1)
        self.androidstudio.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.androidstudio.setStyleSheet("background-color: lightgray;")
        from datetime import datetime
        start_time = datetime.now()
        cluster = MongoClient("")       #MongoDB Database link
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainID
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('User opened android studio')

        icon26= QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.androidstudio.setIcon(icon26)
        
        self.androidstudio.setStyleSheet("background:none;""background-color: transparent;")

        # do your work here
        try:
           subprocess.call([x["path_of_Android studio"]],shell=True)
        except:
                text="Check the location added and Try again"
                title="Verification"
                ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)
                
        end_time = datetime.now()
        android=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Android":android}}})
      except:
        self.androidstudio.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)


    def premier(self):
        t = threading.Thread(target=self.log7)
        t.start()

    def log7(self):
      try:
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap("Adobe_Premiere_Pro_Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.premierpro.setIcon(icon27)
        #print(1)
        self.premierpro.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
       
        from datetime import datetime
        start_time = datetime.now()
        cluster = MongoClient("")           #MongoDB Database link
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainID
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('User opened Adobe Premier Pro')

        icon27= QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.premierpro.setIcon(icon27)
        
        self.premierpro.setStyleSheet("background:none;""background-color: transparent;")

        # do your work here
        
        subprocess.call([x["path_of_Premier pro"]],shell=True)
        
                
        end_time = datetime.now()
        premier=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Premier_pro":premier}}})
      except:
        self.premierpro.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)


    def pych(self):
        t = threading.Thread(target=self.log8)
        t.start()

    def log8(self):
      try:
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap("Py_Charm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pycharm.setIcon(icon28)
        #print(1)
        self.pycharm.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.pycharm.setStyleSheet("background-color: lightgray;")
        from datetime import datetime
        start_time = datetime.now()
        cluster = MongoClient("")       #MongoDB Database link
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainID
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('User opened Pycharm')
        
        icon28= QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pycharm.setIcon(icon28)
        
        self.pycharm.setStyleSheet("background:none;""background-color: transparent;")
        from datetime import datetime
        
        # do your work here
        subprocess.call([x["path_of_Phycharm"]],shell=True)
        end_time = datetime.now()
        phycharm=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Pycharm":phycharm}}})
      except:
        self.pycharm.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)



    def photo(self):
        t = threading.Thread(target=self.log9)
        t.start()

    def log9(self):
      try:
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap("Photoshop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.photoshop.setIcon(icon29)
        #print(1)
        self.photoshop.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.photoshop.setStyleSheet("background-color: lightgray;")
        from datetime import datetime
        start_time = datetime.now()
        cluster = MongoClient("")       #MongoDB Database link
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainID
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('User opened Adobe Photoshop')

        icon29= QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.photoshop.setIcon(icon29)
        
        self.photoshop.setStyleSheet("background:none;""background-color: transparent;")
        from datetime import datetime
        # do your work here
        subprocess.call([x["path_of_Photoshop"]],shell=True)
        end_time = datetime.now()
        photoshop=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Photoshop":photoshop}}})
      except:
        self.photoshop.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)



    def tabl(self):
        t = threading.Thread(target=self.log10)
        t.start()

    def log10(self):
      try:
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap("Tablaeu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tableau.setIcon(icon30)
        #print(1)
        self.tableau.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.tableau.setStyleSheet("background-color: lightgray;")
        start_time = datetime.now()
        cluster = MongoClient("")       #MongoDB Database link
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainID
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('User opened Tableu')

        icon30= QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tableau.setIcon(icon30)
        
        self.tableau.setStyleSheet("background:none;""background-color: transparent;")

        # do your work here
        subprocess.call([x["path_of_Tableau"]],shell=True)
        end_time = datetime.now()
        tableau=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Tableau":tableau}}})
      except:
        self.tableau.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)

 
    def fig(self):
        t = threading.Thread(target=self.log11)
        t.start()

    def log11(self):
      try:
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap("FigmaLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.figma.setIcon(icon31)
        #print(1)
        self.figma.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")        #self.figma.setStyleSheet("background-color: lightgray;")

        from datetime import datetime
        start_time = datetime.now()
        cluster = MongoClient("")       #PSQL Database link
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainID
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('User opened Figma')

        icon31= QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.figma.setIcon(icon31)
        
        self.figma.setStyleSheet("background:none;""background-color: transparent;")

        # do your work here
        from datetime import datetime
        subprocess.call([x["path_of_Figma"]],shell=True)
        end_time = datetime.now()
        figma=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Figma":figma}}})
      except:
        self.figma.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)


    def idl(self):
        t = threading.Thread(target=self.log12)
        t.start()

    def log12(self):
        
        try:
            icon32= QtGui.QIcon()
            icon32.addPixmap(QtGui.QPixmap("python.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.idle.setIcon(icon32)
            #print(1)
            #self.idle.setStyleSheet("background-color:blue;")
           
            self.idle.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
            
            from datetime import datetime
            start_time = datetime.now()
            cluster = MongoClient("")           #MongoDB Database link
            db = cluster["test"]
            collection=db["Locations"]
            collection2=db["Time tracking"]
            global mainID
            Id= mainID
            myquery={"_id":Id}
            x=collection.find_one(myquery)
            f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            f_handler.setFormatter(f_format)
            logger.addHandler(f_handler)
            logger.warning('User opened Idle Python')

            #self.idle.setStyleSheet("background-color:transparent;")###mmmmm
            icon32= QtGui.QIcon()
            icon32.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
            self.idle.setIcon(icon32)                 #mmmmmmmmmm
            
            self.idle.setStyleSheet("background:none;""background-color: transparent;")
            
            # do your work here
            #import subprocess
            subprocess.call([x["path_of_Idle"]],shell=True)
            
            from datetime import datetime
            end_time = datetime.now()
          
            idle=format(end_time - start_time)
           
            collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Idle_python":idle}}})
            
        except Exception as e:
            #print(e)
            self.idle.setStyleSheet("background:none;""background-color: transparent;")
            text="Check the internet connection"
            title="Unsuccessful"
            ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)


           
    def ardu(self):
        t = threading.Thread(target=self.log13)
        t.start()

    def log13(self):
      try:
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap("ardiuno.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ardiuno.setIcon(icon33)
        #print(1)
        self.ardiuno.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.ardiuno.setStyleSheet("background-color: lightgray;")
        from datetime import datetime
        start_time = datetime.now()
        cluster = MongoClient("")       #MongoDB Database link
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainID
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('User opened Arduino Uno')

        icon33= QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ardiuno.setIcon(icon33)
        
        self.ardiuno.setStyleSheet("background:none;""background-color: transparent;")

        # do your work here
        from datetime import datetime
        subprocess.call([x["path_of_Arduino illustrator"]],shell=True)
        end_time = datetime.now()
        arduino=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Arduino":arduino}}})
      except:
        self.ardiuno.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)


    def illus(self):
        t = threading.Thread(target=self.log14)
        t.start()

    def log14(self):
      try:
        icon34 = QtGui.QIcon()
        icon34.addPixmap(QtGui.QPixmap("AI.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.illustrator.setIcon(icon34)
        #print(1)
        self.illustrator.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.illustrator.setStyleSheet("background-color: lightgray;")
        from datetime import datetime
        start_time = datetime.now()
        cluster = MongoClient("")       #MongoDB Database link
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainID
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('User opened Adobe Illustrator')

        icon34= QtGui.QIcon()
        icon34.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.illustrator.setIcon(icon34)
        
        self.illustrator.setStyleSheet("background:none;""background-color: transparent;")

        # do your work here
        from datetime import datetime
        subprocess.call([x["path_of_Adobe illustrator"]],shell=True)
        end_time = datetime.now()
        illustrator=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Adobe_illustrator":illustrator}}})
      except:
        self.illustrator.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)



    def wp(self):
        t = threading.Thread(target=self.log15)
        t.start()

    def log15(self):
      try:
        icon35 = QtGui.QIcon()
        icon35.addPixmap(QtGui.QPixmap("wps.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.wps.setIcon(icon35)
        #print(1)
        self.wps.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.wps.setStyleSheet("background-color: lightgray;")
        from datetime import datetime
        start_time = datetime.now()
        cluster = MongoClient("")              #MongoDB Database link
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainID
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('User opened WPS Office')

        icon35= QtGui.QIcon()
        icon35.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.wps.setIcon(icon35)
        
        self.wps.setStyleSheet("background:none;""background-color: transparent;")

        # do your work here
        from datetime import datetime
        subprocess.call([x["path_of_Wps_office"]],shell=True)
        end_time = datetime.now()
        wps_office=format(end_time - start_time)
        
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"WPS_office":wps_office}}})
      except:
        self.wps.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)


        
    def Qtdes(self):
        t = threading.Thread(target=self.log16)
        t.start()

    def log16(self):
      try:
        icon36 = QtGui.QIcon()
        icon36.addPixmap(QtGui.QPixmap("qtdesigner.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Qtdesigner.setIcon(icon36)
        #print(1)
        self.Qtdesigner.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.Qtdesigner.setStyleSheet("background-color: lightgray;")
        from datetime import datetime
        start_time = datetime.now()
        cluster = MongoClient("")              #MongoDB Database link
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainID
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('User opened Qt Designer')

        icon36= QtGui.QIcon()
        icon36.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Qtdesigner.setIcon(icon36)
        
        self.Qtdesigner.setStyleSheet("background:none;""background-color: transparent;")

        # do your work here
        from datetime import datetime
        subprocess.call([x["path_of_Qt designer"]],shell=True)
        end_time = datetime.now()
        qtdesign=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Qtdesigner":qtdesign}}})
      except:
        self.Qtdesigner.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)


    def prot(self):
        t = threading.Thread(target=self.log17)
        t.start()

    def log17(self):
      try:
        icon37 = QtGui.QIcon()
        icon37.addPixmap(QtGui.QPixmap("Proteus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.proteus.setIcon(icon37)
        #print(1)
        self.proteus.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.proteus.setStyleSheet("background-color: lightgray;")
        from datetime import datetime
        start_time = datetime.now()
        cluster = MongoClient("")              #MongoDB Database link
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainID
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('User opened Proteus')

        icon37= QtGui.QIcon()
        icon37.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.proteus.setIcon(icon37)
        
        self.proteus.setStyleSheet("background:none;""background-color: transparent;")

        # do your work here
        from datetime import datetime
        subprocess.call([x["path_of_Proteus"]],shell=True)
        end_time = datetime.now()
        proteus=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Proteus":proteus}}})
      except:
        self.proteus.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)


    def aftere(self):
        t = threading.Thread(target=self.log18)
        t.start()

    def log18(self):
      try:
        icon38 = QtGui.QIcon()
        icon38.addPixmap(QtGui.QPixmap("Adobe_After_Effects_Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aftereffects.setIcon(icon38)
        #print(1)
        self.aftereffects.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.aftereffects.setStyleSheet("background-color: lightgray;")
        from datetime import datetime
        start_time = datetime.now()
        cluster = MongoClient("")       #MongoDB Database link
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainID
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('User opened Adobe AfterEffects')
        
        icon38= QtGui.QIcon()
        icon38.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aftereffects.setIcon(icon38)
        
        self.aftereffects.setStyleSheet("background:none;""background-color: transparent;")
        
        # do your work here
        from datetime import datetime
        subprocess.call([x["path_of_After effects"]],shell=True)
        end_time = datetime.now()
        After_effects=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"After_effects":After_effects}}})
      except:
        self.aftereffects.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)


    def code(self):
        t = threading.Thread(target=self.log19)
        t.start()

    def log19(self):
      try:
        icon39 = QtGui.QIcon()
        icon39.addPixmap(QtGui.QPixmap("Code.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.codeblocks.setIcon(icon39)
        #print(1)
        self.codeblocks.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.codeblocks.setStyleSheet("background-color: lightgray;")
        from datetime import datetime
        start_time = datetime.now()
        cluster = MongoClient("")       #MongoDB Database link
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time_tracking"]
        global mainID
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('User opened CodeBlocks')

        icon39= QtGui.QIcon()
        icon39.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.codeblocks.setIcon(icon39)
        
        self.codeblocks.setStyleSheet("background:none;""background-color: transparent;")
        
        from datetime import datetime
        subprocess.call([x["path_of_Code blocks"]],shell=True)
        end_time = datetime.now()
        code_block=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Code blocks":code_block}}})   
      except:
        self.codeblocks.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)


    def solid(self):
        t = threading.Thread(target=self.log20)
        t.start()
        
    def log20(self):
      try:
        icon40 = QtGui.QIcon()
        icon40.addPixmap(QtGui.QPixmap("sw.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.solidworks.setIcon(icon40)
        #print(1)
        self.solidworks.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.solidworks.setStyleSheet("background-color: lightgray;")
        from datetime import datetime
        start_time = datetime.now()
        cluster = MongoClient("")       #MongoDB Database link
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainID
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('User opened SolidWorks')

        icon40= QtGui.QIcon()
        icon40.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.solidworks.setIcon(icon40)
        
        self.solidworks.setStyleSheet("background:none;""background-color: transparent;")
        from datetime import datetime
        subprocess.call([x["path_of_Solid works"]],shell=True)
        end_time = datetime.now()
        solid_work=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Solid works":solid_work}}})
      except:
        self.solidworks.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)



    def wod(self):
        t = threading.Thread(target=self.log61)
        t.start()
        

    def log61(self):
      try:
        icon41 = QtGui.QIcon()
        icon41.addPixmap(QtGui.QPixmap("word.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.word.setIcon(icon41)
        #print(1)
        self.word.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.word.setStyleSheet("background-color: lightgray;")
        from datetime import datetime
        start_time = datetime.now()
        cluster = MongoClient("")              #MongoDB Database link
        
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainId
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('user opened word')

        icon41= QtGui.QIcon()
        icon41.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.word.setIcon(icon41)
        
        self.word.setStyleSheet("background:none;""background-color: transparent;")

        # do your work here
        from datetime import datetime
        subprocess.call([x["path _of_word"]],shell=True)
        end_time = datetime.now()
        word=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Word":word}}})
      except:
        self.word.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)



    def excel(self):
        t = threading.Thread(target=self.log62)
        t.start()
        

    def log62(self):
      try:
        icon42 = QtGui.QIcon()
        icon42.addPixmap(QtGui.QPixmap("Excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MS_Excel.setIcon(icon42)
        #print(1)
        self.MS_Excel.setStyleSheet("border:10px solid;""background:none;""background-color: blue;""border-color:red;")
        
        #self.MS_Excel.setStyleSheet("background-color: lightgray;")
        from datetime import datetime
        start_time = datetime.now()
        cluster = MongoClient("")       #MongoDB Database link
        
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainId
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('user opened excel')

        icon42= QtGui.QIcon()
        icon42.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MS_Excel.setIcon(icon42)
        
        self.MS_Excel.setStyleSheet("background:none;""background-color: transparent;")

        # do your work here
        from datetime import datetime
        subprocess.call([x["path_of_excel"]],shell=True)
        end_time = datetime.now()
        excel=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Excel":excel}}})
      except:
        self.MS_Excel.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)


    def power(self):
        t = threading.Thread(target=self.log63)
        t.start()
        

    def log63(self):
      try:
        icon43 = QtGui.QIcon()
        icon43.addPixmap(QtGui.QPixmap("powerpoint.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MS_Powerpoint.setIcon(icon43)
        #print(1)
        self.MS_Powerpoint.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.MS_Powerpoint.setStyleSheet("background-color: lightgray;")
        from datetime import datetime
        start_time = datetime.now()
        cluster = MongoClient("")       #MongoDB Database link
        
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainId
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('user opened powerpoint')

        icon43= QtGui.QIcon()
        icon43.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MS_Powerpoint.setIcon(icon43)
        
        self.MS_Powerpoint.setStyleSheet("background:none;""background-color: transparent;")

        # do your work here
        from datetime import datetime
        subprocess.call([x["path_of_powerpoint"]],shell=True)
        end_time = datetime.now()
        ppt=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"powerpoint":ppt}}})
      except:
        self.MS_Powerpoint.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)




    def edge(self):
        t = threading.Thread(target=self.log64)
        t.start()
        

    def log64(self):
      try:
        icon44 = QtGui.QIcon()
        icon44.addPixmap(QtGui.QPixmap("edge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Microsoft_Edge.setIcon(icon44)
        #print(1)
        self.Microsoft_Edge.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.Microsoft_Edge.setStyleSheet("background-color: lightgray;")
        from datetime import datetime
        start_time = datetime.now()
        cluster = MongoClient("")              #MongoDB Database link
        
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainId
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('user opened microsoft_edge')

        icon44= QtGui.QIcon()
        icon44.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Microsoft_Edge.setIcon(icon44)
        
        self.Microsoft_Edge.setStyleSheet("background:none;""background-color: transparent;")
        
        
        subprocess.call([x["path_of_edge"]],shell=True)
        
        from datetime import datetime
        
        end_time = datetime.now()
        
        ms_edge=format(end_time - start_time)
        
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"microsoft_edge":ms_edge}}})
        

      except:
        self.Microsoft_Edge.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)

  

    def Tmv(self):
        t = threading.Thread(target=self.log65)
        t.start()
        

    def log65(self):
      try:
        icon45 = QtGui.QIcon()
        icon45.addPixmap(QtGui.QPixmap("teamviewer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Team_viewer.setIcon(icon45)
        #print(1)
        self.Team_viewer.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.Team_viewer.setStyleSheet("background-color: lightgray;")
        from datetime import datetime
        start_time = datetime.now()
        cluster = MongoClient("")              #MongoDB Database link
        
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainId
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('user opened team_viewer')

        icon45= QtGui.QIcon()
        icon45.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Team_viewer.setIcon(icon45)
        
        self.Team_viewer.setStyleSheet("background:none;""background-color: transparent;")

        # do your work here
        from datetime import datetime
        subprocess.call([x["path_of_team_viewer"]],shell=True)
        end_time = datetime.now()
        tview=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Team_viewer":tview}}})

      except:
        self.Team_viewer.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)




    def jio(self):
        t = threading.Thread(target=self.log66)
        t.start()
        

    def log66(self):
      try:
        icon46 = QtGui.QIcon()
        icon46.addPixmap(QtGui.QPixmap("Jio_Meet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Jio_meet.setIcon(icon46)
        #print(1)
        self.Jio_meet.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.Jio_meet.setStyleSheet("background-color: lightgray;")
        from datetime import datetime
        start_time = datetime.now()
        cluster = MongoClient("")              #MongoDB Database link
        
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainId
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('user opened jio_meet')

        icon46= QtGui.QIcon()
        icon46.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Jio_meet.setIcon(icon46)
        
        self.Jio_meet.setStyleSheet("background:none;""background-color: transparent;")

        # do your work here
        from datetime import datetime
        subprocess.call([x["path_of_jio_meet"]],shell=True)
        end_time = datetime.now()
        meet=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Jio_meet":meet}}})

      except:
        self.Jio_meet.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)




    def dis(self):
        t = threading.Thread(target=self.log67)
        t.start()
        

    def log67(self):
      try:
        icon47 = QtGui.QIcon()
        icon47.addPixmap(QtGui.QPixmap("Discord.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Discord.setIcon(icon47)
        #print(1)
        self.Discord.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.Discord.setStyleSheet("background-color: lightgray;")
        from datetime import datetime
        start_time = datetime.now()
        cluster = MongoClient("")              #MongoDB Database link
        
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainId
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('user opened discord')

        icon47= QtGui.QIcon()
        icon47.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Discord.setIcon(icon47)
        
        self.Discord.setStyleSheet("background:none;""background-color: transparent;")

        # do your work here
        from datetime import datetime
        subprocess.call([x["path_of_discord"]],shell=True)
        end_time = datetime.now()
        dcord=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Discord":dcord}}})

      except:
        self.Discord.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)


    def whatsapp(self):
        t = threading.Thread(target=self.log68)
        t.start()
        

    def log68(self):
      try:
        icon48 = QtGui.QIcon()
        icon48.addPixmap(QtGui.QPixmap("whatsapp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Whatsapp.setIcon(icon48)
        #print(1)
        self.Whatsapp.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.Whatsapp.setStyleSheet("background-color: lightgray;")
        from datetime import datetime
        start_time = datetime.now()
        cluster = MongoClient("")              #MongoDB Database link
        
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainId
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('user opened whatsapp')

        icon48= QtGui.QIcon()
        icon48.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Whatsapp.setIcon(icon48)
        
        self.Whatsapp.setStyleSheet("background:none;""background-color: transparent;")

        # do your work here
        from datetime import datetime
        subprocess.call([x["path_of_whatsapp"]],shell=True)
        end_time = datetime.now()
        wapp=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Whatsapp":wapp}}})

      except:
        self.Whatsapp.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)





    def svisual(self):
        t = threading.Thread(target=self.log69)
        t.start()
        

    def log69(self):
      try:
        icon49 = QtGui.QIcon()
        icon49.addPixmap(QtGui.QPixmap("sw_vis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Solidwork_visualize.setIcon(icon49)
        #print(1)
        self.Solidwork_visualize.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.Solidwork_visualize.setStyleSheet("background-color: lightgray;")
        from datetime import datetime
        start_time = datetime.now()
        cluster = MongoClient("")                  #MongoDB Database link
        
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainId
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('user opened solidwork_visualize')

        icon49= QtGui.QIcon()
        icon49.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Solidwork_visualize.setIcon(icon49)
        
        self.Solidwork_visualize.setStyleSheet("background:none;""background-color: transparent;")

        # do your work here
        from datetime import datetime
        subprocess.call([x["path_of_solidwork_visualize"]],shell=True)
        end_time = datetime.now()
        swvisual=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"solidwork_visualize":swvisual}}})
      except:
        self.Solidwork_visualize.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)



    def spy(self):
        print(88)
        t = threading.Thread(target=self.log70)
        t.start()
        

    def log70(self):
      try:   #print(88)
        icon50 = QtGui.QIcon()
        icon50.addPixmap(QtGui.QPixmap("whatsapp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Spyder.setIcon(icon50)
        #print(1)
        self.Spyder.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.Spyder.setStyleSheet("background-color: lightgray;")
        start_time = datetime.now()
        cluster = MongoClient("")              #MongoDB Database link
        
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainId
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('user opened Spyder')
        
        
        icon50 = QtGui.QIcon()
        icon50.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Spyder.setIcon(icon50)
        
        self.Spyder.setStyleSheet("background:none;""background-color: transparent;")

        # do your work here
        subprocess.call([x["path_of_Spyder"]],shell=True)
        end_time = datetime.now()
        spy=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Spyder":spy}}})
      except:
        self.Spyder.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)


       

    def any(self):
        #print(88)
        t = threading.Thread(target=self.log71)
        t.start()
        

    def log71(self):
      try:
        icon51 = QtGui.QIcon()
        icon51.addPixmap(QtGui.QPixmap("whatsapp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Any_desk.setIcon(icon51)
        #print(1)
        self.Any_desk.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        
        start_time = datetime.now()
        cluster = MongoClient("")              #MongoDB Database link
        
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainId
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('user opened Any_desk')

        icon51= QtGui.QIcon()
        icon51.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Any_desk.setIcon(icon51)
        
        self.Any_desk.setStyleSheet("background:none;""background-color: transparent;")

        # do your work here
        subprocess.call([x["path_of_Any_desk"]],shell=True)
        end_time = datetime.now()
        an=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Any_desk":an}}})
      except:
        self.Any_desk.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)


    def post(self):       #####################mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
        print(14) 
        t = threading.Thread(target=self.log72)
        t.start()
    def log72(self):
      try:  #print(88)
        icon52 = QtGui.QIcon()
        icon52.addPixmap(QtGui.QPixmap("whatsapp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Postman.setIcon(icon52)
        #print(1)
        self.Postman.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.Blender.setStyleSheet("background-color: lightgray;")
        start_time = datetime.now()
        cluster = MongoClient("")              #MongoDB Database link
        
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainId
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('user opened Postman')

        icon52= QtGui.QIcon()
        icon52.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Postman.setIcon(icon52)
        
        self.Postman.setStyleSheet("background:none;""background-color: transparent;")

        # do your work here
        subprocess.call([x["path_of_postman"]],shell=True)
        end_time = datetime.now()
        po=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Postman":po}}})
      except:
        self.Postman.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)

    def blen(self):
        #print(88)
        t = threading.Thread(target=self.log73)
        t.start()
        

    def log73(self):
      try:  
        icon53 = QtGui.QIcon()
        icon53.addPixmap(QtGui.QPixmap("whatsapp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Blender.setIcon(icon53)
        #print(1)
        self.Blender.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.Blender.setStyleSheet("background-color: lightgray;")
        start_time = datetime.now()
        cluster = MongoClient("")              #MongoDB Database link
        
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainId
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('user opened Blender')

        icon53= QtGui.QIcon()
        icon53.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Blender.setIcon(icon53)
        
        self.Blender.setStyleSheet("background:none;""background-color: transparent;")

        # do your work here
        subprocess.call([x["path_of_Blender"]],shell=True)
        end_time = datetime.now()
        sw=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Blender":sw}}})
      except:
        self.Blender.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)

    def ux(self):
       
        t = threading.Thread(target=self.log74)
        t.start()
        

    def log74(self):
      try:  

        icon54 = QtGui.QIcon()
        icon54.addPixmap(QtGui.QPixmap("whatsapp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Ui_UX.setIcon(icon54)
        #print(1)
        self.Ui_UX.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.Ui_UX.setStyleSheet("background-color: lightgray;")
        start_time = datetime.now()
        cluster = MongoClient("")              #MongoDB Database link
        
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainId
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('user opened Ui_UX')


        icon54= QtGui.QIcon()
        icon54.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Ui_UX.setIcon(icon54)
        
        self.Ui_UX.setStyleSheet("background:none;""background-color: transparent;")

        # do your work here
        subprocess.call([x["path_of_Ui_UX"]],shell=True)
        end_time = datetime.now()
        swv=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Ui_UX":swv}}})
      except:
        self.Ui_UX.setStyleSheet("background:none;""background-color: transparent;")

        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)

    def cnc(self):
       
        t = threading.Thread(target=self.log75)
        t.start()
        

    def log75(self):
      try:  
        icon55 = QtGui.QIcon()
        icon55.addPixmap(QtGui.QPixmap("whatsapp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Cnc_viewer.setIcon(icon55)
        #print(1)
        self.Cnc_viewer.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.Cnc_viewer.setStyleSheet("background-color: lightgray;")
        start_time = datetime.now()
        cluster = MongoClient("")              #MongoDB Database link
        
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainId
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('user opened Cnc_viewer')


        icon55= QtGui.QIcon()
        icon55.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Cnc_viewer.setIcon(icon55)
        
        self.Cnc_viewer.setStyleSheet("background:none;""background-color: transparent;")

        # do your work here
        subprocess.call([x["path_of_Cnc_viewer"]],shell=True)
        end_time = datetime.now()
        swvi=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Cnc_viewer":swvi}}})
      except:
        self.Cnc_viewer.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)


    def mongo(self):
        
        t = threading.Thread(target=self.log76)
        t.start()
        

    def log76(self):
      try:  
        icon56 = QtGui.QIcon()
        icon56.addPixmap(QtGui.QPixmap("whatsapp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Mongodb_compass.setIcon(icon56)
        #print(1)
        self.Mongodb_compass.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.Mongodb_compass.setStyleSheet("background-color: lightgray;")
        start_time = datetime.now()
        cluster = MongoClient("")              #MongoDB Database link
        
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainId
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('user opened Mongodb_compass')

        icon56= QtGui.QIcon()
        icon56.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Mongodb_compass.setIcon(icon56)
        
        self.Mongodb_compass.setStyleSheet("background:none;""background-color: transparent;")

        # do your work here
        subprocess.call([x["path_of_Mongodb_compass"]],shell=True)
        end_time = datetime.now()
        mon=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Mongodb_compass":mon}}})
      except:
        self.Mongodb_compass.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)


    def goo(self):
        
        t = threading.Thread(target=self.log77)
        t.start()
        

    def log77(self):
      try: 
        icon57 = QtGui.QIcon()
        icon57.addPixmap(QtGui.QPixmap("whatsapp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Google_meet.setIcon(icon57)
        #print(1)
        self.Google_meet.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.Google_meet.setStyleSheet("background-color: lightgray;")
        start_time = datetime.now()
        cluster = MongoClient("")              #MongoDB Database link
        
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainId
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('user opened Google_meet')

        icon57= QtGui.QIcon()
        icon57.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Google_meet.setIcon(icon57)
        
        self.Google_meet.setStyleSheet("background:none;""background-color: transparent;")

        # do your work here
        subprocess.call([x["path_of_Google_meet"]],shell=True)
        end_time = datetime.now()
        gool=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Google_meet":gool}}})
      except:
        self.Google_meet.setStyleSheet("background:none;""background-color: transparent;")  
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)

    def cd(self):
        
        t = threading.Thread(target=self.log78)
        t.start()
        

    def log78(self):
      try:
        icon58 = QtGui.QIcon()
        icon58.addPixmap(QtGui.QPixmap("whatsapp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmd.setIcon(icon58)
        #print(1)
        self.cmd.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.cmd.setStyleSheet("background-color: lightgray;")
        start_time = datetime.now()
        cluster = MongoClient("")                  #MongoDB Database link
        
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainId
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('user opened cmd')

        icon58= QtGui.QIcon()
        icon58.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmd.setIcon(icon58)
        
        self.cmd.setStyleSheet("background:none;""background-color: transparent;")

        # do your work here
        subprocess.call([x["path_of_cmd"]],shell=True)
        end_time = datetime.now()
        cm=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"cmd":cm}}})
      except:        
        self.cmd.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)


    def git(self):
        t = threading.Thread(target=self.log79)
        t.start()
        
        
    def log79(self):
      try:
        icon59 = QtGui.QIcon()
        icon59.addPixmap(QtGui.QPixmap("whatsapp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Github_desktop.setIcon(icon59)
        #print(1)
        self.Github_desktop.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        #self.cmd.setStyleSheet("background-color: lightgray;")
        start_time = datetime.now()
        cluster = MongoClient("")              #MongoDB Database link
        
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainId
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('user opened Github')

        icon59= QtGui.QIcon()
        icon59.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Github_desktop.setIcon(icon59)
        
        self.Github_desktop.setStyleSheet("background:none;""background-color: transparent;")

        # do your work here
        subprocess.call([x["path_of_github"]],shell=True)
        end_time = datetime.now()
        git=format(end_time - start_time)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,"Github":git}}})
      except:
        self.Github_desktop.setStyleSheet("background:none;""background-color: transparent;")
        text="Check the internet connection"
        title="Unsuccessful"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)


   
    
    def log80(self,app_name,path,name,app_logo):
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(app_logo), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        name.setIcon(icon26)
        #print(1)
        name.setStyleSheet("background:none;""background-color: blue;")#"border:10px solid;""border-color:red;")
        
        

        
        from datetime import datetime
        start_time = datetime.now()
        cluster = MongoClient("")              #MongoDB Database link
        db = cluster["test"]
        collection=db["Locations"]
        collection2=db["Time tracking"]
        global mainId
        Id= mainID
        myquery={"_id":Id}
        x=collection.find_one(myquery)
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('user opened '+str(app_name))
        #name.setStyleSheet("background-color: transparent;")
        
        icon32= QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap("TRANSPARENT(COMPLETE).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        name.setIcon(icon32)                
            
       
        name.setStyleSheet("background:none;""background-color: transparent;")


        # do your work here
        subprocess.call([x[path]],shell=True)
        from datetime import datetime
        end_time = datetime.now()
        #print(end_time,start_time)
        gitt=format(end_time - start_time)
        #print(gitt)
        collection2.update_one(myquery ,{ "$push":{"duration_of_app":{"starttime":start_time,app_name:gitt}}})
        
    def see1(self):        #add location code
        self.window1=QtWidgets.QMainWindow()
        global mainID
        self.i_d=mainID
        self.ui1=Ui_openwindow(self.i_d)
        self.ui1.setupUi(self.window1)
        self.window1.show()

    def see2(self):        #add location code
        self.window2=QtWidgets.QMainWindow()
        global mainID
        self.i_d=mainID
        self.ui2=Ui_userid(self.i_d)
        self.ui2.setupUi(self.window2)
        self.window2.show()

    def see3(self):
      try:
        global mainID
        conn=psycopg2.connect('')              #PSQL Database link
        cur=conn.cursor()
        cur.execute("delete from login_mac where user_id = '%d'"%(mainID))
        conn.commit()
        self.logout(b,m)#############################################3333333
        """
        msg = QMessageBox()
        msg.setWindowTitle("Logout")
        msg.setText("Successfully Logged out \n You can close the operation page")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
        """
        #self.operations.close()
        import os
        
            os.system("taskkill /f /im python.exe")                             # this is only for executing .py file ##while exe comment this
        except:
            print("check this difference for .py and .exe")
      except:
        text="Check the internet connection"
        title="Information"
        ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)
 
   
   
   

    def see4(self):        #add app code

        import subprocess
        subprocess.Popen(['newapp.py'],shell=True)
        '''self.window4=QtWidgets.QMainWindow()
        global mainID
        self.i_d=mainID
        self.ui4=Ui_addopenwindow(self.i_d)
        self.ui4.setupUi(self.window4)
        self.window4.show()'''

    def see5(self):        #open location code
        self.window5=QtWidgets.QMainWindow()
        global mainID
        self.i_d=mainID
        self.ui5=Ui_appwindow(self.i_d)
        self.ui5.setupUi(self.window5)
        self.window5.show()

    def see6(self):        #change location code
        import subprocess
        subprocess.Popen(['change_location.py'],shell=True)
        '''self.window6=QtWidgets.QMainWindow()
        global mainID
        self.i_d=mainID
        self.ui6=Ui_openwindow1(self.i_d)
        self.ui6.setupUi(self.window6)
        self.window6.show()'''


    def see7(self):#remove location code
        import subprocess
        subprocess.Popen(['removeapp.py'],shell=True)


        '''self.window7=QtWidgets.QMainWindow()
        global mainID
        self.i_d=mainID
        self.ui7=Ui_appwindow2(self.i_d)
        self.ui7.setupUi(self.window7)
        self.window7.show()'''


    
 
        
    def retranslateUi(self, operations):
        cluster = MongoClient("")              #MongoDB Database link
        db = cluster["test"]
        collection30=db["Locations"]
        myid= mainID
        
        myquery1={"_id":myid}
        m=collection30.find_one(myquery1)
        
        _translate = QtCore.QCoreApplication.translate
        operations.setWindowTitle(_translate("operations", "Athrv-Ed LMS Productivity Tracker"))
        self.label_8.setText(_translate("operations", "Productivity Tracker"))
        
        self.label.setText(_translate("operations", "Top performer"))
        
        
        self.label_11.setText(_translate("operations", "Time   :"))

        self.label_2.setText(_translate("operations", "        Hi , "+ name1+"!!!"))
        self.pushButton.setText(_translate("operations", "Search on Web"))
        self.pushButton_2.setStatusTip(_translate("operations", "Reading Mode"))
        self.pushButton_2.setText(_translate("operations", "Reading Mode OFF"))
        self.pushButton_3.setText(_translate("operations", "Pause"))
        self.pushButton_4.setText(_translate("operations", "Resume"))
        self.label_5.setText(_translate("operations", "Click to Pause work"))
        self.label_6.setText(_translate("operations", "Click to Resume work"))
        self.menuEdit.setTitle(_translate("operations", "Edit"))
        self.menuExtra_features.setTitle(_translate("operations", "Extra features"))
        self.menuExtra_Apps.setTitle(_translate("operations", "Extra Apps"))
        self.actionAdd_Location.setText(_translate("operations", "Add Location"))
        self.actionview_time.setText(_translate("operations", "Working details"))

        self.actiondark_mode.setText(_translate("operations", "Dark mode"))    ###########################
        self.actionaddapp.setText(_translate("operations", "Add Apps"))
        
        self.actionopenapp.setText(_translate("operations", "Open Apps"))
        self.actionremoveapp.setText(_translate("operations", "Remove Apps"))
        self.actionchangeapp.setText(_translate("operations", "Change app location"))


        self.pushButton_5.setStatusTip(_translate("operations", "LMS PORTAL"))
        self.pushButton_5.setText(_translate("operations", "LMS PORTAL"))
        self.pushButton_6.setStatusTip(_translate("operations", "CHAT APP"))
        self.pushButton_6.setText(_translate("operations", "CHAT APP"))
        self.pushButton_7.setStatusTip(_translate("operations", "YOUTUBE"))
        self.pushButton_7.setText(_translate("operations", "YOUTUBE"))
        self.pushButton_8.setStatusTip(_translate("operations", "MAIL"))
        self.pushButton_8.setText(_translate("operations", "MAIL"))

        self.actionLogout.setText(_translate("operations", "Logout"))
        
        self.vscode.setStatusTip(_translate("operations",("Visual Studio "+m["path_of_Visual studio"])))
        self.androidstudio.setStatusTip(_translate("operations",("Android studio "+m["path_of_Android studio"])))
        self.premierpro.setStatusTip(_translate("operations",("Premier pro "+m["path_of_Premier pro"])))
        self.pycharm.setStatusTip(_translate("operations",("Pycharm "+m["path_of_Phycharm"])))
        self.photoshop.setStatusTip(_translate("operations",("Photoshop "+m["path_of_Photoshop"])))
        self.tableau.setStatusTip(_translate("operations",("Tableau "+m["path_of_Tableau"])))
        self.figma.setStatusTip(_translate("operations",("Figma "+m["path_of_Figma"])))
        self.idle.setStatusTip(_translate("operations",("Idle "+m["path_of_Idle"])))
        self.ardiuno.setStatusTip(_translate("operations",("Arduino IDE "+m["path_of_Arduino illustrator"])))
        self.illustrator.setStatusTip(_translate("operations",("Adobe illustrator "+m["path_of_Adobe illustrator"])))
        self.wps.setStatusTip(_translate("operations",("Wps office "+m["path_of_Wps_office"])))
        self.Qtdesigner.setStatusTip(_translate("operations",("Qt designer "+m["path_of_Qt designer"])))
        self.aftereffects.setStatusTip(_translate("operations",("After effects "+m["path_of_After effects"])))
        self.proteus.setStatusTip(_translate("operations",("Proteus "+m["path_of_Proteus"])))
        self.codeblocks.setStatusTip(_translate("operations",("Code blocks "+m["path_of_Code blocks"])))
        self.solidworks.setStatusTip(_translate("operations", ("Solid works "+m["path_of_Solid works"])))
        self.word.setStatusTip(_translate("operations", ("MS_word "+m["path _of_word"])))
        
        self.MS_Excel.setStatusTip(_translate("operations", ("Ms_Excel "+m["path_of_excel"])))
        self.MS_Powerpoint.setStatusTip(_translate("operations", ("MS_Powerpoint "+m["path_of_powerpoint"])))
        self.Microsoft_Edge.setStatusTip(_translate("operations", ("Microsoft_Edge "+m["path_of_edge"])))
        self.Team_viewer.setStatusTip(_translate("operations", ("Team_viewer "+m["path_of_team_viewer"])))
        self.Jio_meet.setStatusTip(_translate("operations", ("Jio_meet "+m["path_of_jio_meet"])))
        self.Discord.setStatusTip(_translate("operations", ("Discord "+m["path_of_discord"])))
        self.Whatsapp.setStatusTip(_translate("operations", ("Whatsapp "+m["path_of_whatsapp"])))
        self.Solidwork_visualize.setStatusTip(_translate("operations", ("Solidwork_visualize "+m["path_of_solidwork_visualize"])))
        
        self.Spyder.setStatusTip(_translate("operations", ("Spyder "+m["path_of_Spyder"])))
        self.Any_desk.setStatusTip(_translate("operations", ("Any_desk "+m["path_of_Any_desk"])))
        self.Postman.setStatusTip(_translate("operations", ("Postman "+m["path_of_Postman"])))
        self.Blender.setStatusTip(_translate("operations", ("Blender "+m["path_of_Blender"])))
        self.Ui_UX.setStatusTip(_translate("operations", ("EXTRA "+m["path_of_Ui_UX"])))
        self.Cnc_viewer.setStatusTip(_translate("operations", ("EXTRA "+m["path_of_Cnc_viewer"])))
        self.Mongodb_compass.setStatusTip(_translate("operations", ("Mongodb_compass "+m["path_of_Mongodb_compass"])))
        self.Google_meet.setStatusTip(_translate("operations", ("Google_meet "+m["path_of_Google_meet"])))
        self.cmd.setStatusTip(_translate("operations", ("CMD "+m["path_of_cmd"])))
        self.Github_desktop.setStatusTip(_translate("operations", ("Github_desktop "+m["path_of_Github_desktop"])))
        
        
        
 
             
    def pause_window(self):
      if resume_pause[0]==0:
        resume_pause.clear()
        resume_pause.append(1)
        op.clear()
        op.append(1)
        
        global pause_time
        
        pause_time = datetime.now().replace(microsecond=0)
        
        nowww = datetime.now()
        #print("gjhkk")
        st_time = str(start_time1.strftime("%H:%M:%S"))
        current_w_time = str(nowww.strftime("%H:%M:%S"))
        #print("kjiuo")
        FMT = '%H:%M:%S'
        #print(99999)
        try:
            t_tdelta = datetime.strptime(current_w_time, FMT) - datetime.strptime(st_time, FMT)
            #print(t_tdelta)
        except Exception as e:
            print(e)
        if str(t_tdelta) < "0:30:00":
            #print("ya")
            tttt = threading.Thread(target=self.auto_save)#(b,m,op,start_time1,pause_time,k,today))
            tttt.start()
        msg = QMessageBox()
        msg.setWindowTitle("Pause")
        msg.setText("Your Work has been paused")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

        self.pushButton_3.setStyleSheet("border-radius:10px;\n" "background-color: red;\n" "color: rgb(255, 255, 255)")
        self.pushButton_4.setStyleSheet("border-radius:10px;\n""background-color: rgb(85, 170, 255)")
        
        t = threading.Thread(target=self.pause_window2)
        t.start()
        return pause_time

        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.warning('User has paused his work')
        
      else:

            f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            f_handler.setFormatter(f_format)
            logger.addHandler(f_handler)
            logger.warning('User has paused his work again')
            
            msg = QMessageBox()
            msg.setWindowTitle("Pause")
            msg.setText("Your Work is already paused")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

          
    def pause_window2(self):

                j.clear()
                j.append(0)
                k.clear()
                k.append(0)

                class LASTINPUTINFO(Structure):
                                _fields_ = [
                                    ('cbSize', c_uint),
                                    ('dwTime', c_uint),
                                ]
                def get_idle_duration():
                    lastInputInfo = LASTINPUTINFO()
                    lastInputInfo.cbSize = sizeof(lastInputInfo)
                    windll.user32.GetLastInputInfo(byref(lastInputInfo))
                    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
                    return millis / 1000.0
               
                t=0
                process_time={}
                timestamp = {}
                
                while True:
                     import time
                     time.sleep(1)
                                              
                     GetLastInputInfo = int(get_idle_duration())
                    
                     if GetLastInputInfo>=0:
                                    
                            j.extend([GetLastInputInfo])
                                 
                                    
                            if  GetLastInputInfo==0 :
                                c=int(j[-2])
                                if c >=0:             
                                        
                                        d=int(k[0])
                                        d=d+c
                                        k.clear()
                                        k.append(d)

                     t+=1
    
    
    def resume_window(self):
     
        op.clear()
        #print(op)
        op.append(0)
        #print("kgfyg")
        if resume_pause[0]==0:
            msg = QMessageBox()
            msg.setWindowTitle("Resume")
            msg.setText("Please resume your work")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            self.pushButton_4.setStyleSheet("border-radius:10px;\n" "background-color: green;\n" "color: rgb(255, 255, 255)")
            self.pushButton_3.setStyleSheet("border-radius:10px;\n""background-color: rgb(85, 170, 255)")
            f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            f_handler.setFormatter(f_format)
            logger.addHandler(f_handler)
            logger.warning('User has resumed his work in the beginning ')
                
        else:
            global resume_time,interval
            resume_time = datetime.now().replace(microsecond=0)
            
            interval = format(resume_time-pause_time)
            
            m.append(interval)
            #print("ojuhi")
            msg = QMessageBox()
            msg.setWindowTitle("Resume")
            msg.setText("Your work has been resumed")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
            #print(b,"b is")
            b0=(int(b[0]))
            k0=(int(k[0]))
            
            if k0>b0:
                bk=0
            else:
               bk=int(b0-k0)
               
            b.clear()
            b.append(bk)
            self.pushButton_4.setStyleSheet("border-radius:10px;\n" "background-color: green;\n" "color: rgb(255, 255, 255)")
            self.pushButton_3.setStyleSheet("border-radius:10px;\n""background-color: rgb(85, 170, 255)")
            resume_pause.clear()
            resume_pause.append(0)
            
            f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            f_handler.setFormatter(f_format)
            logger.addHandler(f_handler)
            logger.warning('User has resumed his work')


     


    def logout(self,b,m):
      global t_w_t_lis,imidle
      #print(imidle)
      vv.append(1)
      
      from datetime import date, timedelta
      try:
            global dif_v
            dif_v.append(0)
            #QtWidgets.QApplication.instance().quit()
            
            
            try:                                         #checks whether the internet connection is on
                urlopen('http://216.58.192.142', timeout=1)
                
            except:                                      #prints this message if internet connection is off
                msg = QMessageBox()
                msg.setWindowTitle("Network connection")
                msg.setText("Please check the internet connection\n and then enter OK to save your work")
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()
                    
            if t_w_t_lis!=[]:
                tttt5 = threading.Thread(target=self.auto_save)#(b,m,op,start_time1,pause_time,k,today))
                tttt5.start()
                
            conn=psycopg2.connect('')              #PSQL Database link
            cur=conn.cursor()
            cur.execute( 'select * from productivity')
            data=cur.fetchall()

            
            from datetime import datetime
            if op[0]==1:           #if the user has closed the app without resuming his work
                global resume_time,interval
                resume_time = datetime.now().replace(microsecond=0)
                
                interval = format(resume_time-pause_time)
                m.append(interval)
                
                b0=(int(b[0]))
                k0=(int(k[0]))
                
                if k0>b0:
                   bk=0
                else:
                  bk=int(b0-k0)

     
                b.clear()
                b.append(bk)
            
            Id=mainID 
            myquery={"_id":Id}
            import datetime as datetime2
            b=int(b[0])
            b-=int(imidle[0])
            from time import strftime
            from time import gmtime
            from datetime import datetime
            
            end_time = datetime.now().replace(microsecond=0)
            total = format(end_time - start_time1)
            total=str(total)
            #print("to",total)
            total=datetime.strptime(total,"%H:%M:%S")
            #print(total)
            
            idle_time = b
            
            
            import time
            #from datetime import datetime
            #import datetime
            
            sumd=datetime2.timedelta()
            for i in m:
                (hh,mm,ss)=i.split(':')
                d=datetime2.timedelta(hours=int(hh),minutes=int(mm),seconds=int(ss))
                sumd +=d
            sumd=str(sumd)
            
            sumd=datetime.strptime(sumd,"%H:%M:%S")
            

            idle_time=strftime("%H:%M:%S",gmtime(idle_time))
            
            idle_time=datetime.strptime(idle_time,"%H:%M:%S")
            
            
            actual_time=format(total-sumd)#idle_time
            
            actual_time2=str(actual_time)
            actual_time2=datetime.strptime(actual_time,"%H:%M:%S")
           
            if idle_time>actual_time2:
               
                total_working_hrs="0:00:00"
            else:
                #print("ya2")
                total_working_hrs=format(actual_time2-idle_time)
            #print("total working hours")
           
             

            idle_time=str(idle_time)
            idle_time=datetime2.datetime.strptime(idle_time,"%Y-%m-%d %H:%M:%S") 
            idle_time=format(idle_time.time())
            
            sumd=str(sumd)
            sumd=datetime2.datetime.strptime(sumd,"%Y-%m-%d %H:%M:%S") 
            sumd=format(sumd.time())
            
            total=str(total)
            total=datetime2.datetime.strptime(total,"%Y-%m-%d %H:%M:%S") 
            total=format(total.time())

            
            
            total_working_hrs=str(total_working_hrs)
            total_working_hrs=datetime2.datetime.strptime(total_working_hrs,"%H:%M:%S") 
            total_working_hrs=format(total_working_hrs.time())
            
            total=format(total)
            idle_time=format(idle_time)
            sumd=format(sumd)

            
            
            cur.execute("select * from productivity where date='%s' AND user_id=%d"%(today,Id))
            data=cur.fetchall()
            
            for x in data:
                   
                       if x[0] == Id:
                            

                            from datetime import date            

                            idle_time1=x[3]                        #  ["Actual_Idle_time"]     #values from database      #idle_time
                            total_app_time1=x[2]                   #["Total_App_time"]                                    #total
                            pause_resume1=x[4]                     #["Pause_Resume_Interval"]                             #sumd
                            total_working_hours=x[5]               #["Total_Working_Hours"]                               #total_working_hrs

                             
                            
                            idle_time1=str(idle_time1)
                            idle_time1=datetime2.datetime.strptime(idle_time1,"%H:%M:%S") 
                            idle_time1=format(idle_time1.time())
                            
                            
                            (h1,m1,s1)=idle_time1.split(':')
                            idle_time1=(int(h1)*3600)+(int(m1)*60)+int(s1)
                            (h1,m1,s1)=idle_time.split(':')
                            idle_time=(int(h1)*3600)+(int(m1)*60)+int(s1)   
                            idle_time_final2= (idle_time1+idle_time)
                            idle_time_final=format(strftime("%H:%M:%S",gmtime(idle_time_final2))) 

                         
                            total_app_time1=str(total_app_time1)
                            total_app_time1=datetime2.datetime.strptime(total_app_time1,"%H:%M:%S")
                            total_app_time1=format(total_app_time1.time())
                            (h1,m1,s1)=total_app_time1.split(':')
                            total_app_time1=(int(h1)*3600)+(int(m1)*60)+int(s1)
                            (h1,m1,s1)=total.split(':')
                            total=(int(h1)*3600)+(int(m1)*60)+int(s1)
                            total_app_time1_final2=(total_app_time1+total)
                            total_app_time1_final=format(strftime("%H:%M:%S",gmtime(total_app_time1_final2)))
                            
                        
                            pause_resume1=str(pause_resume1)
                            pause_resume1=datetime2.datetime.strptime(pause_resume1,"%H:%M:%S")
                            pause_resume1=format(pause_resume1.time())
                            (h1,m1,s1)=pause_resume1.split(':')
                            pause_resume1=(int(h1)*3600)+(int(m1)*60)+int(s1)
                            (h1,m1,s1)=sumd.split(':')
                            sumd=(int(h1)*3600)+(int(m1)*60)+int(s1)
                            pause_resume1_final2=(pause_resume1+sumd)
                            pause_resume1_final=format(strftime("%H:%M:%S",gmtime(pause_resume1_final2)))

                            #print(total_app_time1_final2,pause_resume1_final2,idle_time_final2)
                            woooork = int(pause_resume1_final2+idle_time_final2)
                            total_working_hours_final2=(total_app_time1_final2-woooork)

                           
                           
                            total_working_hours_final=format(strftime("%H:%M:%S",gmtime(total_working_hours_final2)))


                            #do additions here
                           
                           
                            cur.execute("update productivity SET total_app_time='%s',actual_idle_time='%s',pause_resume_interval='%s',total_working_hours='%s' WHERE user_id=%d AND date='%s'" %(total_app_time1_final,idle_time_final,pause_resume1_final,total_working_hours_final,Id,today))   
                            conn.commit()
    
                            op.clear()
                            op.append(2)
                            
                            f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                            f_handler.setFormatter(f_format)
                            logger.addHandler(f_handler)
                            logger.critical('Successfully saved to database finals--idle time'+str(idle_time_final))
                            logger.critical('Successfully saved to database finals--start time'+str(start_time1))
                            logger.critical('Successfully saved to database finals--app time'+str(total_app_time1_final))
                            logger.critical('Successfully saved to database finals--total working time'+str(total_working_hours_final))
                            
                            
                            

                            f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                            f_handler.setFormatter(f_format)
                            logger.addHandler(f_handler)
                            logger.critical('Successfully saved to database finals')
                            #print("finALLY")

                            text="your working hours is saved successfully"
                            title="Successful"
                            ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)

                            
                            
                            
                        
                            break
            
            if data==[]:       #save to database if the user has used the app first time today
                         #collection3.update_one(myquery,{"$set":{today:{"Date":today,"Total_App_time":total,"Actual_Idle_time":idle_time,"Pause_Resume_Interval":sumd,"Total_Working_Hours":total_working_hrs}}})
                         cur.execute("insert into productivity (user_id,date,total_app_time,actual_idle_time,pause_resume_interval,total_working_hours) VALUES (%d,'%s','%s','%s','%s','%s')"%(Id,today,total,idle_time,sumd,total_working_hrs))
                       
                         conn.commit()
                         
                         op.clear()
                         op.append(2)
                         
                         f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                         f_handler.setFormatter(f_format)
                         logger.addHandler(f_handler)
                         logger.critical('Successfully  saved to database finals--idle time'+str(idle_time))
                         logger.critical('Successfully  saved to database finals--start time'+str(start_time1))
                         logger.critical('Successfully   saved to database finals--app time'+str(total))
                         logger.critical('Successfully   saved to database finals--total working time'+str(total_working_hrs))
                         

                         f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                         f_handler.setFormatter(f_format)
                         logger.addHandler(f_handler)
                         logger.critical('Successfully saved to database finals')
                         #print("finALLY")

                         text="your working hours is saved successfully"
                         title="Successful"
                         ctypes.windll.user32.MessageBoxW(0,text,title,0x1000)

                        
                         
                         
                        
                       
                         

                       
      except Exception as e:
        #print(e)
        #global dif_v
        dif_v.clear()
        f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)
        logger.critical('Operation Page has been Crashed'+str(e))
        op.clear()
        op.append(2)
        import os
        os.system("taskkill /f /im final_operation_page.exe")   ################# 'END TASK' of the app from task manager
 

    

from datetime import date as d, timedelta as t
#import datetime, time
time = time.strftime("%H:%M:%S", time.localtime())

yesterday = d.today() - t(days=1)
today1=d.today()
global today
start = '00:00:00'
end = '03:00:00'
if time > start and time < end:                   #work done before today morning 6am is considered as yesterdays work
  #print("in")
  today=yesterday

else:
  #print("out")
  today=today1
#print(today)
     
    

        


if __name__=="__main__":
    Id=mainID
    conn=psycopg2.connect('')              #PSQL Database link
    #print(122)
    cur=conn.cursor()

    from datetime import date, timedelta
    today8 = date.today() - timedelta(days=1)
    cur.execute( "select user_id,total_working_hours from productivity where date='%s'" %(today8))
    load1 =cur.fetchall()
    if load1 == []:
        name4 = "None"
        load9 = "None"
    else:
        #print(len(load1))
        leng = len(load1)
        leng1=0
        list2=[]
        list3=[]
        while(leng1<leng):
            list1 = load1[leng1]
            #print(list1)
            time21 = str(list1[1])
            #print(time1)
            h25,m25,s25 = time21.split(':')
            time22 = int(h25)*3600 + int(m25)*60 + int(s25)
            list2.append(list1[0])
            list3.append(time22)
            (leng1)+=1

        l3 = max(list3)
        p3 = list3.index(l3)
        id3 = list2[p3]
        cur.execute( 'select name1 from member1 where member_id =(%d)'%(id3))
        load7 = cur.fetchall()
        #print(load7[0])
        name3 = load7[0]
        name4 = (name3[0])
        #print(today8)

        import time
        load9 = time.strftime('%H:%M:%S', time.gmtime(int(l3)))
        #print(load9)

    


    cur.execute( 'select name1 from member1 where member_id =(%d)'%(Id))
    data1 =cur.fetchall()
    #print(data1)
                    
    name =data1[0]
    name1= name[0]
    #print(name1)
    #name4 = "Meghana"
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    operations = QtWidgets.QMainWindow()
    ui = Ui_operations()
    ui.setupUi(operations)
    operations.show()
    if (sys.flags.interactive != 1):   
            QtWidgets.QApplication.instance().exec_()    
    

            Ui_operations().logout(b,m)
            
            
    

