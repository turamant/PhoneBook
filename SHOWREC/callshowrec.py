import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialogButtonBox, QVBoxLayout, QMenuBar, QMenu, QGroupBox, QHBoxLayout, QPushButton

from PyQt_ToolKit.DELETE.xxx import Dialog
from showrec import *
from PyQt5 import QtSql, QtWidgets

def createConnection():
    db = QtSql.QSqlDatabase.addDatabase('QPSQL')
    db.setHostName('127.0.0.1')
    db.setDatabaseName('shopdb')
    print(db.databaseName())
    db.setUserName('user1')
    db.setPassword('password1')
    db.setPort(5432)
    db.open()
    print("Нет ошибок!", db.lastError().text())
    print('Basa подключена')
    return True

class MyForm(QtWidgets.QDialog):
    #NumGridRows = 3
    #NumButtons = 2
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable("products2")
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.model.select()
        self.ui.tableView.setModel(self.model)
        self.createMenu()
        self.createHorizontalGroupBox()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.setMenuBar(self.menuBar)
        mainLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Basic Layouts")

    def createMenu(self):
        self.menuBar = QMenuBar()

        self.fileMenu = QMenu("&File", self)
        self.exitAction = self.fileMenu.addAction("E&xit")
        self.menuBar.addMenu(self.fileMenu)

        self.exitAction.triggered.connect(self.accept)

    def createHorizontalGroupBox(self):
        self.horizontalGroupBox = QGroupBox("123dvdffd")
        layout = QHBoxLayout()

        for i in range(Dialog.NumButtons):
            button = QPushButton("Button %d" % (i + 1))
            button.clicked.connect(self.on_click)
            layout.addWidget(button)

        self.horizontalGroupBox.setLayout(layout)


    @pyqtSlot()
    def on_click(self):
        print('PyQt button click')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    if not createConnection():
        sys.exit(1)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())