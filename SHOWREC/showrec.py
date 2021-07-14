# Form implementation generated from reading ui file 'showrec.ui'
from PyQt5 import QtCore, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(800, 900)
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(70, 50, 650, 600))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        #self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

def retranslateUi(self, Dialog):
    Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, QtWidgets.QApplication.UnicodeUTF8))
