from mainwindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from scrapper import initDB, updateDb, dbToCoursesList
from sys import exit
from tab import TabPage
from findDialog import Ui_course_search

class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        initDB()
        self.courses = dbToCoursesList()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.addSemester()
        self.ui.add_semester_but.clicked.connect(self.addSemester)
        self.ui.courses_tab_widget.tabCloseRequested.connect(self.removeSemester)
        self.not_show = False
        self.show()

    def openSearchDialog(self):
        self.searchWindow = QtWidgets.QDialog()
        self.search_ui = Ui_course_search()
        self.search_ui.setupUi(self.searchWindow)
        self.searchWindow.show()

    def createTab(self):
        self.Form = QtWidgets.QWidget()
        ui = TabPage()
        ui.setupUi(self.Form)
        return self.Form

    def addSemester(self):
        tab = self.createTab()
        tab.children()[5].clicked.connect(lambda state: self.addRow(tab.children()[7]))
        tab.children()[6].clicked.connect(lambda state: self.removeRow(tab.children()[7]))
        tab.children()[8].clicked.connect(self.openSearchDialog)
        self.ui.semesters.append(tab)
        self.ui.courses_tab_widget.insertTab(self.ui.courses_tab_widget.count(),self.ui.semesters[len(self.ui.semesters)-1], str(self.ui.courses_tab_widget.count()+1)+" סמסטר")

    def removeSemester(self, i):
        self.ui.courses_tab_widget.removeTab(i)

    def addRow(self,table):
        table.setRowCount(table.rowCount() + 1)
        table.setCellWidget(table.rowCount() - 1, 0, self.createComboBox())

    def removeRow(self,table):
        rows = table.rowCount()
        if table.item(rows - 1, 1) == None:
            table.setRowCount(rows - 1)
        else:
            ans = table.my_close()
            if ans:
                table.setRowCount(rows - 1)

    def createComboBox(self):
        combo_box = QtWidgets.QComboBox()
        combo_box.setFocusPolicy(QtCore.Qt.StrongFocus)
        combo_box.setLayoutDirection(QtCore.Qt.RightToLeft)
        combo_box.addItem("חובה")
        combo_box.addItem("רשימה א")
        combo_box.addItem("רשימה ב")
        combo_box.addItem("פרוייקט")
        combo_box.addItem("ספורט")
        combo_box.addItem("מל\"ג")
        combo_box.addItem("חופשי")
        return combo_box

    def my_close(self):
        if not self.not_show:
            cb = QtWidgets.QCheckBox("לא להראות שוב.")
            msgbox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question, "מחיקה", "למחוק שורה בעלת תוכן?")
            msgbox.addButton(QtWidgets.QMessageBox.Yes)
            msgbox.addButton(QtWidgets.QMessageBox.No)
            msgbox.setDefaultButton(QtWidgets.QMessageBox.No)
            msgbox.setCheckBox(cb)

            reply = msgbox.exec()

            self.not_show = bool(cb.isChecked())
            if reply == QtWidgets.QMessageBox.No:
                return False
            else:
                return True
        else:
            return True

