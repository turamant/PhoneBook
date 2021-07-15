"""
Контейнер - Сетка - Grid

"""
import sys

from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QApplication


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        self.setLayout(layout)

        label = QLabel("Label (0, 0)")
        layout.addWidget(label, 0, 0)
        label = QLabel("Label (0, 1)")
        layout.addWidget(label, 0, 1)
        label = QLabel("Label (1, 0) охватывает 2 столбца")
        layout.addWidget(label, 1, 0, 1, 2)
        label = QLabel("Label (1, 0) охватывает 2 строки 2 rows")
        layout.addWidget(label, 0, 2, 2, 1)

        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    screen = Window()
    sys.exit(app.exec_())