import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from dialogfirst import Ui_DialogFirst
from dialogsecond import Ui_DialogSecond

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogFirst()
        self.ui.setupUi(self)
        self.ui.pushButtonFirst.clicked.connect(self.gotoScreen2)

    def gotoScreen2(self):
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Screen2(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogSecond()
        self.ui.setupUi(self)
        self.ui.pushButtonSecond.clicked.connect(self.gotoScreen1)

    def gotoScreen1(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)

if __name__=='__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    mainwindow = MainWindow()
    widget.addWidget(mainwindow)
    widget.setFixedHeight(300)
    widget.setFixedWidth(400)
    widget.show()

    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")
