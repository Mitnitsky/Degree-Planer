# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/vov4ik/Projects/DegreePlanner/findDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from extended_combo_box import ExtendedComboBox


class Ui_course_search(object):
    def setupUi(self, course_search):
        course_search.setObjectName("course_search")
        course_search.resize(498, 443)
        self.gridLayout = QtWidgets.QGridLayout(course_search)
        self.gridLayout.setObjectName("gridLayout")
        self.course_num_label = QtWidgets.QLabel(course_search)
        self.course_num_label.setStyleSheet("font: 12pt \"Noto Sans\";")
        self.course_num_label.setObjectName("course_num_label")
        self.gridLayout.addWidget(self.course_num_label, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(course_search)
        self.pushButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/row-clean.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.comboBox = ExtendedComboBox(course_search)
        self.comboBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboBox.setCurrentText("")
        self.comboBox.setMaxVisibleItems(50)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.lineEdit().setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboBox.lineEdit().setLayoutDirection(QtCore.Qt.RightToLeft)

        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.course_info_label = QtWidgets.QLabel(course_search)
        self.course_info_label.setStyleSheet("font: 12pt \"Noto Sans\";")
        self.course_info_label.setObjectName("course_info_label")
        self.verticalLayout.addWidget(self.course_info_label)
        self.find_course_in = QtWidgets.QTextEdit(course_search)
        self.find_course_in.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.find_course_in.setLocale(QtCore.QLocale(QtCore.QLocale.Hebrew, QtCore.QLocale.Israel))
        self.find_course_in.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.find_course_in.setTextInteractionFlags(
            QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.find_course_in.setObjectName("find_course_in")
        self.verticalLayout.addWidget(self.find_course_in)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.close_search_button = QtWidgets.QPushButton(course_search)
        self.close_search_button.setObjectName("close_search_button")
        self.horizontalLayout_2.addWidget(self.close_search_button)
        self.add_course_button = QtWidgets.QPushButton(course_search)
        self.add_course_button.setObjectName("add_course_button")
        self.horizontalLayout_2.addWidget(self.add_course_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.retranslateUi(course_search)
        self.pushButton.clearFocus()
        self.pushButton.clicked.connect(self.comboBox.clearEditText)
        QtCore.QMetaObject.connectSlotsByName(course_search)
        course_search.setTabOrder(self.comboBox, self.pushButton)
        course_search.setTabOrder(self.close_search_button, self.find_course_in)

    def retranslateUi(self, course_search):
        _translate = QtCore.QCoreApplication.translate
        course_search.setWindowTitle(_translate("course_search", "Dialog"))
        self.course_num_label.setText(_translate("course_search", "הכנס מספר/שם קורס:"))
        self.course_info_label.setText(_translate("course_search", "מידע על הקורס:"))
        self.find_course_in.setHtml(_translate("course_search",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                               "<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.close_search_button.setText(_translate("course_search", "סגור"))
        self.add_course_button.setText(_translate("course_search", "הוסף"))