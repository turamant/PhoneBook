import sys
from PyQt5 import QtWidgets

from Sander.FirstToSecondWindow.dialogfirst import Ui_DialogFirst
from Sander.FirstToSecondWindow.dialogsecond import Ui_DialogSecond


def openSecondWindow():
    global dialsec
    dialsec = QtWidgets.QDialog()
    ui = Ui_DialogSecond()
    ui.setupUi(dialsec)
    dialfir.close()
    #dialfir.hide()
    dialsec.show()

    def returnToFirstWindow():
        dialsec.close()
        dialfir.show()

    ui.pushButtonSecond.clicked.connect(returnToFirstWindow)

app = QtWidgets.QApplication(sys.argv)
dialfir = QtWidgets.QDialog()
ui = Ui_DialogFirst()
ui.setupUi(dialfir)
dialfir.show()

ui.pushButtonFirst.clicked.connect(openSecondWindow)














sys.exit(app.exec_())