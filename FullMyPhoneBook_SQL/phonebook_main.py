import sys
from datetime import datetime

import MySQLdb
import psycopg2
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMessageBox

from Ui.tableview import Ui_TableDialog

from Ui.tableview2 import Ui_TableDialog2
from Ui.welcomescreen import Ui_Dialog
from Ui.signup import Ui_SignUpDialog
from fillprofile import Ui_fillProfileDialog
from Ui.recoveryPassword import Ui_RecoveryPasswordDialog
from Ui.renewPassword import Ui_RenewPasswordDialog
from Ui.birthdayonweek import Ui_BirthDayTableDialog

import sqlite3

saveuser = ""
savepassword = ""


class DataBaseConnection:
    def dataBaseOpenSqlite(self):
        """
        Соединение с базой данных Sqlite
        :return: conn
        """
        try:
            conn = sqlite3.connect("DataBase/ph_book1.db")
        except sqlite3.Error:
            print("База не доступна")
            sys.exit(app.exec_())
        return conn

    def dataBaseOpenMySqldb(self):
        """
        Соединение с базой данных Sqlite
        :return: conn
        """
        try:
            conn = MySQLdb.connect(host="localhost",
                                   user="user1",
                                   passwd="password1",
                                   db="shop")
        except MySQLdb.OperationalError:
            print("База не доступна")
            sys.exit(app.exec_())
        return conn

    def dataBaseOpenPostgre(self):
        """
         Соединение с базой данных Sqlite
         :return: conn
         """
        try:
            conn = psycopg2.connect(database="studentdb",
                                    user="user1",
                                    password="password1",
                                    host="127.0.0.1",
                                    port="5432"
                                    )
        except psycopg2.OperationalError:
            print("База не доступна")
            sys.exit(app.exec_())
        return conn

class MessageBox(QMessageBox):
    def __init__(self):
        QMessageBox.__init__(self)
        self.setText("This is a MessageBox, typically used to convey short messages to the user.")
        #self.setInformativeText("Informative text provides more space to explain the message ")
        #self.setIcon(QMessageBox.Information)
        self.setStandardButtons(QMessageBox.Close)

class BaseForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TableDialog()
        self.ui.setupUi(self)

        self.message = QMessageBox()
        self.dbconn = DataBaseConnection()

    def editLineClear(self):
        """
        Обнуляет поля LineEdit (4 шт)
        :return:
        """
        for line in self.list_line_edit:
            line.clear()

    def SearchRows_1(self):
        """
        Слот - Передает sql в метод выборки SearchRows
        :return:
        """
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
        sql = self.sqlBase('Ю', 'Яяяя')
        self.SearchRows(sql)

    def SearchRows_14(self):
        sql = self.sqlBase('A', 'zzz')
        self.SearchRows(sql)

    def SearchRows_All(self):
        """
        Слот-метод , загружает все записи из Таблицы
        :return:
        """
        sql = f"SELECT name, nomer, year, month, day from phonebook ORDER By name"
        self.SearchRows(sql)

    def sqlBase(self, a, b):
        """
        Подготавливает SQL запрос
        :param a: начальная точка поиска
        :param b: конечная точка поиска
        :return: sql
        """
        sql = f"SELECT name, nomer, year, month, day FROM phonebook WHERE name >=" \
              f" '{a}' AND name <= '{b}'  ORDER BY name ASC"
        return sql

    def SearchRows(self, sqlStatement=f"SELECT name, nomer, year, month, day from phonebook ORDER By name"):
        """
        Поиск записей по SQL запросу.
        По умолчанию загружает все записи из Таблицы
        :param sqlStatement:
        :return:
        """
        conn = self.dbconn.dataBaseOpenSqlite()
        cur = conn.cursor()
        cur.execute(sqlStatement)
        rows = cur.fetchall()
        row = 0
        self.ui.tableWidget.setRowCount(len(rows))
        for person in rows:
            print(person)
            self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person[0]))
            self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(person[1]))
            self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(person[2])))
            self.ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(person[3])))
            self.ui.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(person[4])))
            row += 1
        cur.close()
        conn.close()

    def gotoWelcome(self):
        """
        Переход на главный экран приложения
        :return:
        """
        global saveuser, savepassword
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        # сохраняем пользователя и пароль в текущей сессии
        welcome.ui.nameuserLineEdit.setText(saveuser)
        welcome.ui.passwordLineEdit.setText(savepassword)

class MyFormUser(BaseForm):
    def __init__(self):
        super().__init__()

        # Кнопки сортировки
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
        self.ui.AZsearchPushButton_14.clicked.connect(self.SearchRows_14)

        # кнопка загрузки всех данных в главную страницу таблицы
        self.ui.ALLsearchPushButton_16.clicked.connect(self.SearchRows_All)

        self.ui.labelUser.setText(saveuser)

        self.ui.cancelPushButton.clicked.connect(self.gotoWelcome)

        # Ширина колонок таблицы
        self.ui.tableWidget.setColumnWidth(0, 200)
        self.ui.tableWidget.setColumnWidth(1, 200)
        self.ui.tableWidget.setColumnWidth(2, 100)
        self.ui.tableWidget.setColumnWidth(3, 100)
        self.ui.tableWidget.setColumnWidth(4, 100)
        self.ui.tableWidget.setSortingEnabled(True)

        self.SearchRows()

class InheretensFormTableAdmin(MyFormUser):
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
        self.ui.AZsearchPushButton_14.clicked.connect(self.SearchRows_14)
        self.ui.ALLsearchPushButton_16.clicked.connect(self.SearchRows_All)

        self.ui.cancelPushButton.clicked.connect(self.gotoWelcome)

        self.ui.addPushButton.clicked.connect(self.insertNewRecord)
        self.ui.updatePushButton.clicked.connect(self.updateRecord)
        self.ui.deletePushButton.clicked.connect(self.deleteRecord)

        self.list_line_edit = [self.ui.nameLineEdit,
                               self.ui.nomerLineEdit,
                               self.ui.yearLineEdit,
                               self.ui.monthLineEdit,
                               self.ui.dayLineEdit,
                               ]

        self.ui.tableWidget.setColumnWidth(0, 200)
        self.ui.tableWidget.setColumnWidth(1, 200)
        self.ui.tableWidget.setColumnWidth(2, 100)
        self.ui.tableWidget.setColumnWidth(3, 100)
        self.ui.tableWidget.setColumnWidth(4, 100)
        self.ui.tableWidget.setSortingEnabled(True)

        self.SearchRows()
        self.ui.tableWidget.cellClicked.connect(self.cellClick)  # установить обработчик щелча мыши в таблице

    def SearchRows_All(self):
        """
        (Переопределенный метод)
        Слот-метод, очищает поля и выводит все записи
        :return:
        """
        sql = f"SELECT name, nomer, year, month, day from phonebook ORDER By name"
        self.SearchRows(sql)
        self.editLineClear()  # обнуляет 4 поля LineEdit

    def sqlBase(self, a, b):
        """
        (Переопределеннный метод)
        Подготавливает SQL запрос
        :param a: начальная точка поиска
        :param b: конечная точка поиска
        :return: sql
        """
        sql = f"SELECT name, nomer, year, month, day FROM phonebook WHERE name >=" \
              f" '{a}' AND name <= '{b}'  ORDER BY name ASC"
        self.editLineClear()  # обнуляет 4 поля LineEdit
        return sql

    def cellClick(self, row, col):
        """
        обработка щелчка мыши по таблице
        :param row: номер строки
        :param col: номер столбца
        :return:
        """
        self.ui.nameLineEdit.setText(self.ui.tableWidget.item(row, 0).text().strip())
        self.ui.nomerLineEdit.setText(self.ui.tableWidget.item(row, 1).text().strip())
        self.ui.yearLineEdit.setText(self.ui.tableWidget.item(row, 2).text().strip())
        self.ui.monthLineEdit.setText(self.ui.tableWidget.item(row, 3).text().strip())
        self.ui.dayLineEdit.setText(self.ui.tableWidget.item(row, 4).text().strip())

    def insertNewRecord(self):
        """
        Вставка новой записи в Таблицу
        :return:
        """
        name = self.ui.nameLineEdit.text().capitalize()
        nomer = self.ui.nomerLineEdit.text()
        day = self.ui.dayLineEdit.text()
        month = self.ui.monthLineEdit.text()
        year = self.ui.yearLineEdit.text()
        query = f"INSERT INTO phonebook (name, nomer, day, month, year) VALUES ('{name}', '{nomer}', '{day}','{month}','{year}')"
        conn = self.dbconn.dataBaseOpenSqlite()
        cur = conn.cursor()
        try:
            cur.execute(query)
            conn.commit()
            self.editLineClear()
            print("Добавлена успешно!")
            self.SearchRows_All()
        except sqlite3.IntegrityError:
            conn.rollback()
            self.message.setInformativeText("Произошла ошибка доступа")
            self.message.show()
            print("Произошла ошибка доступа")
        finally:
            conn.close()

    def updateRecord(self):
        """
        Изменение записи в Таблице
        :return:
        """
        name = self.ui.nameLineEdit.text().capitalize()
        nomer = self.ui.nomerLineEdit.text()
        day = self.ui.dayLineEdit.text()
        month = self.ui.monthLineEdit.text()
        year = self.ui.yearLineEdit.text()
        query = f"SELECT * from phonebook where name='{name}'"
        conn = self.dbconn.dataBaseOpenSqlite()
        cur = conn.cursor()
        cur.execute(query)
        row = cur.fetchone()
        try:
            if row == None:
                print("Нет такой фамилии в таблице")
            else:
                print("Есть такая фамилия")
                name = row[0]
                print(name)
            query_update = f"UPDATE phonebook SET nomer='{nomer}', day='{day}'," \
                           f" month='{month}', year='{year}' WHERE name='{name}'"
            cur.execute(query_update)
            conn.commit()
            self.editLineClear()
            self.SearchRows_All()
            print("Изменения проведены успешно")
        except sqlite3.IntegrityError:
            conn.rollback()
            self.message.setInformativeText("Ошибка операции изменения записи")
            self.message.show()
        finally:
            conn.close()

    def deleteRecord(self):
        name = self.ui.nameLineEdit.text()
        query = f"SELECT * FROM phonebook WHERE name='{name}'"
        query_delete = f"DELETE from phonebook WHERE name='{name}'"
        conn = self.dbconn.dataBaseOpenSqlite()
        cur = conn.cursor()
        try:
            cur.execute(query)
            row = cur.fetchone()
            if row == None:
                print("Нет такого контакта в таблице")
            else:
                print("Есть такая информайия о контакте")
                cur.execute(query_delete)
                print("Контакт удален!")
                conn.commit()
                self.editLineClear()
                self.SearchRows_All()
        except sqlite3.IntegrityError:
            conn.rollback()
            self.message.setInformativeText("Произошла ошибка операции удаления")
            self.message.show()
        finally:
            conn.close()

class WelcomeScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.cancelPushButton.clicked.connect(self.gotoExit)
        self.ui.signupPushButton.clicked.connect(self.gotoCreate)
        self.ui.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.loginPushButton.clicked.connect(self.loginFunction)

        self.ui.echoPasswordCheckBox.stateChanged.connect(self.dispAmount)
        self.ui.saveMeCheckBox.clicked.connect(self.saveMe)

        self.ui.forgotPasswordPushButton.clicked.connect(self.gotoRecoveryPassword)
        self.ui.changePasswordPushButton.clicked.connect(self.gotoChangePassword)
        self.ui.birthDayPushButtn.clicked.connect(self.gotoBirthDayOnWeek)

        #Если стоит галка сохранить, то должны запуститься эти две строки
        #if self.ui..... self.ui.saveMeCheckBox.stateChanged.connect(self.saveMe)
        #self.ui.nameuserLineEdit.setText("")
        #self.ui.passwordLineEdit.setText("")
        #self.saveuser = ""
        #self.savepassword = ""

        self.message = QMessageBox()
        self.message.setStyleSheet("background-color: yellow;")
        self.message.setText("Ошибка авторизации!")

        self.dbconn = DataBaseConnection()

    def saveMe(self):
        pass

    def saveMe_reserv(self):
        """
        сохранить пользователя с паролем в БД , для автоматического входа
        """
        if self.ui.saveMeCheckBox.isChecked():
            print("Нажата")
        user = self.ui.nameuserLineEdit.text()
        password = self.ui.passwordLineEdit.text()
        query = f"INSERT INTO saveme (email, password) VALUES ('{user}', '{password}')"
        conn = self.dbconn.dataBaseOpenSqlite()
        cur = conn.cursor()
        try:
            cur.execute(query)
            conn.commit()
        except sqlite3.IntegrityError:
            conn.rollback()
        finally:

            cur.close()
            conn.close()

    def dispAmount(self):
        """
        Показать / спрятать пароль (password)
        """
        print("Мы тут")
        self.ui.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        if self.ui.echoPasswordCheckBox.isChecked() == True:
            self.ui.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
            print("Wea are here")


    def loginFunction(self):
        global saveuser, savepassword
        user = self.ui.nameuserLineEdit.text()
        password = self.ui.passwordLineEdit.text()
        query = 'SELECT password FROM users WHERE email =\'' + user + "\'"
        if len(user) == 0 or len(password) == 0:
            self.message.setInformativeText("Заполните все поля правильно!")
            self.message.show()
        else:
            conn = self.dbconn.dataBaseOpenSqlite()
            cur = conn.cursor()
            try:
                cur.execute(query)
                row = cur.fetchone()
                if row == None:
                    self.message.setInformativeText("Такого пользователя нет!")
                    self.message.show()
                elif row != [] and row[0] == password:
                    print("Successfull logged it!")

                    if user == 'admin':  #'admin@admin.com':
                        saveuser = user
                        savepassword = password
                        mytable = InheretensFormTableAdmin()

                    else:
                        saveuser = user
                        savepassword = password
                        mytable = MyFormUser()
                        print("а это было", saveuser, savepassword)

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

    def gotoBirthDayOnWeek(self):
        birthday = BirthDayOnWeek()
        widget.addWidget(birthday)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    #def gotoWelcome(self):
    #    welcome = WelcomeScreen()
    #    widget.addWidget(welcome)
    #    widget.setCurrentIndex(widget.currentIndex() + 1)

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

    def gotoExit(self):
        sys.exit(app.exec_())

class ChangePassword(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RenewPasswordDialog()
        self.ui.setupUi(self)
        self.ui.recoveryPasswordPushButton.clicked.connect(self.renewPasswordFunction)
        self.ui.cancelPushButton.clicked.connect(self.gotoCansel)
        self.dbconn = DataBaseConnection()

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
        selectStament  = f" SELECT email, password FROM users WHERE email='{self.ui.emailField.text()}' and" \
                         f" password='{self.ui.oldPasswordField.text()}'"
        updateStament = f" UPDATE users set password='{self.ui.newPasswordField.text()}' " \
                        f" WHERE email='{self.ui.emailField.text()}'"

        conn = self.dbconn.dataBaseOpenSqlite()
        cur = conn.cursor()
        try:
            cur.execute(selectStament)
            row = cur.fetchone()
            if row == None:
                self.message.setInformativeText("Некорректный email или password!")
                self.message.show()
            else:
                if self.ui.newPasswordField.text() == self.ui.renewPasswordField.text():
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

        self.dbconn = DataBaseConnection()

        self.message = QMessageBox()
        self.message.setStyleSheet("background-color: red;")
        self.message.setText("Ошибка регистрации!")

    def send_mail(self, parol):
        """
        почтовый клиент
        :param parol:
        :return:
        """
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        login = "viktoraskvart@yandex.ru"
        password = "......." # вставьте пароль от вашего почтового SMT-сервера
        url = "smtp.yandex.ru"
        toaddr = "viktoraskvart@yandex.ru"

        msg = MIMEMultipart()
        msg['Subject'] = "Ваш забытый пароль"
        msg['From'] = "viktoraskvart@yandex.ru"
        body = f"Ваш забытый пароль: {parol}"
        msg.attach(MIMEText(body, 'plain'))
        try:
            server = smtplib.SMTP_SSL(url, 465)
            server.login(login, password)
            server.sendmail(login, toaddr, msg.as_string())
            server.quit()
        except TimeoutError:
            print("Нет связи с сервером")

    def gotoCansel(self):
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoWelcome(self):
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def recoverysignupFunction(self):
        """
        Восстановление пароля через отправку на почту пароля
        :return:
        """
        user = self.ui.recoveryPasswordField.text()
        query = f"SELECT * FROM users WHERE email='{user}'"
        conn = self.dbconn.dataBaseOpenSqlite()
        cur = conn.cursor()
        try:
            cur.execute(query)
            row = cur.fetchone()
            print(row)
            if row == None:
                self.message.setInformativeText("Такого пользователя нет!")
                self.message.show()
            elif row != []:
                parol = {row[1]}
                self.send_mail(parol)

                self.message.setStyleSheet("background-color: green;")
                self.message.setText("Пароль выслан на вашу почту!")
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

        self.dbconn = DataBaseConnection()


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
            conn = self.dbconn.dataBaseOpenSqlite()
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

class BirthDayOnWeek(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_BirthDayTableDialog()
        self.ui.setupUi(self)
        self.ui.HeadLabel.text()

        self.dbconn = DataBaseConnection()
        self.load_data_birthday()
        self.ui.tableWidget.setSortingEnabled(True)




        self.ui.cancelPushButton.clicked.connect(MyFormUser.gotoWelcome)



    def daysInMonthDefine(self):
        """
        Определяем дней в месяце
        :return:
        """
        current_datetime = datetime.now()
        month = current_datetime.month
        m = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        all_day = 0
        for k, v in m.items():
            if k == month:
                all_day = v
        return all_day

    def data_birthday_on_week(self):
        """
        Готовим даты текущего месяца и следующего
        :return:
        """
        current_datetime = datetime.now()
        month = current_datetime.month
        day = current_datetime.day
        all_day = self.daysInMonthDefine()
        month2 = 0
        day2 = 0
        print("all_day: ", all_day)
        if day + 7 > all_day:
            month2 = month + 1
            day2 = 31 - day
        return month, day, month2, day2, all_day


    def load_data_birthday(self):
        """
        Выборка дней рождения на текущий месяц
        от текущего дня до 31 дня
        :return:
        """
        conn = self.dbconn.dataBaseOpenSqlite()
        month, day, month2, day2, all_day = self.data_birthday_on_week()
        sqlStatement = f"SELECT name, nomer, year, month, day from phonebook WHERE " \
                       f"month={month} and day BETWEEN {day} and {all_day} ORDER BY day"
        #conn = sqlite3.connect("DataBase/ph_book1.db")

        cur = conn.cursor()
        cur.execute(sqlStatement)
        rows = cur.fetchall()
        rows2 = 0
        if day2 != 0 or month2 != 0:
            sqlStatement2 = f"SELECT name, nomer, year, month, day from phonebook WHERE " \
                           f"month={month2} and day BETWEEN {1} and {day2} ORDER BY day"
            cur.execute(sqlStatement2)
            rows2 = cur.fetchall()
        rows = rows + rows2
        row = 0
        self.ui.tableWidget.setRowCount(len(rows))
        for person in rows:
            print(person)
            self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person[0]))
            self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(person[1]))
            self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(person[2])))
            self.ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(person[3])))
            self.ui.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(person[4])))
            row += 1
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
