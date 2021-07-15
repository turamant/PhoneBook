"""
RadioButton - это переключаемая кнопка,
которая обычно используется вместе с другими RadioButton.
Только одна из кнопок может быть выбрана в один момент.
"""

from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        self.setLayout(layout)

        radiobutton = QRadioButton("Бразилия")
        radiobutton.setChecked(True)
        radiobutton.country = "Brazil"
        radiobutton.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(radiobutton, 0, 0)

        radiobutton = QRadioButton("Аргентина")
        radiobutton.country = "Argentina"
        radiobutton.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(radiobutton, 0, 1)

        radiobutton = QRadioButton("Россия")
        radiobutton.country = "Russia"
        radiobutton.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(radiobutton, 0, 2)
        self.show()

    def on_radio_button_toggled(self):
        radiobutton = self.sender()
        if radiobutton.isChecked():
            print("Selected country is %s" % (radiobutton.country))

if __name__=='__main__':
    app = QApplication(sys.argv)
    screen = Window()
    sys.exit(app.exec_())