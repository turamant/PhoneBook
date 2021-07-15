import sys

from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QLabel, QTextEdit, QPushButton, QCheckBox


class TwoWindow(QDialog):
    def __init__(self):
        super(TwoWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.lb1 = QLabel("Search for: ", self)
        self.lb1.setStyleSheet("font-size: 15px; ")
        self.lb1.move(10, 10)

        self.te = QTextEdit(self)
        self.te.move(10, 40)
        self.te.resize(250, 25)

        self.src = QPushButton("Find", self)
        self.src.move(270, 40)

        self.lb2 = QLabel("Replace all by: ", self)
        self.lb2.setStyleSheet("font-size: 15px; ")
        self.lb2.move(10, 80)

        self.rp = QTextEdit(self)
        self.rp.move(10, 110)
        self.rp.resize(250, 25)

        self.rpb = QPushButton("Replace", self)
        self.rpb.move(270, 110)
        self.setGeometry(300, 300, 360, 250)

        self.show()



class MyWindow(QWindow):
    """
    Косячное окно получается
    Но когда его нагружаешь инфой , то все нормально!
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setTitle("Window")
        self.resize(800, 900)
        self.show()

class MainWindow(QMainWindow):
    """
    Хорошее главное окно!
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("this is MainWindow")
        self.resize(800, 900)
        self.show()

def main():
    app = QApplication(sys.argv)
    #screen1 = MyWindow()
    screen2 = MainWindow()
    screen3 = TwoWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
