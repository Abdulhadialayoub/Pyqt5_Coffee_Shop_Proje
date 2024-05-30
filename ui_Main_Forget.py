from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets
import pymysql as mycon
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class Ui_Main_Forget(object):
     def setupUi(self, Main_Forget):
            if Main_Forget.objectName():
                Main_Forget.setObjectName(u"Main_Forget")
            Main_Forget.resize(506, 353)
            self.Frame_Forget = QWidget(Main_Forget)
            self.Frame_Forget.setObjectName(u"Frame_Forget")
            self.frame = QFrame(self.Frame_Forget)
            self.frame.setObjectName(u"frame")
            self.frame.setGeometry(QRect(10, 10, 481, 331))
            self.frame.setStyleSheet(u"QFrame {	\n"
                                     "	background-color: rgb(255,192, 128);	\n"
                                     "	color: rgb(220, 220, 220);\n"
                                     "	border-radius: 10px;\n"
                                     "}")
            self.frame.setFrameShape(QFrame.StyledPanel)
            self.frame.setFrameShadow(QFrame.Raised)
            self.label_title_2 = QLabel(self.frame)
            self.label_title_2.setObjectName(u"label_title_2")
            self.label_title_2.setGeometry(QRect(0, 40, 481, 81))
            font = QFont()
            font.setFamily(u"Segoe UI")
            font.setPointSize(40)
            self.label_title_2.setFont(font)
            self.label_title_2.setStyleSheet(u"color: rgb(24,12,0);")
            self.label_title_2.setAlignment(Qt.AlignCenter)
            self.lineEdit = QLineEdit(self.frame)
            self.lineEdit.setObjectName(u"lineEdit")
            self.lineEdit.setGeometry(QRect(80, 170, 311, 41))
            self.lineEdit.setStyleSheet(u"background-color: rgb(255,255,255);\n"
                                        "	color: rgb(24, 12, 0);\n"
                                        "	border-style: none;\n"
                                        "	border-radius: 10px;\n"
                                        "	")
            self.lineEdit.setFrame(False)
            self.toolButton = QToolButton(self.frame)
            self.toolButton.setObjectName(u"toolButton")
            self.toolButton.setGeometry(QRect(250, 250, 181, 41))
            self.toolButton.setStyleSheet(u"background-color: rgb(24,14,0);\n"
                                          "	color: rgb(255, 255, 255);\n"
                                          "	border-style: none;\n"
                                          "	border-radius: 10px;\n"
                                          "	text-align: center;")
            self.toolButton_2 = QToolButton(self.frame)
            self.toolButton_2.setObjectName(u"toolButton_2")
            self.toolButton_2.setGeometry(QRect(40, 250, 181, 41))
            self.toolButton_2.setStyleSheet(u"background-color: rgb(24,14,0);\n"
                                            "	color: rgb(255, 255, 255);\n"
                                            "	border-style: none;\n"
                                            "	border-radius: 10px;\n"
                                            "	text-align: center;")
            Main_Forget.setCentralWidget(self.Frame_Forget)

            self.retranslateUi(Main_Forget)

            QMetaObject.connectSlotsByName(Main_Forget)
            # setupUi
            self.toolButton.clicked.connect(lambda: self.SercahAndSend())
            self.toolButton_2.clicked.connect(lambda:self.Cancel())
     def Emailmsg(self):
        msg = QMessageBox()
        msg.setWindowTitle("ERROR")
        msg.setText("Please write the Email")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()
     def Theaccountmsg(self):
        msg = QMessageBox()
        msg.setWindowTitle("info")
        msg.setText("The account is available we will send your password please check your Email.")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()
     def Theaccount(self):
        msg = QMessageBox()
        msg.setWindowTitle("info")
        msg.setText("The account is Unavailable")
        msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()
     def sendpass(self):
        try:
            from_email = "abdulhadieleyyub17@gmail.com"
            password = "uiug pwpq bfix ndnm"
            Email=self.lineEdit.text()
            mydb = mycon.connect(host="localhost", user="root", password="", database="coffe_shop")
            mycursor = mydb.cursor()
            sql = "SELECT password FROM log_db WHERE Email=%s"
            mycursor.execute(sql, (Email,))
            result = mycursor.fetchone()
            if result:
                db_password = result[0]
                message_body = f"Hi, your password: {db_password}"
            # Email configuration
            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = Email
            msg['Subject'] = "Your Password"
            msg.attach(MIMEText(message_body, 'plain'))

            # Connect to SMTP server
            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.starttls()
            smtp.login(from_email, password)
            #Send email
            smtp.sendmail(from_email,Email, msg.as_string())
            #close SMTP connection
            smtp.quit()
            hata = QMessageBox()
            hata.setWindowTitle("Status")
            hata.setText("The password has be send to your email")
            hata.setIcon(QMessageBox.Information)
            x = hata.exec_()
        except Exception as e:
            hata = QMessageBox()
            hata.setWindowTitle("Error")
            hata.setText(str(e))
            hata.setIcon(QMessageBox.Critical)
            x = hata.exec_()
     def empty(self):
        if self.lineEdit.text() == "":
            return True
        else:
            return False
     def SercahAndSend(self):
        if self.empty():
            self.Emailmsg()
        else:
            try:
                Email= self.lineEdit.text()
                mydb = mycon.connect(host="localhost", user="root", password="", database="coffe_shop")
                mycursor = mydb.cursor()
                mycursor.execute("SELECT * FROM log_db WHERE Email=%s", (Email))
                result = mycursor.fetchone()
                if result:
                   self.Theaccountmsg()
                   self.sendpass()

                else:
                   self.Theaccount()
            except Exception as e:
                hata=QMessageBox()
                hata.setWindowTitle("Error")
                hata.setText(str(e))
                hata.setIcon(QMessageBox.Critical)
                x = hata.exec_()
     def exitmessage(self):
        msg = QMessageBox()
        msg.setWindowTitle("Status")
        msg.setText("You are about to cancel the process. After that, if you want to continue, you should run the app once again.")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        x = msg.exec_()
        if x == QMessageBox.Ok:
            QApplication.quit()
        else:
            msg.Cancel
     def Cancel(self):
        self.exitmessage()
     def retranslateUi(self, Main_Forget):
        Main_Forget.setWindowTitle(QCoreApplication.translate("Main_Forget", u"MainWindow", None))
        self.label_title_2.setText(QCoreApplication.translate("Main_Forget", u"<strong>Coffee</strong> Shop", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Main_Forget", u"Enter The Email", None))
        self.toolButton.setText(QCoreApplication.translate("Main_Forget", u"Serach The Email", None))
        self.toolButton_2.setText(QCoreApplication.translate("Main_Forget", u"Cancel", None))
    # retranslateUi