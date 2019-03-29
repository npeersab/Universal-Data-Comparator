# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_welcome_dialog(object):
    def setupUi(self, welcome_dialog):
        welcome_dialog.setObjectName("welcome_dialog")
        welcome_dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        welcome_dialog.resize(350, 150)
        welcome_dialog.setMaximumSize(QtCore.QSize(350, 150))
        self.gridLayout = QtWidgets.QGridLayout(welcome_dialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 21, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(92, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.butto_frame = QtWidgets.QFrame(welcome_dialog)
        self.butto_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.butto_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.butto_frame.setObjectName("butto_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.butto_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.create_button = QtWidgets.QPushButton(self.butto_frame)
        self.create_button.setObjectName("create_button")
        self.verticalLayout.addWidget(self.create_button)
        self.open_button = QtWidgets.QPushButton(self.butto_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_button.sizePolicy().hasHeightForWidth())
        self.open_button.setSizePolicy(sizePolicy)
        self.open_button.setObjectName("open_button")
        self.verticalLayout.addWidget(self.open_button)
        self.gridLayout.addWidget(self.butto_frame, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(91, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 21, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 1)

        self.retranslateUi(welcome_dialog)
        QtCore.QMetaObject.connectSlotsByName(welcome_dialog)

    def retranslateUi(self, welcome_dialog):
        _translate = QtCore.QCoreApplication.translate
        welcome_dialog.setWindowTitle(_translate("welcome_dialog", "Welcome"))
        self.create_button.setText(_translate("welcome_dialog", "Create New Project"))
        self.open_button.setText(_translate("welcome_dialog", "Open Existing Project"))

