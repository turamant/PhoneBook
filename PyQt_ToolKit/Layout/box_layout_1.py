"""
Контейнер коробка либо один столбец или строку виджетов.
Меняется динамически в зависимости от количество виджетов
Подобен GridLayout
"""

from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.setLayout(layout)
        label = QLabel("Label 1")
        label.setToolTip("This ToolTip simply displays text.")
        layout.addWidget(label, 0)
        label = QLabel("Label 2")
        layout.addWidget(label, 0)

        layout2 = QBoxLayout(QBoxLayout.TopToBottom)
        layout.addLayout(layout2)
        label = QLabel("Label 3")
        layout2.addWidget(label, 0)
        label = QLabel("Label 4")
        layout2.addWidget(label, 0)
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    screen = Window()
    sys.exit(app.exec_())