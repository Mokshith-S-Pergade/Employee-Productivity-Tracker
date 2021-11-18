# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'termsandconditions.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Terms_conditions(object):
    def setupUi(self, Terms_conditions):
        Terms_conditions.setObjectName("Terms_conditions")
        Terms_conditions.resize(850, 881)
        Terms_conditions.setMaximumSize(QtCore.QSize(850, 881))
        Terms_conditions.setStyleSheet("background-color: rgb(0, 121, 173);")

        
        icon=QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Athrved3.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        Terms_conditions.setWindowIcon(icon)
        
        self.centralwidget = QtWidgets.QWidget(Terms_conditions)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 310, 771, 511))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, -20, 851, 121))
        self.label_9.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -20, 221, 141))
        self.label.setStyleSheet("background-color:transparent;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Athrved.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(500, 20, 341, 52))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(26)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.label_10.setObjectName("label_10")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 110, 171, 181))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("terms3.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        Terms_conditions.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Terms_conditions)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 26))
        self.menubar.setObjectName("menubar")
        Terms_conditions.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Terms_conditions)
        self.statusbar.setObjectName("statusbar")
        Terms_conditions.setStatusBar(self.statusbar)

        self.retranslateUi(Terms_conditions)
        QtCore.QMetaObject.connectSlotsByName(Terms_conditions)

    def retranslateUi(self, Terms_conditions):
        _translate = QtCore.QCoreApplication.translate
        Terms_conditions.setWindowTitle(_translate("Terms_conditions", "MainWindow"))
        self.textEdit.setHtml(_translate("Terms_conditions", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Terms and Conditions</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; font-weight:600; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Josefin Sans\'; font-size:11pt; font-weight:600; color:#000000; background-color:#ffffff;\">1. GENERAL</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Josefin Sans\'; font-size:11pt; color:#000000; background-color:#ffffff;\">This application is created and designed by members of Athrv-Ed, and is a property of Athrv-Ed, Learning and Innovation Hub, NMAMIT, Nitte, Karnataka. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Josefin Sans\'; font-size:11pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Josefin Sans\'; font-size:11pt; color:#000000; background-color:#ffffff;\">i. This application works as a Athrv-Ed LMS Productivity Tracker , hence it is accessible to only the core members of Athrv-Ed. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Josefin Sans\'; font-size:11pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Josefin Sans\'; font-size:11pt; color:#000000; background-color:#ffffff;\">ii. Your login is authorised by the company, and you understand and accept that as an operational/administrative measure the company might revoke your access to the application without any prior notice.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Josefin Sans\'; font-size:11pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Josefin Sans\'; font-size:11pt; font-weight:600; color:#000000; background-color:#ffffff;\">2. PRIVACY</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Josefin Sans\'; font-size:11pt; color:#000000; background-color:#ffffff;\">i. The data entered in the application is visible only to the members of the company. In no ways the company support or encourage the breach of your privacy. Any private information entered will be processed only with the user\'s acknowledgement.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Josefin Sans\'; font-size:11pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Josefin Sans\'; font-size:11pt; color:#000000; background-color:#ffffff;\">ii. By agreeing to the terms and condition you assure that any information entered by you is true and is to the best of your knowledge. (You may be asked to provide documentation proof for the qualifications you entered on the application).</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Josefin Sans\'; font-size:11pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Josefin Sans\'; font-size:11pt; color:#000000; background-color:#ffffff;\">iii. By agreeing to the terms and conditions, you understand and ensure that you will not misuse the portal in any means possible and that you will use it only for the tasks and work related to the company.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Josefin Sans\'; font-size:11pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Josefin Sans\'; font-size:11pt; color:#000000; background-color:#ffffff;\">iv. By agreeing to the terms and conditions you will allow the application to take random screenshots at random intervals of time.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Josefin Sans\'; font-size:11pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Josefin Sans\'; font-size:11pt; color:#000000; background-color:#ffffff;\">v. The screenshots will be stored in our database, and in no way will the privacy of the user will be breached or will be made public without your consent.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Josefin Sans\'; font-size:11pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Josefin Sans\'; font-size:11pt; color:#000000; background-color:#ffffff;\">vi. You can find the screenshots in the same folder where the application is stored. If you notice that any of your private information is captured in the screenshot please contact the developing team or operations team immediately.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Josefin Sans\'; font-size:11pt; font-weight:600; color:#000000;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Josefin Sans\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Josefin Sans\'; font-size:10pt; font-weight:600; color:#000000; background-color:#ffffff;\">By Agreeing to the terms and conditions you agree that you are a registered member of Athrv-Ed. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Josefin Sans\'; font-size:8pt; font-weight:600; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Josefin Sans\'; font-size:8pt; color:#000000; background-color:#ffffff;\">P.S – Please note without accepting the terms and conditions you will not be able to register as a user to the application.</span></p></body></html>"))
        self.label_10.setText(_translate("Terms_conditions", "Productivity Tracker"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Terms_conditions = QtWidgets.QMainWindow()
    ui = Ui_Terms_conditions()
    ui.setupUi(Terms_conditions)
    Terms_conditions.show()
    sys.exit(app.exec_())
