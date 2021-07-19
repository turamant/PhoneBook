import sys
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

from demochekbox import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.checkBoxChees.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxOliva.stateChanged.connect(self.dispAmount)
        self.ui.echeckBoxSousaj.stateChanged.connect(self.dispAmount)
        self.show()

    def dispAmount(self):
        amount=10
        if self.ui.checkBoxChees.isChecked() == True:
            amount=amount+1
        if self.ui.checkBoxOliva.isChecked() == True:
            amount=amount+1
        if self.ui.echeckBoxSousaj.isChecked() == True:
            amount=amount+2
        self.ui.labelAmount.setText("Total amount for pizza is" + str(amount))

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())