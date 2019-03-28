# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(755, 642)
        self.central_widget = QtWidgets.QWidget(window)
        self.central_widget.setObjectName("central_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.central_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.test_project_tree = QtWidgets.QTreeWidget(self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.test_project_tree.sizePolicy().hasHeightForWidth())
        self.test_project_tree.setSizePolicy(sizePolicy)
        self.test_project_tree.setObjectName("test_project_tree")
        self.test_project_tree.headerItem().setText(0, "1")
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
        window.setCentralWidget(self.central_widget)
        self.menu_bar = QtWidgets.QMenuBar(window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 755, 21))
        self.menu_bar.setObjectName("menu_bar")
        self.file_menu = QtWidgets.QMenu(self.menu_bar)
        self.file_menu.setObjectName("file_menu")
        self.new_menu = QtWidgets.QMenu(self.file_menu)
        self.new_menu.setObjectName("new_menu")
        window.setMenuBar(self.menu_bar)
        self.status_bar = QtWidgets.QStatusBar(window)
        self.status_bar.setObjectName("status_bar")
        window.setStatusBar(self.status_bar)
        self.test_case_action = QtWidgets.QAction(window)
        self.test_case_action.setObjectName("test_case_action")
        self.connection_action = QtWidgets.QAction(window)
        self.connection_action.setObjectName("connection_action")
        self.test_project_action = QtWidgets.QAction(window)
        self.test_project_action.setObjectName("test_project_action")
        self.new_menu.addAction(self.test_project_action)
        self.new_menu.addAction(self.test_case_action)
        self.new_menu.addAction(self.connection_action)
        self.file_menu.addAction(self.new_menu.menuAction())
        self.menu_bar.addAction(self.file_menu.menuAction())

        self.connection_action.triggered.connect(self.test)

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def test(self):
        print('hee')

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "MainWindow"))
        self.test_results_label.setText(_translate("window", "Test Results"))
        self.result_table.setSortingEnabled(True)
        item = self.result_table.verticalHeaderItem(0)
        item.setText(_translate("window", "1"))
        item = self.result_table.verticalHeaderItem(1)
        item.setText(_translate("window", "2"))
        item = self.result_table.verticalHeaderItem(2)
        item.setText(_translate("window", "3"))
        item = self.result_table.horizontalHeaderItem(0)
        item.setText(_translate("window", "ID"))
        item = self.result_table.horizontalHeaderItem(1)
        item.setText(_translate("window", "Test Case Name"))
        item = self.result_table.horizontalHeaderItem(2)
        item.setText(_translate("window", "Execution Time Stamp"))
        item = self.result_table.horizontalHeaderItem(3)
        item.setText(_translate("window", "Status"))
        __sortingEnabled = self.result_table.isSortingEnabled()
        self.result_table.setSortingEnabled(False)
        self.result_table.setSortingEnabled(__sortingEnabled)
        self.progress_label.setText(_translate("window", "TextLabel"))
        self.file_menu.setTitle(_translate("window", "File"))
        self.new_menu.setTitle(_translate("window", "New"))
        self.test_case_action.setText(_translate("window", "Test Case"))
        self.connection_action.setText(_translate("window", "Connection"))
        self.test_project_action.setText(_translate("window", "Test Project"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())

