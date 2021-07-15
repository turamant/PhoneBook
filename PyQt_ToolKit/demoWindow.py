import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Hello")
        layout = QGridLayout()
        self.setLayout(layout)
        label = QLabel("Hello, turamant!")
        layout.addWidget(label, 0, 0)
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    screen = MyWindow()
    sys.exit(app.exec_())