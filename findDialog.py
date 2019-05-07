# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'findDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from scrapper import findCourseInDB


class Ui_course_search(object):
    def setupUi(self, course_search):
        course_search.setObjectName("course_search")
        course_search.resize(502, 433)
        self.gridLayout = QtWidgets.QGridLayout(course_search)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.course_num_in = QtWidgets.QLineEdit(course_search)
        self.course_num_in.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.course_num_in.setText("")
        self.course_num_in.setAlignment(QtCore.Qt.AlignRight
                                        | QtCore.Qt.AlignTrailing
                                        | QtCore.Qt.AlignVCenter)
        self.course_num_in.setObjectName("course_num_in")
        self.horizontalLayout.addWidget(self.course_num_in)
        self.course_num_label = QtWidgets.QLabel(course_search)
        self.course_num_label.setObjectName("course_num_label")
        self.horizontalLayout.addWidget(self.course_num_label)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.close_search_button = QtWidgets.QPushButton(course_search)
        self.close_search_button.setObjectName("close_search_button")
        self.horizontalLayout_2.addWidget(self.close_search_button)
        self.add_course_button = QtWidgets.QPushButton(course_search)
        self.add_course_button.setObjectName("add_course_button")
        self.horizontalLayout_2.addWidget(self.add_course_button)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.find_course_button = QtWidgets.QPushButton(course_search)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.find_course_button.sizePolicy().hasHeightForWidth())
        self.find_course_button.setSizePolicy(sizePolicy)
        self.find_course_button.setObjectName("find_course_button")
        self.verticalLayout.addWidget(self.find_course_button)
        self.course_info_label = QtWidgets.QLabel(course_search)
        self.course_info_label.setObjectName("course_info_label")
        self.verticalLayout.addWidget(self.course_info_label)
        self.find_course_in = QtWidgets.QTextEdit(course_search)
        self.find_course_in.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.find_course_in.setLocale(
            QtCore.QLocale(QtCore.QLocale.Hebrew, QtCore.QLocale.Israel))
        self.find_course_in.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.find_course_in.setTextInteractionFlags(
            QtCore.Qt.TextSelectableByKeyboard
            | QtCore.Qt.TextSelectableByMouse)
        self.find_course_in.setObjectName("find_course_in")
        self.verticalLayout.addWidget(self.find_course_in)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.retranslateUi(course_search)
        QtCore.QMetaObject.connectSlotsByName(course_search)
        course_search.setTabOrder(self.course_num_in, self.find_course_button)
        course_search.setTabOrder(self.find_course_button,
                                  self.add_course_button)
        course_search.setTabOrder(self.add_course_button,
                                  self.close_search_button)
        course_search.setTabOrder(self.close_search_button,
                                  self.find_course_in)
        self.find_course_button.clicked.connect(self.findCourse)
        # self.close_search_button.clicked.connect(self)

    def retranslateUi(self, course_search):
        _translate = QtCore.QCoreApplication.translate
        course_search.setWindowTitle(_translate("course_search", "Dialog"))
        self.course_num_label.setText(_translate("course_search",
                                                 "מס\' קורס:"))
        self.close_search_button.setText(_translate("course_search", "סגור"))
        self.add_course_button.setText(_translate("course_search", "הוסף"))
        self.find_course_button.setText(_translate("course_search", "חפש"))
        self.course_info_label.setText(
            _translate("course_search", "מידע על הקורס:"))
        self.find_course_in.setHtml(
            _translate(
                "course_search",
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                "<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"
            ))

    def findCourse(self):
        if self.course_num_in.text() != "":
            self.find_course_in.setPlainText(
                repr(findCourseInDB(self.course_num_in.text())))
        else:
            self.find_course_in.setPlainText("הקורס לא נמצא במערכת")
