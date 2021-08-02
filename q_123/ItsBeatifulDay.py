import os
import sys

import MySQLdb
import psycopg2
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication,  QMessageBox

from Ui.tableview import Ui_TableDialog

from Ui.tableview2user import Ui_TableDialog2
from Ui.welcomescreen import Ui_Dialog
from Ui.signup import Ui_SignUpDialog
from Ui.recoveryPassword import Ui_RecoveryPasswordDialog
from Ui.renewPassword import Ui_RenewPasswordDialog
from Ui.birthday import Ui_BirthDayTableDialog
from Ui.alluser import Ui_AllUserTableDialog
from Ui.helpscreen import Ui_HelpScreenDialog

import sqlite3

saveuser = ""
savepassword = ""

class DataBase:
    host = "localhost"
    user = "user1"
    passwd = "password1"
    db = "phonebook"

    def __init__(self):
        self.conn = MySQLdb.connect(self.host,
                                    self.user,
                                    self.passwd,
                                    self.db,
                                    use_unicode=True,
                                    charset="utf8")
        self.cur = self.conn.cursor()

    def insert(self, query):
        try:
            self.cur.execute(query)
            self.conn.commit()
        except Exception as ex:
            self.conn.rollback()

    def update(self, query):
        try:
            self.cur.execute(query)
            self.conn.commit()
        except Exception as ex:
            self.conn.rollback()

    def delete(self, query):
        try:
            self.cur.execute(query)
            self.conn.commit()
        except Exception as ex:
            self.conn.rollback()

    def read(self, query):
        try:
            self.cur.execute(query)
        except Exception as ex:
            print("Ошибка чтения данных")

    def search(self, query):
        try:
            self.cur.execute(query)
        except Exception as ex:
            print("Ощибка поиска")

    def __del__(self):
        self.conn.close()

class MessageBox(QMessageBox):
    def __init__(self):
        QMessageBox.__init__(self)
        self.setText("This is a MessageBox, typically used to convey short messages to the user.")
        self.setInformativeText("Informative text provides more space to explain the message ")
        self.setIcon(QMessageBox.Information)
        self.setStandardButtons(QMessageBox.Close)

class BaseForm(QDialog):
    def __init__(self):
        self.db = DataBase()
        super().__init__()
        self.ui = Ui_TableDialog()
        self.ui.setupUi(self)
        self.message = QMessageBox()

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
        sql = f"SELECT name, nomer, birthday from phonebook ORDER By name"
        self.SearchRows(sql)

    def sqlBase(self, a, b):
        """
        Подготавливает SQL запрос
        :param a: начальная точка поиска
        :param b: конечная точка поиска
        :return: sql
        """
        sql = f"SELECT name, nomer, birthday FROM phonebook WHERE name >=" \
              f" '{a}' AND name <= '{b}'  ORDER BY name ASC"
        return sql

    def SearchRows(self, sqlStatement=f"SELECT name, nomer, birthday from phonebook ORDER By birthday"):
        """
        Поиск записей по SQL запросу.
        По умолчанию загружает все записи из Таблицы
        :param sqlStatement:
        :return:
        """
        self.db.search(sqlStatement)
        rows = self.db.cur.fetchall()
        row = 0
        self.ui.tableWidget.setRowCount(len(rows))
        for person in rows:
            print(" .", person)
            self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person[0]))
            self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(person[1]))
            self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(person[2])))
            row += 1

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


    def gotoHelp(self):
        help = HelpScreen()
        widget.addWidget(help)
        widget.setCurrentIndex(widget.currentIndex()+1)

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

        self.ui.helpPushButton.clicked.connect(self.gotoHelp)

        # кнопка загрузки всех данных в главную страницу таблицы
        self.ui.ALLsearchPushButton_16.clicked.connect(self.SearchRows_All)

        self.ui.labelUser.setText(saveuser)

        self.ui.cancelPushButton.clicked.connect(self.gotoWelcome)

        # Ширина колонок таблицы
        self.ui.tableWidget.setColumnWidth(0, 200)
        self.ui.tableWidget.setColumnWidth(1, 200)
        self.ui.tableWidget.setColumnWidth(2, 300)
        self.ui.tableWidget.setSortingEnabled(True)

        self.SearchRows()

class AllUserForm(QDialog):
    def __init__(self):
        self.db = DataBase()
        super().__init__()
        self.ui = Ui_AllUserTableDialog()
        self.ui.setupUi(self)
        self.ui.HeadLabel.text()
        self.ui.userTableWidget.setSortingEnabled(True)
        self.ui.cancelPushButton.clicked.connect(self.gotoInheretensFormTableAdmin)
        self.ui.emailLabel.text()
        self.ui.emailLineEdit.text()
        self.ui.delPushButton.clicked.connect(self.deleteUserFunction)
        self.ui.userTableWidget.cellClicked.connect(self.cellClick)

        # Ширина колонок таблицы
        self.ui.userTableWidget.setColumnWidth(0, 200)
        self.ui.userTableWidget.setColumnWidth(1, 200)
        self.ui.userTableWidget.setColumnWidth(2, 300)
        self.ui.userTableWidget.setSortingEnabled(True)

        self.ui.labelUser.setText(saveuser)

        self.loadUser()

    def editLineClear(self):
        """
        Обнуляет поля LineEdit (4 шт)
        :return:
        """
        self.ui.emailLineEdit.clear()

    def deleteUserFunction(self):
        email = self.ui.emailLineEdit.text()
        query = f"SELECT * FROM users WHERE email='{email}'"
        query_delete = f"DELETE from users WHERE email='{email}'"
        self.db.read(query)
        row = self.db.cur.fetchone()
        if row == None:
            print("Нет такого контакта в таблице")
        else:
            print("Есть такая информайия о контакте")
            self.db.delete(query_delete)
            self.editLineClear()
            self.loadUser()

    def cellClick(self, row, col):
        """
        обработка щелчка мыши по таблице
        :param row: номер строки
        :param col: номер столбца
        :return:
        """
        self.ui.emailLineEdit.setText(self.ui.userTableWidget.item(row, 0).text().strip())

    def gotoInheretensFormTableAdmin(self):
        admin = InheretensFormTableAdmin()
        widget.addWidget(admin)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def loadUser(self):
        """
        Поиск записей по SQL запросу.
        По умолчанию загружает все записи из Таблицы
        :param sqlStatement:
        :return:
        """
        sqlStatement = f"SELECT email, password, save from users ORDER By email"
        self.db.read(sqlStatement)
        rows = self.db.cur.fetchall()
        row = 0
        self.ui.userTableWidget.setRowCount(len(rows))
        for person in rows:
            self.ui.userTableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person[0]))
            self.ui.userTableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(person[1]))
            self.ui.userTableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(person[2]))
            row += 1

class InheretensFormTableAdmin(MyFormUser):
    def __init__(self):
        self.db = DataBase()
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

        self.ui.userPushButton.clicked.connect(self.gotoAllUserForm)
        self.ui.birthDayPushButtn.clicked.connect(self.gotoBirthDayOnWeek)

        self.ui.addPushButton.clicked.connect(self.insertNewRecord)
        self.ui.updatePushButton.clicked.connect(self.updateRecord)
        self.ui.deletePushButton.clicked.connect(self.deleteRecord)

        self.list_line_edit = [self.ui.nameLineEdit,
                               self.ui.nomerLineEdit,
                               self.ui.dayLineEdit,
                               ]

        self.ui.tableWidget.setColumnWidth(0, 200)
        self.ui.tableWidget.setColumnWidth(1, 200)
        self.ui.tableWidget.setColumnWidth(2, 300)
        self.ui.tableWidget.setSortingEnabled(True)

        self.SearchRows()
        self.ui.tableWidget.cellClicked.connect(self.cellClick)  # установить обработчик щелча мыши в таблице

    def gotoAllUserForm(self):
        adminform = AllUserForm()
        widget.addWidget(adminform)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoBirthDayOnWeek(self):
        birthday = BirthDayOnWeek()
        widget.addWidget(birthday)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def SearchRows_All(self):
        """
        (Переопределенный метод)
        Слот-метод, очищает поля и выводит все записи
        :return:
        """
        sql = f"SELECT name, nomer, birthday from phonebook ORDER By name"
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
        sql = f"SELECT name, nomer, birthday FROM phonebook WHERE name >=" \
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
        self.ui.dayLineEdit.setText(self.ui.tableWidget.item(row, 2).text().strip())

    def insertNewRecord(self):
        """
        Вставка новой записи в Таблицу
        :return:
        """
        name = self.ui.nameLineEdit.text().capitalize()
        nomer = self.ui.nomerLineEdit.text()
        birthday = self.ui.dayLineEdit.text()
        query = f"INSERT INTO phonebook (name, nomer, birthday) VALUES ('{name}', '{nomer}', '{birthday}')"
        self.db.insert(query)
        self.editLineClear()
        print("Добавлена успешно!")
        self.SearchRows_All()

    def updateRecord(self):
        """
        Изменение записи в Таблице
        :return:
        """
        name = self.ui.nameLineEdit.text().capitalize()
        nomer = self.ui.nomerLineEdit.text()
        birthday = self.ui.dayLineEdit.text()
        query = f"SELECT * from phonebook where name='{name}'"
        query_update = f"UPDATE phonebook SET nomer='{nomer}', birthday='{birthday}'" \
                       f" WHERE name='{name}'"
        self.db.read(query)
        row = self.db.cur.fetchone()
        if row == None:
            print("Нет такой фамилии в таблице")
        else:
            print("Есть такая фамилия")
            name = row[1]
            print(name)
            self.db.update(query_update)
            self.editLineClear()
            self.SearchRows_All()
            print("Изменения проведены успешно")

    def deleteRecord(self):
        name = self.ui.nameLineEdit.text()
        query = f"SELECT * FROM phonebook WHERE name='{name}'"
        query_delete = f"DELETE from phonebook WHERE name='{name}'"
        self.db.read(query)
        row = self.db.cur.fetchone()
        if row == None:
            print("Нет такого контакта в таблице")
        else:
            print("Есть такая информайия о контакте")
            self.db.delete(query_delete)
            self.editLineClear()
            self.SearchRows_All()

class WelcomeScreen(QDialog):
    def __init__(self):
        self.db = DataBase()
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.message = QMessageBox()
        self.message.setStyleSheet("background-color: yellow;")
        self.message.setText("Ошибка авторизации!")
        self.startSave()

        self.ui.cancelPushButton.clicked.connect(self.gotoExit)
        self.ui.signupPushButton.clicked.connect(self.gotoCreate)
        self.ui.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.loginPushButton.clicked.connect(self.loginFunction)

        self.ui.echoPasswordCheckBox.stateChanged.connect(self.dispAmount)
        self.ui.saveMeCheckBox.clicked.connect(self.saveMe)

        self.ui.forgotPasswordPushButton.clicked.connect(self.gotoRecoveryPassword)
        self.ui.changePasswordPushButton.clicked.connect(self.gotoChangePassword)

        self.ui.helpPushButton.clicked.connect(self.gotoHelp)

    def gotoHelp(self):
        help = HelpScreen()
        widget.addWidget(help)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def startSave(self):
        global saveuser, savepassword
        query = f"SELECT email, password, save FROM users WHERE save='1'"
        self.db.read(query)
        row = self.db.cur.fetchone()
        if row == None:
             print("Нет запомненного пользователя!", row)
        else:
             self.ui.nameuserLineEdit.setText(row[0])
             self.ui.passwordLineEdit.setText(row[1])

    def saveMe(self):
        if self.ui.saveMeCheckBox.isChecked() == True:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!", self.ui.saveMeCheckBox.isChecked())
            return False

    def saveUser(self, saveuser):
        if self.saveMe() == False:
            print("Значение равно - ", self.saveMe())
            email = saveuser
            print("email", email)
            save = "1"
            query = f"SELECT * from users where email='{email}'"
            self.db.read(query)
            row = self.db.cur.fetchone()
            if row == None:
                print("Нет такой фамилии в таблице", row)
            else:
                name = row[0]
                print("Есть такая фамилия", name)
                query_update = f"UPDATE users SET save='{save}' WHERE email='{email}'"
                self.db.update(query_update)
                print("Изменения проведены успешно")

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
        print("hello")
        global saveuser, savepassword
        user = self.ui.nameuserLineEdit.text()
        password = self.ui.passwordLineEdit.text()
        query = f"SELECT password FROM users WHERE email='{user}'"
        if len(user) == 0 or len(password) == 0:
            self.message.setInformativeText("Заполните все поля правильно!")
            self.message.show()
        else:
            self.db.read(query)
            row = self.db.cur.fetchone()
            print("..row..: ", row)
            if row == None:
                self.message.setInformativeText("Такого пользователя нет!")
                self.message.show()
            elif row != [] and row[0] == password:
                print("Successfull logged it!", user)
                if user == 'admin':  #'admin@admin.com':
                    saveuser = user
                    savepassword = password
                    self.saveUser(saveuser)
                    mytable = InheretensFormTableAdmin()
                else:
                    saveuser = user
                    savepassword = password
                    self.saveUser(saveuser)
                    print(user, password)
                    mytable = MyFormUser()
                    print(saveuser, savepassword)
                    print("а это было", saveuser, savepassword)
                widget.addWidget(mytable)
                widget.setCurrentIndex(widget.currentIndex() + 1)
            else:
                self.message.setInformativeText("Ошибка имени или пароля!")
                self.message.show()

    def gotoBirthDayOnWeek(self):
        birthday = BirthDayOnWeek()
        widget.addWidget(birthday)
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
        #self.conn.close()
        create = CreateAccScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoExit(self):
        sys.exit(app.exec_())

class ChangePassword(QDialog):
    def __init__(self):
        self.db = DataBase()
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
        """
        Смена старого пароля на новый
        :return:
        """
        email = self.ui.emailField.text()
        old_password = self.ui.oldPasswordField.text()
        new_password = self.ui.newPasswordField.text()
        renew_password = self.ui.renewPasswordField.text()
        selectStament  = f" SELECT email, password FROM users WHERE email='{email}' and" \
                         f" password='{old_password}'"
        updateStament = f" UPDATE users set password='{new_password}' " \
                        f" WHERE email='{email}'"
        self.db.read(selectStament)
        row = self.db.cur.fetchone()
        print("row:", row)
        if row == None:
            self.message.setInformativeText("Некорректный email или password!")
            self.message.show()
        elif new_password == renew_password:
            self.db.update(updateStament)
            self.message.setStyleSheet("background-color: green;")
            self.message.setText("Пароль изменен!")
            self.message.setInformativeText(f"Вы успешно изменили пароль")
            self.message.show()
            self.gotoWelcome()
        else:
            print("Два пароля не совпадают")

class RecoveryPassword(QDialog):
    def __init__(self):
        self.db = DataBase()
        super().__init__()
        self.ui = Ui_RecoveryPasswordDialog()
        self.ui.setupUi(self)
        self.ui.recoveryPasswordPushButton.clicked.connect(self.recoverysignupFunction)
        self.ui.cancelPushButton.clicked.connect(self.gotoCansel)

        self.message = QMessageBox()
        self.message.setStyleSheet("background-color: red;")
        self.message.setText("Ошибка регистрации!")

    def send_mail(self, mail_addr, parol):
        """
        почтовый клиент
        :param parol:
        :return:
        """
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        login = self.ui.smtpClientField_2.text()
        password = self.ui.smtpPasswordField_3.text()
        url = self.ui.smtpURLField_4.text()
        toaddr = mail_addr

        msg = MIMEMultipart()
        msg['Subject'] = "Ваш забытый пароль от PhoneBook"
        msg['From'] = login
        body = f"Ваш забытый пароль от PhoneBook: {parol}"
        msg.attach(MIMEText(body, 'plain'))
        try:
            server = smtplib.SMTP_SSL(url, 465)
            server.login(login, password)
            server.sendmail(login, toaddr, msg.as_string())
            server.quit()
        except TimeoutError:
            print("Нет связи с сервером")
        except smtplib.SMTPAuthenticationError:
            self.message.setStyleSheet("background-color: red;")
            self.message.setText("Отредактируйте адрес SMT- сервера, укажите пароль!")
            self.message.show()

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
        user = self.ui.adresEmailField.text()
        query = f"SELECT * FROM users WHERE email='{user}'"
        self.db.read(query)
        row = self.db.cur.fetchone()
        print(row)
        if row == None:
            self.message.setInformativeText("Такого пользователя нет!")
            self.message.show()
        elif row != []:
            parol = row[2]
            mail_addr = row[1]
            self.send_mail(mail_addr, parol)
            self.gotoWelcome()
        else:
            self.message.setInformativeText("Ошибка имени или пароля!")
            self.message.show()

class CreateAccScreen(QDialog):
    def __init__(self):
        self.db = DataBase()
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


    def signupFunction(self):
        """
        Регистрация нового аккаунта
        :return:
        """
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
            self.db.insert(query)
            self.message.setStyleSheet("background-color: green;")
            self.message.setText("Успешная регистрация!")
            self.message.setInformativeText(f"Вы успешно зарегистрированы с ником - {user}")
            self.message.show()
            self.gotoWelcome()

class HelpScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_HelpScreenDialog()
        self.ui.setupUi(self)

        self.ui.helpCancelPushButton.clicked.connect(self.gotoWelcome)

    def gotoWelcome(self):
        """
        Переход на главный экран приложения
        :return:
        """
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class BirthDayOnWeek(QDialog):
    def __init__(self):
        self.db = DataBase()
        super().__init__()
        self.ui = Ui_BirthDayTableDialog()
        self.ui.setupUi(self)

        self.ui.headLabe.text()

        # Ширина колонок таблицы
        self.ui.tableWidget.setColumnWidth(0, 200)
        self.ui.tableWidget.setColumnWidth(1, 200)
        self.ui.tableWidget.setColumnWidth(2, 300)
        self.ui.tableWidget.setSortingEnabled(True)

        self.ui.labelUser.setText(saveuser)
        self.load_data_birthday()
        self.ui.tableWidget.setSortingEnabled(True)
        self.ui.cancelPushButton.clicked.connect(self.gotoInheretenseFormAdmin)


    def gotoInheretenseFormAdmin(self):
        admin = InheretensFormTableAdmin()
        widget.addWidget(admin)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def load_data_birthday(self):
        """
        Выборка дней рождения на неделю вперед
        :return:
        """


        sqlStatement = f"SELECT name, nomer, birthday from phonebook " \
                       f"WHERE DAYOFYEAR(birthday)" \
                       f" BETWEEN DAYOFYEAR(NOW()) AND DAYOFYEAR(DATE_ADD(NOW(), INTERVAL 1 WEEK))" \
                       f" ORDER BY DAYOFYEAR(birthday)"

        #if self.sqlsystem == "SQLITE":
        #    sqlStatement = f"SELECT name,nomer, birthday from phonebook" \
        #                   f" WHERE (strftime('%m-%d', birthday) " \
        #                   f" between strftime('%m-%d', date('now', 'weekday 0', '-6 days')) and " \
        #                   f" strftime('%m-%d', date('now', 'weekday 0', '-6 days', '+13 days'))) " \
        #                   f"ORDER BY strftime('%m-%d',birthday)"

        self.db.read(sqlStatement)
        rows = self.db.cur.fetchall()
        print('=========^ rows: ',rows)
        row = 0
        self.ui.tableWidget.setRowCount(len(rows))
        for person in rows:
            self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person[0]))
            self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(person[1]))
            self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(person[2])))
            row += 1

if __name__=='__main__':
    app = QApplication(sys.argv)
    if DataBase():
        welcome = WelcomeScreen()
        widget = QtWidgets.QStackedWidget()
        widget.addWidget(welcome)
        widget.setFixedHeight(800)
        widget.setFixedWidth(1200)
        widget.show()
    else:
        print("Нет соединения с базой данных")
        sys.exit(1)

    try:
        sys.exit(app.exec_())
    except:
        print("Выход")
