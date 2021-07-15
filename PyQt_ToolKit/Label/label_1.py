"""
Виджет Label используется для отображения текста пользователю.
Это может быть что угодно, от односложных меток, обозначающих цель
другого виджета, в отдельные предложения, в многострочные блоки текста,
состоящие из нескольких абзацев.
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

        label = QLabel("Пайтон из Монти")
        layout.addWidget(label, 0, 0)

        label = QLabel("Несколько человек изучают Python")
        label.setWordWrap(True)
        layout.addWidget(label, 0, 1)
        self.show()


if __name__=='__main__':
    app = QApplication(sys.argv)
    screen = Window()
    sys.exit(app.exec_())
