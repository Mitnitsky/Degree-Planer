from mainwindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from scrapper import *
from sys import exit
from tab import TabPage, createRemoveLineButton
from findDialog import Ui_course_search
from progress import Ui_Form
from itertools import product
from updatedbthread import mythread
import threading

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        initDB()
        self.courses = dbToCoursesList()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.addSemester()
        self.ui.add_semester_but.clicked.connect(self.addSemester)
        self.ui.courses_tab_widget.tabCloseRequested.connect(
            self.removeSemester)
        self.not_show_remove_course = False
        self.not_show_remove_semester = False
        self.show()
        self.ui.actionUpdate_Courses_DB.triggered.connect(self.dbUpdate)

    def dbUpdate(self):
        # self.progress_ui = Ui_Form()
        # self.progress_ui.setupUi(self.progressBar)
        self.progressBar = QtWidgets.QProgressBar()
        self.progressBar.show()
        semester_tag = "input"
        semester_attrs = {"type": "radio", "name": "SEM"}
        faculties_tag = "option"
        faculties_attrs = {}
        search_url = 'https://ug3.technion.ac.il/rishum/search'
        semesters = getData(search_url, semester_tag, semester_attrs, "values")
        faculties = getData(search_url, faculties_tag, faculties_attrs, "values")
        packages = []
        for combination in product(semesters, faculties):
            packages.append(preparePackage(combination[0], combination[1]))
        course_numbers = set()
        for package in packages:
            for course in getCourses(search_url, package):
                course_numbers.add(course)
        cnt = 0
        course_ammount = len(course_numbers)
        li = [course_numbers,0]
        self.progressBar = QtWidgets.QProgressBar()
        self.progressBar.show()
        self.thread = mythread(li,semesters)
        self.thread.run()
        while self.thread.alive:
            self.progressBar.setValue(li[1]/course_ammount)


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
        table = tab.children()[7]
        tab.children()[5].clicked.connect(lambda state: self.addRow(
            table))
        tab.children()[6].clicked.connect(lambda state: self.removeRow(
            table))
        tab.children()[8].clicked.connect(self.openSearchDialog)
        value = []
        lambdas = []
        buttons = []
        for i in range(0, table.rowCount()):
            button = createRemoveLineButton(str(i))
            value.append(i)
            lambdas.append(lambda state: self.clearRow(table))
            button.clicked.connect(lambdas[i])
            buttons.append(button)
            table.setCellWidget(i, table.columnCount()-1, buttons[i])

        self.ui.semesters.append(tab)
        self.ui.courses_tab_widget.insertTab(
            self.ui.courses_tab_widget.count(),
            self.ui.semesters[len(self.ui.semesters) - 1],
            str(self.ui.courses_tab_widget.count() + 1) + " סמסטר")
    
    def clearRow(self, table):
        row = int(self.sender().objectName())
        for column in range(1, table.columnCount()-1):
            if table.item(row,column) != None:
                table.item(row,column).setText("")

    def removeSemester(self, i):
        self.my_close("semester", "האם למחוק סמסטר ?")
        self.ui.courses_tab_widget.removeTab(i)

    def addRow(self, table):
        table.setRowCount(table.rowCount() + 1)
        table.setCellWidget(table.rowCount() - 1, 0, self.createComboBox())
        button = createRemoveLineButton(str(table.rowCount()-1))
        button.clicked.connect(lambda state: self.clearRow(table))
        table.setCellWidget(table.rowCount() - 1, table.columnCount()-1, button)

    def removeRow(self, table):
        rows = table.rowCount()
        # table.
        if table.item(rows - 1, 1) == None:
            table.setRowCount(rows - 1)
        else:
            ans = self.my_close("row", "למחוק שורה בעלת תוכן?")
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

    def my_close(self, not_show_param, msg):
        if not_show_param == "row" and not self.not_show_remove_course:
            return self.warningMsg(not_show_param,msg)
        elif not_show_param == "semester" and not self.not_show_remove_semester:
            return self.warningMsg(not_show_param,msg)

    def warningMsg(self, not_show_param, msg):
        cb = QtWidgets.QCheckBox("לא להראות שוב.")
        msgbox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question,
                                    "מחיקה", msg)
        msgbox.addButton(QtWidgets.QMessageBox.Yes)
        msgbox.addButton(QtWidgets.QMessageBox.No)
        msgbox.setDefaultButton(QtWidgets.QMessageBox.No)
        msgbox.setCheckBox(cb)
        reply = msgbox.exec()
        if not_show_param == "semester":
            self.not_show_remove_semester = bool(cb.isChecked())
        elif not_show_param == "row":
            self.not_show_remove_course = bool(cb.isChecked())
        if reply == QtWidgets.QMessageBox.No:
            return False
        else:
            return True
    #TODO:
