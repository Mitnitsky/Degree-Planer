# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maindesign.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from findDialog import Ui_course_search


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1981, 805)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.add_semester_but = QtWidgets.QPushButton(self.centralwidget)
        self.add_semester_but.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/list-add.svg"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_semester_but.setIcon(icon)
        self.add_semester_but.setObjectName("add_semester_but")
        self.verticalLayout_4.addWidget(self.add_semester_but)
        spacerItem = QtWidgets.QSpacerItem(20, 40,
                                           QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.courses_tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.courses_tab_widget.sizePolicy().hasHeightForWidth())
        self.courses_tab_widget.setSizePolicy(sizePolicy)
        self.courses_tab_widget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.courses_tab_widget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.courses_tab_widget.setTabsClosable(True)
        self.courses_tab_widget.setObjectName("courses_tab_widget")
        self.semesters = list()
        self.horizontalLayout.addWidget(self.courses_tab_widget)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.progress_label_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.progress_label_8.sizePolicy().hasHeightForWidth())
        self.progress_label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.progress_label_8.setFont(font)
        self.progress_label_8.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.progress_label_8.setStyleSheet("font: 16pt \"Noto Sans\";\n"
                                            "text-decoration: underline;")
        self.progress_label_8.setAlignment(QtCore.Qt.AlignBottom
                                           | QtCore.Qt.AlignLeading
                                           | QtCore.Qt.AlignLeft)
        self.progress_label_8.setObjectName("progress_label_8")
        self.verticalLayout_15.addWidget(self.progress_label_8)
        self.frame_11 = QtWidgets.QFrame(self.centralwidget)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.horizontalLayout_93 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_93.setSpacing(0)
        self.horizontalLayout_93.setObjectName("horizontalLayout_93")
        self.horizontalLayout_45 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        self.deg_points_label = QtWidgets.QLabel(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.deg_points_label.sizePolicy().hasHeightForWidth())
        self.deg_points_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.deg_points_label.setFont(font)
        self.deg_points_label.setObjectName("deg_points_label")
        self.horizontalLayout_45.addWidget(self.deg_points_label)
        spacerItem5 = QtWidgets.QSpacerItem(6, 20, QtWidgets.QSizePolicy.Fixed,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_45.addItem(spacerItem5)
        self.deg_points_in = QtWidgets.QLineEdit(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.deg_points_in.sizePolicy().hasHeightForWidth())
        self.deg_points_in.setSizePolicy(sizePolicy)
        self.deg_points_in.setAlignment(QtCore.Qt.AlignCenter)
        self.deg_points_in.setReadOnly(False)
        self.deg_points_in.setObjectName("deg_points_in")
        self.horizontalLayout_45.addWidget(self.deg_points_in)
        self.horizontalLayout_93.addLayout(self.horizontalLayout_45)
        spacerItem6 = QtWidgets.QSpacerItem(490, 20,
                                            QtWidgets.QSizePolicy.Fixed,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_93.addItem(spacerItem6)
        self.gridLayout_10.addLayout(self.horizontalLayout_93, 0, 0, 1, 1)
        self.horizontalLayout_44 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_44.setObjectName("horizontalLayout_44")
        self.frame = QtWidgets.QFrame(self.frame_11)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.desc_label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.desc_label.sizePolicy().hasHeightForWidth())
        self.desc_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.desc_label.setFont(font)
        self.desc_label.setObjectName("desc_label")
        self.verticalLayout_21.addWidget(self.desc_label)
        self.horizontalLayout_80 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_80.setSpacing(0)
        self.horizontalLayout_80.setObjectName("horizontalLayout_80")
        self.average_lab_7 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.average_lab_7.sizePolicy().hasHeightForWidth())
        self.average_lab_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.average_lab_7.setFont(font)
        self.average_lab_7.setObjectName("average_lab_7")
        self.horizontalLayout_80.addWidget(self.average_lab_7)
        self.average_in_7 = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.average_in_7.sizePolicy().hasHeightForWidth())
        self.average_in_7.setSizePolicy(sizePolicy)
        self.average_in_7.setText("")
        self.average_in_7.setAlignment(QtCore.Qt.AlignCenter)
        self.average_in_7.setReadOnly(True)
        self.average_in_7.setObjectName("average_in_7")
        self.horizontalLayout_80.addWidget(self.average_in_7)
        self.verticalLayout_21.addLayout(self.horizontalLayout_80)
        self.horizontalLayout_81 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_81.setSpacing(0)
        self.horizontalLayout_81.setObjectName("horizontalLayout_81")
        self.points_label_7 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.points_label_7.sizePolicy().hasHeightForWidth())
        self.points_label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.points_label_7.setFont(font)
        self.points_label_7.setObjectName("points_label_7")
        self.horizontalLayout_81.addWidget(self.points_label_7)
        self.points_in_7 = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.points_in_7.sizePolicy().hasHeightForWidth())
        self.points_in_7.setSizePolicy(sizePolicy)
        self.points_in_7.setText("")
        self.points_in_7.setAlignment(QtCore.Qt.AlignCenter)
        self.points_in_7.setReadOnly(True)
        self.points_in_7.setObjectName("points_in_7")
        self.horizontalLayout_81.addWidget(self.points_in_7)
        self.verticalLayout_21.addLayout(self.horizontalLayout_81)
        self.horizontalLayout_82 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_82.setSpacing(0)
        self.horizontalLayout_82.setObjectName("horizontalLayout_82")
        self.points_left_label_7 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.points_left_label_7.sizePolicy().hasHeightForWidth())
        self.points_left_label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.points_left_label_7.setFont(font)
        self.points_left_label_7.setObjectName("points_left_label_7")
        self.horizontalLayout_82.addWidget(self.points_left_label_7)
        self.points_left_in_7 = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.points_left_in_7.sizePolicy().hasHeightForWidth())
        self.points_left_in_7.setSizePolicy(sizePolicy)
        self.points_left_in_7.setText("")
        self.points_left_in_7.setAlignment(QtCore.Qt.AlignCenter)
        self.points_left_in_7.setReadOnly(True)
        self.points_left_in_7.setObjectName("points_left_in_7")
        self.horizontalLayout_82.addWidget(self.points_left_in_7)
        self.verticalLayout_21.addLayout(self.horizontalLayout_82)
        self.horizontalLayout_83 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_83.setSpacing(0)
        self.horizontalLayout_83.setObjectName("horizontalLayout_83")
        self.points_left_to_choose_label_7 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.points_left_to_choose_label_7.
                                     sizePolicy().hasHeightForWidth())
        self.points_left_to_choose_label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.points_left_to_choose_label_7.setFont(font)
        self.points_left_to_choose_label_7.setObjectName(
            "points_left_to_choose_label_7")
        self.horizontalLayout_83.addWidget(self.points_left_to_choose_label_7)
        self.points_left_to_choose_in_7 = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.points_left_to_choose_in_7.sizePolicy().hasHeightForWidth())
        self.points_left_to_choose_in_7.setSizePolicy(sizePolicy)
        self.points_left_to_choose_in_7.setText("")
        self.points_left_to_choose_in_7.setAlignment(QtCore.Qt.AlignCenter)
        self.points_left_to_choose_in_7.setReadOnly(True)
        self.points_left_to_choose_in_7.setObjectName(
            "points_left_to_choose_in_7")
        self.horizontalLayout_83.addWidget(self.points_left_to_choose_in_7)
        self.verticalLayout_21.addLayout(self.horizontalLayout_83)
        spacerItem7 = QtWidgets.QSpacerItem(
            20, 77, QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_21.addItem(spacerItem7)
        self.gridLayout_7.addLayout(self.verticalLayout_21, 0, 0, 1, 1)
        self.horizontalLayout_44.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(self.frame_11)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.horizontalLayout_85 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_85.setObjectName("horizontalLayout_85")
        spacerItem8 = QtWidgets.QSpacerItem(112, 20,
                                            QtWidgets.QSizePolicy.Fixed,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_85.addItem(spacerItem8)
        self.done_label_7 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.done_label_7.sizePolicy().hasHeightForWidth())
        self.done_label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(7)
        self.done_label_7.setFont(font)
        self.done_label_7.setStyleSheet("font: 57 12pt \"Noto Sans\";")
        self.done_label_7.setObjectName("done_label_7")
        self.horizontalLayout_85.addWidget(self.done_label_7)
        self.of_label_7 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.of_label_7.sizePolicy().hasHeightForWidth())
        self.of_label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(7)
        self.of_label_7.setFont(font)
        self.of_label_7.setStyleSheet("font: 57 10pt \"Noto Sans\";")
        self.of_label_7.setObjectName("of_label_7")
        self.horizontalLayout_85.addWidget(self.of_label_7)
        self.verticalLayout_23.addLayout(self.horizontalLayout_85)
        self.horizontalLayout_92 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_92.setObjectName("horizontalLayout_92")
        self.must_label = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.must_label.sizePolicy().hasHeightForWidth())
        self.must_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.must_label.setFont(font)
        self.must_label.setObjectName("must_label")
        self.horizontalLayout_92.addWidget(self.must_label)
        self.must_done_in = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.must_done_in.sizePolicy().hasHeightForWidth())
        self.must_done_in.setSizePolicy(sizePolicy)
        self.must_done_in.setText("")
        self.must_done_in.setAlignment(QtCore.Qt.AlignCenter)
        self.must_done_in.setReadOnly(True)
        self.must_done_in.setObjectName("must_done_in")
        self.horizontalLayout_92.addWidget(self.must_done_in)
        self.must_of_in = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.must_of_in.sizePolicy().hasHeightForWidth())
        self.must_of_in.setSizePolicy(sizePolicy)
        self.must_of_in.setAlignment(QtCore.Qt.AlignCenter)
        self.must_of_in.setObjectName("must_of_in")
        self.horizontalLayout_92.addWidget(self.must_of_in)
        self.verticalLayout_23.addLayout(self.horizontalLayout_92)
        self.horizontalLayout_86 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_86.setObjectName("horizontalLayout_86")
        self.list_a_label_7 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.list_a_label_7.sizePolicy().hasHeightForWidth())
        self.list_a_label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.list_a_label_7.setFont(font)
        self.list_a_label_7.setObjectName("list_a_label_7")
        self.horizontalLayout_86.addWidget(self.list_a_label_7)
        self.list_a_done_in_7 = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.list_a_done_in_7.sizePolicy().hasHeightForWidth())
        self.list_a_done_in_7.setSizePolicy(sizePolicy)
        self.list_a_done_in_7.setText("")
        self.list_a_done_in_7.setAlignment(QtCore.Qt.AlignCenter)
        self.list_a_done_in_7.setReadOnly(True)
        self.list_a_done_in_7.setObjectName("list_a_done_in_7")
        self.horizontalLayout_86.addWidget(self.list_a_done_in_7)
        self.list_a_of_in_7 = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.list_a_of_in_7.sizePolicy().hasHeightForWidth())
        self.list_a_of_in_7.setSizePolicy(sizePolicy)
        self.list_a_of_in_7.setAlignment(QtCore.Qt.AlignCenter)
        self.list_a_of_in_7.setObjectName("list_a_of_in_7")
        self.horizontalLayout_86.addWidget(self.list_a_of_in_7)
        self.verticalLayout_23.addLayout(self.horizontalLayout_86)
        self.horizontalLayout_87 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_87.setObjectName("horizontalLayout_87")
        self.list_b_label_7 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.list_b_label_7.sizePolicy().hasHeightForWidth())
        self.list_b_label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.list_b_label_7.setFont(font)
        self.list_b_label_7.setObjectName("list_b_label_7")
        self.horizontalLayout_87.addWidget(self.list_b_label_7)
        self.list_b_done_in_7 = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.list_b_done_in_7.sizePolicy().hasHeightForWidth())
        self.list_b_done_in_7.setSizePolicy(sizePolicy)
        self.list_b_done_in_7.setText("")
        self.list_b_done_in_7.setAlignment(QtCore.Qt.AlignCenter)
        self.list_b_done_in_7.setReadOnly(True)
        self.list_b_done_in_7.setObjectName("list_b_done_in_7")
        self.horizontalLayout_87.addWidget(self.list_b_done_in_7)
        self.list_b_of_in_7 = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.list_b_of_in_7.sizePolicy().hasHeightForWidth())
        self.list_b_of_in_7.setSizePolicy(sizePolicy)
        self.list_b_of_in_7.setAlignment(QtCore.Qt.AlignCenter)
        self.list_b_of_in_7.setObjectName("list_b_of_in_7")
        self.horizontalLayout_87.addWidget(self.list_b_of_in_7)
        self.verticalLayout_23.addLayout(self.horizontalLayout_87)
        self.horizontalLayout_88 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_88.setObjectName("horizontalLayout_88")
        self.project_label_7 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.project_label_7.sizePolicy().hasHeightForWidth())
        self.project_label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.project_label_7.setFont(font)
        self.project_label_7.setObjectName("project_label_7")
        self.horizontalLayout_88.addWidget(self.project_label_7)
        self.project_done_in_7 = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.project_done_in_7.sizePolicy().hasHeightForWidth())
        self.project_done_in_7.setSizePolicy(sizePolicy)
        self.project_done_in_7.setText("")
        self.project_done_in_7.setAlignment(QtCore.Qt.AlignCenter)
        self.project_done_in_7.setReadOnly(True)
        self.project_done_in_7.setObjectName("project_done_in_7")
        self.horizontalLayout_88.addWidget(self.project_done_in_7)
        self.project_of_in_7 = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.project_of_in_7.sizePolicy().hasHeightForWidth())
        self.project_of_in_7.setSizePolicy(sizePolicy)
        self.project_of_in_7.setAlignment(QtCore.Qt.AlignCenter)
        self.project_of_in_7.setObjectName("project_of_in_7")
        self.horizontalLayout_88.addWidget(self.project_of_in_7)
        self.verticalLayout_23.addLayout(self.horizontalLayout_88)
        self.horizontalLayout_94 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_94.setObjectName("horizontalLayout_94")
        self.malag_label_7 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.malag_label_7.sizePolicy().hasHeightForWidth())
        self.malag_label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.malag_label_7.setFont(font)
        self.malag_label_7.setObjectName("malag_label_7")
        self.horizontalLayout_94.addWidget(self.malag_label_7)
        self.malag_done_in_7 = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.malag_done_in_7.sizePolicy().hasHeightForWidth())
        self.malag_done_in_7.setSizePolicy(sizePolicy)
        self.malag_done_in_7.setText("")
        self.malag_done_in_7.setAlignment(QtCore.Qt.AlignCenter)
        self.malag_done_in_7.setReadOnly(True)
        self.malag_done_in_7.setObjectName("malag_done_in_7")
        self.horizontalLayout_94.addWidget(self.malag_done_in_7)
        self.malag_of_in_7 = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.malag_of_in_7.sizePolicy().hasHeightForWidth())
        self.malag_of_in_7.setSizePolicy(sizePolicy)
        self.malag_of_in_7.setAlignment(QtCore.Qt.AlignCenter)
        self.malag_of_in_7.setObjectName("malag_of_in_7")
        self.horizontalLayout_94.addWidget(self.malag_of_in_7)
        self.verticalLayout_23.addLayout(self.horizontalLayout_94)
        self.horizontalLayout_89 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_89.setObjectName("horizontalLayout_89")
        self.sport_label_7 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sport_label_7.sizePolicy().hasHeightForWidth())
        self.sport_label_7.setSizePolicy(sizePolicy)
        self.sport_label_7.setStyleSheet("font: 10pt \"Noto Sans\";\n"
                                         "text-decoration: underline;")
        self.sport_label_7.setObjectName("sport_label_7")
        self.horizontalLayout_89.addWidget(self.sport_label_7)
        self.sport_done_in_7 = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sport_done_in_7.sizePolicy().hasHeightForWidth())
        self.sport_done_in_7.setSizePolicy(sizePolicy)
        self.sport_done_in_7.setText("")
        self.sport_done_in_7.setAlignment(QtCore.Qt.AlignCenter)
        self.sport_done_in_7.setReadOnly(True)
        self.sport_done_in_7.setObjectName("sport_done_in_7")
        self.horizontalLayout_89.addWidget(self.sport_done_in_7)
        self.sport_of_in_7 = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sport_of_in_7.sizePolicy().hasHeightForWidth())
        self.sport_of_in_7.setSizePolicy(sizePolicy)
        self.sport_of_in_7.setAlignment(QtCore.Qt.AlignCenter)
        self.sport_of_in_7.setObjectName("sport_of_in_7")
        self.horizontalLayout_89.addWidget(self.sport_of_in_7)
        self.verticalLayout_23.addLayout(self.horizontalLayout_89)
        self.horizontalLayout_90 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_90.setObjectName("horizontalLayout_90")
        self.free_label_7 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.free_label_7.sizePolicy().hasHeightForWidth())
        self.free_label_7.setSizePolicy(sizePolicy)
        self.free_label_7.setStyleSheet("font: 10pt \"Noto Sans\";\n"
                                        "text-decoration: underline;")
        self.free_label_7.setObjectName("free_label_7")
        self.horizontalLayout_90.addWidget(self.free_label_7)
        self.free_done_in_7 = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.free_done_in_7.sizePolicy().hasHeightForWidth())
        self.free_done_in_7.setSizePolicy(sizePolicy)
        self.free_done_in_7.setText("")
        self.free_done_in_7.setAlignment(QtCore.Qt.AlignCenter)
        self.free_done_in_7.setReadOnly(True)
        self.free_done_in_7.setObjectName("free_done_in_7")
        self.horizontalLayout_90.addWidget(self.free_done_in_7)
        self.free_of_in_7 = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.free_of_in_7.sizePolicy().hasHeightForWidth())
        self.free_of_in_7.setSizePolicy(sizePolicy)
        self.free_of_in_7.setAlignment(QtCore.Qt.AlignCenter)
        self.free_of_in_7.setObjectName("free_of_in_7")
        self.horizontalLayout_90.addWidget(self.free_of_in_7)
        self.verticalLayout_23.addLayout(self.horizontalLayout_90)
        self.horizontalLayout_91 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_91.setObjectName("horizontalLayout_91")
        self.english_checkbox_7 = QtWidgets.QCheckBox(self.frame_3)
        self.english_checkbox_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.english_checkbox_7.setObjectName("english_checkbox_7")
        self.horizontalLayout_91.addWidget(self.english_checkbox_7)
        spacerItem9 = QtWidgets.QSpacerItem(334, 20,
                                            QtWidgets.QSizePolicy.Fixed,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_91.addItem(spacerItem9)
        self.verticalLayout_23.addLayout(self.horizontalLayout_91)
        self.frame_12 = QtWidgets.QFrame(self.frame_3)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_23.addWidget(self.frame_12)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40,
                                             QtWidgets.QSizePolicy.Minimum,
                                             QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_23.addItem(spacerItem10)
        self.gridLayout_8.addLayout(self.verticalLayout_23, 0, 0, 1, 1)
        self.horizontalLayout_44.addWidget(self.frame_3)
        self.gridLayout_10.addLayout(self.horizontalLayout_44, 1, 0, 1, 1)
        self.verticalLayout_15.addWidget(self.frame_11)
        self.horizontalLayout.addLayout(self.verticalLayout_15)
        self.horizontalLayout_22.addLayout(self.horizontalLayout)
        self.gridLayout_3.addLayout(self.horizontalLayout_22, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1981, 36))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionUpdate_Courses_DB = QtWidgets.QAction(MainWindow)
        self.actionUpdate_Courses_DB.setObjectName("actionUpdate_Courses_DB")
        self.menu.addAction(self.actionSaveAs)
        self.menu.addAction(self.actionLoad)
        self.menu.addAction(self.actionUpdate_Courses_DB)
        self.menubar.addAction(self.menu.menuAction())
        self.retranslateUi(MainWindow)
        self.courses_tab_widget.setCurrentIndex(0)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_semester_but.setText(_translate("MainWindow", "הוסף סמסטר"))
        self.progress_label_8.setText(
            _translate("MainWindow", "התקדמות בתואר:"))
        self.deg_points_label.setText(_translate("MainWindow",
                                                 "נקודות לתואר:"))
        self.deg_points_in.setText(_translate("MainWindow", "0"))
        self.desc_label.setText(_translate("MainWindow", "כללי:"))
        self.average_lab_7.setText(_translate("MainWindow", "ממוצע תואר:"))
        self.points_label_7.setText(_translate("MainWindow", "נק\"ז בוצעו:"))
        self.points_left_label_7.setText(
            _translate("MainWindow", "נק\"ז נותרו:"))
        self.points_left_to_choose_label_7.setText(
            _translate("MainWindow", "נותר לשבץ:"))
        self.done_label_7.setText(_translate("MainWindow", "שובצו:"))
        self.of_label_7.setText(_translate("MainWindow", "מתוך(יש למלא):"))
        self.must_label.setText(_translate("MainWindow", "חובה:"))
        self.must_of_in.setText(_translate("MainWindow", "0"))
        self.list_a_label_7.setText(_translate("MainWindow", "רשימה א\':"))
        self.list_a_of_in_7.setText(_translate("MainWindow", "0"))
        self.list_b_label_7.setText(_translate("MainWindow", "רשימה ב\':"))
        self.list_b_of_in_7.setText(_translate("MainWindow", "0"))
        self.project_label_7.setText(_translate("MainWindow", "פרוייקט:"))
        self.project_of_in_7.setText(_translate("MainWindow", "0"))
        self.malag_label_7.setText(_translate("MainWindow", "מל\"ג:"))
        self.malag_of_in_7.setText(_translate("MainWindow", "0"))
        self.sport_label_7.setText(_translate("MainWindow", "ספורט:"))
        self.sport_of_in_7.setText(_translate("MainWindow", "0"))
        self.free_label_7.setText(_translate("MainWindow", "בחירה חופשית:"))
        self.free_of_in_7.setText(_translate("MainWindow", "0"))
        self.english_checkbox_7.setText(
            _translate("MainWindow", "פטור באנגלית"))
        self.menu.setTitle(_translate("MainWindow", "Menu"))
        self.actionSaveAs.setText(_translate("MainWindow", "Save as."))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionUpdate_Courses_DB.setText(
            _translate("MainWindow", "Update Courses DB"))
