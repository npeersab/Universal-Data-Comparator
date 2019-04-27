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
from sys import exit

from PyQt5.QtWidgets import QMenu, QAction
from PyQt5 import QtCore, QtWidgets

from connection import Connection
from dialog import ConnectionTypeDialog, TestCaseDialog
from qt_items import TreeWidgetItem
from test import TestProject, TestCase


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, project: TestProject):
        super().__init__()
        self.project = project

        ##########################################
        # Auto generated UI code starts from here #
        ##########################################

        self.setObjectName("main_window")
        self.resize(755, 544)
        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName("central_widget")
        self.central_widget_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.central_widget_layout.setObjectName("central_widget_layout")
        self.splitter = QtWidgets.QSplitter(self.central_widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(5)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.test_project_tree_frame = QtWidgets.QFrame(self.splitter)
        self.test_project_tree_frame.setBaseSize(QtCore.QSize(0, 0))
        self.test_project_tree_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.test_project_tree_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.test_project_tree_frame.setObjectName("test_project_tree_frame")
        self.test_project_tree_frame_layout = QtWidgets.QVBoxLayout(self.test_project_tree_frame)
        self.test_project_tree_frame_layout.setObjectName("test_project_tree_frame_layout")
        self.test_project_tree = QtWidgets.QTreeWidget(self.test_project_tree_frame)
        self.test_project_tree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.test_project_tree.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.test_project_tree.setAnimated(True)
        self.test_project_tree.setObjectName("test_project_tree")
        self.test_project_tree.headerItem().setText(0, "1")
        self.test_project_tree_frame_layout.addWidget(self.test_project_tree)
        self.result_frame = QtWidgets.QFrame(self.splitter)
        self.result_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.result_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.result_frame.setObjectName("result_frame")
        self.result_frame_layout = QtWidgets.QVBoxLayout(self.result_frame)
        self.result_frame_layout.setObjectName("result_frame_layout")
        self.test_results_label = QtWidgets.QLabel(self.result_frame)
        self.test_results_label.setObjectName("test_results_label")
        self.result_frame_layout.addWidget(self.test_results_label)
        self.result_table = QtWidgets.QTableWidget(self.result_frame)
        self.result_table.setAutoFillBackground(False)
        self.result_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.result_table.setDragDropOverwriteMode(False)
        self.result_table.setAlternatingRowColors(True)
        self.result_table.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.result_table.setWordWrap(False)
        self.result_table.setObjectName("result_table")
        self.result_table.setColumnCount(4)
        self.result_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(3, item)
        self.result_table.horizontalHeader().setVisible(True)
        self.result_table.horizontalHeader().setHighlightSections(True)
        self.result_table.horizontalHeader().setSortIndicatorShown(False)
        self.result_table.verticalHeader().setVisible(True)
        self.result_frame_layout.addWidget(self.result_table)
        self.progress_bar = QtWidgets.QProgressBar(self.result_frame)
        self.progress_bar.setProperty("value", 24)
        self.progress_bar.setObjectName("progress_bar")
        self.result_frame_layout.addWidget(self.progress_bar)
        self.progress_label = QtWidgets.QLabel(self.result_frame)
        self.progress_label.setObjectName("progress_label")
        self.result_frame_layout.addWidget(self.progress_label)
        self.central_widget_layout.addWidget(self.splitter)
        self.setCentralWidget(self.central_widget)
        self.menu_bar = QtWidgets.QMenuBar(self)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 755, 21))
        self.menu_bar.setObjectName("menu_bar")
        self.file_menu = QtWidgets.QMenu(self.menu_bar)
        self.file_menu.setObjectName("file_menu")
        self.new_menu = QtWidgets.QMenu(self.file_menu)
        self.new_menu.setObjectName("new_menu")
        self.setMenuBar(self.menu_bar)
        self.status_bar = QtWidgets.QStatusBar(self)
        self.status_bar.setObjectName("status_bar")
        self.setStatusBar(self.status_bar)
        self.new_test_project_action = QtWidgets.QAction(self)
        self.new_test_project_action.setObjectName("new_test_project_action")
        self.new_test_case_action = QtWidgets.QAction(self)
        self.new_test_case_action.setObjectName("new_test_case_action")
        self.new_connection_action = QtWidgets.QAction(self)
        self.new_connection_action.setObjectName("new_connection_action")
        self.save_action = QtWidgets.QAction(self)
        self.save_action.setObjectName("save_action")
        self.save_as_action = QtWidgets.QAction(self)
        self.save_as_action.setObjectName("save_as_action")
        self.exit_action = QtWidgets.QAction(self)
        self.exit_action.setObjectName("exit_action")
        self.new_menu.addAction(self.new_test_project_action)
        self.new_menu.addSeparator()
        self.new_menu.addAction(self.new_test_case_action)
        self.new_menu.addAction(self.new_connection_action)
        self.file_menu.addAction(self.new_menu.menuAction())
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.save_action)
        self.file_menu.addAction(self.save_as_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.exit_action)
        self.menu_bar.addAction(self.file_menu.menuAction())

        ###################################
        # Auto generated UI code ends here #
        ###################################

        self.splitter.setSizes([250, 600])
        self.splitter.setStretchFactor(0, 0)
        self.splitter.setStretchFactor(1, 1)
        self.test_cases_item = TreeWidgetItem(name='Test Cases', value=self.project.test_cases)
        self.connections_item = TreeWidgetItem(name='Connections', value=self.project.connections)

        self.setup_signals()
        self.re_translate_ui()
        self.load_project()

    def add_connection(self, connection: Connection):
        """
        Add connection to Test Project and Test Project Tree

        :param connection: Connection which has to be added in Test Project
        """

        # Add the Connection to Test Project
        self.project.add_connection(connection)

        # Create TreeWidgetItem for Connection and add to Test Project Tree
        connection_item = TreeWidgetItem(name=connection.name, value=connection)
        self.connections_item.addChild(connection_item)

    def add_test_case(self, test_case: TestCase):
        """
        Add Test Case to Test Project and Test Project Tree

        :param test_case: TestCase which has to be added in Test Project
        """

        # Add the Test Case to Test Project
        self.project.add_test_case(test_case)

        # Create TreeWidgetItem for Test Case and add to Test Project Tree
        test_case_item = TreeWidgetItem(name=test_case.name, value=test_case)
        self.test_cases_item.addChild(test_case_item)

    def load_project(self):
        """
        Load all Test Cases and Connection from Test Project into Test Project Tree
        """

        # Set Project name to Tree Header
        self.test_project_tree.headerItem().setText(0, self.project.name)

        # Add all Test Cases to the Test Cases Item
        for test_case in self.project.test_cases:
            test_case_item = TreeWidgetItem(name=test_case.name, value=test_case)
            self.test_cases_item.addChild(test_case_item)

        # Add all Connections to the Connections Item
        for connection in self.project.connections:
            connection_item = TreeWidgetItem(name=connection.name, value=connection)
            self.connections_item.addChild(connection_item)

        # Add Test Cases and Connections item to Test Project Tree
        self.test_project_tree.addTopLevelItems((self.test_cases_item, self.connections_item))

    def delete_tree_items(self, *items: TreeWidgetItem):
        """
        Delete the Tree Widget items from The Test Project Tree

        :param items: TreeWidgetItem which has to be deleted
        """

        root = self.test_project_tree.invisibleRootItem()
        for item in items:
            (item.parent() or root).removeChild(item)

    def on_edit_triggered(self):
        """
        On clicking edit menu action
        """
        item = self.test_project_tree.selectedItems()[0]

        if isinstance(item.value, TestCase):
            test_case_dialog = TestCaseDialog(self, item.value)
            test_case_dialog.show()

    def on_execute_triggered(self):
        """
        On clicking edit menu action
        """

        items = self.test_project_tree.selectedItems()
        for item in items:
            if isinstance(item.value, TestCase):
                test_result = item.value.execute()
                test_result.save_results()

    @staticmethod
    def on_exit():
        exit()

    def on_new_connection_triggered(self):
        dialog = ConnectionTypeDialog(self)
        dialog.show()

    def on_new_test_case_triggered(self):
        test_case_dialog = TestCaseDialog(self)
        test_case_dialog.show()

    def on_new_test_project_triggered(self):
        pass

    def on_save_as_triggered(self):
        pass

    def on_save_triggered(self):
        with open('{}.tpr'.format(self.project.name), 'wb') as out:
            for connection in self.project.connections:
                connection.close_connection()
            pickle.dump(self.project, out, fix_imports=True, protocol=pickle.HIGHEST_PROTOCOL)
        pass

    def on_tree_right_click(self, position):
        menu = QMenu()
        selected_items = self.test_project_tree.selectedItems()

        new_menu = QMenu('New')
        new_menu.addAction(self.new_test_case_action)
        new_menu.addAction(self.new_connection_action)
        menu.addAction(new_menu.menuAction())

        for item in selected_items:
            if not isinstance(item.value, TestCase):
                break
        else:
            execute_action = QAction('Execute')
            execute_action.triggered.connect(self.on_execute_triggered)
            menu.addAction(execute_action)

        if len(selected_items) == 1:
            edit_action = QAction('Edit')
            edit_action.triggered.connect(self.on_edit_triggered)
            menu.addAction(edit_action)

        menu.exec_(self.test_project_tree.viewport().mapToGlobal(position))

    def re_translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("main_window", "MainWindow"))
        self.test_results_label.setText(_translate("main_window", "Test Results"))
        self.result_table.setSortingEnabled(True)
        item = self.result_table.horizontalHeaderItem(0)
        item.setText(_translate("main_window", "ID"))
        item = self.result_table.horizontalHeaderItem(1)
        item.setText(_translate("main_window", "Test Case Name"))
        item = self.result_table.horizontalHeaderItem(2)
        item.setText(_translate("main_window", "Execution Time Stamp"))
        item = self.result_table.horizontalHeaderItem(3)
        item.setText(_translate("main_window", "Status"))
        self.progress_label.setText(_translate("main_window", "Executing Test Case 2"))
        self.file_menu.setTitle(_translate("main_window", "File"))
        self.new_menu.setTitle(_translate("main_window", "New"))
        self.new_test_project_action.setText(_translate("main_window", "Test Project"))
        self.new_test_project_action.setShortcut(_translate("main_window", "Ctrl+N"))
        self.new_test_case_action.setText(_translate("main_window", "Test Case"))
        self.new_test_case_action.setShortcut(_translate("main_window", "Ctrl+Shift+T"))
        self.new_connection_action.setText(_translate("main_window", "Connection"))
        self.new_connection_action.setShortcut(_translate("main_window", "Ctrl+Shift+C"))
        self.save_action.setText(_translate("main_window", "Save"))
        self.save_action.setShortcut(_translate("main_window", "Ctrl+S"))
        self.save_as_action.setText(_translate("main_window", "Save As.."))
        self.save_as_action.setShortcut(_translate("main_window", "Ctrl+Shift+S"))
        self.exit_action.setText(_translate("main_window", "Exit"))
        self.exit_action.setShortcut(_translate("main_window", "Ctrl+Q"))

    def setup_signals(self):
        """
        Connect the signals to slots
        """

        self.exit_action.triggered.connect(self.on_exit)
        self.new_connection_action.triggered.connect(self.on_new_connection_triggered)
        self.new_test_case_action.triggered.connect(self.on_new_test_case_triggered)
        self.new_test_project_action.triggered.connect(self.on_new_test_project_triggered)
        self.save_action.triggered.connect(self.on_save_triggered)
        self.test_project_tree.customContextMenuRequested.connect(self.on_tree_right_click)
