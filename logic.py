from mainwindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from scrapper import *
from sys import exit
from tab import TabPage, createRemoveLineButton
from findDialog import Ui_course_search
from progress import Ui_Form
from itertools import product
from course import Course
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
        self.ui.must_of_in.textChanged.connect(self.update)
        self.ui.list_a_of_in_7.textChanged.connect(self.update)
        self.ui.list_b_of_in_7.textChanged.connect(self.update)
        self.ui.project_of_in_7.textChanged.connect(self.update)
        self.ui.sport_of_in_7.textChanged.connect(self.update)
        self.ui.malag_of_in_7.textChanged.connect(self.update)
        self.ui.free_done_in_7.textChanged.connect(self.update)
        self.ui.deg_points_in.textChanged.connect(self.update)
        self.not_show_remove_course = False
        self.not_show_remove_semester = False
        self.ui.english_checkbox_7.stateChanged['int'].connect(self.update)
        self.show()
        self.ui.actionUpdate_Courses_DB.triggered.connect(self.dbUpdate)

    def dbUpdate(self):
        self.progress_ui = Ui_Form()
        self.progressBar = QtWidgets.QProgressBar()
        self.progress_ui.setupUi(self.progressBar)
        self.progressBar.show()
        self.course_update = [0]
        # semester_tag = "input"
        # semester_attrs = {"type": "radio", "name": "SEM"}
        # faculties_tag = "option"
        # faculties_attrs = {}
        # search_url = 'https://ug3.technion.ac.il/rishum/search'
        # semesters = getData(search_url, semester_tag, semester_attrs, "values")
        # faculties = getData(search_url, faculties_tag, faculties_attrs, "values")
        # packages = []
        # for combination in product(semesters, faculties):
        #     packages.append(preparePackage(combination[0], combination[1]))
        # course_numbers = set()
        # for package in packages:
        #     for course in getCourses(search_url, package):
        #         course_numbers.add(course)
        # cnt = 0
        # course_amount = len(course_numbers)
        # li = [course_numbers,0]
        self.progressBar.setValue(0)
        self.thread = threading.Thread(target=updateDb, args=[self.course_update]).start()
        self.thread2 = threading.Thread(target=self.updateProgressBar, args=[]).start()
        # self.thread = mythread(li,semesters)
        # while self.thread.isAlive():


    def updateProgressBar(self):
        while self.thread2.isAlive():
            self.progressBar.setValue(self.course_update[0])

    def openSearchDialog(self):
        self.searchWindow = QtWidgets.QDialog()
        self.search_ui = Ui_course_search()
        self.search_ui.setupUi(self.searchWindow)
        self.searchWindow.children()[3].clicked.connect(lambda state: self.closeIt(self.searchWindow)) #close
        self.searchWindow.children()[4].clicked.connect(lambda state: self.addCourse(self.searchWindow)) #add
        self.searchWindow.show()

    def checkIfRowIsEmpty(self,table, row):
        for column in range(1, table.columnCount()-1):
            if table.item(row,column):
                if table.item(row,column).text() != "":
                    return False
        return True

    def addCourseContent(self, course_num, table, row): 
        course = findCourseInDB(course_num)
        course_num = QtWidgets.QTableWidgetItem()
        course_num.setText(str(course.number))
        course_name = QtWidgets.QTableWidgetItem()
        course_name.setText(course.name)
        course_points = QtWidgets.QTableWidgetItem()
        if course.points == 0:
            course_points.setText("0")
        else:
            course_points.setText(str(course.points))
        course_name.setTextAlignment(QtCore.Qt.AlignCenter)
        course_num.setTextAlignment(QtCore.Qt.AlignCenter)
        course_num.setToolTip("מקוצועות קדם: "+course.reprDependencies()+"\n"
            +"מקצועות צמודים: "+course.repOtherData(course.parallel)+"\n"
                +"מקצועות ללא זיכוי נוסף: "+ course.repOtherData(course.similarities)+"\n"
                    +"מקצועות ללא זיכוי נוסף(מוכלים): "+course.repOtherData(course.inclusive))
        # course_num.
        course_points.setTextAlignment(QtCore.Qt.AlignCenter)
        table.setItem(row,1,course_num)
        table.setItem(row,2,course_name)
        table.setItem(row,3,course_points)
        return

    def findEmptyRow(self, widget):
        table = self.ui.courses_tab_widget.currentWidget().children()[7]
        for row in range(table.rowCount()):
            if self.checkIfRowIsEmpty(table, row):
                return row
        self.addRow(table)
        return table.rowCount()-1

    def addCourse(self, widget):
        if widget.children()[1].text() == '':
            self.errorMsg("לא הוכנס מספר קורס, נסה שנית.")
            return
        inputText = widget.children()[7].toPlainText()
        if inputText == '' or inputText == "'הקורס לא נמצא במערכת, נסה שנית.'":
            self.errorMsg("הקורס לא נמצא במערכת, נסה שנית.")
            return
        row = self.findEmptyRow(widget)
        table = self.ui.courses_tab_widget.currentWidget().children()[7]
        self.addCourseContent( widget.children()[1].text(), table, row)
        widget.close() #TODO: Questionable, might leave widget open to add other courses as well

    def closeIt(self, widget):
        widget.close()

    def createTab(self):
        self.Form = QtWidgets.QWidget()
        ui = TabPage()
        ui.setupUi(self.Form)
        return self.Form
    
    def updateAverage(self):
        total_sum = 0
        total_points = 0
        for tab in range(self.ui.courses_tab_widget.count()):
            semester_sum = 0
            semester_points = 0
            table = self.ui.courses_tab_widget.widget(tab).children()[7]
            semester_average = self.ui.courses_tab_widget.widget(tab).children()[2] #Average
            for row in range(table.rowCount()):
                try:
                    if table.item(row,3) and float(table.item(row,3).text()) > 0:
                        if table.item(row,4) and float(table.item(row,4).text()) > 0:
                            semester_points += float(table.item(row,3).text())
                            semester_sum += float(table.item(row,3).text()) * float(table.item(row,4).text())
                except (ValueError, AttributeError):
                    continue
            if(semester_points > 0):
                semester_average.setText(str((semester_sum / semester_points)))
            else:
                semester_average.setText(str(0))
            total_points += semester_points
            total_sum += semester_sum
        if total_points > 0:
            self.ui.average_in_7.setText(str(total_sum / total_points))
        else:
            self.ui.average_in_7.setText(str(0))
            

    def updatePoints(self):
        points = {"חובה":0, \
                  "רשימה א":0, \
                  "רשימה ב":0, \
                  "פרוייקט":0, \
                  "ספורט":0, \
                  "מל\"ג":0, \
                  "חופשי":0}
        points_done = 0
        for tab in range(self.ui.courses_tab_widget.count()):
            table = self.ui.courses_tab_widget.widget(tab).children()[7]
            table_points = self.ui.courses_tab_widget.widget(tab).children()[4] #Points
            table_points.setText("0")
            for row in range(table.rowCount()):
                try:
                    if table.item(row,3) and float(table.item(row,3).text()) > 0:
                        try:
                            if table.item(row,4) and float(table.item(row,4).text()) > 0:
                                points_done += float(table.item(row,3).text())
                        except ValueError:
                            pass
                        points[table.cellWidget(row,0).currentText()] += float(table.item(row,3).text())
                        table_points.setText(str(float(table_points.text()) + float(table.item(row,3).text())))
                except (ValueError, AttributeError):
                    continue
        self.ui.list_a_done_in_7.setText(str(points["רשימה א"]))
        self.ui.list_b_done_in_7.setText(str(points["רשימה ב"]))
        self.ui.project_done_in_7.setText(str(points["פרוייקט"]))
        self.ui.sport_done_in_7.setText(str(points["ספורט"]))
        self.ui.malag_done_in_7.setText(str(points["מל\"ג"]))
        self.ui.free_done_in_7.setText(str(points["חופשי"]))
        if self.ui.english_checkbox_7.isChecked():
            exemption = 3
        else:
            exemption = 0
        self.ui.must_done_in.setText(str(points["חובה"]+exemption))
        self.ui.points_left_to_choose_in_7.setText(str(float(self.ui.deg_points_in.text())-sum(points.values())-exemption))
        self.ui.points_in_7.setText(str(float(points_done)+exemption))
        self.ui.points_left_in_7.setText(str(float(self.ui.deg_points_in.text())-float(self.ui.points_in_7.text())))

    def updateTooltips(self):
        for tab in range(self.ui.courses_tab_widget.count()):
            table = self.ui.courses_tab_widget.widget(tab).children()[7]
            for row in range(table.rowCount()):
                try:
                    if table.item(row,1) and table.item(row,1).text().isEmpty():
                       table.item(row,1).setToolTip("")
                except (ValueError, AttributeError):
                    continue


    def update(self):
        try:
            #TODO: HANDLE ERRORS !
            self.updateAverage()
            self.updatePoints()
            self.updateTooltips()
        except ZeroDivisionError:
            return

    def addSemester(self):
        tab = self.createTab()
        table = tab.children()[7]
        table.cellChanged['int','int'].connect(self.update)
        tab.children()[5].clicked.connect(lambda state: self.addRow(
            table))
        tab.children()[6].clicked.connect(lambda state: self.removeRow(
            table))
        tab.children()[8].clicked.connect(self.openSearchDialog)
        value = []
        lambdas = []
        buttons = []
        item = QtWidgets.QTableWidgetItem()
        for i in range(0, table.rowCount()):
            button = createRemoveLineButton(str(i))
            value.append(i)
            lambdas.append(lambda state: self.clearRow(table))
            button.clicked.connect(lambdas[i])
            buttons.append(button)
            table.setCellWidget(i, table.columnCount()-1, buttons[i])
            table.cellWidget(i,0).currentIndexChanged['int'].connect(self.update)
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
                table.item(row,column).setToolTip("")
        self.update()

    def updateTabNames(self):
        for i in range(self.ui.courses_tab_widget.count()):
            tab_name = "סמסטר " + str(i+1)
            self.ui.courses_tab_widget.setTabText(i, tab_name)

    def removeSemester(self, i):
        if self.my_close("semester", "האם למחוק סמסטר ?"):
            self.ui.courses_tab_widget.removeTab(i)
            self.updateTabNames()
            self.update()
        

    def addRow(self, table):
        table.setRowCount(table.rowCount() + 1)
        table.setItem(table.rowCount()-1, 0, QtWidgets.QTableWidgetItem())
        table.setCellWidget(table.rowCount() - 1, 0, self.createComboBox())
        button = createRemoveLineButton(str(table.rowCount()-1))
        button.clicked.connect(lambda state: self.clearRow(table))
        table.cellWidget(table.rowCount()-1,0).currentIndexChanged['int'].connect(self.update)
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
        self.update()

    def createComboBox(self):
        combo_box = QtWidgets.QComboBox()
        combo_box.setFocusPolicy(QtCore.Qt.StrongFocus)
        combo_box.setLayoutDirection(QtCore.Qt.RightToLeft)
        combo_box.addItem("חובה")
        combo_box.addItem("רשימה א")
        combo_box.addItem("רשימה ב")
        combo_box.addItem("פרוייקט")
        combo_box.addItem("מל\"ג")
        combo_box.addItem("ספורט")
        combo_box.addItem("חופשי")
        return combo_box

    def my_close(self, not_show_param, msg):
        if not_show_param == "row" and not self.not_show_remove_course:
            return self.warningMsg(not_show_param,msg)
        elif not_show_param == "semester" and not self.not_show_remove_semester:
            return self.warningMsg(not_show_param,msg)

    def errorMsg(self, msg):
        msgbox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question,
                                    "שגיאה", msg)
        msgbox.addButton(QtWidgets.QMessageBox.Ok)
        msgbox.exec()

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
