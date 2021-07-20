import concurrent.futures
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QTableWidgetItem

from login import Ui_LoginDialog
from welcomescreen import Ui_Dialog
from FullMyPhoneBook.signup import  Ui_SignUpDialog
from FullMyPhoneBook.fillprofile import Ui_fillProfileDialog

from tableview import *

import sqlite3


class WelcomeScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.loginDialog.clicked.connect(self.gotologin)
        self.ui.signupButton.clicked.connect(self.gotocreate)

    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotocreate(self):
        create = CreateAccScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class CreateAccScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SignUpDialog()
        self.ui.setupUi(self)
        self.ui.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.confirmField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.signUpButton.clicked.connect(self.signupFunction)

    def signupFunction(self):
        user = self.ui.emailField.text()
        password = self.ui.passwordField.text()
        confirmpassword = self.ui.confirmField.text()
        if len(user) == 0 or len(password) == 0 or len(confirmpassword) == 0:
            self.ui.errorLabel.setText("Заполните все поля!")

        elif password != confirmpassword:
            self.ui.errorLabel.setText("Пароли не совпадают!")

        else:
            conn = sqlite3.connect("shop_data.db")
            cur = conn.cursor()
            user_info = [user, password]
            cur.execute(f"INSERT INTO login_info (username, password) VALUES ('{user}', '{password}')")

            conn.commit()
            conn.close()

            fillprofile = FillProfileScreen()
            widget.addWidget(fillprofile)
            widget.setCurrentIndex(widget.currentIndex() + 1)


class FillProfileScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_fillProfileDialog()
        self.ui.setupUi(self)

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TableDialog()
        self.ui.setupUi(self)
        self.ui.pushButtonDisplayRows.clicked.connect(self.DisplayRows)


    def DisplayRows(self):
        sqlStatement = "SELECT * FROM  phonebook"
        try:
            conn = sqlite3.connect("phonebook2.db")
            cur = conn.cursor()
            cur.execute(sqlStatement)
            rows = cur.fetchall()
            print(rows)
            rowNo = 0

            for tuple in rows:
                colNo = 0
                for columns in tuple:
                    oneColumn = QTableWidgetItem(columns)
                    self.ui.tableWidget.setItem(rowNo, colNo, oneColumn)
                    colNo += 1
                rowNo += 1
        except:
            self.ui.tableWidget.clear()
            self.ui.pushButtonDisplayRows.setText("Error in accessing table")
        finally:
            conn.close()

class LoginScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)
        self.ui.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.loginLoginDialog.clicked.connect(self.loginFunction)

    def loginFunction(self):
        user = self.ui.emailField.text()
        password = self.ui.passwordField.text()
        query = 'SELECT password FROM login_info WHERE username =\'' + user + "\'"

        if len(user) == 0 or len(password) == 0:
            self.ui.errorLabel.setText("Заполните все поля правильно!")
        else:
            try:
                conn = sqlite3.connect("shop_data.db")
                cur = conn.cursor()
                cur.execute(query)
                result_pass = cur.fetchone()
                print(result_pass)
                if result_pass == None:
                    self.ui.errorLabel.setText("Извините бананьев некоректный имя или пароль")

                elif result_pass != [] and result_pass[0] == password:
                    print("Successfull logged it!")
                    mytable = MyForm()
                    widget.addWidget(mytable)
                    widget.setCurrentIndex(widget.currentIndex() + 1)
                else:
                    self.ui.errorLabel.setText("Invalid username or password")

            except:
                self.ui.label_2.setText("Error in accessing row")
            finally:
                conn.close()






if __name__=='__main__':
    app = QApplication(sys.argv)
    welcome = WelcomeScreen()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(welcome)
    widget.setFixedHeight(800)
    widget.setFixedWidth(1200)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Выход")