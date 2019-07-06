# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eng_tab.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class TabPage(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1064, 541)
        Form.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.courses_table = QtWidgets.QTableWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.courses_table.sizePolicy().hasHeightForWidth())
        self.courses_table.setSizePolicy(sizePolicy)
        self.courses_table.setMouseTracking(True)
        self.courses_table.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.courses_table.setObjectName("courses_table")
        self.courses_table.setColumnCount(6)
        self.courses_table.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.courses_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.courses_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.courses_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.courses_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.courses_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.courses_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.courses_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.courses_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.courses_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.courses_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.courses_table.setHorizontalHeaderItem(5, item)
        self.courses_table.horizontalHeader().setVisible(True)
        self.courses_table.horizontalHeader().setCascadingSectionResizes(False)
        self.courses_table.horizontalHeader().setSortIndicatorShown(True)
        self.courses_table.horizontalHeader().setStretchLastSection(False)
        self.courses_table.verticalHeader().setVisible(False)
        self.courses_table.verticalHeader().setCascadingSectionResizes(True)
        self.courses_table.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout.addWidget(self.courses_table)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.semester_table_add_line = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.semester_table_add_line.sizePolicy().hasHeightForWidth())
        self.semester_table_add_line.setSizePolicy(sizePolicy)
        self.semester_table_add_line.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.semester_table_add_line.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/list-add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.semester_table_add_line.setIcon(icon)
        self.semester_table_add_line.setIconSize(QtCore.QSize(32, 32))
        self.semester_table_add_line.setObjectName("semester_table_add_line")
        self.horizontalLayout_6.addWidget(self.semester_table_add_line)
        self.semester_table_remove_line = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.semester_table_remove_line.sizePolicy().hasHeightForWidth())
        self.semester_table_remove_line.setSizePolicy(sizePolicy)
        self.semester_table_remove_line.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.semester_table_remove_line.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/list-remove.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.semester_table_remove_line.setIcon(icon1)
        self.semester_table_remove_line.setIconSize(QtCore.QSize(32, 32))
        self.semester_table_remove_line.setObjectName("semester_table_remove_line")
        self.horizontalLayout_6.addWidget(self.semester_table_remove_line)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.semester_average_in = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.semester_average_in.sizePolicy().hasHeightForWidth())
        self.semester_average_in.setSizePolicy(sizePolicy)
        self.semester_average_in.setMaximumSize(QtCore.QSize(75, 16777215))
        self.semester_average_in.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.semester_average_in.setText("")
        self.semester_average_in.setAlignment(QtCore.Qt.AlignCenter)
        self.semester_average_in.setReadOnly(True)
        self.semester_average_in.setObjectName("semester_average_in")
        self.horizontalLayout_7.addWidget(self.semester_average_in)
        self.semester_average_label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.semester_average_label.sizePolicy().hasHeightForWidth())
        self.semester_average_label.setSizePolicy(sizePolicy)
        self.semester_average_label.setMaximumSize(QtCore.QSize(70, 16777215))
        self.semester_average_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.semester_average_label.setObjectName("semester_average_label")
        self.horizontalLayout_7.addWidget(self.semester_average_label)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.semester_points_in = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.semester_points_in.sizePolicy().hasHeightForWidth())
        self.semester_points_in.setSizePolicy(sizePolicy)
        self.semester_points_in.setMaximumSize(QtCore.QSize(75, 16777215))
        self.semester_points_in.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.semester_points_in.setText("")
        self.semester_points_in.setAlignment(QtCore.Qt.AlignCenter)
        self.semester_points_in.setReadOnly(True)
        self.semester_points_in.setObjectName("semester_points_in")
        self.horizontalLayout_8.addWidget(self.semester_points_in)
        self.semester_points_label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.semester_points_label.sizePolicy().hasHeightForWidth())
        self.semester_points_label.setSizePolicy(sizePolicy)
        self.semester_points_label.setMaximumSize(QtCore.QSize(70, 16777215))
        self.semester_points_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.semester_points_label.setObjectName("semester_points_label")
        self.horizontalLayout_8.addWidget(self.semester_points_label)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.semester_add_course = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.semester_add_course.setFont(font)
        self.semester_add_course.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.semester_add_course.setObjectName("semester_add_course")
        self.gridLayout.addWidget(self.semester_add_course, 2, 1, 1, 1)
        self.courses_table.setSortingEnabled(True)
        self.not_show = False
        self.courses_table.setMouseTracking(False)
        self.courses_table.setSortingEnabled(False)
        for row in range(0, self.courses_table.rowCount()):
            item1 = QtWidgets.QTableWidgetItem()
            item2 = QtWidgets.QTableWidgetItem()
            self.courses_table.setItem(row, 0, item1)
            self.courses_table.setCellWidget(row, 0, createComboBox())
            self.courses_table.setItem(row, self.courses_table.columnCount() - 1, item2)
            self.courses_table.setCellWidget(row, self.courses_table.columnCount() - 1,
                                             createRemoveLineButton(str(row)))
            for column in range(1, self.courses_table.columnCount() - 1):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.courses_table.setItem(row, column, item)
                if column >= 3:
                    if column == 3:
                        spin_box = QtWidgets.QDoubleSpinBox()
                        spin_box.setDecimals(1)
                        spin_box.setSingleStep(0.5)
                    else:
                        spin_box = QtWidgets.QSpinBox()
                        spin_box.setSingleStep(1)
                    spin_box.setRange(0, 100)
                    spin_box.setAlignment(QtCore.Qt.AlignCenter)
                    spin_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
                    self.courses_table.setCellWidget(row, column, spin_box)
        self.courses_table.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.courses_table.setSortingEnabled(True)
        item = self.courses_table.verticalHeaderItem(0)
        item.setText(_translate("Form", "New Row"))
        item = self.courses_table.verticalHeaderItem(1)
        item.setText(_translate("Form", "New Row"))
        item = self.courses_table.verticalHeaderItem(2)
        item.setText(_translate("Form", "New Row"))
        item = self.courses_table.verticalHeaderItem(3)
        item.setText(_translate("Form", "New Row"))
        item = self.courses_table.verticalHeaderItem(4)
        item.setText(_translate("Form", "New Row"))
        item = self.courses_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Course"))
        item = self.courses_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Course №"))
        item = self.courses_table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Name"))
        item = self.courses_table.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Points"))
        item = self.courses_table.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Grade"))
        self.semester_table_add_line.setToolTip(_translate("Form",
                                                           "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Add line</span></p></body></html>"))
        self.semester_table_remove_line.setToolTip(_translate("Form",
                                                              "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Remove line</span></p></body></html>"))
        self.semester_average_label.setText(_translate("Form", "Average:"))
        self.semester_points_label.setText(_translate("Form", "Points:"))
        self.semester_add_course.setText(_translate("Form", "Find Course"))


def createComboBox():
    combo_box = QtWidgets.QComboBox()
    combo_box.setFocusPolicy(QtCore.Qt.StrongFocus)
    combo_box.addItem("Mandatory")
    combo_box.addItem("A' list")
    combo_box.addItem("B' list")
    combo_box.addItem("Humanistic")
    combo_box.addItem("Free choice")
    combo_box.addItem("Project")
    combo_box.addItem("Sport")
    return combo_box


def createRemoveLineButton(line):
    semester_table_remove_line = QtWidgets.QPushButton()
    sizePolicy = QtWidgets.QSizePolicy(
        QtWidgets.QSizePolicy.MinimumExpanding,
        QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(
        semester_table_remove_line.sizePolicy().hasHeightForWidth())
    semester_table_remove_line.setSizePolicy(sizePolicy)
    semester_table_remove_line.setLayoutDirection(
        QtCore.Qt.LeftToRight)
    semester_table_remove_line.setText("")
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap("images/row-clean.svg").transformed(QtGui.QTransform().rotate(180)),
                    QtGui.QIcon.Normal, QtGui.QIcon.Off)
    semester_table_remove_line.setIcon(icon1)
    semester_table_remove_line.setIconSize(QtCore.QSize(32, 32))
    semester_table_remove_line.setObjectName(
        line)
    _translate = QtCore.QCoreApplication.translate
    semester_table_remove_line.setToolTip(
        _translate(
            "Form",
            "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Clear line</span></p></body></html>"
        ))
    return semester_table_remove_line
