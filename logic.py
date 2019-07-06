import json
import threading
from time import sleep

from PyQt5 import QtCore, QtWidgets

import Ui_tab_heb
import Ui_main_heb
from Ui_tab_eng import TabPage, createRemoveLineButton, createComboBox
from Ui_findDialog import Ui_course_search
from Ui_main_eng import Ui_MainWindow
from Ui_progress import ProgressWindowForm
from scrapper import *


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.progressBar = QtWidgets.QWidget()
        self.progress_ui = ProgressWindowForm()
        initDB()
        self.searchWindow = False
        self.update_allowed = True
        self.english_ui = self.loadLanguage()
        if self.english_ui:
            self.ui = Ui_MainWindow()
        else:
            self.ui = Ui_main_heb.Ui_MainWindow()
        self.ui.setupUi(self)
        self.not_show_remove_course = False
        self.not_show_remove_semester = False
        self.threadStop = [False]
        self.saveFileName = ''
        self.firstStart = True
        self.saved = True
        self.db_pairs = loadCourseNameNumberPairs()
        self.course_update = [0]
        self.ui.statusbar.setStyleSheet("font: 57 8pt \"Noto Sans\";")
        self.ui.statusbar.showMessage("© 2019 Vladimir Parakhin")
        self.update()
        self.show()
        self.setEventHandlers()
        try:
            file = open('settings.json', "r")
            if file:
                data = json.load(file)
                if '.dps' in data['save_file']:
                    if self.loadData(data['save_file']):
                        self.saveFileName = data['save_file']
                        file.close()
                    else:
                        data['save_file'] = ""
                        file.close()
                        file = open('settings.json', "w")
                        json.dump(data, file, indent=4)
                        file.close()

                if self.ui.courses_tab_widget.count() == 0:
                    self.addSemester()
                    self.saved = True
        except FileNotFoundError:
            if self.ui.courses_tab_widget.count() == 0:
                self.addSemester()
            self.update_allowed = True
            self.saved = True
            pass
        self.firstStart = False

    # Closing main windows override, check if there is unsaved data and prompts the user if so for save
    def closeEvent(self, event):
        if self.english_ui:
            quit_msg = "Exit"
        else:
            quit_msg = "יציאה"
        message_box = QtWidgets.QMessageBox()
        message_box.setWindowTitle(quit_msg)
        if self.english_ui:
            message_box.setText("Do you want to save your changes?")
        else:
            message_box.setText("לשמור לפני יציאה ?")
        message_box.setStandardButtons(
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)
        if not self.saved:
            reply = message_box.exec_()
            if reply == QtWidgets.QMessageBox.Yes:
                self.saveData()
            if reply == QtWidgets.QMessageBox.Cancel:
                event.ignore()
                return
        if self.searchWindow and self.searchWindow.isVisible():
            self.searchWindow.close()
        self.saveWindowDimensions()
        return super().closeEvent(event)

    def saveWindowDimensions(self):
        filename = open("settings.json", "r")
        if filename:
            data = json.load(filename)
            filename.close()
            data['dimensions'][0]['width'] = self.width()
            data['dimensions'][0]['height'] = self.height()
            with open("settings.json", "w") as write_file:
                json.dump(data, write_file, indent=4)

    @staticmethod
    def loadLanguage():
        with open("settings.json", "r") as read_file:
            data = json.load(read_file)
            if data['language'] == 'heb':
                return False
            elif data['language'] == 'eng':
                return True
        return False

    def languageChange(self, language):
        if self.english_ui and language == 'eng':
            return
        elif not self.english_ui and language == 'heb':
            return
        elif self.english_ui and language == 'heb':
            data = self.extractData()
            self.english_ui = False
            self.ui = Ui_main_heb.Ui_MainWindow()
            self.ui.setupUi(self)
            with open("settings.json", "r+") as read_file:
                data_json = json.load(read_file)
                data_json['language'] = 'heb'
                read_file.seek(0)
                json.dump(data_json, read_file, indent=4)
                read_file.truncate()
        elif not self.english_ui and language == 'eng':
            data = self.extractData()
            self.english_ui = True
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            with open("settings.json", "r+") as read_file:
                data_json = json.load(read_file)
                data_json['language'] = 'eng'
                read_file.seek(0)
                json.dump(data_json, read_file, indent=4)
                read_file.truncate()
        if self.searchWindow and self.searchWindow.isVisible():
            self.searchWindow.close()
            self.openSearchDialog()
        self.setEventHandlers()
        self.loadData('', data)

    def setEventHandlers(self):
        self.ui.english_checkbox_7.stateChanged['int'].connect(self.update)
        self.ui.actionUpdate_Courses_DB.triggered.connect(self.dbUpdate)
        self.ui.actionNew.triggered.connect(self.clearData)
        self.ui.actionSave.triggered.connect(self.saveData)
        self.ui.actionSaveAs.triggered.connect(self.saveAsData)
        self.ui.actionLoad.triggered.connect(self.loadData)
        self.ui.actionLoadTemplate.triggered.connect(self.loadTemplate)
        self.ui.actionInfo.triggered.connect(self.showCredit)
        self.ui.add_semester_but.clicked.connect(self.addSemester)
        self.ui.actionHeb.triggered.connect(lambda: self.languageChange('heb'))
        self.ui.actionEnglish.triggered.connect(lambda: self.languageChange('eng'))
        self.ui.courses_tab_widget.tabCloseRequested.connect(
            self.removeSemester)
        self.ui.must_of_in.valueChanged.connect(self.update)
        self.ui.list_a_of_in_7.valueChanged.connect(self.update)
        self.ui.list_b_of_in_7.valueChanged.connect(self.update)
        self.ui.project_of_in_7.valueChanged.connect(self.update)
        self.ui.sport_of_in_7.valueChanged.connect(self.update)
        self.ui.malag_of_in.valueChanged.connect(self.update)
        self.ui.free_of_in_7.valueChanged.connect(self.update)
        self.ui.deg_points_in.valueChanged.connect(self.update)

    # Function which launches data base update, pops progress bar window
    def dbUpdate(self):
        self.progress_ui.setupUi(self.progressBar, self.english_ui)
        self.progressBar.children()[1].children()[3].clicked.connect(self.setStopThread)
        self.progressBar.show()
        self.course_update[0] = 0
        self.threadStop[0] = False
        for tab in range(self.ui.courses_tab_widget.count()):
            self.ui.courses_tab_widget.widget(tab).children()[8].setEnabled(False)  # search button
            if self.english_ui:
                self.ui.courses_tab_widget.widget(tab).children()[8].setToolTip(
                    "Data base update in progress, please wait.")
            else:
                self.ui.courses_tab_widget.widget(tab).children()[8].setToolTip("אמתן לסיום עדכון הנתונים ")
        self.progress_ui.progressBar.setValue(0)
        self.thread_update = threading.Thread(target=updateDb,
                                              args=[self, self.course_update, self.progress_ui, self.threadStop])
        self.thread_stop_checker = threading.Thread(target=self.stopSearch, args=[])
        self.thread_update.start()
        self.thread_stop_checker.start()

    # Function to set a signal for update db thread to stop
    def setStopThread(self):
        self.threadStop[0] = True

    # Function which check whether update db thread finished and restores find course button functionality
    def stopSearch(self):
        while not self.threadStop[0] and self.thread_update.isAlive():
            sleep(0.05)
        self.progressBar.close()
        self.progressBar.destroy()
        for tab in range(self.ui.courses_tab_widget.count()):
            self.ui.courses_tab_widget.widget(tab).children()[8].setEnabled(True)
            self.ui.courses_tab_widget.widget(tab).children()[8].setToolTip("")

    # Clearing the UI input completely 
    def clearData(self, forced=False):
        if not forced:
            if self.english_ui:
                answer = self.warningMsg(not_show_param='', msg="Remove all the data?")
            else:
                answer = self.warningMsg(not_show_param='', msg="למחוק את כל הנתונים?")
        if forced or answer:
            for tab in range(self.ui.courses_tab_widget.count() - 1, -1, -1):
                self.removeSemester(tab, force=True)
            self.ui.project_of_in_7.setValue(0.0)
            self.ui.list_a_of_in_7.setValue(0.0)
            self.ui.list_b_of_in_7.setValue(0.0)
            self.ui.sport_of_in_7.setValue(0.0)
            self.ui.malag_of_in.setValue(0.0)
            self.ui.deg_points_in.setValue(0.0)
            self.ui.free_of_in_7.setValue(0.0)
            self.ui.must_of_in.setValue(0.0)
            self.ui.english_checkbox_7.setChecked(False)
            self.update()
        if self.ui.courses_tab_widget.count() == 0:
            self.addSemester()

    # Load saved data from file using pickle module
    def loadData(self, filename='', data=None):
        if data is None:
            data = []
        if len(data) == 0:
            self.update_allowed = False
            if not self.firstStart and not self.saved:
                if self.english_ui:
                    answer = self.warningMsg(not_show_param='', msg="Do you want save all the changes?")
                else:
                    answer = self.warningMsg(not_show_param='', msg="שינויים שלא נשמרו ימחקו, לשמור?")
                if answer:
                    self.saveData()
            if filename == '' or not filename:
                filename = QtWidgets.QFileDialog.getOpenFileName(self, 'טעינה', '', "Save files (*.dps)")
                if filename[0] == '':
                    self.update_allowed = True
                    return False
                filename = filename[0]
            try:
                filename = open(filename, "rb")
            except FileNotFoundError:
                if self.english_ui:
                    self.errorMsg("Couldn't open the file")
                else:
                    self.errorMsg("פתיחת קובץ כשלה")
                self.update_allowed = True
                return False
        self.clearData(True)
        # The data is stored in the following way 
        # content[0] first list contains values from the points value which the user stored
        index = 0
        try:
            if len(data) == 0:
                content = pickle.loads(filename.read())
            else:
                content = data
            self.ui.deg_points_in.setValue(content[0][0])
            self.ui.must_of_in.setValue(content[0][1])
            self.ui.list_a_of_in_7.setValue(content[0][2])
            self.ui.list_b_of_in_7.setValue(content[0][3])
            self.ui.project_of_in_7.setValue(content[0][4])
            self.ui.malag_of_in.setValue(content[0][5])
            self.ui.sport_of_in_7.setValue(content[0][6])
            self.ui.free_of_in_7.setValue(content[0][7])
            self.ui.english_checkbox_7.setChecked(content[0][8])
            content = content[1:]
            # The other data saved in the following order
            # [i]-semester
            # [i][j]-row
            # [i][j][k]-column
            first_sem = True
            for semester in content:
                if not first_sem:
                    self.addSemester()
                first_sem = False
                if self.english_ui:
                    table = self.ui.courses_tab_widget.widget(index).children()[1]
                else:
                    table = self.ui.courses_tab_widget.widget(index).children()[7]
                row_index = 0
                while len(semester) > table.rowCount():
                    self.addRow(table)
                while len(semester) < table.rowCount():
                    self.removeRow(table)
                for row in semester:
                    for column in range(0, len(row) - 1):
                        if column == 0:
                            item = QtWidgets.QTableWidgetItem()
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            table.setItem(row_index, column, item)
                            if self.english_ui:
                                table.setCellWidget(row_index, column, createComboBox())
                            else:
                                table.setCellWidget(row_index, column, Ui_tab_heb.createComboBox())
                            table.cellWidget(row_index, column).currentIndexChanged.connect(self.update)
                            table.cellWidget(row_index, column).setCurrentIndex(int(row[column]))
                        # Course number
                        elif column == 1:
                            if row[column] != ' ' and row[column] != ' \n':
                                # Course dependencies (parallel, similar, inclusive)
                                table.item(row_index, column).setToolTip(row[column])
                            if row[column + 1] != ' ' and row[column + 1] != ' \n':
                                table.item(row_index, column).setText(row[column + 1])
                        # Course name
                        elif column == 2:
                            if row[column + 1] != ' ' and row[column + 1] != ' \n':
                                table.item(row_index, column).setText(row[column + 1])
                        else:
                            if row[column + 1] != ' ' and row[column + 1] != ' \n':
                                try:
                                    # Course-points spin-box
                                    if column == 3:
                                        spin_box = QtWidgets.QDoubleSpinBox()
                                        spin_box.setDecimals(1)
                                        spin_box.setSingleStep(0.5)
                                    # Course-grade spin-box
                                    else:
                                        spin_box = QtWidgets.QSpinBox()
                                        spin_box.setSingleStep(1)
                                    spin_box.setRange(0, 100)
                                    spin_box.setAlignment(QtCore.Qt.AlignCenter)
                                    spin_box.valueChanged.connect(self.update)
                                    spin_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
                                    table.setCellWidget(row_index, column, spin_box)
                                    table.cellWidget(row_index, column).valueChanged.connect(self.update)
                                    table.cellWidget(row_index, column).setValue(float(row[column + 1]))
                                except ValueError:
                                    table.cellWidget(row_index, column).setValue(0.0)
                    row_index += 1
                index += 1
            self.update_allowed = True
        except EOFError:
            if self.english_ui:
                self.errorMsg("File corrupted")
            else:
                self.errorMsg("קריאת הקובץ נכשלה")
        if self.ui.courses_tab_widget.count() == 0:
            self.addSemester()
        self.update()
        if len(data) == 0:
            self.saved = True
        return True

    # Load template of courses
    def loadTemplate(self):
        self.update_allowed = False
        if not self.firstStart and not self.saved:
            if self.english_ui:
                answer = self.warningMsg(not_show_param='', msg="Do you want save all the changes?")
            else:
                answer = self.warningMsg(not_show_param='', msg="שינויים שלא נשמרו ימחקו, לשמור?")
            if answer:
                self.saveData()
        if self.english_ui:
            filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Load', '', "Json-Templates files (*.json)")
        else:
            filename = QtWidgets.QFileDialog.getOpenFileName(self, 'טעינה', '', "Json-Templates files (*.json)")
        if filename[0] == '':
            self.update_allowed = True
            if self.english_ui:
                return
            else:
                return
        filename = filename[0]
        courses = []
        try:
            with open(filename, "r+") as read_file:
                data_json = json.load(read_file)
                total_points = data_json["Points"]
                mandatory = data_json["Mandatory"]
                a_list = data_json["A' List"]
                b_list = data_json["B' List"]
                humanistic = data_json["Humanistic"]
                free_points = data_json["Free choice"]
                sport = data_json["Sport"]
                for semester in data_json["Courses"][0]:
                    courses.append(data_json["Courses"][0][semester])
        except (KeyError, FileNotFoundError):
            self.update_allowed = True
            if self.english_ui:
                self.errorMsg("File corrupted")
            else:
                self.errorMsg("קריאת הקובץ נכשלה")
            return
        self.clearData(forced=True)
        if self.english_ui:
            table = self.ui.courses_tab_widget.currentWidget().children()[1]
        else:
            table = self.ui.courses_tab_widget.currentWidget().children()[7]
        first_sem = True
        for semester in courses:
            if not first_sem:
                self.addSemester()
            for course in semester:
                if course == "MATH":
                    math_course = Course()
                    math_course.name = "מתמטי נוסף"
                    math_course.number = "104"
                    self.addCourseContent(0, math_course)
                elif course == "SCI":
                    sci_course = Course()
                    sci_course.name = "קורס מדעי"
                    self.addCourseContent(0, sci_course)
                elif course == "SPORT":
                    sport_course = Course()
                    sport_course.name = "ספורט"
                    sport_course.points = 1
                    self.addCourseContent(0, sport_course)
                else:
                    self.addCourseContent(course_num=course)
            first_sem = False
        self.ui.deg_points_in.setValue(total_points)
        self.ui.must_of_in.setValue(mandatory)
        self.ui.list_a_of_in_7.setValue(a_list)
        self.ui.list_b_of_in_7.setValue(b_list)
        self.ui.project_of_in_7.setValue(0)
        self.ui.malag_of_in.setValue(humanistic)
        self.ui.sport_of_in_7.setValue(sport)
        self.ui.free_of_in_7.setValue(free_points)
        self.ui.english_checkbox_7.setChecked(False)
        self.update_allowed = True
        self.update()
        self.saved = True

    # Save as function change the pointer to current saved file
    def saveAsData(self):
        self.saveFileName = ''
        self.saveData()

    # Save function, saves the data from the app using pickle
    def saveData(self):
        if self.saveFileName == '':
            if self.english_ui:
                filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save as', '', "Save files (*.dps)")
            else:
                filename = QtWidgets.QFileDialog.getSaveFileName(self, 'שמירה בשם', '', "Save files (*.dps)")
            if filename[0] == '':
                return
            self.saveFileName = filename[0]
        try:
            file = open(self.saveFileName, "wb+")
        except FileNotFoundError:
            if self.english_ui:
                self.errorMsg("Couldn't open file.")
            else:
                self.errorMsg("פתיחת קובץ כשלה")
            return
        if not file:
            if self.english_ui:
                self.errorMsg("Couldn't open file.")
            else:
                self.errorMsg("פתיחת קובץ כשלה")
            return
        byte_array = self.extractData()
        file.write(pickle.dumps(byte_array))
        # Caching the filename in settings.json in order to use save function seamlessly afterwards
        with open('settings.json', 'r+') as write_file:
            data_json = json.load(write_file)
            data_json['save_file'] = self.saveFileName
            write_file.seek(0)
            json.dump(data_json, write_file, indent=4)
            write_file.truncate()
        self.saved = True

    # The function extracts all the user-input data and returns it in 3-dimensional array.
    def extractData(self):
        byte_array = list()
        inputs = list()
        inputs.append(self.ui.deg_points_in.value())
        inputs.append(self.ui.must_of_in.value())
        inputs.append(self.ui.list_a_of_in_7.value())
        inputs.append(self.ui.list_b_of_in_7.value())
        inputs.append(self.ui.project_of_in_7.value())
        inputs.append(self.ui.malag_of_in.value())
        inputs.append(self.ui.sport_of_in_7.value())
        inputs.append(self.ui.free_of_in_7.value())
        inputs.append(self.ui.english_checkbox_7.isChecked())
        byte_array.append(inputs)
        for tab in range(self.ui.courses_tab_widget.count()):
            if self.english_ui:
                table = self.ui.courses_tab_widget.widget(tab).children()[1]
            else:
                table = self.ui.courses_tab_widget.widget(tab).children()[7]
            semester = list()
            for row in range(table.rowCount()):
                rows = list()
                for column in range(table.columnCount() - 1):
                    if column == 0:
                        if table.cellWidget(row, column):
                            rows.append(table.cellWidget(row, column).currentIndex())
                    elif column <= 2:
                        if table.item(row, column):
                            if column == 1:
                                rows.append(table.item(row, column).toolTip())
                            rows.append(table.item(row, column).text())
                    else:
                        if table.cellWidget(row, column):
                            rows.append(table.cellWidget(row, column).value())
                semester.append(rows)
            byte_array.append(semester)
        return byte_array

    # Function which shows credit window with contact information
    def showCredit(self):
        message_det = """<address>
                        Degree Planner
                        Version: 1.0<br>
                        Contact details:<br> 
                        <a href='vov4ikpa@gmail.com'>\tEmail</a><br>
                        <a href='https://github.com/Vladimir-pa/Degree-Planner'>\tGithub</a><br>
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

    # Function which opens the course search dialog in order to search within 
    #   the data base for courses and add them into the table
    def openSearchDialog(self):
        self.searchWindow = QtWidgets.QWidget()
        self.search_ui = Ui_course_search()
        self.search_ui.setupUi(self.searchWindow, self.english_ui)
        # db_pairs contains all courses from the technion for quick lookup
        # in the following format "<course-name> - <course-number>"
        for course in self.db_pairs:
            self.searchWindow.children()[3].addItem(course)
        self.searchWindow.children()[3].currentIndexChanged.connect(self.findCourse)
        self.searchWindow.children()[7].clicked.connect(lambda state: self.closeIt(self.searchWindow))  # close
        self.searchWindow.children()[8].clicked.connect(lambda state: self.addCourse(self.searchWindow))  # add
        if self.english_ui:
            self.searchWindow.setWindowTitle("Course search")
        else:
            self.searchWindow.setWindowTitle("חיפוש קורסים")
        self.searchWindow.children()[3].setCurrentText("")
        self.searchWindow.show()

    # Function which find the course in the data-base list in course search ui
    # the function is being called on index change of the spinbox with the course in the ui
    # the function updates the additional information about the course
    def findCourse(self):
        if self.searchWindow.children()[3].currentText() != '':
            course = findCourseInDB(self.searchWindow.children()[3].currentText().split(" - ")[0])
            if self.english_ui:
                course.english = True
            self.searchWindow.children()[6].setPlainText(repr(course))
        else:
            self.searchWindow.children()[6].setPlainText("")

    # Given a table and a row checks whether the row is empty
    def checkIfRowIsEmpty(self, table, row):
        for column in range(1, table.columnCount() - 1):
            if table.item(row, column):
                if column >= 3:
                    if table.cellWidget(row, column).value() > 0:
                        return False
                if table.item(row, column).text() != "":
                    return False
        return True

    # Function which adds the course content into the table on current open semester in an empty row
    def addCourseContent(self, course_num, course=None):
        if course is None:
            course = findCourseInDB(course_num)
        if type(course) != Course:
            print(course_num+"\n")
            return
        for i in range(0, self.ui.courses_tab_widget.count()):
            if self.english_ui:
                semester_table = self.ui.courses_tab_widget.widget(i).children()[1]
            else:
                semester_table = self.ui.courses_tab_widget.widget(i).children()[7]
            if self.courseInTable(semester_table, str(course.number)):
                if self.english_ui:
                    if not self.warningMsg(title="Warning", msg="Course " + str(
                            course.number) + " exist in the table, add again?" + "\n(In Semester" + str(i + 1) + ")"):
                        return
                else:
                    if not self.warningMsg(title="התראה",
                                           msg="הקורס " + str(
                                               course.number) + " קיים בטבלה, להוסיף שוב?" + "\n(בסמסטר " + str(
                                               i + 1) + ")"):
                        return
        row = self.findEmptyRow(semester_table)
        course_num = QtWidgets.QTableWidgetItem()
        course_num.setText(str(course.number))
        course_name = QtWidgets.QTableWidgetItem()
        course_name.setText(course.name)
        course_points = QtWidgets.QTableWidgetItem()
        semester_table.cellWidget(row, 3).setValue(course.points)
        course_name.setTextAlignment(QtCore.Qt.AlignCenter)
        course_num.setTextAlignment(QtCore.Qt.AlignCenter)
        if self.english_ui:
            tooltip = ("Pre-requisites: " + course.reprDependencies() + "\n" if course.reprDependencies() != "" else "") \
                      + ("Side courses: " + course.repOtherData(course.parallel) + "\n" if course.repOtherData(
                course.parallel) != "" else "") \
                      + ("Similar courses: " + course.repOtherData(
                course.similarities) + "\n" if course.repOtherData(course.similarities) != "" else "") \
                      + ("Similar courses(included): " + course.repOtherData(course.inclusive) if course.repOtherData(
                course.inclusive) != "" else "")
        else:
            tooltip = ("מקוצועות קדם: " + course.reprDependencies() + "\n" if course.reprDependencies() != "" else "") \
                      + ("מקצועות צמודים: " + course.repOtherData(course.parallel) + "\n" if course.repOtherData(
                course.parallel) != "" else "") \
                      + ("מקצועות ללא זיכוי נוסף: " + course.repOtherData(
                course.similarities) + "\n" if course.repOtherData(course.similarities) != "" else "") \
                      + ("מקצועות ללא זיכוי נוסף(מוכלים): " + course.repOtherData(
                course.inclusive) if course.repOtherData(
                course.inclusive) != "" else "")
        course_num.setToolTip(tooltip)
        course_points.setTextAlignment(QtCore.Qt.AlignCenter)
        semester_table.setItem(row, 1, course_num)
        semester_table.setItem(row, 2, course_name)
        return

    # Function which check whether or not the course with the given course number is present in the table in current
    # semester
    def courseInTable(self, table, course_num, semesters_number=-1):
        if semesters_number == -1:
            semesters_number = table.rowCount()
        for row in range(0, semesters_number):
            if table.item(row, 1) and table.item(row, 1).text() == course_num and course_num != '':
                return True
        return False

    #   Function which find an empty row in the current semester table
    def findEmptyRow(self, table):
        for row in range(table.rowCount()):
            if self.checkIfRowIsEmpty(table, row):
                return row
        self.addRow(table)
        return table.rowCount() - 1

    # Function which adds the course from the search ui on add-course button click event
    def addCourse(self, course_info):
        combo_text = course_info.children()[3].currentText()
        if combo_text == '':
            if self.english_ui:
                self.errorMsg("Please choose course and try again.")
            else:
                self.errorMsg("לא נבחר קורס, אנא נסה שנית")
            return
        course_number = combo_text.split(" - ")[0]
        if self.english_ui:
            table = self.ui.courses_tab_widget.currentWidget().children()[1]
        else:
            table = self.ui.courses_tab_widget.currentWidget().children()[7]
        if self.searchWindow.children()[4].isChecked():
            dependencies = self.checkDependencies(table, course_number, self.ui.courses_tab_widget.currentIndex())
            if len(dependencies) > 0:
                dependencies_msg = self.createDependenciesMessage(dependencies)
                self.prerequisitesWarningMessage(dependencies_msg)
        self.addCourseContent(course_number)

    def checkDependencies(self, table, course_number, current_semester):
        course = findCourseInDB(course_number)
        if "השלמות" in course.name:
            return True
        if len(course.dependencies) == 0 and len(course.parallel) == 0:
            return True
        dependencies = []
        parallels = []
        for option in course.dependencies:
            inner_dependencies = []
            for course_number in option:
                if not self.courseInTable(table, course_number, current_semester - 1):
                    inner_dependencies.append(course_number)
            if len(dependencies) == 0 or len(inner_dependencies) < len(dependencies):
                dependencies = inner_dependencies
        for course_number in course.parallel:
            inner_parallels = []
            if not self.courseInTable(table, course_number, current_semester - 1):
                parallels.append(course_number)
        return [dependencies, parallels]

    def createDependenciesMessage(self, dependencies):
        msg = ""
        if len(dependencies[0]) > 0:
            if self.english_ui:
                msg += "Following pre-requisites are missing:\n"
            else:
                msg += "חסרים הקדמים הבאים בסמסטרים קודמים:\n"
            separator = ""
            for course_number in dependencies[0]:
                course = findCourseInDB(course_number)
                msg += separator + course.number + " - " + course.name
                separator = "\n"
            msg += "\n\n"
        if len(dependencies[1]) > 0:
            if self.english_ui:
                msg += "Following parallel courses are missing:\n"
            else:
                msg += "חסרים הצמודים הבאים בסמסטר נוכחי או בסמסטרים קודמים:\n"
            separator = ""
            for course_number in dependencies[1]:
                course = findCourseInDB(course_number)
                msg += separator + course.number + " - " + course.name
                separator = "\n"
        msg += "\n\n"
        return msg

    # Function which closes the widget
    def closeIt(self, widget):
        widget.close()

    # Function which creates a new tab for a new semester
    def createTab(self):
        self.Form = QtWidgets.QWidget()
        if self.english_ui:
            ui = TabPage()
        else:
            ui = Ui_tab_heb.TabPage()
        ui.setupUi(self.Form)
        return self.Form

    # Function which is a part of update() function
    # the function calculates and updates the averages of each semester and the total average
    def updateAverage(self):
        total_sum = 0
        total_points = 0
        for tab in range(self.ui.courses_tab_widget.count()):
            semester_sum = 0
            semester_points = 0
            if self.english_ui:
                table = self.ui.courses_tab_widget.widget(tab).children()[1]
            else:
                table = self.ui.courses_tab_widget.widget(tab).children()[7]
            if self.english_ui:
                semester_average = self.ui.courses_tab_widget.widget(tab).children()[4]
            else:
                semester_average = self.ui.courses_tab_widget.widget(tab).children()[2]
            for row in range(table.rowCount()):
                try:
                    if table.cellWidget(row, 3) and float(table.cellWidget(row, 3).value()) > 0:
                        if table.cellWidget(row, 4) and float(table.cellWidget(row, 4).value()) > 0:
                            semester_points += float(table.cellWidget(row, 3).value())
                            semester_sum += float(table.cellWidget(row, 3).value()) * float(
                                table.cellWidget(row, 4).value())
                except (ValueError, AttributeError):
                    continue
            if semester_points > 0:
                semester_average.setText(str(round(semester_sum / semester_points, 2)))
            else:
                semester_average.setText(str(0.0))
            total_points += semester_points
            total_sum += semester_sum
        if total_points > 0:
            self.ui.average_in_7.setText(str(round(total_sum / total_points, 2)))
        else:
            self.ui.average_in_7.setText(str(0.0))

    # Function which is a part of update() function
    # the function calculates and updates the points of each semester and the total points information
    def updatePoints(self):
        if self.english_ui:
            points = {"Mandatory": 0,
                      "A' list": 0,
                      "B' list": 0,
                      "Project": 0,
                      "Sport": 0,
                      "Humanistic": 0,
                      "Free choice": 0,
                      }
        else:
            points = {"חובה": 0,
                      "רשימה א": 0,
                      "רשימה ב": 0,
                      "פרוייקט": 0,
                      "ספורט": 0,
                      "מל\"ג": 0,
                      "חופשי": 0}
        points_done = 0
        for tab in range(self.ui.courses_tab_widget.count()):
            if self.english_ui:
                table = self.ui.courses_tab_widget.widget(tab).children()[1]
                table_points = self.ui.courses_tab_widget.widget(tab).children()[6]  # Points
            else:
                table = self.ui.courses_tab_widget.widget(tab).children()[7]
                table_points = self.ui.courses_tab_widget.widget(tab).children()[4]  # Points
            table_points.setText("0")
            for row in range(table.rowCount()):
                try:
                    try:
                        table.cellWidget(row, 3).setText(str(float(table.cellWidget(row, 3).value())))
                    except (ValueError, AttributeError):
                        pass
                    if table.cellWidget(row, 3) and float(table.cellWidget(row, 3).value()) > 0:
                        try:
                            if table.cellWidget(row, 4) and float(table.cellWidget(row, 4).value()) > 0:
                                points_done += float(table.cellWidget(row, 3).value())
                        except ValueError:
                            pass
                        points[table.cellWidget(row, 0).currentText()] += float(table.cellWidget(row, 3).value())
                        table_points.setText(
                            str(round(float(table_points.text()) + float(table.cellWidget(row, 3).value()), 1)))
                except (ValueError, AttributeError, KeyError):
                    continue
        if self.english_ui:
            self.ui.list_a_done_in_7.setText(str(self.ui.list_a_of_in_7.value() - points["A' list"]))
            self.ui.list_b_done_in_7.setText(str(self.ui.list_b_of_in_7.value() - points["B' list"]))
            self.ui.project_done_in_7.setText(str(self.ui.project_of_in_7.value() - points["Project"]))
            self.ui.sport_done_in_7.setText(str(self.ui.sport_of_in_7.value() - points["Sport"]))
            self.ui.malag_done_in.setText(str(self.ui.malag_of_in.value() - points["Humanistic"]))
            self.ui.free_done_in_7.setText(str(self.ui.free_of_in_7.value() - points["Free choice"]))
        else:
            self.ui.list_a_done_in_7.setText(str(self.ui.list_a_of_in_7.value() - points["רשימה א"]))
            self.ui.list_b_done_in_7.setText(str(self.ui.list_b_of_in_7.value() - points["רשימה ב"]))
            self.ui.project_done_in_7.setText(str(self.ui.project_of_in_7.value() - points["פרוייקט"]))
            self.ui.sport_done_in_7.setText(str(self.ui.sport_of_in_7.value() - points["ספורט"]))
            self.ui.malag_done_in.setText(str(self.ui.malag_of_in.value() - points["מל\"ג"]))
            self.ui.free_done_in_7.setText(str(self.ui.free_of_in_7.value() - points["חופשי"]))
        if self.ui.english_checkbox_7.isChecked():
            exemption = 3
        else:
            exemption = 0
        if self.english_ui:
            self.ui.must_done_in.setText(str(float(self.ui.must_of_in.value() - points["Mandatory"] - exemption)))
        else:
            self.ui.must_done_in.setText(str(float(self.ui.must_of_in.value() - points["חובה"] - exemption)))
        self.ui.points_left_to_choose_in_7.setText(
            str(self.ui.deg_points_in.value() - sum(points.values()) - exemption))
        self.ui.points_in_7.setText(str(float(points_done) + exemption))
        self.ui.points_left_in_7.setText(str(self.ui.deg_points_in.value() - float(self.ui.points_in_7.text())))

    # Function which is a part of update() function
    # the function calculates and updates the tooltips for every course in the semester
    def updateTooltips(self):
        for tab in range(self.ui.courses_tab_widget.count()):
            if self.english_ui:
                table = self.ui.courses_tab_widget.widget(tab).children()[1]
            else:
                table = self.ui.courses_tab_widget.widget(tab).children()[7]
            for row in range(table.rowCount()):
                try:
                    if table.item(row, 1) and (table.item(row, 1).text() == '' or table.item(row, 1).text() == ' '):
                        table.item(row, 1).setToolTip("")
                    if table.item(row, 2) and not (table.item(row, 2).text() == '' or table.item(row, 2).text() == ' '):
                        table.item(row, 2).setToolTip(table.item(row, 2).text())
                except (ValueError, AttributeError):
                    continue

    # Update function which keeps all the data of the program updated
    def update(self):
        if self.update_allowed:
            try:
                self.updateAverage()
                self.updatePoints()
                self.updateTooltips()
                self.saved = False
            except (ValueError, AttributeError):
                pass

    # Add new empty semester to the program
    def addSemester(self):
        tab = self.createTab()
        if self.english_ui:
            table = tab.children()[1]
            tab.children()[2].clicked.connect(lambda state: self.addRow(
                table))
            tab.children()[3].clicked.connect(lambda state: self.removeRow(
                table))
        else:
            table = tab.children()[7]
            tab.children()[5].clicked.connect(lambda state: self.addRow(
                table))
            tab.children()[6].clicked.connect(lambda state: self.removeRow(
                table))
        table.cellChanged['int', 'int'].connect(self.update)
        tab.children()[8].clicked.connect(self.openSearchDialog)
        value = []
        lambdas = []
        buttons = []
        for row in range(0, table.rowCount()):
            table.cellWidget(row, 3).valueChanged.connect(self.update)  # Check whether course points were update
            table.cellWidget(row, 4).valueChanged.connect(self.update)  # Check whether course grade was updated
            if self.english_ui:
                button = createRemoveLineButton(str(row))
            else:
                button = Ui_tab_heb.createRemoveLineButton(str(row))
            value.append(row)
            lambdas.append(lambda state: self.clearRow(table))
            button.clicked.connect(lambdas[row])
            buttons.append(button)
            table.setCellWidget(row, table.columnCount() - 1, buttons[row])
            table.cellWidget(row, 0).currentIndexChanged.connect(self.update)
        self.ui.semesters.append(tab)
        if self.english_ui:
            self.ui.courses_tab_widget.insertTab(
                self.ui.courses_tab_widget.count(),
                self.ui.semesters[len(self.ui.semesters) - 1],
                "Semester " + str(self.ui.courses_tab_widget.count() + 1))
        else:
            self.ui.courses_tab_widget.insertTab(
                self.ui.courses_tab_widget.count(),
                self.ui.semesters[len(self.ui.semesters) - 1],
                str(self.ui.courses_tab_widget.count() + 1) + " סמסטר")
        self.update()

    # Function which is being called on clear-row button clicked in the table event
    # the function clears rows content, if the row is clear removes the row
    def clearRow(self, table):
        row = self.find_row(table, self.sender().objectName())
        empty = self.checkIfRowIsEmpty(table, row)
        if empty:
            table.removeRow(row)
            self.update()
            return
        table.cellWidget(row, 0).setCurrentIndex(0)
        for column in range(1, table.columnCount() - 1):
            if table.item(row, column) is not None:
                table.item(row, column).setText("")
                table.item(row, column).setToolTip("")
            if column >= 3:
                table.cellWidget(row, column).setValue(0)
        self.update()

    # Function which finds the row number of signal sender
    def find_row(self, table, senders_id):
        for row in range(0, table.rowCount()):
            clear_button_cell = table.columnCount() - 1
            if table.cellWidget(row, clear_button_cell):
                if table.cellWidget(row, clear_button_cell).objectName() == senders_id:
                    return row
        return table.rowCount()

    # Function which updates the numeric order of semester names in case of removal
    def updateTabNames(self):
        for i in range(self.ui.courses_tab_widget.count()):
            if self.english_ui:
                tab_name = "Semester " + str(i + 1)
            else:
                tab_name = "סמסטר " + str(i + 1)
            self.ui.courses_tab_widget.setTabText(i, tab_name)

    # Function which check if the semester has any input data,
    # if so prompts the user to ensure that he wants to remove the semester
    # and deletes it
    def removeSemester(self, i, force=False):
        empty_semester = True
        if self.english_ui:
            table = self.ui.courses_tab_widget.widget(i).children()[1]
        else:
            table = self.ui.courses_tab_widget.widget(i).children()[7]
        for row in range(table.rowCount()):
            if not self.checkIfRowIsEmpty(table, row):
                empty_semester = False
                break
        if force or empty_semester or (self.english_ui and self.my_close("semester", "Remove non-empty semester?")) or (
                not self.english_ui and self.my_close("semester", "למחוק סמסטר בעל תוכן?")):
            self.ui.courses_tab_widget.removeTab(i)
            if self.ui.courses_tab_widget.count() == 0:
                self.addSemester()
            self.updateTabNames()
            self.update()

    # Function which adds an empty row to the current semester
    def addRow(self, table):
        table.setRowCount(table.rowCount() + 1)
        table.setItem(table.rowCount() - 1, 0, QtWidgets.QTableWidgetItem())
        if self.english_ui:
            table.setCellWidget(table.rowCount() - 1, 0, createComboBox())
        else:
            table.setCellWidget(table.rowCount() - 1, 0, Ui_tab_heb.createComboBox())
        for column in range(1, table.columnCount() - 1):
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            table.setItem(table.rowCount() - 1, column, item)
            if column >= 3:
                if column == 3:
                    spin_box = QtWidgets.QDoubleSpinBox()
                    spin_box.setDecimals(1)
                    spin_box.setSingleStep(0.5)
                else:
                    spin_box = QtWidgets.QSpinBox()
                    spin_box.setSingleStep(1)
                spin_box.setRange(0, 100)
                spin_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
                spin_box.setAlignment(QtCore.Qt.AlignCenter)
                table.setCellWidget(table.rowCount() - 1, column, spin_box)
                table.cellWidget(table.rowCount() - 1, column).valueChanged.connect(self.update)
        if self.english_ui:
            button = createRemoveLineButton(str(table.rowCount() - 1))
        else:
            button = Ui_tab_heb.createRemoveLineButton(str(table.rowCount() - 1))
        button.clicked.connect(lambda state: self.clearRow(table))
        table.cellWidget(table.rowCount() - 1, 0).currentIndexChanged['int'].connect(self.update)
        table.setCellWidget(table.rowCount() - 1, table.columnCount() - 1, button)

    # Function which deletes the last row from the semester
    # if it is not empty prompts request 
    def removeRow(self, table):
        rows = table.rowCount()
        if rows == 0:
            return
        if self.checkIfRowIsEmpty(table, table.rowCount() - 1):
            table.setRowCount(rows - 1)
        else:
            if self.english_ui:
                answer = self.my_close("row", "Remove non-empty row?")
            else:
                answer = self.my_close("row", "למחוק שורה בעלת תוכן?")
            if answer:
                table.setRowCount(rows - 1)
        self.update()

    # Function which transforms check if there is "do not ask again" flag for removal
    # was checked if so allows removal without dialog, otherwise opens dialog to ensure removal
    def my_close(self, not_show_param, msg):
        if not_show_param == "row" and not self.not_show_remove_course:
            answer = self.warningMsg(not_show_param=not_show_param, msg=msg)
            return answer
        elif not_show_param == "semester" and not self.not_show_remove_semester:
            answer = self.warningMsg(not_show_param=not_show_param, msg=msg)
            return answer
        return True

    # Function which displays error message
    def errorMsg(self, msg):
        if self.english_ui:
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question,
                                            "Error", msg)
            msg_box.addButton(QtWidgets.QPushButton('Proceed'), QtWidgets.QMessageBox.YesRole)
        else:
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question,
                                            "שגיאה", msg)
            msg_box.addButton(QtWidgets.QPushButton('המשך'), QtWidgets.QMessageBox.YesRole)
        msg_box.exec()

    # Function which creates a prompt of removal or save
    def warningMsg(self, title="", not_show_param='', msg='ERROR'):
        if self.english_ui:
            if title == "":
                title = "Remove"
            check_box = QtWidgets.QCheckBox("Don't ask again.")
            msg_box = QtWidgets.QMessageBox(self)
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question, title, msg)
            msg_box.addButton(QtWidgets.QPushButton('Yes'), QtWidgets.QMessageBox.YesRole)
            msg_box.addButton(QtWidgets.QPushButton('No'), QtWidgets.QMessageBox.NoRole)
        else:
            if title == "":
                title = "מחיקה"
            check_box = QtWidgets.QCheckBox("לא להראות שוב")
            msg_box = QtWidgets.QMessageBox(self)
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question, title, msg)
            msg_box.addButton(QtWidgets.QPushButton('כן'), QtWidgets.QMessageBox.YesRole)
            msg_box.addButton(QtWidgets.QPushButton('לא'), QtWidgets.QMessageBox.NoRole)
        if not_show_param == "semester" or not_show_param == "row":
            msg_box.setCheckBox(check_box)
        reply = msg_box.exec()
        if not_show_param == "semester":
            self.not_show_remove_semester = bool(check_box.isChecked())
        elif not_show_param == "row":
            self.not_show_remove_course = bool(check_box.isChecked())
        if reply == 0:
            return True
        elif reply == 1:
            return False

    # Function which creates a dependencies warning message
    def prerequisitesWarningMessage(self, msg):
        if self.english_ui:
            msg += "Add anyway?"
            msg_box = QtWidgets.QMessageBox(self)
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question, "Warning", msg)
            msg_box.addButton(QtWidgets.QPushButton('Yes'), QtWidgets.QMessageBox.YesRole)
            msg_box.addButton(QtWidgets.QPushButton('No'), QtWidgets.QMessageBox.NoRole)
        else:
            msg += "להוסיף בכל זאת?"
            msg_box = QtWidgets.QMessageBox(self)
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question, "התראה", msg)
            msg_box.addButton(QtWidgets.QPushButton('כן'), QtWidgets.QMessageBox.YesRole)
            msg_box.addButton(QtWidgets.QPushButton('לא'), QtWidgets.QMessageBox.NoRole)
        reply = msg_box.exec()
        if reply == 0:
            return True
        elif reply == 1:
            return False
