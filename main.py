from PyQt5 import QtWidgets
from logic import MyWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MyWindow()
    app.exec()
