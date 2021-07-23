

import concurrent.futures
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QTableWidgetItem, QMessageBox

from FullMyPhoneBook.tableview import Ui_TableDialog
from FullMyPhoneBook.tableview2 import Ui_TableDialog2
from FullMyPhoneBook.welcomescreen import Ui_Dialog
from FullMyPhoneBook.signup import Ui_SignUpDialog
from FullMyPhoneBook.fillprofile import Ui_fillProfileDialog
from FullMyPhoneBook.recoveryPassword import Ui_RecoveryPasswordDialog
from FullMyPhoneBook.renewPassword import Ui_RenewPasswordDialog
from FullMyPhoneBook.insertnewrecord import Ui_InsertDialog


import sqlite3


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TableDialog()
        self.ui.setupUi(self)
        self.ui.displayRowspushButton.clicked.connect(self.DisplayRows)
        self.ui.ABsearchPushButton_1.clicked.connect(self.SearchRows_1)
        self.ui.VGsearchPushButton_2.clicked.connect(self.SearchRows_2)
        self.ui.DEsearchPushButton_3.clicked.connect(self.SearchRows_3)
        self.ui.GZIIsearchPushButton_4.clicked.connect(self.SearchRows_4)
        self.ui.KLsearchPushButton_5.clicked.connect(self.SearchRows_5)
        self.ui.MNsearchPushButton_6.clicked.connect(self.SearchRows_6)
        self.ui.OPsearchPushButton_7.clicked.connect(self.SearchRows_7)
        self.ui.RSsearchPushButton_8.clicked.connect(self.SearchRows_8)
        self.ui.TYsearchPushButton_9.clicked.connect(self.SearchRows_9)
        self.ui.FHsearchPushButton_10.clicked.connect(self.SearchRows_10)
        self.ui.ZHSSsearchPushButton_11.clicked.connect(self.SearchRows_11)
        self.ui.IEsearchPushButton_12.clicked.connect(self.SearchRows_12)
        self.ui.YouYjasearchPushButton_13.clicked.connect(self.SearchRows_13)

        self.ui.addPushButton.clicked.connect(self.gotoInsertNewRecord)


    def gotoInsertNewRecord(self):
        insertnewrecord = InsertNewRecord()
        widget.addWidget(insertnewrecord)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def SearchRows_1(self):
        sql = self.sqlBase('А', 'Бя')
        self.SearchRows(sql)


    def SearchRows_2(self):
        sql = self.sqlBase('В', 'Гя')
        self.SearchRows(sql)

    def SearchRows_3(self):
        sql = self.sqlBase('Д', 'Ея')
        self.SearchRows(sql)


    def SearchRows_4(self):
        sql = self.sqlBase('Ж', 'Йя')
        self.SearchRows(sql)


    def SearchRows_5(self):
        sql = self.sqlBase('К', 'Ля')
        self.SearchRows(sql)


    def SearchRows_6(self):
        sql = self.sqlBase('М', 'Ня')
        self.SearchRows(sql)


    def SearchRows_7(self):
        sql = self.sqlBase('О', 'Пя')
        self.SearchRows(sql)


    def SearchRows_8(self):
        sql = self.sqlBase('Р', 'Ся')
        self.SearchRows(sql)


    def SearchRows_9(self):
        sql = self.sqlBase('Т', 'Уя')
        self.SearchRows(sql)


    def SearchRows_10(self):
        sql = self.sqlBase('Ф', 'Хя')
        self.SearchRows(sql)


    def SearchRows_11(self):
        sql = self.sqlBase('Ц', 'Щя')
        self.SearchRows(sql)


    def SearchRows_12(self):
        sql = self.sqlBase('Ъ', 'Эя')
        self.SearchRows(sql)


    def SearchRows_13(self):
        sql = self.sqlBase('Ю', 'Яя')
        self.SearchRows(sql)

    def sqlBase(self, a, b):
        sql = f"SELECT name, nomer, year, day, month FROM phonebook WHERE name >=" \
              f" '{a}' AND name <= '{b}'  ORDER BY name ASC"
        return sql

    def SearchRows(self, sqlStatement):
        try:
            conn = sqlite3.connect("ph_book1.db")
        except sqlite3.Error:
            print("База не доступна")
            sys.exit(app.exec_())
        cur = conn.cursor()
        try:
            cur.execute(sqlStatement)
            rows = cur.fetchall()
            print(rows)
            rowNo = 0
            self.ui.selectTableWidget.clear()
            for tuple in rows:
                colNo = 0
                for columns in tuple:
                    oneColumn = QTableWidgetItem(columns)
                    self.ui.selectTableWidget.setItem(rowNo, colNo, oneColumn)
                    colNo += 1
                rowNo += 1
        except sqlite3.IntegrityError:
            self.ui.selectTableWidget.clear()
            self.message.setInformativeText("Ошибка доступа к таблице")
            self.message.show()
        finally:
            cur.close()
            conn.close()

    def DisplayRows(self):
        """
        вывести все записи таблицы '..nameTable...'
        """
        sqlStatement = "SELECT * FROM  phonebook Order By name asc"
        #sqlStatement = "SELECT * FROM phonebook WHERE name < 'И' ORDER BY family desc"
        try:
            conn = sqlite3.connect("ph_book1.db")
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
                    self.ui.allTableWidget.setItem(rowNo, colNo, oneColumn)
                    colNo += 1
                rowNo += 1
        except sqlite3.IntegrityError:
            self.ui.allTableWidget.clear()
            self.message.setInformativeText("Ошибка доступа к таблице")
            self.message.show()
        finally:
            cur.close()
            conn.close()
class MyForm2(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TableDialog2()
        self.ui.setupUi(self)
        self.ui.ABsearchPushButton_1.clicked.connect(self.SearchRows_1)
        self.ui.VGsearchPushButton_2.clicked.connect(self.SearchRows_2)
        self.ui.DEsearchPushButton_3.clicked.connect(self.SearchRows_3)
        self.ui.GZIIsearchPushButton_4.clicked.connect(self.SearchRows_4)
        self.ui.KLsearchPushButton_5.clicked.connect(self.SearchRows_5)
        self.ui.MNsearchPushButton_6.clicked.connect(self.SearchRows_6)
        self.ui.OPsearchPushButton_7.clicked.connect(self.SearchRows_7)
        self.ui.RSsearchPushButton_8.clicked.connect(self.SearchRows_8)
        self.ui.TYsearchPushButton_9.clicked.connect(self.SearchRows_9)
        self.ui.FHsearchPushButton_10.clicked.connect(self.SearchRows_10)
        self.ui.ZHSSsearchPushButton_11.clicked.connect(self.SearchRows_11)
        self.ui.IEsearchPushButton_12.clicked.connect(self.SearchRows_12)
        self.ui.YouYjasearchPushButton_13.clicked.connect(self.SearchRows_13)

        self.ui.addPushButton.clicked.connect(self.insertNewRecord)


    #def gotoInsertNewRecord(self):
    #    insertnewrecord = InsertNewRecord()
    #    widget.addWidget(insertnewrecord)
    #    widget.setCurrentIndex(widget.currentIndex() + 1)
    #def gotoMyForm2(self):
        #myform = MyForm2()
        #widget.addWidget(myform)
        #widget.setCurrentIndex(widget.currentIndex() + 1)

    def insertNewRecord(self):
        name = self.ui.nameLineEdit.text()
        nomer = self.ui.nomerLineEdit.text()
        day = self.ui.dayLineEdit.text()
        month = self.ui.monthLineEdit.text()
        year = self.ui.yearLineEdit.text()

        try:
            conn = sqlite3.connect("ph_book1.db")
        except sqlite3.Error:
            print("База не доступна")
            sys.exit(app.exec_())
        cur = conn.cursor()

        try:
            query = f"INSERT INTO phonebook (name, nomer, day, month, year) VALUES ('{name}', '{nomer}', '{day}','{month}','{year}')"
            cur.execute(query)
            conn.commit()
            print("Добавлена успешно!")
            #self.gotoMyForm2()
        except sqlite3.IntegrityError:
            conn.rollback()
            print("Произошла ошибка доступа")

        finally:

            cur.close()
            conn.close()

    def SearchRows_1(self):
        sql = self.sqlBase('А', 'В')
        self.SearchRows(sql)
    def SearchRows_2(self):
        sql = self.sqlBase('В', 'Д')
        self.SearchRows(sql)

    def SearchRows_3(self):
        sql = self.sqlBase('Д', 'Ж')
        self.SearchRows(sql)


    def SearchRows_4(self):
        sql = self.sqlBase('Ж', 'К')
        self.SearchRows(sql)


    def SearchRows_5(self):
        sql = self.sqlBase('К', 'М')
        self.SearchRows(sql)


    def SearchRows_6(self):
        sql = self.sqlBase('М', 'О')
        self.SearchRows(sql)


    def SearchRows_7(self):
        sql = self.sqlBase('О', 'Р')
        self.SearchRows(sql)


    def SearchRows_8(self):
        sql = self.sqlBase('Р', 'Т')
        self.SearchRows(sql)


    def SearchRows_9(self):
        sql = self.sqlBase('Т', 'Ф')
        self.SearchRows(sql)


    def SearchRows_10(self):
        sql = self.sqlBase('Ф', 'Ц')
        self.SearchRows(sql)


    def SearchRows_11(self):
        sql = self.sqlBase('Ц', 'Ъ')
        self.SearchRows(sql)


    def SearchRows_12(self):
        sql = self.sqlBase('Ъ', 'Ю')
        self.SearchRows(sql)


    def SearchRows_13(self):
        sql = self.sqlBase('Ю', 'Яя')
        self.SearchRows(sql)

    def sqlBase(self, a, b):
        sql = f"SELECT name, nomer, year, day, month FROM phonebook WHERE name >=" \
              f" '{a}' AND name <= '{b}'  ORDER BY name ASC"
        return sql

    def SearchRows(self, sqlStatement):
        try:
            conn = sqlite3.connect("ph_book1.db")
        except sqlite3.Error:
            print("База не доступна")
            sys.exit(app.exec_())
        cur = conn.cursor()
        try:
            cur.execute(sqlStatement)
            rows = cur.fetchall()
            print(rows)
            rowNo = 0
            self.ui.selectTableWidget.clear()
            for tuple in rows:
                colNo = 0
                for columns in tuple:
                    oneColumn = QTableWidgetItem(columns)
                    self.ui.selectTableWidget.setItem(rowNo, colNo, oneColumn)
                    colNo += 1
                rowNo += 1
        except sqlite3.IntegrityError:
            self.ui.selectTableWidget.clear()
            self.message.setInformativeText("Ошибка доступа к таблице")
            self.message.show()
        finally:
            cur.close()
            conn.close()




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
        self.ui.saveMeCheckBox.stateChanged.connect(self.saveMe)
        self.ui.forgotPasswordPushButton.clicked.connect(self.gotoRecoveryPassword)
        self.ui.changePasswordPushButton.clicked.connect(self.gotoChangePassword)

        self.message = QMessageBox()
        self.message.setStyleSheet("background-color: yellow;")
        self.message.setText("Ошибка авторизации!")

    def saveMe(self):
        """
        сохранить пользователя с паролем в БД , для автоматического входа
        """
        if self.ui.saveMeCheckBox.isChecked():
            print("Нажата")
        user = self.ui.nameuserLineEdit.text()
        password = self.ui.passwordLineEdit.text()
        query = f"INSERT INTO saveme (email, password) VALUES ('{user}', '{password}')"
        try:
            conn = sqlite3.connect("ph_book1.db")
        except sqlite3.Error:
            print("База не доступна")
            sys.exit(app.exec_())
        cur = conn.cursor()

        try:
            cur.execute(query)
            conn.commit()
        except sqlite3.IntegrityError:
            conn.rollback()
        finally:

            cur.close()
            conn.close()

        print("Отжата")
        if self.ui.echoPasswordCheckBox.isChecked() == True:
            print("Нажата")

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
        query = 'SELECT password FROM users WHERE email =\'' + user + "\'"
        if len(user) == 0 or len(password) == 0:
            self.message.setInformativeText("Заполните все поля правильно!")
            self.message.show()
        else:
            try:
                conn = sqlite3.connect("ph_book1.db")
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
                    if user == 'admin@admin.com':
                        mytable = MyForm()
                    else:
                        mytable = MyForm2()
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

    def gotoWelcome(self):
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex() + 1)

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
        selectStament  = "SELECT email, password FROM users Where email like '" + self.ui.emailField.text() +\
                "'and password like'" + self.ui.oldPasswordField.text()+"'"
        try:
            conn = sqlite3.connect("ph_book1.db")
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
                    updateStament = " UPDATE users set password = '" + self.ui.newPasswordField.text() +\
                                    "' WHERE email like '" + self.ui.emailField.text() + "'"
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
        select = 'SELECT * FROM users WHERE email =\'' + user + "\'"

        try:
            conn = sqlite3.connect("ph_book1.db")
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
                query_update = 'UPDATE users set password="89999" WHERE email =\'' + user + "\'"
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
        query = f"INSERT INTO users (email, password) VALUES ('{user}', '{password}')"
        if len(user) == 0 or len(password) == 0 or len(confirmpassword) == 0:
            self.message.setInformativeText("Заполните все поля!")
            self.message.show()

        elif password != confirmpassword:
            self.message.setInformativeText("Пароли не совпадают!")
            self.message.show()

        else:
            try:
                conn = sqlite3.connect("ph_book1.db")
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

class InsertNewRecord(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_InsertDialog()
        self.ui.setupUi(self)

        self.ui.insertPushButton.clicked.connect(self.insertFunction)
        self.ui.cancelPushButton.clicked.connect(self.gotoCansel)

        self.message = QMessageBox()
        self.message.setStyleSheet("background-color: red;")
        self.message.setText("Ошибка регистрации!")

    def gotoCansel(self):
        myform = MyForm()
        widget.addWidget(myform)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoMyForm(self):
        myform = MyForm()
        widget.addWidget(myform)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def insertFunction(self):
        name = self.ui.nameField.text()
        nomer = self.ui.nomerField.text()
        day = self.ui.dayField.text()
        month = self.ui.monthField.text()
        year = self.ui.yearField.text()


        try:
            conn = sqlite3.connect("ph_book1.db")
        except sqlite3.Error:
            print("База не доступна")
            sys.exit(app.exec_())
        cur = conn.cursor()

        try:
            query = f"INSERT INTO phonebook (name, nomer, day, month, year) VALUES ('{name}', '{nomer}', '{day}','{month}','{year}')"
            cur.execute(query)
            conn.commit()
            self.message.setStyleSheet("background-color: green;")
            self.message.setText("Успешнно добавлен!")
            self.message.setInformativeText(f"{name} успешно добален в телефонную книгу")
            self.message.show()
            self.gotoMyForm()
        except sqlite3.IntegrityError:
            conn.rollback()
            self.message.setInformativeText("Пользователь с таким именем уже есть")
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
