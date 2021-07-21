import concurrent.futures
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QTableWidgetItem, QMessageBox
from login import Ui_LoginDialog
from welcomescreen import Ui_Dialog
from FullMyPhoneBook.signup import Ui_SignUpDialog
from FullMyPhoneBook.fillprofile import Ui_fillProfileDialog
from FullMyPhoneBook.recoveryPassword import Ui_RecoveryPasswordDialog
from FullMyPhoneBook.renewPassword import Ui_RenewPasswordDialog

from tableview import *

import sqlite3

class WelcomeScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.cancelPushButton.clicked.connect(self.gotoCancel)
        self.ui.signupPushButton.clicked.connect(self.gotoCreate)
        self.ui.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.loginPushButton.clicked.connect(self.loginFunction)
        self.ui.echoPasswordCheckBox.stateChanged.connect(self.dispAmount)
        self.ui.saveMeCheckBox.clicked.connect(self.saveMe)
        self.ui.forgotPasswordPushButton.clicked.connect(self.gotoRecoveryPassword)
        self.ui.changePasswordPushButton.clicked.connect(self.gotoChangePassword)

        self.message = QMessageBox()
        self.message.setStyleSheet("background-color: yellow;")
        self.message.setText("Ошибка авторизации!")

    def saveMe(self):
        """
        сохранить пользователя с паролем в БД , для автоматического входа
        """

    def dispAmount(self):
        """
        Показать / спрятать пароль (password)
        """
        self.ui.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        if self.ui.echoPasswordCheckBox.isChecked() == True:
            self.ui.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)

    def loginFunction(self):
        user = self.ui.nameuserLineEdit.text()
        password = self.ui.passwordLineEdit.text()
        #query = 'SELECT password FROM login_info WHERE username =\'' + user + "\'"
        query = 'SELECT password FROM users WHERE username =\'' + user + "\'"
        if len(user) == 0 or len(password) == 0:
            self.message.setInformativeText("Заполните все поля правильно!")
            self.message.show()
        else:
            try:
                conn = sqlite3.connect("shop_data.db")
            except sqlite3.Error:
                print("База не доступна")
                sys.exit(app.exec_())
            cur = conn.cursor()
            try:
                cur.execute(query)
                result_pass = cur.fetchone()
                print(result_pass)
                if result_pass == None:
                    self.message.setInformativeText("Такого пользователя нет!")
                    self.message.show()
                elif result_pass != [] and result_pass[0] == password:
                    print("Successfull logged it!")
                    mytable = MyForm()
                    widget.addWidget(mytable)
                    widget.setCurrentIndex(widget.currentIndex() + 1)
                else:
                    self.message.setInformativeText("Ошибка имени или пароля!")
                    self.message.show()

            except:
                self.message.setInformativeText("Ошибка доступа к записям!")
                self.message.show()
            finally:
                cur.close()
                conn.close()

    def gotoRecoveryPassword(self):
        recovery = RecoveryPassword()
        widget.addWidget(recovery)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoChangePassword(self):
        change = ChangePassword()
        widget.addWidget(change)
        widget.setCurrentIndex(widget.currentIndex() + 1)


    def gotoCreate(self):
        create = CreateAccScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoCancel(self):
        sys.exit(app.exec_())

class ChangePassword(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RenewPasswordDialog()
        self.ui.setupUi(self)
        self.ui.recoveryPasswordPushButton.clicked.connect(self.renewPasswordFunction)
        self.ui.cancelPushButton.clicked.connect(self.gotoCansel)

        self.message = QMessageBox()
        self.message.setStyleSheet("background-color: red;")
        self.message.setText("Ошибка регистрации!")

    def gotoCansel(self):
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoWelcome(self):
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def renewPasswordFunction(self):
        selectStament  = "SELECT username, password FROM users Where username like '" + self.ui.emailField.text() +\
                "'and password like'" + self.ui.oldPasswordField.text()+"'"
        try:
            conn = sqlite3.connect("shop_data.db")
        except sqlite3.Error:
            print("база не доступна")
            sys.exit(app.exec_())
        cur = conn.cursor()
        try:
            cur.execute(selectStament)
            row = cur.fetchone()
            if row == None:
                self.message.setInformativeText("Некорректный email или password!")
                self.message.show()
            else:
                if self.ui.newPasswordField.text() == self.ui.renewPasswordField.text():
                    updateStament = "UPDATE users set password = '" + self.ui.newPasswordField.text() +\
                                    "' WHERE username like'" + self.ui.emailField.text() + "'"
                    with conn:
                        cur.execute(updateStament)
                        self.message.setStyleSheet("background-color: green;")
                        self.message.setText("Пароль изменен!")
                        self.message.setInformativeText(f"Вы успешно изменили пароль")
                        self.message.show()
                        self.gotoWelcome()
                else:
                    print("Два пароля не совпадают")
        except sqlite3.IntegrityError as e:
            print("Error in accessing", e)
        finally:
            cur.close()
            conn.close()

class RecoveryPassword(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RecoveryPasswordDialog()
        self.ui.setupUi(self)
        self.ui.recoveryPasswordPushButton.clicked.connect(self.recoverysignupFunction)
        self.ui.cancelPushButton.clicked.connect(self.gotoCansel)

        self.message = QMessageBox()
        self.message.setStyleSheet("background-color: red;")
        self.message.setText("Ошибка регистрации!")

    def gotoCansel(self):
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoWelcome(self):
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def recoverysignupFunction(self):
        user = self.ui.recoveryPasswordField.text()
        select = 'SELECT * FROM users WHERE username =\'' + user + "\'"

        try:
            conn = sqlite3.connect("shop_data.db")
        except sqlite3.Error:
            print("База не доступна")
            sys.exit(app.exec_())
        cur = conn.cursor()
        try:
            cur.execute(select)
            row = cur.fetchone()
            print(row)
            if row == None:
                self.message.setInformativeText("Такого пользователя нет!")
                self.message.show()
            elif row != []:
                print("Отправить пароль на почту!")
                print(f"Был пароль {row[1]} ")
                query_update = 'UPDATE users set password="89999" WHERE username =\'' + user + "\'"
                cur.execute(query_update)
                conn.commit()
                self.message.setStyleSheet("background-color: green;")
                self.message.setText("Пароль изменен!")
                self.message.setInformativeText(f"Вы успешно изменили пароль с ником - {user}")
                self.message.show()
                self.gotoWelcome()

            else:
                self.message.setInformativeText("Ошибка имени или пароля!")
                self.message.show()
        except sqlite3.IntegrityError:
            conn.rollback()
        finally:
            cur.close()
            conn.close()

class CreateAccScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SignUpDialog()
        self.ui.setupUi(self)
        self.ui.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.confirmField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.signUpPushButton.clicked.connect(self.signupFunction)
        self.ui.cancelPushButton.clicked.connect(self.gotoCansel)


        self.message = QMessageBox()
        self.message.setStyleSheet("background-color: red;")
        self.message.setText("Ошибка регистрации!")

    def gotoWelcome(self):
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoCansel(self):
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoFillProfile(self):
        fillprofile = FillProfileScreen()
        widget.addWidget(fillprofile)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def signupFunction(self):
        user = self.ui.nameuserField.text()
        password = self.ui.passwordField.text()
        confirmpassword = self.ui.confirmField.text()
        query = f"INSERT INTO users (username, password) VALUES ('{user}', '{password}')"
        if len(user) == 0 or len(password) == 0 or len(confirmpassword) == 0:
            self.message.setInformativeText("Заполните все поля!")
            self.message.show()

        elif password != confirmpassword:
            self.message.setInformativeText("Пароли не совпадают!")
            self.message.show()

        else:
            try:
                conn = sqlite3.connect("shop_data.db")
            except sqlite3.Error:
                print("База не доступна")
                sys.exit(app.exec_())
            cur = conn.cursor()

            try:
                cur.execute(query)
                conn.commit()
                self.message.setStyleSheet("background-color: green;")
                self.message.setText("Успешная регистрация!")
                self.message.setInformativeText(f"Вы успешно зарегистрированы с ником - {user}")
                self.message.show()
                self.gotoWelcome()
                # self.gotoFillProfile()
            except sqlite3.IntegrityError:
                conn.rollback()
                self.message.setInformativeText("Пользователь с таким именем уже есть")
                self.message.show()
            finally:
                cur.close()
                conn.close()





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
        self.ui.displayRowspushButton.clicked.connect(self.DisplayRows)



    def DisplayRows(self):
        sqlStatement = "SELECT * FROM  phonebook"
        try:
            conn = sqlite3.connect("phonebook2.db")
        except sqlite3.Error:
            print("База не доступна")
            sys.exit(app.exec_())
        cur = conn.cursor()
        try:
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
        except sqlite3.IntegrityError:
            self.ui.tableWidget.clear()
            self.message.setInformativeText("Ошибка доступа к таблице")
            self.message.show()
        finally:
            cur.close()
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