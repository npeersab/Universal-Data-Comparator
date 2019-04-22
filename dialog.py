#  Copyright (c) 2019. Noorulhasan Peersab <npeersab77@gmail.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
import pickle

import pyodbc

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QAction, QFileDialog
from pyodbc import OperationalError

from connection import OdbcDsnConnection, UserDetails, OdbcConnection
from message_box import ErrorMessageBox, InformationMessageBox, WarningMessageBox
from test import TestProject, TestCase


class WelcomeDialog(QWidget):
    def __init__(self, start_main, parent=None):
        super().__init__(parent=parent, flags=QtCore.Qt.Window)
        self.start_main = start_main

        ##########################################
        # Auto generated UI code starts from here #
        ##########################################

        self.setObjectName("welcome_dialog")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.resize(350, 110)
        self.setMaximumSize(QtCore.QSize(350, 110))
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        spacer_item_1 = QtWidgets.QSpacerItem(20, 21, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacer_item_1, 0, 1, 1, 1)
        spacer_item_2 = QtWidgets.QSpacerItem(92, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacer_item_2, 1, 0, 1, 1)
        self.button_frame = QtWidgets.QFrame(self)
        self.button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_frame.setObjectName("button_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.button_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.create_button = QtWidgets.QPushButton(self.button_frame)
        self.create_button.setMinimumSize(QtCore.QSize(150, 0))
        self.create_button.setAutoFillBackground(False)
        self.create_button.setFlat(False)
        self.create_button.setObjectName("create_button")
        self.verticalLayout.addWidget(self.create_button)
        self.open_button = QtWidgets.QPushButton(self.button_frame)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.open_button.sizePolicy().hasHeightForWidth())
        self.open_button.setSizePolicy(size_policy)
        self.open_button.setAutoFillBackground(False)
        self.open_button.setFlat(False)
        self.open_button.setObjectName("open_button")
        self.verticalLayout.addWidget(self.open_button)
        self.gridLayout.addWidget(self.button_frame, 1, 1, 1, 1)
        spacer_item_3 = QtWidgets.QSpacerItem(91, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacer_item_3, 1, 2, 1, 1)
        spacer_item_4 = QtWidgets.QSpacerItem(20, 21, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacer_item_4, 2, 1, 1, 1)

        ###################################
        # Auto generated UI code ends here #
        ###################################

        self.setup_signals()
        self.re_translate_ui()

    def re_translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("welcome_dialog", "Welcome"))
        self.create_button.setText(_translate("welcome_dialog", "Create New Project"))
        self.create_button.setShortcut(_translate("welcome_dialog", "Ctrl+N"))
        self.open_button.setText(_translate("welcome_dialog", "Open Existing Project"))
        self.open_button.setShortcut(_translate("welcome_dialog", "Ctrl+O"))

    def setup_signals(self):
        self.create_button.clicked.connect(self.on_create_clicked)
        self.open_button.clicked.connect(self.on_open_clicked)

    def on_create_clicked(self):
        create_project_dialog = CreateProjectDialog(self)
        create_project_dialog.show()

    def on_open_clicked(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, 'Select Project File', '', 'Test Project Files (*.tpr)',
                                                  options=options)
        if filename:
            with open(filename, 'rb') as project_file:
                test_project = pickle.load(project_file, fix_imports=True)

            self.start_main(test_project)
            self.close()

    def create_project(self, project):
        self.start_main(project)
        self.hide()


class ConnectionTypeDialog(QWidget):
    """
    Create Dialog Window to Select Connection Type
    """

    def __init__(self, parent):
        super().__init__(parent=parent, flags=QtCore.Qt.Window)
        self.setWindowModality(QtCore.Qt.WindowModal)

        ##########################################
        # Auto generated UI code starts from here #
        ##########################################

        self.setObjectName("connection_type_window")
        self.setEnabled(True)
        self.resize(339, 302)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_frame = QtWidgets.QFrame(self)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.selector_frame = QtWidgets.QFrame(self.main_frame)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.selector_frame.sizePolicy().hasHeightForWidth())
        self.selector_frame.setSizePolicy(size_policy)
        self.selector_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.selector_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.selector_frame.setObjectName("selector_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.selector_frame)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.connection_type_label = QtWidgets.QLabel(self.selector_frame)
        self.connection_type_label.setObjectName("connection_type_label")
        self.verticalLayout_3.addWidget(self.connection_type_label)
        self.connection_type_list = QtWidgets.QListWidget(self.selector_frame)
        self.connection_type_list.setObjectName("connection_type_list")
        item = QtWidgets.QListWidgetItem()
        self.connection_type_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.connection_type_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.connection_type_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.connection_type_list.addItem(item)
        self.verticalLayout_3.addWidget(self.connection_type_list)
        self.verticalLayout_2.addWidget(self.selector_frame)
        self.button_frame = QtWidgets.QFrame(self.main_frame)
        self.button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_frame.setObjectName("button_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.button_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacer = QtWidgets.QSpacerItem(127, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacer)
        self.next_button = QtWidgets.QPushButton(self.button_frame)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.next_button.sizePolicy().hasHeightForWidth())
        self.next_button.setSizePolicy(size_policy)
        self.next_button.setObjectName("next_button")
        self.horizontalLayout.addWidget(self.next_button)
        self.cancel_button = QtWidgets.QPushButton(self.button_frame)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.verticalLayout_2.addWidget(self.button_frame)
        self.verticalLayout.addWidget(self.main_frame)

        ###################################
        # Auto generated UI code ends here #
        ###################################

        self.re_translate_ui()
        self.set_connector()

    def re_translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("connection_type_window", "Connection Type"))
        self.connection_type_label.setText(_translate("connection_type_window", "Select Connection Type:"))
        __sortingEnabled = self.connection_type_list.isSortingEnabled()
        self.connection_type_list.setSortingEnabled(False)
        item = self.connection_type_list.item(0)
        item.setText(_translate("connection_type_window", "ODBC (Using Existing DSN)"))
        item = self.connection_type_list.item(1)
        item.setText(_translate("connection_type_window", "ODBC"))
        item = self.connection_type_list.item(2)
        item.setText(_translate("connection_type_window", "JDBC"))
        item = self.connection_type_list.item(3)
        item.setText(_translate("connection_type_window", "Native Python"))
        self.connection_type_list.setSortingEnabled(__sortingEnabled)
        self.next_button.setText(_translate("connection_type_window", "Next"))
        self.next_button.setShortcut(_translate("connection_type_window", "Return"))
        self.cancel_button.setText(_translate("connection_type_window", "Cancel"))
        self.cancel_button.setShortcut(_translate("connection_type_window", "Esc"))

    def set_connector(self):
        self.next_button.clicked.connect(self.on_next_clicked)
        self.cancel_button.clicked.connect(self.on_cancel_clicked)

    def on_next_clicked(self):
        connection_type = self.connection_type_list.selectedItems()

        if len(connection_type) > 0:
            connection_methods = {self.connection_type_list.item(0).text(): self.odbc_using_dsn,
                                  self.connection_type_list.item(1).text(): self.odbc,
                                  self.connection_type_list.item(2).text(): self.jdbc,
                                  self.connection_type_list.item(3).text(): self.native_python}

            connection_methods[connection_type[0].text()]()

    def on_cancel_clicked(self):
        self.close()

    def odbc_using_dsn(self):
        odbc_dsn_dialog = OdbcDsnDialog(self.parent())
        odbc_dsn_dialog.show()
        self.close()
        pass

    def odbc(self):
        odbc_dialog = OdbcDialog(self.parent())
        odbc_dialog.show()
        self.close()

    def jdbc(self):
        pass

    def native_python(self):
        pass


class CreateProjectDialog(QWidget):

    def __init__(self, parent):
        super().__init__(parent=parent, flags=QtCore.Qt.Window)

        ##########################################
        # Auto generated UI code starts from here #
        ##########################################

        self.setObjectName("create_project")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.resize(400, 135)
        self.setMaximumSize(QtCore.QSize(400, 135))
        self.create_project_layout = QtWidgets.QVBoxLayout(self)
        self.create_project_layout.setObjectName("create_project_layout")
        self.widget = QtWidgets.QWidget(self)
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
        spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.button_frame_layout.addItem(spacer)
        self.create_project_button = QtWidgets.QPushButton(self.button_frame)
        self.create_project_button.setObjectName("create_project_button")
        self.button_frame_layout.addWidget(self.create_project_button)
        self.cancel_button = QtWidgets.QPushButton(self.button_frame)
        self.cancel_button.setObjectName("cancel_button")
        self.button_frame_layout.addWidget(self.cancel_button)
        self.widget_layout.addWidget(self.button_frame)
        self.create_project_layout.addWidget(self.widget)

        ###################################
        # Auto generated UI code ends here #
        ###################################

        self.re_translate_ui()
        self.setup_signals()

    def re_translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("create_project", "Create New Project"))
        self.project_name_label.setText(_translate("create_project", "Project Name:"))
        self.create_project_button.setText(_translate("create_project", "Create Project"))
        self.create_project_button.setShortcut(_translate("create_project", "Return"))
        self.cancel_button.setText(_translate("create_project", "Cancel"))
        self.cancel_button.setShortcut(_translate("create_project", "Esc"))

    def setup_signals(self):
        self.create_project_button.clicked.connect(self.on_create_project_clicked)
        self.cancel_button.clicked.connect(self.on_cancel_clicked)

    def on_create_project_clicked(self):
        project_name = self.project_name_field.text()

        if project_name == '':
            message = WarningMessageBox(self, 'No Project Name', 'Please Enter Project Name')
            message.show()
        else:
            project = TestProject(project_name)
            self.parent().create_project(project)
            self.close()

    def on_cancel_clicked(self):
        self.close()


class CreateTestCaseDialog(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent, flags=QtCore.Qt.Window)

        ##########################################
        # Auto generated UI code starts from here #
        ##########################################

        self.setObjectName("create_test_case_dialog")
        self.resize(596, 494)
        self.create_test_case_dialog_layout = QtWidgets.QVBoxLayout(self)
        self.create_test_case_dialog_layout.setObjectName("create_test_case_dialog_layout")
        self.main_frame = QtWidgets.QFrame(self)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.main_frame_layout = QtWidgets.QVBoxLayout(self.main_frame)
        self.main_frame_layout.setObjectName("main_frame_layout")
        self.test_case_name_frame = QtWidgets.QFrame(self.main_frame)
        self.test_case_name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.test_case_name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.test_case_name_frame.setObjectName("test_case_name_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.test_case_name_frame)
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.test_case_name_label = QtWidgets.QLabel(self.test_case_name_frame)
        self.test_case_name_label.setObjectName("test_case_name_label")
        self.gridLayout.addWidget(self.test_case_name_label, 0, 0, 1, 1)
        self.test_case_name_line_edit = QtWidgets.QLineEdit(self.test_case_name_frame)
        self.test_case_name_line_edit.setObjectName("test_case_name_line_edit")
        self.gridLayout.addWidget(self.test_case_name_line_edit, 0, 1, 1, 1)
        self.main_frame_layout.addWidget(self.test_case_name_frame)
        self.tabs = QtWidgets.QTabWidget(self.main_frame)
        self.tabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabs.setElideMode(QtCore.Qt.ElideNone)
        self.tabs.setDocumentMode(False)
        self.tabs.setTabBarAutoHide(False)
        self.tabs.setObjectName("tabs")
        self.source_tab = QtWidgets.QWidget()
        self.source_tab.setObjectName("source_tab")
        self.source_tab_layout = QtWidgets.QVBoxLayout(self.source_tab)
        self.source_tab_layout.setObjectName("source_tab_layout")
        self.source_config_frame = QtWidgets.QFrame(self.source_tab)
        self.source_config_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.source_config_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.source_config_frame.setObjectName("source_config_frame")
        self.source_config_frame_layout = QtWidgets.QHBoxLayout(self.source_config_frame)
        self.source_config_frame_layout.setContentsMargins(0, -1, -1, -1)
        self.source_config_frame_layout.setObjectName("source_config_frame_layout")
        self.source_select_connection_label = QtWidgets.QLabel(self.source_config_frame)
        self.source_select_connection_label.setObjectName("source_select_connection_label")
        self.source_config_frame_layout.addWidget(self.source_select_connection_label)
        self.source_connection_combo_box = QtWidgets.QComboBox(self.source_config_frame)
        self.source_connection_combo_box.setObjectName("source_connection_combo_box")
        self.source_config_frame_layout.addWidget(self.source_connection_combo_box)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.source_config_frame_layout.addItem(spacerItem)
        self.source_sort_check_box = QtWidgets.QCheckBox(self.source_config_frame)
        self.source_sort_check_box.setObjectName("source_sort_check_box")
        self.source_config_frame_layout.addWidget(self.source_sort_check_box)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.source_config_frame_layout.addItem(spacerItem1)
        self.source_tab_layout.addWidget(self.source_config_frame)
        self.source_query_label = QtWidgets.QLabel(self.source_tab)
        self.source_query_label.setObjectName("source_query_label")
        self.source_tab_layout.addWidget(self.source_query_label)
        self.source_query_text_edit = QtWidgets.QPlainTextEdit(self.source_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.source_query_text_edit.sizePolicy().hasHeightForWidth())
        self.source_query_text_edit.setSizePolicy(sizePolicy)
        self.source_query_text_edit.setObjectName("source_query_text_edit")
        self.source_tab_layout.addWidget(self.source_query_text_edit)
        self.tabs.addTab(self.source_tab, "")
        self.target_tab = QtWidgets.QWidget()
        self.target_tab.setObjectName("target_tab")
        self.target_tab_layout = QtWidgets.QVBoxLayout(self.target_tab)
        self.target_tab_layout.setObjectName("target_tab_layout")
        self.target_config_frame = QtWidgets.QFrame(self.target_tab)
        self.target_config_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.target_config_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.target_config_frame.setObjectName("target_config_frame")
        self.target_config_frame_layout = QtWidgets.QHBoxLayout(self.target_config_frame)
        self.target_config_frame_layout.setContentsMargins(0, -1, -1, -1)
        self.target_config_frame_layout.setObjectName("target_config_frame_layout")
        self.target_select_connection_label = QtWidgets.QLabel(self.target_config_frame)
        self.target_select_connection_label.setObjectName("target_select_connection_label")
        self.target_config_frame_layout.addWidget(self.target_select_connection_label)
        self.target_connection_combo_box = QtWidgets.QComboBox(self.target_config_frame)
        self.target_connection_combo_box.setObjectName("target_connection_combo_box")
        self.target_config_frame_layout.addWidget(self.target_connection_combo_box)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.target_config_frame_layout.addItem(spacerItem2)
        self.target_sort_check_box = QtWidgets.QCheckBox(self.target_config_frame)
        self.target_sort_check_box.setObjectName("target_sort_check_box")
        self.target_config_frame_layout.addWidget(self.target_sort_check_box)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.target_config_frame_layout.addItem(spacerItem3)
        self.target_tab_layout.addWidget(self.target_config_frame)
        self.target_query_label = QtWidgets.QLabel(self.target_tab)
        self.target_query_label.setObjectName("target_query_label")
        self.target_tab_layout.addWidget(self.target_query_label)
        self.target_query_text_edit = QtWidgets.QPlainTextEdit(self.target_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.target_query_text_edit.sizePolicy().hasHeightForWidth())
        self.target_query_text_edit.setSizePolicy(sizePolicy)
        self.target_query_text_edit.setObjectName("target_query_text_edit")
        self.target_tab_layout.addWidget(self.target_query_text_edit)
        self.tabs.addTab(self.target_tab, "")
        self.main_frame_layout.addWidget(self.tabs)
        self.bottom_frame = QtWidgets.QFrame(self.main_frame)
        self.bottom_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_frame.setObjectName("bottom_frame")
        self.button_frame_layout = QtWidgets.QHBoxLayout(self.bottom_frame)
        self.button_frame_layout.setObjectName("button_frame_layout")
        self.max_mismatch_size_label = QtWidgets.QLabel(self.bottom_frame)
        self.max_mismatch_size_label.setObjectName("max_mismatch_size_label")
        self.button_frame_layout.addWidget(self.max_mismatch_size_label)
        self.max_mismatch_size_line_edit = QtWidgets.QLineEdit(self.bottom_frame)
        self.max_mismatch_size_line_edit.setObjectName("max_mismatch_size_line_edit")
        self.button_frame_layout.addWidget(self.max_mismatch_size_line_edit)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.button_frame_layout.addItem(spacerItem4)
        self.save_button = QtWidgets.QPushButton(self.bottom_frame)
        self.save_button.setObjectName("save_button")
        self.button_frame_layout.addWidget(self.save_button)
        self.cancel_button = QtWidgets.QPushButton(self.bottom_frame)
        self.cancel_button.setObjectName("cancel_button")
        self.button_frame_layout.addWidget(self.cancel_button)
        self.main_frame_layout.addWidget(self.bottom_frame)
        self.create_test_case_dialog_layout.addWidget(self.main_frame)

        ###################################
        # Auto generated UI code ends here #
        ###################################

        self.re_translate_ui()
        self.tabs.setCurrentIndex(0)
        self.load_connections()
        self.setup_signals()

    def re_translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("create_test_case_dialog", "Create New Test Case"))
        self.test_case_name_label.setText(_translate("create_test_case_dialog", "Test Case Name"))
        self.source_select_connection_label.setText(_translate("create_test_case_dialog", "Select Connection:"))
        self.source_sort_check_box.setText(_translate("create_test_case_dialog", "Sort Result"))
        self.source_query_label.setText(_translate("create_test_case_dialog", "Query:"))
        self.tabs.setTabText(self.tabs.indexOf(self.source_tab), _translate("create_test_case_dialog", "Source"))
        self.target_select_connection_label.setText(_translate("create_test_case_dialog", "Select Connection:"))
        self.target_sort_check_box.setText(_translate("create_test_case_dialog", "Sort Result"))
        self.target_query_label.setText(_translate("create_test_case_dialog", "Query:"))
        self.tabs.setTabText(self.tabs.indexOf(self.target_tab), _translate("create_test_case_dialog", "Target"))
        self.max_mismatch_size_label.setText(_translate("create_test_case_dialog", "Max Mismatch Size:"))
        self.save_button.setText(_translate("create_test_case_dialog", "Save"))
        self.cancel_button.setText(_translate("create_test_case_dialog", "Cancel"))

    def load_connections(self):
        project: TestProject = self.parent().project

        for connection in project.connections:
            self.source_connection_combo_box.addItem(connection.name, connection)
            self.target_connection_combo_box.addItem(connection.name, connection)

        action = QAction('Create New Connection')
        self.source_connection_combo_box.addAction(action)
        self.target_connection_combo_box.addAction(action)

    def setup_signals(self):
        self.save_button.clicked.connect(self.on_save_button_clicked)
        self.cancel_button.clicked.connect(self.on_cancel_button_clicked)

    def on_save_button_clicked(self):
        test_case_name = self.test_case_name_line_edit.text()
        source_connection = self.source_connection_combo_box.currentData()
        source_query = self.source_query_text_edit.toPlainText()
        sort_source = self.source_sort_check_box.isChecked()
        target_connection = self.target_connection_combo_box.currentData()
        target_query = self.target_query_text_edit.toPlainText()
        sort_target = self.target_sort_check_box.isChecked()
        max_mismatch_size = int(self.max_mismatch_size_line_edit.text())

        test_case = TestCase(name=test_case_name, source_connection=source_connection, source_query=source_query,
                             sort_source=sort_source, target_connection=target_connection, target_query=target_query,
                             sort_target=sort_target, max_mismatch_size=max_mismatch_size)
        self.parent().add_test_case(test_case)
        self.close()

    def on_cancel_button_clicked(self):
        self.close()


class OdbcDsnDialog(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent, flags=QtCore.Qt.Window)
        self.connection = None

        ##########################################
        # Auto generated UI code starts from here #
        ##########################################

        self.setObjectName("odbc_dsn_dialog")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.resize(400, 250)
        self.setMaximumSize(QtCore.QSize(400, 250))
        self.vertical_layout = QtWidgets.QVBoxLayout(self)
        self.vertical_layout.setObjectName("vertical_layout")
        self.main_frame = QtWidgets.QFrame(self)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.main_frame_layout = QtWidgets.QVBoxLayout(self.main_frame)
        self.main_frame_layout.setObjectName("main_frame_layout")
        self.form_frame = QtWidgets.QFrame(self.main_frame)
        self.form_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.form_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.form_frame.setObjectName("form_frame")
        self.formLayout = QtWidgets.QFormLayout(self.form_frame)
        self.formLayout.setObjectName("formLayout")
        self.connection_name_label = QtWidgets.QLabel(self.form_frame)
        self.connection_name_label.setObjectName("connection_name_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.connection_name_label)
        self.connection_name_line_edit = QtWidgets.QLineEdit(self.form_frame)
        self.connection_name_line_edit.setObjectName("connection_name_line_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.connection_name_line_edit)
        self.dsn_label = QtWidgets.QLabel(self.form_frame)
        self.dsn_label.setObjectName("dsn_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.dsn_label)
        self.dsn_combo_box = QtWidgets.QComboBox(self.form_frame)
        self.dsn_combo_box.setObjectName("dsn_combo_box")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dsn_combo_box)
        self.windows_auth_check_box = QtWidgets.QCheckBox(self.form_frame)
        self.windows_auth_check_box.setObjectName("windows_auth_check_box")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.windows_auth_check_box)
        self.user_name_label = QtWidgets.QLabel(self.form_frame)
        self.user_name_label.setObjectName("user_name_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.user_name_label)
        self.username_line_edit = QtWidgets.QLineEdit(self.form_frame)
        self.username_line_edit.setObjectName("username_line_edit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.username_line_edit)
        self.password_label = QtWidgets.QLabel(self.form_frame)
        self.password_label.setObjectName("password_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.password_label)
        self.password_line_edit = QtWidgets.QLineEdit(self.form_frame)
        self.password_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line_edit.setObjectName("password_line_edit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.password_line_edit)
        self.main_frame_layout.addWidget(self.form_frame)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.main_frame_layout.addItem(spacerItem)
        self.button_frame = QtWidgets.QFrame(self.main_frame)
        self.button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_frame.setObjectName("button_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.button_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.connect_button = QtWidgets.QPushButton(self.button_frame)
        self.connect_button.setObjectName("connect_button")
        self.horizontalLayout.addWidget(self.connect_button)
        self.save_button = QtWidgets.QPushButton(self.button_frame)
        self.save_button.setEnabled(False)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout.addWidget(self.save_button)
        self.cancel_button = QtWidgets.QPushButton(self.button_frame)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.main_frame_layout.addWidget(self.button_frame)
        self.vertical_layout.addWidget(self.main_frame)

        ###################################
        # Auto generated UI code ends here #
        ###################################

        self.re_translate_ui()
        self.load_dsn()
        self.setup_signals()

    def re_translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("odbc_dsn_dialog", "ODBC DSN Connection"))
        self.connection_name_label.setText(_translate("odbc_dsn_dialog", "Connection Name:"))
        self.dsn_label.setText(_translate("odbc_dsn_dialog", "Data Source Name: "))
        self.windows_auth_check_box.setText(_translate("odbc_dsn_dialog", "Use windows authentication"))
        self.user_name_label.setText(_translate("odbc_dsn_dialog", "Username:"))
        self.password_label.setText(_translate("odbc_dsn_dialog", "Password:"))
        self.connect_button.setText(_translate("odbc_dsn_dialog", "Connect"))
        self.connect_button.setShortcut(_translate("odbc_dsn_dialog", "Return"))
        self.save_button.setText(_translate("odbc_dsn_dialog", "Save"))
        self.save_button.setShortcut(_translate("odbc_dsn_dialog", "Ctrl+S"))
        self.cancel_button.setText(_translate("odbc_dsn_dialog", "Cancel"))
        self.cancel_button.setShortcut(_translate("odbc_dsn_dialog", "Esc"))

    def load_dsn(self):
        for dsn in pyodbc.dataSources():
            self.dsn_combo_box.addItem(dsn)

    def setup_signals(self):
        self.windows_auth_check_box.toggled.connect(self.on_windows_auth_toggled)
        self.connect_button.clicked.connect(self.on_connect_clicked)
        self.cancel_button.clicked.connect(self.on_cancel_clicked)
        self.save_button.clicked.connect(self.on_save_clicked)

    def on_windows_auth_toggled(self):
        if self.windows_auth_check_box.isChecked():
            self.username_line_edit.setDisabled(True)
            self.password_line_edit.setDisabled(True)
        else:
            self.username_line_edit.setDisabled(False)
            self.password_line_edit.setDisabled(False)

    def on_connect_clicked(self):

        connection_name = self.connection_name_line_edit.text()
        dsn = self.dsn_combo_box.currentText()
        trusted_connection = self.windows_auth_check_box.isChecked()
        
        username = ''
        password = ''
        if not trusted_connection:
            username = self.username_line_edit.text()
            password = self.password_line_edit.text()
        user_details = UserDetails(username, password)
        
        self.connection = OdbcDsnConnection(connection_name, dsn, trusted_connection)
        self.connection.user_details = user_details
        try:
            self.connection.connect()
        except OperationalError as e:
            self.save_button.setEnabled(False)
            message = ErrorMessageBox(self, 'Connection Failed', 'Connection Failed for Data Source {}'.format(dsn),
                                      e.args[1])
            message.show()
        except Exception as e:
            self.save_button.setEnabled(False)
            message = ErrorMessageBox(self, 'Connection Failed', 'Connection Failed for Data Source {}'.format(dsn),
                                      str(e))
            message.show()
        else:
            self.save_button.setEnabled(True)
            message = InformationMessageBox(self, 'Connection Successful',
                                            'Connection Successful for Data Source {}'.format(dsn))
            message.show()

    def on_cancel_clicked(self):
        self.close()

    def on_save_clicked(self):
        self.parent().add_connection(self.connection)
        self.close()


class OdbcDialog(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent, flags=QtCore.Qt.Window)
        self.connection = None

        ###########################################
        # Auto generated UI code starts from here #
        ###########################################

        self.setObjectName("odbc_dialog")
        self.resize(420, 329)
        self.odbc_dialog_layout = QtWidgets.QVBoxLayout(self)
        self.odbc_dialog_layout.setObjectName("odbc_dialog_layout")
        self.main_frame = QtWidgets.QFrame(self)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.main_frame_layout = QtWidgets.QVBoxLayout(self.main_frame)
        self.main_frame_layout.setObjectName("main_frame_layout")
        self.form_frame = QtWidgets.QFrame(self.main_frame)
        self.form_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.form_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.form_frame.setObjectName("form_frame")
        self.formLayout = QtWidgets.QFormLayout(self.form_frame)
        self.formLayout.setObjectName("formLayout")
        self.connection_name_label = QtWidgets.QLabel(self.form_frame)
        self.connection_name_label.setObjectName("connection_name_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.connection_name_label)
        self.connection_name_line_edit = QtWidgets.QLineEdit(self.form_frame)
        self.connection_name_line_edit.setObjectName("connection_name_line_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.connection_name_line_edit)
        self.driver_label = QtWidgets.QLabel(self.form_frame)
        self.driver_label.setObjectName("driver_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.driver_label)
        self.driver_combo_box = QtWidgets.QComboBox(self.form_frame)
        self.driver_combo_box.setObjectName("driver_combo_box")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.driver_combo_box)
        self.server_label = QtWidgets.QLabel(self.form_frame)
        self.server_label.setObjectName("server_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.server_label)
        self.server_line_edit = QtWidgets.QLineEdit(self.form_frame)
        self.server_line_edit.setObjectName("server_line_edit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.server_line_edit)
        self.port_label = QtWidgets.QLabel(self.form_frame)
        self.port_label.setObjectName("port_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.port_label)
        self.port_line_edit = QtWidgets.QLineEdit(self.form_frame)
        self.port_line_edit.setObjectName("port_line_edit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.port_line_edit)
        self.database_label = QtWidgets.QLabel(self.form_frame)
        self.database_label.setObjectName("database_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.database_label)
        self.database_line_edit = QtWidgets.QLineEdit(self.form_frame)
        self.database_line_edit.setObjectName("database_line_edit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.database_line_edit)
        self.windows_auth_check_box = QtWidgets.QCheckBox(self.form_frame)
        self.windows_auth_check_box.setObjectName("windows_auth_check_box")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.windows_auth_check_box)
        self.username_label = QtWidgets.QLabel(self.form_frame)
        self.username_label.setObjectName("username_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.username_label)
        self.username_line_edit = QtWidgets.QLineEdit(self.form_frame)
        self.username_line_edit.setObjectName("username_line_edit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.username_line_edit)
        self.password_label = QtWidgets.QLabel(self.form_frame)
        self.password_label.setObjectName("password_label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.password_label)
        self.password_line_edit = QtWidgets.QLineEdit(self.form_frame)
        self.password_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line_edit.setObjectName("password_line_edit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.password_line_edit)
        self.main_frame_layout.addWidget(self.form_frame)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.main_frame_layout.addItem(spacerItem)
        self.button_frame = QtWidgets.QFrame(self.main_frame)
        self.button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_frame.setObjectName("button_frame")
        self.button_frame_layout = QtWidgets.QHBoxLayout(self.button_frame)
        self.button_frame_layout.setObjectName("button_frame_layout")
        spacerItem1 = QtWidgets.QSpacerItem(116, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.button_frame_layout.addItem(spacerItem1)
        self.connect_button = QtWidgets.QPushButton(self.button_frame)
        self.connect_button.setObjectName("connect_button")
        self.button_frame_layout.addWidget(self.connect_button)
        self.save_button = QtWidgets.QPushButton(self.button_frame)
        self.save_button.setEnabled(False)
        self.save_button.setObjectName("save_button")
        self.button_frame_layout.addWidget(self.save_button)
        self.cancel_button = QtWidgets.QPushButton(self.button_frame)
        self.cancel_button.setObjectName("cancel_button")
        self.button_frame_layout.addWidget(self.cancel_button)
        self.main_frame_layout.addWidget(self.button_frame)
        self.odbc_dialog_layout.addWidget(self.main_frame)

        ####################################
        # Auto generated UI code ends here #
        ####################################

        self.re_translate_ui()
        self.setup_signals()
        self.load_odbc_drivers()

    def re_translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("odbc_dialog", "ODBC Connection"))
        self.driver_label.setText(_translate("odbc_dialog", "Driver:"))
        self.server_label.setText(_translate("odbc_dialog", "Server:"))
        self.port_label.setText(_translate("odbc_dialog", "Port:"))
        self.database_label.setText(_translate("odbc_dialog", "Database:"))
        self.username_label.setText(_translate("odbc_dialog", "Username:"))
        self.password_label.setText(_translate("odbc_dialog", "Password:"))
        self.connection_name_label.setText(_translate("odbc_dialog", "Connection Name:"))
        self.windows_auth_check_box.setText(_translate("odbc_dialog", "Use Windows authentication"))
        self.connect_button.setText(_translate("odbc_dialog", "Connect"))
        self.connect_button.setShortcut(_translate("odbc_dialog", "Return"))
        self.save_button.setText(_translate("odbc_dialog", "Save"))
        self.save_button.setShortcut(_translate("odbc_dialog", "Ctrl+S"))
        self.cancel_button.setText(_translate("odbc_dialog", "Cancel"))
        self.cancel_button.setShortcut(_translate("odbc_dialog", "Esc"))

    def setup_signals(self):
        self.windows_auth_check_box.toggled.connect(self.on_windows_auth_toggled)
        self.connect_button.clicked.connect(self.on_connect_clicked)
        self.cancel_button.clicked.connect(self.on_cancel_clicked)
        self.save_button.clicked.connect(self.on_save_clicked)

    def load_odbc_drivers(self):
        for driver in pyodbc.drivers():
            self.driver_combo_box.addItem(driver)

    def on_windows_auth_toggled(self):
        if self.windows_auth_check_box.isChecked():
            self.username_line_edit.setDisabled(True)
            self.password_line_edit.setDisabled(True)
        else:
            self.username_line_edit.setDisabled(False)
            self.password_line_edit.setDisabled(False)

    def on_connect_clicked(self):
        connection_name = self.connection_name_line_edit.text()
        driver = self.driver_combo_box.currentText()
        server = self.server_line_edit.text()
        port = self.port_line_edit.text()
        database = self.database_line_edit.text()
        trusted_connection = self.windows_auth_check_box.isChecked()
        
        username = ''
        password = ''
        if not trusted_connection:
            username = self.username_line_edit.text()
            password = self.password_line_edit.text()
        user_details = UserDetails(username, password)
        
        self.connection = OdbcConnection(connection_name, driver, server, port, database, trusted_connection)
        self.connection.user_details = user_details
        try:
            self.connection.connect()
        except OperationalError as e:
            self.save_button.setEnabled(False)
            message = ErrorMessageBox(self, 'Connection Failed', 'Connection Failed for Server {}'.format(server),
                                      e.args[1])
            message.show()
        except Exception as e:
            self.save_button.setEnabled(False)
            message = ErrorMessageBox(self, 'Connection Failed', 'Connection Failed for Server {}'.format(server),
                                      str(e))
            message.show()
        else:
            self.save_button.setEnabled(True)
            message = InformationMessageBox(self, 'Connection Successful',
                                            'Connection Successful for Server {}'.format(server))
            message.show()

    def on_cancel_clicked(self):
        self.close()

    def on_save_clicked(self):
        self.parent().add_connection(self.connection)
        self.close()
