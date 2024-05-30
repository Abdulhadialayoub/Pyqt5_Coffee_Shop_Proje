from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets
import pymysql as mycon

import LOG_FORM
from ui_Main_Forget import Ui_Main_Forget
from ui_Coffee_Shop import MainApp
import sys

#class ui_Coffee_Shop(QMainWindow):
    #def __init__(self):
      #  QMainWindow.__init__(self)
      #  self.ui = Ui_MainWindow()
      #  self.ui.setupUi(self)
        ## UI ==> INTERFACE CODES
        ########################################################################
      #  self.setWindowModality(QtCore.Qt.ApplicationModal)
class ui_Main_Forget(QMainWindow):
  def __init__(self):
      QMainWindow.__init__(self)
      self.ui=Ui_Main_Forget()
      self.ui.setupUi(self)
      ## UI ==> INTERFACE CODES
      ########################################################################
      self.setWindowModality(QtCore.Qt.ApplicationModal)
      ## REMOVE TITLE BAR
      self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
      self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

class Ui_LOG_FORM:
    def __init__(self):
        self.LOG_FORM = None

    def hide_window(self):
        self.frame.hide()
    def close_page(self):
        self.frame.close()
        self.Stack_back.close()
        self.hide_window()
        self.forpage = ui_Main_Forget()
        self.forpage.show()
    def setupUi(self, LOG_FORM):
          self.LOG_FORM = LOG_FORM
          LOG_FORM.setObjectName("LOG_FORM")
          LOG_FORM.resize(400, 516)
          self.Stack_back = QStackedWidget(LOG_FORM)
          self.Stack_back.setObjectName("Stack_back")
          self.Stack_back.setGeometry(QRect(10, 10, 381, 491))

          self.Login_Page = QWidget()
          self.Login_Page.setObjectName("Login_Page")

          self.frame = QFrame(self.Login_Page)
          self.frame.setObjectName("frame")
          self.frame.setGeometry(QRect(-10, 0, 391, 501))
          self.frame.setStyleSheet(
              "QFrame { background-color: rgb(255,192, 128); color: rgb(220, 220, 220); border-radius: 10px; }")
          self.frame.setFrameShape(QFrame.StyledPanel)
          self.frame.setFrameShadow(QFrame.Raised)

          self.label = QLabel(self.frame)
          self.label.setObjectName(u"label")
          self.label.setGeometry(QRect(90, 20, 221, 141))
          font = QFont()
          font.setFamily(u"Viner Hand ITC")
          font.setPointSize(20)
          self.label.setFont(font)
          self.label.setStyleSheet(u"color: rgb(24, 14, 0);\n"
                                   "	border-style: none;")
          self.label.setPixmap(QPixmap(u":/RES/logo.png"))
          self.label.setScaledContents(True)
          self.label.setAlignment(Qt.AlignCenter)

          self.lineEdit = QLineEdit(self.frame)
          self.lineEdit.setObjectName("lineEdit")
          self.lineEdit.setGeometry(QRect(90, 210, 221, 31))
          self.lineEdit.setStyleSheet(
              "background-color: rgb(255,255,255); color: rgb(24, 12, 0); border-style: none; border-radius: 10px;")
          self.lineEdit_2 = QLineEdit(self.frame)
          self.lineEdit_2.setObjectName(u"lineEdit_2")
          self.lineEdit_2.setGeometry(QRect(90, 310, 221, 31))
          self.lineEdit_2.setStyleSheet(u"background-color: rgb(255,255,255);\n"
                                        "	color: rgb(24, 12,0);\n"
                                        "	border-style: none;\n"
                                        "	border-radius: 10px;\n"
                                        "	")
          self.lineEdit_2.setEchoMode(QLineEdit.Password)
          self.label_2 = QLabel(self.frame)
          self.label_2.setObjectName("label_2")
          self.label_2.setGeometry(QRect(30, 180, 191, 21))
          font1 = QFont()
          font1.setFamily("Viner Hand ITC")
          font1.setPointSize(12)
          self.label_2.setFont(font1)
          self.label_2.setStyleSheet("color: rgb(24, 14, 0); border-style: none;")

          self.label_3 = QLabel(self.frame)
          self.label_3.setObjectName("label_3")
          self.label_3.setGeometry(QRect(20, 280, 91, 20))
          font2 = QFont()
          font2.setFamily("Viner Hand ITC")
          font2.setPointSize(12)
          self.label_3.setFont(font2)
          self.label_3.setStyleSheet("color: rgb(24, 14, 0); border-style: none;")

          self.toolButton_2 = QToolButton(self.frame)
          self.toolButton_2.setObjectName("toolButton_2")
          self.toolButton_2.setGeometry(QRect(210, 370, 161, 31))
          self.toolButton_2.setStyleSheet(
              "background-color: rgb(24,14,0); color: rgb(255, 255, 255); border-style: none; border-radius: 10px; text-align: center;")

          self.toolButton_4 = QToolButton(self.frame)
          self.toolButton_4.setObjectName("toolButton_4")
          self.toolButton_4.setGeometry(QRect(30, 370, 161, 31))
          self.toolButton_4.setStyleSheet(
              "background-color: rgb(24,14,0); color: rgb(255, 255, 255); border-style: none; border-radius: 10px; text-align: center;")

          self.toolButton_5 = QToolButton(self.frame)
          self.toolButton_5.setObjectName("toolButton_5")
          self.toolButton_5.setGeometry(QRect(120, 430, 161, 31))
          self.toolButton_5.setStyleSheet(
              "background-color: rgb(24,14,0); color: rgb(255, 255, 255); border-style: none; border-radius: 10px; text-align: center;")

          self.Stack_back.addWidget(self.Login_Page)

          self.Register_Page = QWidget()
          self.Register_Page.setObjectName("Register_Page")

          self.frame_2 = QFrame(self.Register_Page)
          self.frame_2.setObjectName("frame_2")
          self.frame_2.setGeometry(QRect(0, 0, 381, 501))
          self.frame_2.setStyleSheet(
              "QFrame { background-color: rgb(255,192, 128); color: rgb(220, 220, 220); border-radius: 10px; }")
          self.frame_2.setFrameShape(QFrame.StyledPanel)
          self.frame_2.setFrameShadow(QFrame.Raised)

          self.lineEdit_3 = QLineEdit(self.frame_2)
          self.lineEdit_3.setObjectName("lineEdit_3")
          self.lineEdit_3.setGeometry(QRect(40, 210, 291, 31))
          self.lineEdit_3.setStyleSheet(
              "background-color: rgb(255,255,255); color: rgb(24, 12, 0); border-style: none; border-radius: 10px;")

          self.lineEdit_4 = QLineEdit(self.frame_2)
          self.lineEdit_4.setObjectName("lineEdit_4")
          self.lineEdit_4.setGeometry(QRect(40, 260, 291, 31))
          self.lineEdit_4.setStyleSheet(
              "background-color: rgb(255,255,255); color: rgb(24, 12, 0); border-style: none; border-radius: 10px;")

          self.lineEdit_5 = QLineEdit(self.frame_2)
          self.lineEdit_5.setObjectName("lineEdit_5")
          self.lineEdit_5.setGeometry(QRect(40, 300, 291, 31))
          self.lineEdit_5.setStyleSheet(
              "background-color: rgb(255,255,255); color: rgb(24, 12, 0); border-style: none; border-radius: 10px;")

          self.lineEdit_6 = QLineEdit(self.frame_2)
          self.lineEdit_6.setObjectName("lineEdit_6")
          self.lineEdit_6.setGeometry(QRect(40, 340, 291, 31))
          self.lineEdit_6.setStyleSheet(
              "background-color: rgb(255,255,255); color: rgb(24, 12, 0); border-style: none; border-radius: 10px;")

          self.toolButton = QToolButton(self.frame_2)
          self.toolButton.setObjectName("toolButton")
          self.toolButton.setGeometry(QRect(110, 380, 171, 41))
          self.toolButton.setStyleSheet(
              "background-color: rgb(24,14,0); color: rgb(255, 255, 255); border-style: none; border-radius: 10px; text-align: center;")

          self.label_5 = QLabel(self.frame_2)
          self.label_5.setObjectName("label_5")
          self.label_5.setGeometry(QRect(80, 60, 211, 101))
          self.label_5.setFont(font)
          self.label_5.setStyleSheet("color: rgb(24, 14, 0); border-style: none;")
          self.label_5.setScaledContents(True)
          self.label_5.setAlignment(Qt.AlignCenter)

          self.toolButton_3 = QToolButton(self.frame_2)
          self.toolButton_3.setObjectName("toolButton_3")
          self.toolButton_3.setGeometry(QRect(70, 430, 241, 41))
          self.toolButton_3.setStyleSheet(
              "background-color: rgb(24,14,0); color: rgb(255, 255, 255); border-style: none; border-radius: 10px; text-align: center;")

          self.Stack_back.addWidget(self.Register_Page)

          self.retranslateUi(LOG_FORM)
          self.Stack_back.setCurrentIndex(0)
          QMetaObject.connectSlotsByName(LOG_FORM)


          # Connect buttons to their respective functions
          self.toolButton_2.clicked.connect(self.Login_def)
          self.toolButton.clicked.connect(self.register_def)
          self.toolButton_5.clicked.connect(self.Forget_page)
          self.toolButton_3.clicked.connect(lambda: self.Stack_back.setCurrentIndex(0))
          self.toolButton_4.clicked.connect(lambda: self.Stack_back.setCurrentIndex(1))
    def show_page(self):
        self.LOG_FORM.close()
        self.page=MainApp()
        self.page.show()
        

    def Forget_page(self):
        # Open a new instance of ui_Main_Forget
        self.close_page()
    def showmsg(self):
        msg = QMessageBox()
        msg.setWindowTitle("ERROR")
        msg.setText("Please Fill The Spaces")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()
    def emptyres(self):
        if self.lineEdit_3.text() == "" or self.lineEdit_4.text() == "" or self.lineEdit_5.text() == "" or self.lineEdit_6.text() == "":
            return True
        else:
            return False
    def empty(self):
        if self.lineEdit.text() == "" or self.lineEdit_2.text() == "" :
            return True
        else:
            return False
    # setupUi
    def Login_def(self):
        if self.empty():
            self.showmsg()
        else:
            try:
                Username = self.lineEdit.text()
                Password = self.lineEdit_2.text()
                mydb = mycon.connect(host="localhost", user="root", password="", database="coffe_shop")
                mycursor = mydb.cursor()
                mycursor.execute("SELECT * FROM log_db WHERE (Username=%s OR Email=%s) AND Password=%s", (Username,Username,Password))
                result = mycursor.fetchone()
                if result:
                    self.show_page()
                else:
                    hata = QMessageBox()
                    hata.setWindowTitle("Error")
                    hata.setText("Incorrect Information")
                    hata.setIcon(QMessageBox.Critical)
                    x = hata.exec_()
            except Exception as e:
                hata = QMessageBox()
                hata.setWindowTitle("Error")
                hata.setText(str(e))
                hata.setIcon(QMessageBox.Critical)
                x = hata.exec_()
    def register_def(self):
        if self.emptyres():
            self.showmsg()
        else:
            try:
                Fullname = self.lineEdit_3.text()
                username = self.lineEdit_4.text()
                Email = self.lineEdit_5.text()
                password = self.lineEdit_6.text()
                mydb = mycon.connect(host="localhost", user="root", password="", database="coffe_shop")
                mycursor = mydb.cursor()
                select_query = "SELECT * FROM log_db WHERE Fullname = %s AND Username = %s AND Email = %s AND Password = %s"
                # Execute the select query with the parameters
                mycursor.execute(select_query, (Fullname, username, Email, password))
                # Fetch the result
                result = mycursor.fetchone()
                # Check if the record already exists
                if result:
                    durum=QMessageBox()
                    durum.setWindowTitle("Status")
                    durum.setText("Already Exists")
                    durum.setIcon(QMessageBox.Information)
                    x = durum.exec_()
                else:
                    # Prepare the SQL query for insertion with placeholders
                    insert_query = "INSERT INTO log_db (Fullname, Username, Email, Password) VALUES (%s, %s, %s, %s)"
                    # Execute the insert query with the parameters
                    mycursor.execute(insert_query, (Fullname, username, Email, password))
                    # Commit the transaction
                    mydb.commit()
                    durum2 = QMessageBox()
                    durum2.setWindowTitle("Status")
                    durum2.setText("Successfully Created")
                    durum2.setIcon(QMessageBox.Information)
                    x = durum2.exec_()
            except Exception as e:
                hata=QMessageBox()
                hata.setWindowTitle("Error")
                hata.setText(str(e))
                hata.setIcon(QMessageBox.Critical)
                x = hata.exec_()
    def retranslateUi(self, LOG_FORM):
        LOG_FORM.setWindowTitle(QCoreApplication.translate("LOG_FORM", u"Form", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("LOG_FORM", u"Email Or Username:", None))
        self.label_3.setText(QCoreApplication.translate("LOG_FORM", u"Password:", None))
        self.toolButton_2.setText(QCoreApplication.translate("LOG_FORM", u"L O G I N  I N", None))
        self.toolButton_4.setText(QCoreApplication.translate("LOG_FORM", u"Click here for register", None))
        self.toolButton_5.setText(QCoreApplication.translate("LOG_FORM", u"Forget Password", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("LOG_FORM", u"Full Name", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("LOG_FORM", u"Username", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("LOG_FORM", u"Email", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("LOG_FORM", u"Password", None))
        self.toolButton.setText(QCoreApplication.translate("LOG_FORM", u"S I G N  U P", None))
        self.label_5.setText(QCoreApplication.translate("LOG_FORM", u"Coffee Shop", None))
        self.toolButton_3.setText(QCoreApplication.translate("LOG_FORM", u"Already have an account? Click here", None))
    # retranslateUi
