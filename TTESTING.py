import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel 
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtGui import QMovie


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        
        
        self.setFixedSize(800,500)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
        self.label_annimation=QLabel(self)
        
        
        
        self.movie=QMovie('smile_loader_by_gleb.gif')
        self.label_annimation.setMovie(self.movie)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(275, 10, 300, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        #font.setUnderline(True)
        font.setWeight(1000)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("border-radius:5px;\n""color:white;\n")#"background-color: blue;")
        self.label.setText("Loading....")
        
        
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(0, 0, 221, 131))
        self.label1.setText("")
        self.label1.setPixmap(QtGui.QPixmap("Athrved.png"))
        self.label1.setScaledContents(True)
        self.label1.setObjectName("label")
        
        
        timer=QTimer(self)
        self.startAnimation()
        timer.singleShot(10000,self.stopAnimation)      #while converting to exe change value to 40000 which is 40 sec display of video # as while converting to exe the apps slows dowm
        self.show()
        
        
    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()



class AppDemo(QWidget):
    def __init__(self):
        
        self.loading_screen=LoadingScreen()
        #self.show()
        
app=QApplication(sys.argv)
demo=AppDemo()
app.exit(app.exec_())






























