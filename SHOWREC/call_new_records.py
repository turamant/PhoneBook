import sys
from DispProducts import *
from PyQt5 import QtSql, QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QGroupBox, QHBoxLayout, QPushButton, QVBoxLayout, QDialog, \
    QTableView, QDialogButtonBox, QMessageBox, QTabWidget
from PyQt5.QtCore import QObject, pyqtSlot, Qt


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

class

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

class TableEditor(QDialog):
    def __init__(self, tableName, parent=None):
        super(TableEditor, self).__init__(parent)

        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable(tableName)
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.model.select()

        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "First name")
        self.model.setHeaderData(2, Qt.Horizontal, "Last name")

        view = QTableView()
        view.setModel(self.model)

        submitButton = QPushButton("Submit")
        submitButton.setDefault(True)
        revertButton = QPushButton("&Revert")
        quitButton = QPushButton("Quit")

        buttonBox = QDialogButtonBox(Qt.Vertical)
        buttonBox.addButton(submitButton, QDialogButtonBox.ActionRole)
        buttonBox.addButton(revertButton, QDialogButtonBox.ActionRole)
        buttonBox.addButton(quitButton, QDialogButtonBox.RejectRole)

        submitButton.clicked.connect(self.submit)
        revertButton.clicked.connect(self.model.revertAll)
        quitButton.clicked.connect(self.close)

        mainLayout = QHBoxLayout()
        mainLayout.addWidget(view)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Cached Table")
        self.setGeometry(500, 100, 600, 600)

    def submit(self):
        self.model.database().transaction()
        if self.model.submitAll():
            self.model.database().commit()
        else:
            self.model.database().rollback()
            QMessageBox.warning(self, "Cached Table",
                        "The database reported an error: %s" % self.model.lastError().text())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    if not createConnection():
        sys.exit(1)
    myapp = MyForm()
    myapp.show()
    editor = TableEditor('products2')
    editor.show()
    sys.exit(app.exec_())