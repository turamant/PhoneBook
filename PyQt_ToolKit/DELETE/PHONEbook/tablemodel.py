from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtSql import QSqlTableModel

import connection


def initializeModel(model):
    model.setTable('person')

    model.setEditStrategy(QSqlTableModel.OnManualSubmit)
    model.select()

    model.setHeaderData(0, Qt.Horizontal, "ID")
    model.setHeaderData(1, Qt.Horizontal, "First name")
    model.setHeaderData(2, Qt.Horizontal, "Last name")


def createView(title, model):
    view = QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    if not connection.createConnection():
        sys.exit(1)

    model = QSqlTableModel()

    initializeModel(model)

    view1 = createView("Table Model (View 1)", model)
    view2 = createView("Table Model (View 2)", model)

    view1.show()
    view2.move(view1.x() + view1.width() + 20, view1.y())
    view2.show()

    sys.exit(app.exec_())