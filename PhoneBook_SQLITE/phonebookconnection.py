from PyQt5 import QtWidgets, QtSql, QtGui



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

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createDB()
    print("Создана база данных!")