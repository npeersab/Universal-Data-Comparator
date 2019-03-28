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

import testproject

from PyQt5 import QtCore, QtWidgets
from dialog import ConnectionTypeDialog, CreateProjectDialog


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        ############################
        # UI code starts from here #
        ############################

        self.setObjectName('main_window')
        self.resize(755, 642)
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
        self.test_project_tree.setObjectName("test_project_tree")
        self.test_project_tree.headerItem().setText(0, 'Test Projects')
        self.horizontalLayout_2.addWidget(self.test_project_tree)
        self.frame = QtWidgets.QFrame(self.central_widget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(9, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.test_results_label = QtWidgets.QLabel(self.frame)
        self.test_results_label.setObjectName("test_results_label")
        self.verticalLayout.addWidget(self.test_results_label)
        self.result_table = QtWidgets.QTableWidget(self.frame)
        self.result_table.setAutoFillBackground(False)
        self.result_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.result_table.setDragDropOverwriteMode(False)
        self.result_table.setAlternatingRowColors(True)
        self.result_table.setWordWrap(False)
        self.result_table.setObjectName("result_table")
        self.result_table.setColumnCount(4)
        self.result_table.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setItem(1, 0, item)
        self.result_table.horizontalHeader().setVisible(True)
        self.result_table.horizontalHeader().setCascadingSectionResizes(True)
        self.result_table.horizontalHeader().setHighlightSections(True)
        self.result_table.horizontalHeader().setSortIndicatorShown(False)
        self.result_table.verticalHeader().setVisible(True)
        self.verticalLayout.addWidget(self.result_table)
        self.progress_bar = QtWidgets.QProgressBar(self.frame)
        self.progress_bar.setProperty("value", 24)
        self.progress_bar.setObjectName("progress_bar")
        self.verticalLayout.addWidget(self.progress_bar)
        self.progress_label = QtWidgets.QLabel(self.frame)
        self.progress_label.setObjectName("progress_label")
        self.verticalLayout.addWidget(self.progress_label)
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
        self.new_test_case_action = QtWidgets.QAction(self)
        self.new_test_case_action.setObjectName("new_test_case_action")
        self.new_connection_action = QtWidgets.QAction(self)
        self.new_connection_action.setObjectName("new_connection_action")
        self.new_test_project_action = QtWidgets.QAction(self)
        self.new_test_project_action.setObjectName("new_test_project_action")
        self.new_menu.addAction(self.new_test_project_action)
        self.new_menu.addAction(self.new_test_case_action)
        self.new_menu.addAction(self.new_connection_action)
        self.file_menu.addAction(self.new_menu.menuAction())
        self.menu_bar.addAction(self.file_menu.menuAction())

        ##########################
        # UI code ends from here #
        ##########################

        self.setup_signals()
        self.re_translate_ui()

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
        __sortingEnabled = self.result_table.isSortingEnabled()
        self.result_table.setSortingEnabled(False)
        self.result_table.setSortingEnabled(__sortingEnabled)
        self.progress_label.setText(_translate("main_window", "TextLabel"))
        self.file_menu.setTitle(_translate("main_window", "File"))
        self.new_menu.setTitle(_translate("main_window", "New"))
        self.new_test_case_action.setText(_translate("main_window", "Test Case"))
        self.new_connection_action.setText(_translate("main_window", "Connection"))
        self.new_test_project_action.setText(_translate("main_window", "Test Project"))

    def setup_signals(self):
        self.new_test_project_action.triggered.connect(self.on_new_test_project)
        self.new_connection_action.triggered.connect(self.on_new_connection)

    def on_new_test_project(self):
        create_project_dialog = CreateProjectDialog(self)
        create_project_dialog.show()

    def add_project(self, project: testproject.TestProject):
        item = QtWidgets.QTreeWidgetItem([project.name])
        item.attached_value = project
        item.addChild(QtWidgets.QTreeWidgetItem(['Test Cases']))
        item.addChild(QtWidgets.QTreeWidgetItem(['Connections']))
        self.test_project_tree.addTopLevelItem(item)

    def on_new_connection(self):
        dialog = ConnectionTypeDialog(self)
        dialog.show()
        pass

    def odbc(self):
        pass
