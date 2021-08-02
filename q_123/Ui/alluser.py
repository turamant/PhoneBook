# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alluser.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AllUserTableDialog(object):
    def setupUi(self, AllUserTableDialog):
        AllUserTableDialog.setObjectName("AllUserTableDialog")
        AllUserTableDialog.resize(1180, 822)
        self.HeadLabel = QtWidgets.QLabel(AllUserTableDialog)
        self.HeadLabel.setGeometry(QtCore.QRect(850, 20, 121, 41))
        self.HeadLabel.setStyleSheet("font: 14pt \"Cantarell\";")
        self.HeadLabel.setObjectName("HeadLabel")
        self.familyLabel = QtWidgets.QLabel(AllUserTableDialog)
        self.familyLabel.setGeometry(QtCore.QRect(800, 710, 171, 41))
        self.familyLabel.setText("")
        self.familyLabel.setObjectName("familyLabel")
        self.userTableWidget = QtWidgets.QTableWidget(AllUserTableDialog)
        self.userTableWidget.setGeometry(QtCore.QRect(130, 70, 691, 681))
        self.userTableWidget.setRowCount(10000)
        self.userTableWidget.setColumnCount(3)
        self.userTableWidget.setObjectName("userTableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.userTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.userTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.userTableWidget.setHorizontalHeaderItem(2, item)
        self.cancelPushButton = QtWidgets.QPushButton(AllUserTableDialog)
        self.cancelPushButton.setGeometry(QtCore.QRect(940, 130, 151, 41))
        self.cancelPushButton.setStyleSheet("border-radius:20px;\n"
"font: 12pt \"Cantarell\";\n"
"background-color: red;")
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.labelUser = QtWidgets.QLabel(AllUserTableDialog)
        self.labelUser.setGeometry(QtCore.QRect(980, 30, 171, 21))
        self.labelUser.setStyleSheet("font: 12pt \"Cantarell\";\n"
"color: rgb(18, 10, 255);")
        self.labelUser.setObjectName("labelUser")
        self.headLabe = QtWidgets.QLabel(AllUserTableDialog)
        self.headLabe.setGeometry(QtCore.QRect(280, 10, 431, 41))
        self.headLabe.setStyleSheet("font: 14pt \"Cantarell\";\n"
"font: 18pt \"Cantarell\";\n"
"color: rgb(43, 0, 255);")
        self.headLabe.setObjectName("headLabe")
        self.delPushButton = QtWidgets.QPushButton(AllUserTableDialog)
        self.delPushButton.setGeometry(QtCore.QRect(872, 340, 241, 36))
        self.delPushButton.setStyleSheet("font: 12pt \"Cantarell\";\n"
"background-color: rgb(255, 35, 6);")
        self.delPushButton.setObjectName("delPushButton")
        self.emailLineEdit = QtWidgets.QLineEdit(AllUserTableDialog)
        self.emailLineEdit.setGeometry(QtCore.QRect(930, 270, 181, 36))
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.emailLabel = QtWidgets.QLabel(AllUserTableDialog)
        self.emailLabel.setGeometry(QtCore.QRect(830, 280, 74, 21))
        self.emailLabel.setStyleSheet("font: 12pt \"Cantarell\";")
        self.emailLabel.setObjectName("emailLabel")

        self.retranslateUi(AllUserTableDialog)
        QtCore.QMetaObject.connectSlotsByName(AllUserTableDialog)

    def retranslateUi(self, AllUserTableDialog):
        _translate = QtCore.QCoreApplication.translate
        AllUserTableDialog.setWindowTitle(_translate("AllUserTableDialog", "Dialog"))
        self.HeadLabel.setText(_translate("AllUserTableDialog", "Зашли как:"))
        item = self.userTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AllUserTableDialog", "E-mail"))
        item = self.userTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AllUserTableDialog", "Password"))
        item = self.userTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("AllUserTableDialog", "Save"))
        self.cancelPushButton.setText(_translate("AllUserTableDialog", "назад"))
        self.labelUser.setText(_translate("AllUserTableDialog", "User"))
        self.headLabe.setText(_translate("AllUserTableDialog", "Все пользователи программы"))
        self.delPushButton.setText(_translate("AllUserTableDialog", "Удалить пользователя"))
        self.emailLabel.setText(_translate("AllUserTableDialog", "email"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AllUserTableDialog = QtWidgets.QDialog()
    ui = Ui_AllUserTableDialog()
    ui.setupUi(AllUserTableDialog)
    AllUserTableDialog.show()
    sys.exit(app.exec_())