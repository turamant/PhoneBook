# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoLineEdit.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(574, 304)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEditName = QtWidgets.QLineEdit(Dialog)
        self.lineEditName.setObjectName("lineEditName")
        self.verticalLayout.addWidget(self.lineEditName)
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setObjectName("labelResponse")
        self.verticalLayout.addWidget(self.labelResponse)
        self.ButtonClickMe = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ButtonClickMe.setFont(font)
        self.ButtonClickMe.setObjectName("ButtonClickMe")
        self.verticalLayout.addWidget(self.ButtonClickMe)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Введите ваше имя"))
        self.lineEditName.setPlaceholderText(_translate("Dialog", "введите ваше имя"))
        self.labelResponse.setText(_translate("Dialog", "TextLabel"))
        self.ButtonClickMe.setText(_translate("Dialog", "Click"))
