from PyQt5 import QtWidgets, QtGui, QtCore
from logic import MyWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setQuitOnLastWindowClosed(True)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("images/main_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    app.setWindowIcon(icon)
    app.setStyle("Breeze")
    application = MyWindow()
    exit(app.exec())
