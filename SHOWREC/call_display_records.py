import sys
from DispProducts import *
from PyQt5 import QtSql, QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QAction, qApp
from PyQt5.QtCore import QObject




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

class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(self.this_call)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        self.show()

    def this_call(self):
        print('bye bye')
        app.quit()


class MyForm(QtWidgets.QDialog):
    recno = 0
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.model = QtSql.QSqlQueryModel(self)
        self.model.setQuery("select * from products2")
        self.record = self.model.record(0)
        self.ui.prodid.setText(str(self.record.value("id")))
        self.ui.prodname.setText(self.record.value("productname"))
        self.ui.qty.setText(str(self.record.value("quantity")))
        self.ui.price.setText(str(self.record.value("price")))
        exitAction = QAction('exit', self)
        exitAction.triggered.connect(self.this_call)


        #QtCore.QObject.connectSlotsByName(self.ui.FirstButton,
        #                                  QtCore.SIGNAL('clicked()'),
        #                                  self.dispFirst)
        #QtCore.QObject.connect(self.ui.PreviousButton, QtCore.SIGNAL('clicked()'),
        #                       self.dispPrevious)
        #QtCore.QObject.connect(self.ui.LastButton, QtCore.SIGNAL('clicked()'),
        #                       self.dispLast)
        #QtCore.QObject.connect(self.ui.NextButton, QtCore.SIGNAL('clicked()'),
        #                       self.dispNext)

    def this_call(self):
        print('bye bye')
        app.quit()

    def dispFirst(self):
        MyForm.recno = 0
        self.record = self.model.record(MyForm.recno)
        self.ui.prodid.setText(str(self.record.value("id")))
        self.ui.prodname.setText(self.record.value("productname"))
        self.ui.qty.setText(str(self.record.value("quantity")))
        self.ui.price.setText(str(self.record.value("price")))

    def dispPrevious(self):
        MyForm.recno -= 1
        if MyForm.recno < 0:
            MyForm.recno = self.model.rowCount()-1
        self.record = self.model.record(MyForm.recno)
        self.ui.prodid.setText(str(self.record.value("id")))
        self.ui.prodname.setText(self.record.value("productname"))
        self.ui.qty.setText(str(self.record.value("quantity")))
        self.ui.price.setText(str(self.record.value("price")))

    def dispLast(self):
        MyForm.recno = self.model.rowCount()-1
        self.record = self.model.record(MyForm.recno)
        self.ui.prodid.setText(str(self.record.value("id")))
        self.ui.prodname.setText(self.record.value("productname"))
        self.ui.qty.setText(str(self.record.value("quantity")))
        self.ui.price.setText(str(self.record.value("price")))

    def dispNext(self):
        MyForm.recno += 1
        if MyForm.recno > self.model.rowCount()-1:
            MyForm.recno = 0
        self.record = self.model.record(MyForm.recno)
        self.ui.prodid.setText(str(self.record.value("id")))
        self.ui.prodname.setText(self.record.value("productname"))
        self.ui.qty.setText(str(self.record.value("quantity")))
        self.ui.price.setText(str(self.record.value("price")))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    if not createConnection():
        sys.exit(1)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())