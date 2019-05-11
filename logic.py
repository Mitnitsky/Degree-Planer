from maindesign import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from scrapper import *
from sys import exit
from tab import TabPage, createRemoveLineButton
from findDialog import Ui_course_search
from progress import Ui_Form
from itertools import product
from course import Course
from updatedbthread import mythread
from tr import tr
import threading
import pickle
import pandas as pd

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        initDB()
        self.update_allowed = True
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
        self.threadStop = [False]
        self.saveFileName = ''
        self.ui.english_checkbox_7.stateChanged['int'].connect(self.update)
        self.show()
        self.ui.actionUpdate_Courses_DB.triggered.connect(self.dbUpdate)
        self.ui.actionNew.triggered.connect(self.new)
        self.ui.actionSave.triggered.connect(self.saveData)
        self.ui.actionSaveAs.triggered.connect(self.saveAsData)
        self.ui.actionLoad.triggered.connect(self.loadData)
        self.ui.action_2.triggered.connect(self.showCredit)
        self.firstStart = True
        self.saved = True
        self.update()
        self.ui.statusbar.setStyleSheet("font: 57 8pt \"Noto Sans\";")
        self.ui.statusbar.showMessage("© 2019 Vladimir Parakhin")
        self.course_update = [0]
        try:
            f = open('settings.cfg', "r")
            if f:
                filename = f.readline()
                if '.dps' in filename:
                    if self.loadData(filename):
                        self.saveFileName = filename
        except FileNotFoundError:
            self.update_allowed = True
            pass
        self.firstStart = False

    def closeEvent(self, event):
        quit_msg = "יציאה"
        messageBox = QtWidgets.QMessageBox()
        messageBox.setWindowTitle(quit_msg)
        messageBox.setText("לשמור לפני יציאה ?")
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)
        if not self.saved:
            reply = messageBox.exec_()
            if reply == QtWidgets.QMessageBox.Yes:
                self.saveData()
            if reply == QtWidgets.QMessageBox.Cancel:
                event.ignore()
                return
        return super().closeEvent(event)

    def dbUpdate(self):
        self.progress_ui = Ui_Form()
        self.progressBar = QtWidgets.QWidget()
        self.progress_ui.setupUi(self.progressBar)
        self.progressBar.children()[1].children()[3].clicked.connect(self.stopSearch)
        self.progressBar.show()
        self.course_update[0] = 0
        self.threadStop[0] = False
        for tab in range(self.ui.courses_tab_widget.count()):
            self.ui.courses_tab_widget.widget(tab).children()[8].setEnabled(False) #search button
            self.ui.courses_tab_widget.widget(tab).children()[8].setToolTip("אמתן לסיום עדכון הנתונים ")
        self.progress_ui.progressBar.setValue(0)
        self.thread = threading.Thread(target=updateDb, args=[self.course_update, self.progress_ui, self.threadStop])
        self.thread.start()

    def stopSearch(self):
        self.threadStop[0] = True
        self.progressBar.close()
        for tab in range(self.ui.courses_tab_widget.count()):
            self.ui.courses_tab_widget.widget(tab).children()[8].setEnabled(True)
            self.ui.courses_tab_widget.widget(tab).children()[8].setToolTip("")
    
    def new(self, force=False):
        if not force:
            ans = self.warningMsg('',"למחוק את כל הנתונים?")
        if force or ans:
            for tab in range(self.ui.courses_tab_widget.count()-1,-1,-1):
                self.removeSemester(tab,force=True)
        if not force:
            self.addSemester()


    def loadData(self, filename=''):
        self.update_allowed = False
        cnt = 0
        if not self.firstStart:
            ans = self.warningMsg('',"שינויים שלא נשמרו ימחקו")
            if not ans:
                self.update_allowed = True
                return
        if filename == '' or not filename:
            filename = QtWidgets.QFileDialog.getOpenFileName(self, 'טעינה', '', "Save files (*.dps)")
            if filename[0] == '':
                self.errorMsg("הקובץ לא נמצא")
                self.update_allowed = True
                return False
            filename = filename[0]
        try:
            filename = open(filename, "rb")
        except FileNotFoundError:
            self.errorMsg("פתיחת הקובץ כשלה")
            self.update_allowed = True
            return False
        if not filename:
            self.errorMsg("פתיחת הקובץ כשלה")
            self.update_allowed = True
            return False
        self.new(True)
        content = pickle.loads(filename.read())
        index = 0
        for semester in content:
            self.addSemester()
            table = self.ui.courses_tab_widget.widget(index).children()[7]
            index_r = 0
            for row in semester:
                for column in range(0,len(row) - 1):
                    if column == 0:
                        item = QtWidgets.QTableWidgetItem()
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        table.setItem(index_r, column, item)
                        index = table.cellWidget(index_r,column).findText(row[column], QtCore.Qt.MatchFixedString)
                        if index >= 0:
                            table.cellWidget(index_r,column).setCurrentIndex(index)
                    elif column == 1:
                        if row[column] != ' ' and row[column] != ' \n':
                            table.item(index_r,column).setToolTip(row[column])
                        if row[column+1] != ' ' and row[column+1] != ' \n':
                            table.item(index_r,column).setText(row[column+1])
                    elif column == 2:
                        if row[column+1] != ' ' and row[column+1] != ' \n':
                            table.item(index_r,column).setText(row[column+1])
                    else:
                        if row[column+1] != ' ' and row[column+1] != ' \n':
                            try:
                                table.cellWidget(index_r,column).setValue(float(row[column+1]))
                            except ValueError:
                                table.cellWidget(index_r,column).setValue(0.0)
                index_r += 1
            index += 1
        self.update_allowed = True
        self.update()
        self.saved = True
        return True

    def saveAsData(self):
        self.saveFileName = ''
        self.saveData()
    
    def saveData(self):
        cnt = 0
        if self.saveFileName == '':
            filename = QtWidgets.QFileDialog.getSaveFileName(self, 'שמירה בשם', '', "Save files (*.dps)")
            if filename[0] == '':
                return
            self.saveFileName = filename[0]
        try:
            f = open(self.saveFileName, "wb+")
        except FileNotFoundError:
            self.errorMsg("פתיחת הקובץ כשלה")
            return
        if not f:
            self.errorMsg("פתיחת הקובץ כשלה")
            return
        byte_array = list()
        for tab in range(self.ui.courses_tab_widget.count()):
            table = self.ui.courses_tab_widget.widget(tab).children()[7]
            semester = list()
            for row in range(table.rowCount()):
                separator ="\n"
                rows = list()
                for column in range(table.columnCount()-1):
                    if column == 0:
                        if table.cellWidget(row,column):
                            rows.append(table.cellWidget(row,column).currentText())
                            separator = ", "
                    else:
                        if table.item(row,column):
                            if column == 1:
                                rows.append(table.item(row,column).toolTip())
                            rows.append(table.item(row,column).text())
                semester.append(rows)
            byte_array.append(semester)
        f.write(pickle.dumps(byte_array))
        cache = open('settings.cfg', 'w+')
        if not cache:
            return
        cache.write(self.saveFileName)
        self.saved = True
    
    def showCredit(self):
        message_det = """<address>
                        Degree Planner
                        Version: 1.0<br>
                        Contact details:<br> 
                        <a href='vov4ikpa@gmail.com'>\tEmail</a><br>
                        <a href='https://github.com/Vladimir-pa/Degree-Planer'>\tGithub</a><br>
                        © 2019 Vladimir Parakhin
                        </address>"""
        msgbox = QtWidgets.QMessageBox()
        msgbox.setText(message_det)
        msgbox.setWindowTitle("About")
        msgbox.setTextFormat(QtCore.Qt.RichText)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        msgbox.setSizePolicy(sizePolicy)
        msgbox.exec()


    def updateProgressBar(self, thread):
        while thread.isAlive():
            self.progress_ui.progressBar.setValue(self.course_update[0])

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

    def addCourseContent(self, widget, course_num, table):
        course = findCourseInDB(course_num)
        if self.courseInTable(table, str(course.number)):
            if not self.warningMsg(msg="הקורס "+str(course.number)+" קיים בטבלה, להוסיף שוב?"):
                return
        row = self.findEmptyRow(widget)
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
        tooltip =  ("מקוצועות קדם: "                   + course.reprDependencies()                + "\n" if course.reprDependencies()                != "" else "" ) \
                 + ("מקצועות צמודים: "                 + course.repOtherData(course.parallel)     + "\n" if course.repOtherData(course.parallel)     != "" else "" ) \
                 + ("מקצועות ללא זיכוי נוסף: "         + course.repOtherData(course.similarities) + "\n" if course.repOtherData(course.similarities) != "" else "" ) \
                 + ("מקצועות ללא זיכוי נוסף(מוכלים): " + course.repOtherData(course.inclusive)           if course.repOtherData(course.inclusive)    != "" else "" )
        course_num.setToolTip(tooltip)
        course_points.setTextAlignment(QtCore.Qt.AlignCenter)
        table.setItem(row,1,course_num)
        table.setItem(row,2,course_name)
        table.setItem(row,3,course_points)
        return

    def courseInTable(self, table, course_num):
        for row in range(0, table.rowCount()):
            if table.item(row, 1) and table.item(row,1).text() == course_num:
                return True
        return False

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
        
        table = self.ui.courses_tab_widget.currentWidget().children()[7]
        self.addCourseContent(widget, widget.children()[1].text(), table)

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
                semester_average.setText(str(round(semester_sum / semester_points, 2)))
            else:
                semester_average.setText(str(0.0))
            total_points += semester_points
            total_sum += semester_sum
        if total_points > 0:
            self.ui.average_in_7.setText(str(round(total_sum / total_points, 2)))
        else:
            self.ui.average_in_7.setText(str(0.0))
            

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
                    try:
                        table.item(row,3).setText(str(float(table.item(row,3).text())))
                    except (ValueError, AttributeError):
                        pass
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
        self.ui.list_a_done_in_7.setText(str(float(self.ui.list_a_of_in_7.text()) - points["רשימה א"]))
        self.ui.list_b_done_in_7.setText(str(float(self.ui.list_b_of_in_7.text()) - points["רשימה ב"]))
        self.ui.project_done_in_7.setText(str(float(self.ui.project_of_in_7.text()) - points["פרוייקט"]))
        self.ui.sport_done_in_7.setText(str(float(self.ui.sport_of_in_7.text()) - points["ספורט"]))
        self.ui.malag_done_in_7.setText(str(float(self.ui.malag_of_in_7.text()) - points["מל\"ג"]))
        self.ui.free_done_in_7.setText(str(float(self.ui.free_of_in_7.text()) - points["חופשי"]))
        if self.ui.english_checkbox_7.isChecked():
            exemption = 3
        else:
            exemption = 0
        self.ui.must_done_in.setText(str(float(points["חובה"]+exemption)))
        self.ui.points_left_to_choose_in_7.setText(str(float(self.ui.deg_points_in.text())-sum(points.values())-exemption))
        self.ui.points_in_7.setText(str(float(points_done)+exemption))
        self.ui.points_left_in_7.setText(str(float(self.ui.deg_points_in.text())-float(self.ui.points_in_7.text())))

    def updateTooltips(self):
        for tab in range(self.ui.courses_tab_widget.count()):
            table = self.ui.courses_tab_widget.widget(tab).children()[7]
            for row in range(table.rowCount()):
                try:
                    if table.item(row,1) and (table.item(row,1).text() == '' or table.item(row,1).text() == ' '):
                       table.item(row,1).setToolTip("")
                    if table.item(row,2) and not (table.item(row,2).text() == '' or table.item(row,2).text() == ' '):
                        table.item(row,2).setToolTip(table.item(row,2).text())
                except (ValueError, AttributeError):
                    continue


    def update(self):
        if self.update_allowed:
            try:
                self.updateAverage()
                self.updatePoints()
                self.updateTooltips()
                self.saved = False
            except (ValueError, AttributeError):
                pass

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
        self.update()
    
    def clearRow(self, table):
        row = int(self.sender().objectName())
        empty = self.checkIfRowIsEmpty(table,row)
        if empty:
            table.removeRow(row)
        for column in range(1, table.columnCount()-1):
            if table.item(row,column) != None:
                table.item(row,column).setText("")
                table.item(row,column).setToolTip("")
        self.update()

    def updateTabNames(self):
        for i in range(self.ui.courses_tab_widget.count()):
            tab_name = "סמסטר " + str(i+1)
            self.ui.courses_tab_widget.setTabText(i, tab_name)

    def removeSemester(self, i, force=False):
        if force or self.my_close("semester", "האם למחוק סמסטר ?"):
            self.ui.courses_tab_widget.removeTab(i)
            self.updateTabNames()
            self.update()
        

    def addRow(self, table):
        table.setRowCount(table.rowCount() + 1)
        table.setItem(table.rowCount()-1, 0, QtWidgets.QTableWidgetItem())
        table.setCellWidget(table.rowCount() - 1, 0, self.createComboBox())
        for column in range(1 , table.columnCount()-1):
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            table.setItem(table.rowCount()-1, column, item)
            if column >= 3:
                spin_box = QtWidgets.QDoubleSpinBox()
                spin_box.setRange(0,100)
                spin_box.setDecimals(1)
                if column == 3:
                    spin_box.setSingleStep(0.5)
                spin_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
                spin_box.setAlignment(QtCore.Qt.AlignCenter)
                table.setCellWidget(table.rowCount()-1,column,spin_box)
        button = createRemoveLineButton(str(table.rowCount()-1))
        button.clicked.connect(lambda state: self.clearRow(table))
        table.cellWidget(table.rowCount()-1,0).currentIndexChanged['int'].connect(self.update)
        table.setCellWidget(table.rowCount() - 1, table.columnCount()-1, button)

    def removeRow(self, table):
        rows = table.rowCount()
        if rows == 0:
            return
        if self.lastRowIsEmpty(table):
            table.setRowCount(rows - 1)
        else:
            ans = self.my_close("row", "למחוק שורה בעלת תוכן?")
            if ans:
                table.setRowCount(rows - 1)
        self.update()
    
    def lastRowIsEmpty(self, table):
        rows = table.rowCount()
        for column in range(0, table.columnCount()):
            if table.item(rows-1, column) and table.item(rows-1, column).text() != '' and table.item(rows-1, column).text() != ' ':
                return False
        return True

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
            ans = self.warningMsg(not_show_param, msg)
            return ans
        elif not_show_param == "semester" and not self.not_show_remove_semester:
            ans = self.warningMsg(not_show_param, msg)
            return ans
        return True

    def errorMsg(self, msg):
        msgbox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question,
                                    "שגיאה", msg)
        msgbox.addButton(QtWidgets.QMessageBox.Ok)
        msgbox.exec()

    def warningMsg(self, not_show_param='', msg='ERROR'):
        cb = QtWidgets.QCheckBox("לא להראות שוב.")
        msgbox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question,
                                    "מחיקה", msg)
        msgbox.addButton(QtWidgets.QMessageBox.Yes)
        msgbox.addButton(QtWidgets.QMessageBox.No)
        msgbox.setDefaultButton(QtWidgets.QMessageBox.No)
        if not_show_param == "semester" or not_show_param == "row":
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
