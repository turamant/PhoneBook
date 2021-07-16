from PyQt5 import QtCore, QtGui, QtWidgets
# Form implementation generated from reading ui file 'DispProducts.ui'

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(600, 400)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 10, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 151, 161))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(190, 40, 71, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 70, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(230, 70, 31, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.FirstButton = QtWidgets.QPushButton(Dialog)
        self.FirstButton.setGeometry(QtCore.QRect(20, 130, 75, 23))
        self.FirstButton.setObjectName(_fromUtf8("FirstButton"))
        self.PreviousButton = QtWidgets.QPushButton(Dialog)
        self.PreviousButton.setGeometry(QtCore.QRect(120, 130, 75, 23))
        self.PreviousButton.setObjectName(_fromUtf8("PreviousButton"))
        self.NextButton = QtWidgets.QPushButton(Dialog)
        self.NextButton.setGeometry(QtCore.QRect(220, 130, 75, 23))
        self.NextButton.setObjectName(_fromUtf8("NextButton"))
        self.LastButton = QtWidgets.QPushButton(Dialog)
        self.LastButton.setGeometry(QtCore.QRect(320, 130, 75, 23))
        self.LastButton.setObjectName(_fromUtf8("LastButton"))
        self.prodid = QtWidgets.QLineEdit(Dialog)
        self.prodid.setGeometry(QtCore.QRect(90, 40, 71, 20))
        self.prodid.setObjectName(_fromUtf8("id"))
        self.prodname = QtWidgets.QLineEdit(Dialog)
        self.prodname.setGeometry(QtCore.QRect(270, 40, 131, 20))
        self.prodname.setObjectName(_fromUtf8("productname"))
        self.qty = QtWidgets.QLineEdit(Dialog)
        self.qty.setGeometry(QtCore.QRect(90, 70, 51, 20))
        self.qty.setObjectName(_fromUtf8("quantity"))
        self.price = QtWidgets.QLineEdit(Dialog)
        self.price.setGeometry(QtCore.QRect(270, 70, 61, 20))
        self.price.setObjectName(_fromUtf8("price"))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QtWidgets.QApplication.translate("Dialog", "Dialog", None))
        self.label.setText(
            QtWidgets.QApplication.translate("Dialog", "List of Products", None))
        self.label_2.setText(
            QtWidgets.QApplication.translate("Dialog", "Product ID", None))
        self.label_3.setText(
            QtWidgets.QApplication.translate("Dialog", "Product Name", None))
        self.label_4.setText(
            QtWidgets.QApplication.translate("Dialog", "Quantity", None))
        self.label_5.setText(
            QtWidgets.QApplication.translate("Dialog", "Price", None))
        self.FirstButton.setText(
            QtWidgets.QApplication.translate("Dialog", "First", None))
        self.PreviousButton.setText(
            QtWidgets.QApplication.translate("Dialog", "Previous", None))
        self.NextButton.setText(
            QtWidgets.QApplication.translate("Dialog", "Next", None))
        self.LastButton.setText(
            QtWidgets.QApplication.translate("Dialog", "Last", None))
