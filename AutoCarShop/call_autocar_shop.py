from PyQt5 import QtSql
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import *
import sys


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

class Dialog(QDialog):
    def __init__(self):
        super(Dialog, self).__init__()
        self.title = 'Окно авторизации'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.initUI()

    def initUI(self):

        layout = QGridLayout()
        self.setLayout(layout)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        label = QLabel("Вам есть 18 лет ?")
        layout.addWidget(label, 0, 0)
        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        layout.addWidget(buttonbox)
        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)
        self.show()

    def accept(self):
        print("Press OK!")
        self.close()


    def reject(self):
        print("Подрастёшь заходи!")
        return True



class TableEditor(QDialog):
    def __init__(self, tableName, parent=None):
        super(TableEditor, self).__init__(parent)

        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable(tableName)
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.model.select()

        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "Name")
        self.model.setHeaderData(2, Qt.Horizontal, "Quantity")
        self.model.setHeaderData(3, Qt.Horizontal, "Price")

        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        self.table_view.setShowGrid(True)
        self.table_view.setMinimumSize(400, 400)
        vh = self.table_view.verticalHeader()
        vh.setVisible(True)
        hh = self.table_view.horizontalHeader()
        hh.setStretchLastSection(True)
        #self.table_view.setWordWrap(True)
        #self.table_view.verticalHeader().hide()



        submitButton = QPushButton("Сохранить")
        #submitButton.setDefault(True)
        revertButton = QPushButton("&Revert")
        revertButton.setDefault(True)
        quitButton = QPushButton("Выход")
        addRowButton = QPushButton("Добавить")
        removeRowButton = QPushButton("Удалить")
        clearContentsButton = QPushButton("Очистить БД")
        sortButton = QPushButton("Сортировка Вкл.")
        #searchBarButton = QPushButton("Искать")
        #copyRowButton = QPushButton("Корировать")

        buttonBox = QDialogButtonBox(Qt.Vertical)
        buttonBox.addButton(submitButton, QDialogButtonBox.ActionRole)
        buttonBox.addButton(revertButton, QDialogButtonBox.ActionRole)
        buttonBox.addButton(quitButton, QDialogButtonBox.RejectRole)
        buttonBox.addButton(addRowButton, QDialogButtonBox.ActionRole)
        buttonBox.addButton(removeRowButton, QDialogButtonBox.ActionRole)
        buttonBox.addButton(clearContentsButton, QDialogButtonBox.ActionRole)
        buttonBox.addButton(sortButton, QDialogButtonBox.ActionRole)
        #buttonBox.addButton(searchBarButton, QDialogButtonBox.ActionRole)
        #buttonBox.addButton(copyRowButton, QDialogButtonBox.ActionRole)

        submitButton.clicked.connect(self.submit)
        revertButton.clicked.connect(self.model.revertAll)
        quitButton.clicked.connect(self.close)
        addRowButton.clicked.connect(self._addRow)
        removeRowButton.clicked.connect(self._removeRow)
        clearContentsButton.clicked.connect(self._clearContents)
        sortButton.clicked.connect(self._sortRow)
        #searchBarButton.clicked.connect(self._searchBar())
        #copyRowButton.clicked.connect(self._copyRow)

        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.table_view)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("База данных товаров")
        self.setGeometry(500, 100, 900, 700)
        self.show()

    @pyqtSlot()
    def _addRow(self):
        rowCount = self.model.rowCount()
        self.model.insertRows(rowCount, 1)

    def _sortRow(self):
        self.table_view.setSortingEnabled(True)




    def _removeRow(self):
        if self.model.rowCount() > 0:
            index = self.table_view.currentIndex().row()
            print(index)
            self.model.removeRow(self.table_view.currentIndex().row())

    def _clearContents(self):
        #self.table_view.rowCount(0)
        pass

    #def _searchBar(self):
    #    searchFor = self.model.select().se\\
    #    searchQ = c.execute(" SELECT * FROM databasetable WHERE title LIKE ('%' || ? || '%') ", (searchFor,))
    #    for row_data in searchQ:
    #        # insert new row at the end of the tableWidget
    #        row_number = self.tableWidget.rowCount()
    #        self.tableWidget.insertRow(row_number)
    #        for column_number, data in enumerate(row_data):
    #            self.tableWidget.setItem(
    #                row_number, column_number, QTableWidgetItem(str(data)))



    #def _copyRow(self):
    #    self.model.insertRow(self.model.rowCount())
    #    rowCount = self.model.rowCount()
    #    columnCount = self.model.columnCount()

    #    for j in range(columnCount):
    #        if not self.item(rowCount - 2, j) is None:
    #            self.setItem(rowCount - 1, j, QTableWidgetItem(self.item(rowCount-2, j).text()))


    def submit(self):
        self.model.database().transaction()
        if self.model.submitAll():
            self.model.database().commit()
        else:
            self.model.database().rollback()
            QMessageBox.warning(self, "Cached Table",
                        "The database reported an error: %s" % self.model.lastError().text())

if __name__=='__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('QPushButton{font-size: 20px; width: 200px; height: 50px;}')
    if not createConnection():
        sys.exit(1)
    editor = TableEditor('products2')
    screen = Dialog()


    sys.exit(app.exec_())