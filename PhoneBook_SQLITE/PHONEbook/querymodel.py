from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtSql import QSqlQuery, QSqlQueryModel

import connection


class CustomSqlModel(QSqlQueryModel):
    def data(self, index, role):
        value = super(CustomSqlModel, self).data(index, role)
        if value is not None and role == Qt.DisplayRole:
            if index.column() == 0:
                return '#%d' % value
            elif index.column() == 2:
                return value.upper()

        if role == Qt.TextColorRole and index.column() == 1:
            return QColor(Qt.blue)

        return value


class EditableSqlModel(QSqlQueryModel):
    def flags(self, index):
        flags = super(EditableSqlModel, self).flags(index)

        if index.column() in (1, 2):
            flags |= Qt.ItemIsEditable

        return flags

    def setData(self, index, value, role):
        if index.column() not in (1, 2):
            return False

        primaryKeyIndex = self.index(index.row(), 0)
        id = self.data(primaryKeyIndex)

        self.clear()

        if index.column() == 1:
            ok = self.setFirstName(id, value)
        else:
            ok = self.setLastName(id, value)

        self.refresh()
        return ok

    def refresh(self):
        self.setQuery('select * from person')
        self.setHeaderData(0, Qt.Horizontal, "ID")
        self.setHeaderData(1, Qt.Horizontal, "First name")
        self.setHeaderData(2, Qt.Horizontal, "Last name")

    def setFirstName(self, personId, firstName):
        query = QSqlQuery()
        query.prepare('update person set firstname = ? where id = ?')
        query.addBindValue(firstName)
        query.addBindValue(personId)
        return query.exec_()

    def setLastName(self, personId, lastName):
        query = QSqlQuery()
        query.prepare('update person set lastname = ? where id = ?')
        query.addBindValue(lastName)
        query.addBindValue(personId)
        return query.exec_()


def initializeModel(model):
    model.setQuery('select * from person')
    model.setHeaderData(0, Qt.Horizontal, "ID")
    model.setHeaderData(1, Qt.Horizontal, "First name")
    model.setHeaderData(2, Qt.Horizontal, "Last name")


offset = 0
views = []

def createView(title, model):
    global offset, views

    view = QTableView()
    views.append(view)
    view.setModel(model)
    view.setWindowTitle(title)
    view.move(100 + offset, 100 + offset)
    offset += 20
    view.show()


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    if not connection.createConnection():
        sys.exit(1)

    plainModel = QSqlQueryModel()
    editableModel = EditableSqlModel()
    customModel = CustomSqlModel()

    initializeModel(plainModel)
    initializeModel(editableModel)
    initializeModel(customModel)

    createView("Plain Query Model", plainModel)
    createView("Editable Query Model", editableModel)
    createView("Custom Query Model", customModel)

    sys.exit(app.exec_())