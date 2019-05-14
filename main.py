from PyQt5 import QtWidgets, QtGui
from sys import exit
from logic import MyWindow
from PyQt5.QtCore import QFile, QTextStream
import breeze_resources

if __name__ == "__main__":
    file = QFile(":/light.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    app = QtWidgets.QApplication([])
    app.setQuitOnLastWindowClosed(True)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("images/main_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    app.setWindowIcon(icon)
    if 'Breeze' in QtWidgets.QStyleFactory.keys():
        app.setStyle('Breeze')
    else:
        app.setStyle('Fusion')
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())
    application = MyWindow()
    exit(app.exec())
 

