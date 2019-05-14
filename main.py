from PyQt5 import QtWidgets, QtGui
from sys import exit
from logic import MyWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setQuitOnLastWindowClosed(True)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("images/main_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    app.setWindowIcon(icon)
    ## Linux case
    if 'Breeze' in QtWidgets.QStyleFactory.keys():
        app.setStyle('Breeze')
    else:
    ## Windows case
        app.setStyle('Fusion')
    application = MyWindow()
    exit(app.exec())
 

