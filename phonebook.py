import sys
from PyQt5 import QtWidgets, QtSql, QtCore


def createDB():
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('phonebook.db')
    if not db.open():
        QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Cannot open database"),
                                       QtWidgets.qApp.tr("Unable to establish a database connection.\n"
                                                 "This example needs SQLite support. Please read "
                                                 "the Qt SQL driver documentation for information "
                                                 "how to build it.\n\n"
                                                 "Click Cancel to exit."),
                                       QtWidgets.QMessageBox.Cancel)
        return False
    query = QtSql.QSqlQuery()
    query.exec_("create table phonebook(id int primary key, "
                "firstname varchar(20), lastname varchar(20))")
    query.exec_("insert into phonebook values(101, 'Roger', 'Federer')")
    query.exec_("insert into phonebook values(102, 'Christiano', 'Ronaldo')")
    query.exec_("insert into phonebook values(103, 'Ussain', 'Bolt')")
    query.exec_("insert into phonebook values(104, 'Sachin', 'Tendulkar')")
    query.exec_("insert into phonebook values(105, 'Saina', 'Nehwal')")
    return True

def initializeModel(model):
    model.setTable('phonebook')
    model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    model.select()
    model.setHeaderData(0, QtCore.Qt.Orientation.Horizontal, "ID")
    model.setHeaderData(1, QtCore.Qt.Orientation.Horizontal, "First name")
    model.setHeaderData(2, QtCore.Qt.Orientation.Horizontal, "Last name")

def createView(title, model):
    view = QtWidgets.QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view

def addrow():
    print(model.rowCount())
    ret = model.insertRows(model.rowCount(), 1)
    print(ret)

def findrow(i):
    delrow = i.row()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    createDB()
    model = QtSql.QSqlTableModel()
    delrow=-1
    initializeModel(model)
    view1 = createView("Table Model (View 1)", model)
    view1.clicked.connect(findrow)
    dlg = QtWidgets.QDialog()
    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(view1)
    button = QtWidgets.QPushButton("Add a row")
    button.clicked.connect(addrow)
    layout.addWidget(button)
    btn1 = QtWidgets.QPushButton("del a row")
    btn1.clicked.connect(lambda: model.removeRow(view1.currentIndex().row()))
    layout.addWidget(btn1)
    dlg.setLayout(layout)
    dlg.setWindowTitle("Database Demo")
    dlg.show()
    sys.exit(app.exec_())