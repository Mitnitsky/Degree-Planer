from PyQt5 import QtCore, QtGui, QtWidgets
from scrapper import *

class mythread(QtCore.QThread):

    def __init__(self, lst, semesters):
        QtCore.QThread.__init__(self)
        self.lst = lst
        self.semesters = semesters
        self.alive = True

    def __del__(self):
        self.alive = False
        self.wait()
    
    def run(self):
        self.alive = True
        for course_number in sorted(self.lst[0]):
            dbAddCourse(getCourseInfo(course_number,
                                    self.semesters[len(self.semesters) - 1]))
            self.lst[1] += 1
        self.__del__()
