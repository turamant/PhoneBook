import sys

import psycopg2
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTableView

from FullMyPhoneBook.gui_autoshop import Ui_MyWidget





class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MyWidget()
        self.ui.setupUi(self)
        self.ui.exitPushButton_4.clicked.connect(self.gotoExit)

# подключить базу данных
        self.con()
        self.table_view = QTableView()


# соединение с базой данных
    def gotoExit(self):
        self.close()
        sys.exit(app.exec_())


    def con(self):
        self.conn = psycopg2.connect(user="user1",
                              password="password1",
                              host="127.0.0.1",
                              port="5432",
                              database="shopdb")
        self.cur = self.conn.cursor()

# обновить таблицу и поля
    def upd(self):
        self.conn.commit()
        self.tb.updt()
        self.idp.setText('')
        self.productname.setText('')
        self.quantity.setText('')
        self.price.setText('')

# добавить в таблицу новую строку
    def ins(self):
        id = self.idp.text()
        productname = self.productname.text()
        quantity = self.quantity.text()
        price = self.price.text()
        try:
            self.cur.execute("""
                    INSERT INTO products2 (id, productname, quantity, price)
                    VALUES (%d, '%s', %s, %s)
                    """ % (int(id), productname, quantity, price))
            print("Типа записалось")
        except:
            print("Не добавилось")
        self.upd()
        print("завершилась!")


# удалить из таблицы строку
    def dels(self):
        try:
            ids = int(self.idp.text()) # идентификатор строки
        except:
            return
        self.cur.execute("delete from products2 where id=%s", (ids,))
        self.upd()

# выход из окна(программы!)
    def squit(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    welcome = MyWidget()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(welcome)
    widget.setFixedHeight(800)
    widget.setFixedWidth(1200)
    widget.show()

    try:
        sys.exit(app.exec_())
    except:
        print("Выход")