from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(457, 377)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(290, 340, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 441, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout.addWidget(self.lineEdit_5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.dateEdit = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_5.addWidget(self.dateEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_6.addWidget(self.lineEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.btn_addTovar = QtWidgets.QPushButton(Dialog)
        self.btn_addTovar.setGeometry(QtCore.QRect(10, 340, 142, 23))
        self.btn_addTovar.setObjectName("btn_addTovar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Код товара: "))
        self.label_7.setText(_translate("Dialog", "                   Новый код:  "))
        self.label_2.setText(_translate("Dialog", "Наименование: "))
        self.label_3.setText(_translate("Dialog", "Цена:  "))
        self.pushButton.setText(_translate("Dialog", "Редактировать цену"))
        self.label_4.setText(_translate("Dialog", "Кол-во: "))
        self.pushButton_2.setText(_translate("Dialog", "Добавить приход"))
        self.label_5.setText(_translate("Dialog", "Дата: "))
        self.label_6.setText(_translate("Dialog", "Документ:  "))
        self.btn_addTovar.setText(_translate("Dialog", "!Добавить новый товар!"))


class DialogAddTovat_inDB(QtWidgets.QDialog, Ui_Dialog):  # AddTovarOBJ):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.buttonBox.accepted.connect(self.acept_data)
        self.buttonBox.rejected.connect(self.rejected_data)
        self.btn_addTovar.clicked.connect(self.addTovar)
        self.lineEdit.setText('Hello World')

        # +++ vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        # Код товара
        data = comboBox_code()
        data_dict = {row[0]: row[1:] for row in data}

        for k, v in data_dict.items():
            self.comboBox.addItem(k, v)  # !!!

        self.comboBox.currentIndexChanged.connect(self.cb_current)
        self.cb_current(0)

    def cb_current(self, index):
        name, price, quantity, data, doc = self.comboBox.currentData()  # !!!
        self.lineEdit.setText(name)
        self.lineEdit_2.setText(price)
        self.lineEdit_3.setText(quantity)
        self.lineEdit_4.setText(doc)

        _data = QtCore.QDateTime.fromString(data, "dd-MM-yyyy")
        self.dateEdit.setDateTime(_data)

    # +++ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    def acept_data(self):
        print('OK')

    def rejected_data(self):
        print('CANCEL')

    def addTovar(self):
        print('Не работает в mainModules.py')


def addTovar_DB():
    DialogAddTovat_inDB_init = DialogAddTovat_inDB()
    DialogAddTovat_inDB_init.show()
    DialogAddTovat_inDB_init.exec_()


# +++ vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
def comboBox_code():  # Запрос кода из базы SQL
    abc = [  # vvvv <----------- !!!!!!!!!
        ['21', 'AGA Антифриз Z40', '250,00', '7.00', '06-04-2021', 'BC44523'],
        ['38', 'Mannol Classic 10W-40', '380,00', '22.00', '26-12-2020', 'BV26646'],
        ['42', 'Fenom Очиститель кар', '200,00', '17.00', '22-01-2019', 'GGD423'],
        ['47', 'Gleid Master -30 жид', '350,00', '25.00', '16-04-2021', 'cX75445']
    ]
    #                                    vv <----------- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    conn = sqlite3.connect('dataTest.db')  # .sqlite')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS tovar(
       code TEXT,
       name TEXT,
       price TEXT,
       quantity TEXT,
       data TEXT,
       doc TEXT);
    """)
    conn.commit()

    cur.executemany('insert into tovar values (?,?,?,?,?,?)', abc)
    conn.commit()

    cur.execute(f"SELECT * FROM tovar")
    data = cur.fetchall()
    # print(* data, sep='\n')
    conn.close()
    return data


# +++ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = DialogAddTovat_inDB()
    w.show()
    sys.exit(app.exec_())