from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2
import datetime

class Ui_userid(object):

    def __init__(self, i_d):
        self.i_d=i_d
        
    
    def setupUi(self, userid):
        userid.setObjectName("userid")
        userid.resize(772, 471)
        userid.setStyleSheet("background-color: rgb(211, 207, 231);")

        
        icon=QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Athrved2.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        userid.setWindowIcon(icon)
        
        self.centralwidget = QtWidgets.QWidget(userid)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(165, 30, 481, 31))#30
        font = QtGui.QFont()
        #font.setFamily("OCR A Extended")
        font.setPointSize(16)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(165, 400, 481, 28))#30
        font = QtGui.QFont()
        #font.setFamily("OCR A Extended")
        font.setPointSize(14)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 80, 691, 311))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setHorizontalHeaderLabels(['Date','Total App Time','Idle Time','Pause Time','Total Working Time'])
        userid.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(userid)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 772, 26))
        self.menubar.setObjectName("menubar")
        userid.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(userid)
        self.statusbar.setObjectName("statusbar")
        userid.setStatusBar(self.statusbar)

        
        Id = self.i_d
        from datetime import date, timedelta
        
        i=1
        conn = psycopg2.connect('')     #PSQL Database link
        cur=conn.cursor()
        self.tableWidget.setRowCount(0)
        list1=[]
        
        while(i<=7):

                today1 = date.today() - timedelta(days=i)
                    
                #print(i,today1,Id)    
                
                
                load = "select * from productivity where date='%s' AND user_id=%d"%(today1,Id)
                cur.execute(load)
                
                data=cur.fetchall()
                #print(data)
                if data == []:
                    #print(str(today1))
                    list1.append(0)
                    self.tableWidget.insertRow(i-1)
                    self.tableWidget.setItem(i-1,0,QtWidgets.QTableWidgetItem(str(today1)))

                    for l in range(1,5):
                        data1 = ["None","None","None","None","None","None","None"]

                        self.tableWidget.setItem(i-1,l,QtWidgets.QTableWidgetItem(str(data1[l])))
                    i+=1
                else:
                    data1=data[0]
                    time1 = str(data1[5])
                    #print(time1)
                    h,m,s = time1.split(':')
                    time2 = int(h)*3600 + int(m)*60 + int(s)
                    #print(time2)
                    list1.append(time2)
                    
                    self.tableWidget.insertRow(i-1)
                    for l in range(1,6):
                            
                    
                            self.tableWidget.setItem(i-1,l-1,QtWidgets.QTableWidgetItem(str(data1[l])))
                    i+=1
        
                #print(e)
        conn.close()

        time3 = sum(list1)
        #print(time3)
        time4 = int(time3/7)
        #print(time4)
        import time
        time5 = time.strftime('%H:%M:%S', time.gmtime(time4))
        #print(time5)
        self.label_2.setText( "Average working time is  "+ str(time5))

        
        #self.pushButton.clicked.connect(self.loaddata)
        self.retranslateUi(userid)
        QtCore.QMetaObject.connectSlotsByName(userid)

    def retranslateUi(self, userid):
        _translate = QtCore.QCoreApplication.translate
        userid.setWindowTitle(_translate("userid", "view_time"))
        self.label.setText(_translate("userid", "Working details of past 7 days"))
        #self.label_2.setText(_translate("userid", "Average working time is"+ time5))
        self.tableWidget.setSortingEnabled(False)
if __name__ == "__main__":
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    userid = QtWidgets.QMainWindow()
    ui = Ui_userid()
    ui.setupUi(userid)
    userid.show()
    sys.exit(app.exec_())
    
        
