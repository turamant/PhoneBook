import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication

class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(self.this_call)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        self.show()

    def this_call(self):
        print('bye bye')
        app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())