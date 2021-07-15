"""
PushButton часто используется, чтобы заставить программу делать что-то,
когда пользователю просто нужно нажать кнопку. Этот
может начинать загрузку или удалять файл.
"""
import sys

from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication

"""                     -=  SIGNALS -=
Одна из общих функций кнопки - это нажатие пользователем и выполнение связанного действия.
Это делается путем подключения сигнала нажатия кнопки к соответствующей функции: 
"""

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        self.setLayout(layout)

        button = QPushButton("Нажми сюда")
        button.setToolTip("This ToolTip simply displays text.")
        button.clicked.connect(self.on_button_clicked)
        layout.addWidget(button, 0, 0)

        button = QPushButton("выход")
        button.clicked.connect(self.exit_window)
        layout.addWidget(button, 0, 1)

        self.show()

    def on_button_clicked(self):
        print("Кнопка была нажата. Я функция - СЛОТ")

    def exit_window(self):
        sys.exit(app.exec_())

if __name__=='__main__':
    app = QApplication(sys.argv)
    screen = Window()
    sys.exit(app.exec_())