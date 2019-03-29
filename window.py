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

from PyQt5.QtWidgets import QMenu, QTreeWidgetItem
from PyQt5 import QtCore, QtWidgets

from dialog import ConnectionTypeDialog, CreateProjectDialog
from qt_items import TreeWidgetItem
from testproject import TestProject


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, project: TestProject):
        super().__init__()
        self.project = project

        ############################
        # UI code starts from here #
        ############################

        self.setObjectName("main_window")
        self.resize(755, 544)
        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName("central_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.central_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.test_project_tree = QtWidgets.QTreeWidget(self.central_widget)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.test_project_tree.sizePolicy().hasHeightForWidth())
        self.test_project_tree.setSizePolicy(size_policy)
        self.test_project_tree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.test_project_tree.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.test_project_tree.setAnimated(True)
        self.test_project_tree.setObjectName("test_project_tree")
        self.test_project_tree.headerItem().setText(0, "1")
        self.horizontalLayout_2.addWidget(self.test_project_tree)
        self.frame = QtWidgets.QFrame(self.central_widget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.vertical_layout = QtWidgets.QVBoxLayout(self.frame)
        self.vertical_layout.setContentsMargins(9, 0, 0, 0)
        self.vertical_layout.setObjectName("vertical_layout")
        self.test_results_label = QtWidgets.QLabel(self.frame)
        self.test_results_label.setObjectName("test_results_label")
        self.vertical_layout.addWidget(self.test_results_label)
        self.result_table = QtWidgets.QTableWidget(self.frame)
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
        self.vertical_layout.addWidget(self.result_table)
        self.progress_bar = QtWidgets.QProgressBar(self.frame)
        self.progress_bar.setProperty("value", 24)
        self.progress_bar.setObjectName("progress_bar")
        self.vertical_layout.addWidget(self.progress_bar)
        self.progress_label = QtWidgets.QLabel(self.frame)
        self.progress_label.setObjectName("progress_label")
        self.vertical_layout.addWidget(self.progress_label)
        self.horizontalLayout_2.addWidget(self.frame)
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

        ##########################
        # UI code ends from here #
        ##########################

        self.setup_signals()
        self.re_translate_ui()
        self.load_project()

    def re_translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("main_window", "MainWindow"))
        self.test_results_label.setText(_translate("main_window", "Test Results"))
        self.result_table.setSortingEnabled(True)
        item = self.result_table.verticalHeaderItem(0)
        item.setText(_translate("main_window", "1"))
        item = self.result_table.verticalHeaderItem(1)
        item.setText(_translate("main_window", "2"))
        item = self.result_table.verticalHeaderItem(2)
        item.setText(_translate("main_window", "3"))
        item = self.result_table.horizontalHeaderItem(0)
        item.setText(_translate("main_window", "ID"))
        item = self.result_table.horizontalHeaderItem(1)
        item.setText(_translate("main_window", "Test Case Name"))
        item = self.result_table.horizontalHeaderItem(2)
        item.setText(_translate("main_window", "Execution Time Stamp"))
        item = self.result_table.horizontalHeaderItem(3)
        item.setText(_translate("main_window", "Status"))
        self.progress_label.setText(_translate("main_window", "TextLabel"))
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
        self.new_test_project_action.triggered.connect(self.on_new_test_project)
        self.new_connection_action.triggered.connect(self.on_new_connection)
        self.exit_action.triggered.connect(self.on_exit)

        self.test_project_tree.customContextMenuRequested.connect(self.on_tree_right_click)

    def load_project(self):
        self.test_project_tree.headerItem().setText(0, self.project.name)
        
        test_cases_item = TreeWidgetItem(self.project.test_cases, name='Test Cases')
        for test_case in self.project.test_cases:
            test_case_item = TreeWidgetItem(test_case)
            test_cases_item.addChild(test_case_item)
        
        connections_item = TreeWidgetItem(self.project.connections, name='Connections')
        for connection in self.project.connections:
            connection_item = TreeWidgetItem(connection)
            connections_item.addChild(connection_item)
        
        self.test_project_tree.addTopLevelItems((test_cases_item, connections_item))

    def on_new_test_project(self):
        create_project_dialog = CreateProjectDialog(self)
        create_project_dialog.show()

    def on_new_connection(self):
        dialog = ConnectionTypeDialog(self)
        dialog.show()

    def on_new_test_case(self):
        pass

    def on_tree_right_click(self, position):
        menu = QMenu()
        new_menu = QMenu('New')
        menu.addAction(new_menu.menuAction())
        new_menu.addAction(self.new_test_case_action)
        new_menu.addAction(self.new_connection_action)
        menu.exec_(self.test_project_tree.viewport().mapToGlobal(position))

    @staticmethod
    def on_exit():
        exit(0)

    def on_save(self):
        pass

    def on_save_as(self):
        pass

    def delete_tree_items(self, *items: QTreeWidgetItem):
        root = self.test_project_tree.invisibleRootItem()
        for item in items:
            (item.parent() or root).removeChild(item)

    def odbc(self):
        pass
