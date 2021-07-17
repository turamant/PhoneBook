import sys
import psycopg2
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QPushButton, QLineEdit
from PyQt5 import QtGui


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

# подключить базу данных
        self.con()

# параметры окна
        self.setGeometry(100, 100, 800, 850)
        self.setWindowTitle('Журнал автомарок')
        self.tb = Tb(self)


# кнопка "обновить"
        self.btn = QPushButton('Обновить', self)
        self.btn.resize(150, 40)
        self.btn.move(620, 10)
        self.btn.clicked.connect(self.upd)

# здесь идентификатор
        self.idp = QLineEdit(self)
        self.idp.resize(150, 40)
        self.idp.move(620, 60)
        self.idp.setReadOnly(False)

# здесь наименование продукта
        self.productname = QLineEdit(self)
        self.productname.resize(150, 40)
        self.productname.move(620, 110)

# здесь количество продукта
        self.quantity = QLineEdit(self)
        self.quantity.resize(150, 40)
        self.quantity.move(620, 160)

# здесь цена
        self.price = QLineEdit(self)
        self.price.resize(150, 40)
        self.price.move(620, 210)

# кнопка добавить запись
        self.btn = QPushButton('Добавить', self)
        self.btn.resize(150, 40)
        self.btn.move(620, 260)
        self.btn.clicked.connect(self.ins)

# кнопка удалить запись
        self.btn = QPushButton('Удалить', self)
        self.btn.resize(150, 40)
        self.btn.move(620, 310)
        self.btn.clicked.connect(self.dels)

# кнопка выход из
        self.btn = QPushButton("Выход", self)
        self.btn.resize(150, 40)
        self.btn.move(620, 360)
        self.btn.clicked.connect(self.squit)

# соединение с базой данных
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




# класс - таблица
class Tb(QTableWidget):
    def __init__(self, wg):
        self.wg = wg  # запомнить окно, в котором эта таблица показывается
        super().__init__(wg)
        self.setGeometry(10, 10, 580, 800)
        self.setColumnCount(4)
        #self.verticalHeader().hide()
        self.updt()    # обновить таблицу
        self.setEditTriggers(QTableWidget.NoEditTriggers) # запретить изменять поля
        self.cellClicked.connect(self.cellClick)  # установить обработчик щелча мыши в таблице



# обновление таблицы
    def updt(self):
        self.clear()
        self.setRowCount(0)
        self.setHorizontalHeaderLabels(['id', 'Марка', 'Количество', 'Цена'])  # заголовки столцов
        self.wg.cur.execute("select * from products2 order by productname")
        rows = self.wg.cur.fetchall()
        i = 0
        for elem in rows:
            self.setRowCount(self.rowCount() + 1)
            j = 0
            for t in elem:  # заполняем внутри строки
                self.setItem(i, j, QTableWidgetItem(str(t).strip()))
                j += 1
            i += 1
        self.resizeColumnsToContents()

# обработка щелчка мыши по таблице
    def cellClick(self, row, col):  # row - номер строки, col - номер столбца
        self.wg.idp.setText(self.item(row, 0).text())
        self.wg.productname.setText(self.item(row, 1).text().strip())
        self.wg.quantity.setText(self.item(row, 2).text().strip())
        self.wg.price.setText(self.item(row, 3).text().strip())


if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())