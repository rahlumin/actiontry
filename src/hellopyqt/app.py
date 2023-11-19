"""
Originally 
PyQT5 hello world
https://pythonprogramminglanguage.com/pyqt5-hello-world/
"""
import sys
from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PySide2.QtCore import QSize


class HelloWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(640, 480))
        self.setWindowTitle("Hello world - pythonprogramminglanguage.com") 

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)

        title = QLabel("Hello World from PyQt", self)
        title.setAlignment(QtCore.Qt.AlignCenter)
        gridLayout.addWidget(title, 0, 0)


def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
