from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtSql import (QSqlQuery, QSqlRelation, QSqlRelationalDelegate,
        QSqlRelationalTableModel, QSqlTableModel)

import connection


def initializeModel(model):
    model.setTable('employee')

    model.setEditStrategy(QSqlTableModel.OnManualSubmit)
    model.setRelation(2, QSqlRelation('city', 'id', 'name'))
    model.setRelation(3, QSqlRelation('country', 'id', 'name'))

    model.setHeaderData(0, Qt.Horizontal, "ID")
    model.setHeaderData(1, Qt.Horizontal, "Name")
    model.setHeaderData(2, Qt.Horizontal, "City")
    model.setHeaderData(3, Qt.Horizontal, "Country")

    model.select()


def createView(title, model):
    view = QTableView()
    view.setModel(model)
    view.setItemDelegate(QSqlRelationalDelegate(view))
    view.setWindowTitle(title)

    return view


def createRelationalTables():
    query = QSqlQuery()

    query.exec_("create table employee(id int, name varchar(20), city int, country int)")
    query.exec_("insert into employee values(1, 'Espen', 5000, 47)")
    query.exec_("insert into employee values(2, 'Harald', 80000, 49)")
    query.exec_("insert into employee values(3, 'Sam', 100, 41)")

    query.exec_("create table city(id int, name varchar(20))")
    query.exec_("insert into city values(100, 'San Jose')")
    query.exec_("insert into city values(5000, 'Oslo')")
    query.exec_("insert into city values(80000, 'Munich')")

    query.exec_("create table country(id int, name varchar(20))")
    query.exec_("insert into country values(41, 'USA')")
    query.exec_("insert into country values(47, 'Norway')")
    query.exec_("insert into country values(49, 'Germany')")


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    if not connection.createConnection():
        sys.exit(1)

    createRelationalTables()

    model = QSqlRelationalTableModel()

    initializeModel(model)

    view = createView("Relational Table Model", model)

    view.show()

    sys.exit(app.exec_())