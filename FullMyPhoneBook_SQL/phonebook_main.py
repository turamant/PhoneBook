import sys


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QTableWidgetItem, QMessageBox

from tableview import Ui_TableDialog

from tableview2 import Ui_TableDialog2
from welcomescreen import Ui_Dialog
from signup import Ui_SignUpDialog
from fillprofile import Ui_fillProfileDialog
from recoveryPassword import Ui_RecoveryPasswordDialog
from renewPassword import Ui_RenewPasswordDialog
from insertnewrecord import Ui_InsertDialog
from birthdayonweek import Ui_BirthDayTableDialog

import sqlite3

saveuser = ""
savepassword = ""

class MyFormUser(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TableDialog()
        self.ui.setupUi(self)


        self.ui.labelUser.setText(saveuser)
        #self.ui.tableWidget.setItem(1, 1, QTableWidgetItem(4))
        self.ui.tableWidget.setColumnWidth(0, 200)
        self.ui.tableWidget.setColumnWidth(1, 200)
        self.ui.tableWidget.setColumnWidth(2, 100)
        self.ui.tableWidget.setColumnWidth(3, 100)
        self.ui.tableWidget.setColumnWidth(4, 100)

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
        self.ui.ALLsearchPushButton_16.clicked.connect(self.load_data)

        self.ui.cancelPushButton.clicked.connect(self.gotoWelcome)

        self.load_data()




    def gotoWelcome(self):
        global saveuser, savepassword
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        welcome.ui.nameuserLineEdit.setText(saveuser)
        welcome.ui.passwordLineEdit.setText(savepassword)
        print("gotowelcome^ ", saveuser, savepassword)


    def load_data(self):
        sqlStatement = f"SELECT name, nomer, year, month, day from phonebook ORDER By name"
        conn = sqlite3.connect("ph_book1.db")
        cur = conn.cursor()
        cur.execute(sqlStatement)
        rows = cur.fetchall()

        row = 0
        self.ui.tableWidget.setRowCount(len(rows))
        print(rows)

        for person in rows:
            print(person)
            self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person[0]))
            self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(person[1]))
            self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(person[2]))
            self.ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(person[3]))
            self.ui.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(person[4]))
            row += 1


        cur.close()
        conn.close()

    def gotoInsertNewRecord(self):
        insertnewrecord = InsertNewRecord()
        widget.addWidget(insertnewrecord)
        widget.setCurrentIndex(widget.currentIndex() + 1)

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
        sql = self.sqlBase('Ю', 'Яяяя')
        self.SearchRows(sql)

    def SearchRows_14(self):
        sql = self.sqlBase('A', 'zzz')
        self.SearchRows(sql)


    def sqlBase(self, a, b):
        sql = f"SELECT name, nomer, year, month, day FROM phonebook WHERE name >=" \
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
            self.ui.tableWidget.clear()
            name_columns = ['Фамилия', 'Телефон', 'Год', 'Месяц', 'День']
            self.ui.tableWidget.setHorizontalHeaderLabels(name_columns)
            self.ui.tableWidget.setRowCount(len(rows))
            rowNo = 0
            for tuple in rows:
                colNo = 0
                for columns in tuple:
                    self.ui.tableWidget.setItem(rowNo, colNo, QTableWidgetItem(columns))
                    colNo += 1
                rowNo += 1
            print("Всего строк", rowNo)
        except sqlite3.IntegrityError:
            self.ui.tableWidget.clear()
            self.message.setInformativeText("Ошибка доступа к таблице")
            self.message.show()
        finally:
            cur.close()
            conn.close()

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
        self.ui.ALLsearchPushButton_16.clicked.connect(self.load_data)

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

        self.load_data()
        self.ui.tableWidget.cellClicked.connect(self.cellClick)  # установить обработчик щелча мыши в таблице


    # обработка щелчка мыши по таблице
    def cellClick(self, row, col):  # row - номер строки, col - номер столбца
        self.ui.nameLineEdit.setText(self.ui.tableWidget.item(row, 0).text().strip())
        self.ui.nomerLineEdit.setText(self.ui.tableWidget.item(row, 1).text().strip())
        self.ui.yearLineEdit.setText(self.ui.tableWidget.item(row, 2).text().strip())
        self.ui.monthLineEdit.setText(self.ui.tableWidget.item(row, 3).text().strip())
        self.ui.dayLineEdit.setText(self.ui.tableWidget.item(row, 4).text().strip())

    def editLineClear(self):
        """
        Обнуляет поля LineEdit (4 шт)
        :return:
        """
        for line in self.list_line_edit:
            line.clear()

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

            self.ui.tableWidget.clear() #обновили таблицу
            self.editLineClear() # обнулили поля LineEdit
            name_columns = ['Фамилия', 'Телефон', 'Год', 'Месяц', 'День']
            self.ui.tableWidget.setHorizontalHeaderLabels(name_columns)
            self.ui.tableWidget.setRowCount(len(rows))
            rowNo = 0
            for tuple in rows:
                colNo = 0
                for columns in tuple:
                    self.ui.tableWidget.setItem(rowNo, colNo, QTableWidgetItem(columns))
                    colNo += 1
                rowNo += 1
            print("Всего строк", rowNo)
        except sqlite3.IntegrityError:
            self.ui.tableWidget.clear()
            self.message.setInformativeText("Ошибка доступа к таблице")
            self.message.show()
        finally:
            cur.close()
            conn.close()

    def insertNewRecord(self):
        name = self.ui.nameLineEdit.text().capitalize()
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
            # self.gotoMyForm2()
        except sqlite3.IntegrityError:
            conn.rollback()
            print("Произошла ошибка доступа")

        finally:

            cur.close()
            conn.close()

    def updateRecord(self):
        name = self.ui.nameLineEdit.text().capitalize()
        nomer = self.ui.nomerLineEdit.text()
        day = self.ui.dayLineEdit.text()
        month = self.ui.monthLineEdit.text()
        year = self.ui.yearLineEdit.text()
        query = f"SELECT * from phonebook where name='{name}'"

        query_update = f"UPDATE phonebook SET nomer='{nomer}', day='{day}'," \
                       f" month='{month}', year='{year}' WHERE name='{name}'"

        try:
            conn = sqlite3.connect("ph_book1.db")
        except sqlite3.Error:
            print("База не доступна")
            sys.exit(app.exec_())
        cur = conn.cursor()
        cur.execute(query)
        row = cur.fetchone()
        if row == None:
            print("Нет такого ID  в таблице")
        else:
            print("Есть такая информайия о продукте с ID %d :")
            nomer = row[1]
            print(nomer)
        cur.execute(query_update)
        cur.close()
        conn.commit()
        print("Изменения проведены успешно для ID: %d")
        conn.close()

    def deleteRecord(self):
        name = self.ui.nameLineEdit.text()
        query = f"SELECT * FROM phonebook WHERE name='{name}'"
        qyery_delete = f"DELETE from phonebook WHERE name='{name}'"
        try:
            conn = sqlite3.connect("ph_book1.db")
        except sqlite3.Error:
            print("База не доступна")
            sys.exit(app.exec_())
        cur = conn.cursor()
        cur.execute(query)
        row = cur.fetchone()
        if row == None:
            print("Нет такого контакта в таблице")
        else:
            print("Есть такая информайия о контакте")
            cur.execute(qyery_delete)
            print("Контакт удален!")
            cur.close()
            conn.commit()
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

    def gotoExit(self):
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

    def send_mail(self, parol):
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        login = "viktoraskvart@yandex.ru"
        password = ".........."
        url = "smtp.yandex.ru"
        toaddr = "viktoraskvart@yandex.ru"

        msg = MIMEMultipart()
        msg['Subject'] = "Ваш забытый пароль"
        msg['From'] = "viktoraskvart@yandex.ru"
        body = f"Ваш забытый пароль: {parol}"
        msg.attach(MIMEText(body, 'plain'))
        try:
            server = smtplib.SMTP_SSL(url, 465)
        except TimeoutError:
            print("Нет связи с сервером")
        server.login(login, password)
        server.sendmail(login, toaddr, msg.as_string())
        server.quit()


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
                parol = {row[1]}
                self.send_mail(parol)

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
        myform = MyFormUser()
        widget.addWidget(myform)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoMyForm(self):
        myform = MyFormUser()
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

class BirthDayOnWeek(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_BirthDayTableDialog()
        self.ui.setupUi(self)
        self.ui.HeadLabel.text()
        self.load_data_birthday()
        self.ui.cancelPushButton.clicked.connect(MyFormUser.gotoWelcome)


    def data_birthday_on_week(self):
        from datetime import datetime
        current_datetime = datetime.now()
        #year = current_datetime.year
        month = current_datetime.month
        day = current_datetime.day
        #if day + 7 > 31:
        #    plusweek_day = 31
        #else:
        #    plusweek_day = day + 7

        return month, day

    def load_data_birthday(self):
        month, day = self.data_birthday_on_week()
        print(month, day)
        yeap = 31


        sqlStatement = f"SELECT name, nomer, year, month, day from phonebook WHERE " \
                       f"month={month} and day BETWEEN {day} and {yeap} ORDER BY day"


        conn = sqlite3.connect("ph_book1.db")
        cur = conn.cursor()
        cur.execute(sqlStatement)
        rows = cur.fetchall()

        row = 0
        self.ui.tableWidget.setRowCount(len(rows))
        print(rows)

        for person in rows:
            print(person)
            self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person[0]))
            self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(person[1]))
            self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(person[2]))
            self.ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(person[3]))
            self.ui.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(person[4]))
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
