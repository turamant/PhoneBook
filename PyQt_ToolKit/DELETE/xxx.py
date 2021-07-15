
from PyQt5.QtWidgets import *


class Dialog(QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self):
        super(Dialog, self).__init__()

        self.createMenu()
        self.createHorizontalGroupBox()


        
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.setMenuBar(self.menuBar)
        mainLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Basic Layouts")

    def createMenu(self):
        self.menuBar = QMenuBar()

        self.fileMenu = QMenu("&File", self)
        self.exitAction = self.fileMenu.addAction("E&xit")
        self.menuBar.addMenu(self.fileMenu)

        self.exitAction.triggered.connect(self.accept)

    def createHorizontalGroupBox(self):
        self.horizontalGroupBox = QGroupBox("Horizontal layout")
        layout = QHBoxLayout()

        for i in range(Dialog.NumButtons):
            button = QPushButton("Button %d" % (i + 1))
            layout.addWidget(button)

        self.horizontalGroupBox.setLayout(layout)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())