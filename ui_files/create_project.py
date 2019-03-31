# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_project.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_create_project(object):
    def setupUi(self, create_project):
        create_project.setObjectName("create_project")
        create_project.setWindowModality(QtCore.Qt.ApplicationModal)
        create_project.resize(400, 135)
        create_project.setMaximumSize(QtCore.QSize(400, 135))
        self.create_project_layout = QtWidgets.QVBoxLayout(create_project)
        self.create_project_layout.setObjectName("create_project_layout")
        self.widget = QtWidgets.QWidget(create_project)
        self.widget.setObjectName("widget")
        self.widget_layout = QtWidgets.QVBoxLayout(self.widget)
        self.widget_layout.setObjectName("widget_layout")
        self.form = QtWidgets.QFrame(self.widget)
        self.form.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.form.setFrameShadow(QtWidgets.QFrame.Raised)
        self.form.setObjectName("form")
        self.form_layout = QtWidgets.QFormLayout(self.form)
        self.form_layout.setObjectName("form_layout")
        self.project_name_label = QtWidgets.QLabel(self.form)
        self.project_name_label.setObjectName("project_name_label")
        self.form_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.project_name_label)
        self.project_name_field = QtWidgets.QLineEdit(self.form)
        self.project_name_field.setObjectName("project_name_field")
        self.form_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.project_name_field)
        self.widget_layout.addWidget(self.form)
        self.button_frame = QtWidgets.QFrame(self.widget)
        self.button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_frame.setObjectName("button_frame")
        self.button_frame_layout = QtWidgets.QHBoxLayout(self.button_frame)
        self.button_frame_layout.setObjectName("button_frame_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.button_frame_layout.addItem(spacerItem)
        self.create_project_button = QtWidgets.QPushButton(self.button_frame)
        self.create_project_button.setObjectName("create_project_button")
        self.button_frame_layout.addWidget(self.create_project_button)
        self.cancel_button = QtWidgets.QPushButton(self.button_frame)
        self.cancel_button.setObjectName("cancel_button")
        self.button_frame_layout.addWidget(self.cancel_button)
        self.widget_layout.addWidget(self.button_frame)
        self.create_project_layout.addWidget(self.widget)

        self.retranslateUi(create_project)
        QtCore.QMetaObject.connectSlotsByName(create_project)

    def retranslateUi(self, create_project):
        _translate = QtCore.QCoreApplication.translate
        create_project.setWindowTitle(_translate("create_project", "Create New Project"))
        self.project_name_label.setText(_translate("create_project", "Project Name:"))
        self.create_project_button.setText(_translate("create_project", "Create Project"))
        self.create_project_button.setShortcut(_translate("create_project", "Return"))
        self.cancel_button.setText(_translate("create_project", "Cancel"))
        self.cancel_button.setShortcut(_translate("create_project", "Esc"))

