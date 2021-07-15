from PyQt5 import QtSql
from PyQt5.QtWidgets import QWidget


def createConnection():
    db = QtSql.QSqlDatabase.addDatabase('QPSQL')
    db.setHostName('127.0.0.1')
    db.setDatabaseName('shopdb')
    db.setUserName('user1')
    db.setPassword('password1')
    db.setPort(5432)
    db.open()
    print ("Нет ошибок", db.lastError().text())
    print("База подключена!")
    return True


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()

    def initUI(self):


if __name__=='__main__':
