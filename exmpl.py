import sys
from PyQt5 import QtCore, QtWidgets

class TabPage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        group = QtWidgets.QGroupBox('Monty Python')
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(group)
        grid = QtWidgets.QGridLayout(group)
        grid.addWidget(QtWidgets.QLabel('Enter a name:'), 0, 0)
        grid.addWidget(QtWidgets.QLabel('Choose a number:'), 0, 1)
        grid.addWidget(QtWidgets.QLineEdit(), 1, 0)
        grid.addWidget(QtWidgets.QComboBox(), 1, 1)
        grid.addWidget(QtWidgets.QPushButton('Click Me!'), 1, 2)
        grid.addWidget(QtWidgets.QSpinBox(), 2, 0)
        grid.addWidget(QtWidgets.QPushButton('Clear Text'), 2, 2)
        grid.addWidget(QtWidgets.QTextEdit(), 3, 0, 1, 3)

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.tabs = QtWidgets.QTabWidget()
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.tabs)
        button = QtWidgets.QToolButton()
        button.setToolTip('Add New Tab')
        button.clicked.connect(self.addNewTab)
        button.setIcon(self.style().standardIcon(
            QtWidgets.QStyle.SP_DialogYesButton))
        self.tabs.setCornerWidget(button, QtCore.Qt.TopLeftCorner)
        self.addNewTab()

    def addNewTab(self):
        text = 'Tab %d' % (self.tabs.count() + 1)
        self.tabs.addTab(TabPage(self.tabs), text)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(600, 100, 300, 200)
    window.show()
    sys.exit(app.exec_())