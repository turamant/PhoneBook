import sys

from PyQt5.QtWidgets import QGridLayout, QLabel, QDialogButtonBox

from Sander.check_db import *
from des import *



def check_input(funct):
    """
    проверка корректности ввода
    """
    def wrapper(self):
        for line_edit in self.base_line_edit:
            if len(line_edit.text()) == 0:
                return
        funct(self)
    return wrapper


class Dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'Окно регистрации нового акаунта'
        self.left = 100
        self.top = 100
        self.width = 420
        self.height = 620
        self.initUI()

    def initUI(self):

        layout = QGridLayout()
        self.setLayout(layout)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        label = QLabel("Вам есть 18 лет ?")
        layout.addWidget(label, 0, 0)
        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        layout.addWidget(buttonbox)
        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)
        self.show()

    def accept(self):
        print("Press OK!")
        return True

    def reject(self):
        print("Подрастёшь заходи!")
        #self.close()
        sys.exit(app.exec_())

class Interface(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Окно авторизации")
        self.show()


        self.base_line_edit = [self.ui.lineEdit, self.ui.lineEdit_2]

        self.ui.loginButton.clicked.connect(self.auth)
        self.ui.registrButton.clicked.connect(self.reg)
        self.ui.canselButton.clicked.connect(self.close)

        self.ui.checkBox_2.stateChanged.connect(self.dispAmount)
        self.ui.checkBox.stateChanged.connect(self.saveMe)
        self.ui.updateButton.clicked.connect(self.updatePassword)

        self.ui.newRegistrButton.clicked.connect(self.newWindow)

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)


    def newWindow(self):
        self.pd = Dialog()

    def dispAmount(self):
        self.ui.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        if self.ui.checkBox_2.isChecked() == True:
            self.ui.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)

    def saveMe(self):
        print("Сохранить учетку для входа!")

    def updatePassword(self):
        print("UpdatePassword")

    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)


    @check_input
    def auth(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        self.check_db.thr_login(name, passw)

    @check_input
    def reg(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        self.check_db.thr_register(name, passw)


if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    mywin = Interface()

    sys.exit(app.exec_())