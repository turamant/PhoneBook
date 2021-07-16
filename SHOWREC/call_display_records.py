import sys
from DispProducts import *
from PyQt5 import QtSql, QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QGroupBox, QHBoxLayout, QPushButton, QVBoxLayout
from PyQt5.QtCore import QObject, pyqtSlot


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

        self.createHorizontalLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

    def createHorizontalLayout(self):
        self.horizontalGroupBox = QGroupBox("What is your favorite color?")
        layout = QHBoxLayout()

        buttonFirst = QPushButton('First', self)
        buttonFirst.clicked.connect(self.dispFirst)
        layout.addWidget(buttonFirst)

        buttonNext = QPushButton('Next', self)
        buttonNext.clicked.connect(self.dispNext)
        layout.addWidget(buttonNext)

        buttonPrevious = QPushButton('Previous', self)
        buttonPrevious.clicked.connect(self.dispPrevious)
        layout.addWidget(buttonPrevious)

        buttonLast = QPushButton('Last', self)
        buttonLast.clicked.connect(self.dispLast)
        layout.addWidget(buttonLast)

        self.horizontalGroupBox.setLayout(layout)

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

    def this_call(self):
        print('bye bye')
        app.quit()

    @pyqtSlot()
    def dispFirst(self):
        MyForm.recno = 0
        self.record = self.model.record(MyForm.recno)
        self.ui.prodid.setText(str(self.record.value("id")))
        self.ui.prodname.setText(self.record.value("productname"))
        self.ui.qty.setText(str(self.record.value("quantity")))
        self.ui.price.setText(str(self.record.value("price")))

    @pyqtSlot()
    def dispPrevious(self):
        MyForm.recno -= 1
        if MyForm.recno < 0:
            MyForm.recno = self.model.rowCount()-1
        self.record = self.model.record(MyForm.recno)
        self.ui.prodid.setText(str(self.record.value("id")))
        self.ui.prodname.setText(self.record.value("productname"))
        self.ui.qty.setText(str(self.record.value("quantity")))
        self.ui.price.setText(str(self.record.value("price")))

    @pyqtSlot()
    def dispLast(self):
        MyForm.recno = self.model.rowCount()-1
        self.record = self.model.record(MyForm.recno)
        self.ui.prodid.setText(str(self.record.value("id")))
        self.ui.prodname.setText(self.record.value("productname"))
        self.ui.qty.setText(str(self.record.value("quantity")))
        self.ui.price.setText(str(self.record.value("price")))

    @pyqtSlot()
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