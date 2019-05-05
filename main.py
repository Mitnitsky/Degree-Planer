from mainwindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from scrapper import initDB, updateDb, dbToCoursesList
from findDialog import Ui_course_search
from sys import exit


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        initDB()
        self.courses = dbToCoursesList()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.semester_add_course.clicked.connect(self.ui.openSearchDialog)
        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MyWindow()
    exit(app.exec())
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())


