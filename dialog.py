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

from PyQt5 import QtCore, QtWidgets
from testproject import TestProject


class ConnectionTypeDialog(QtWidgets.QWidget):

    def __init__(self, parent):
        super().__init__(parent=parent, flags=QtCore.Qt.Window)
        self.setWindowModality(QtCore.Qt.WindowModal)

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
        self.cancel_button.setText(_translate("connection_type_window", "Cancel"))

    def set_connector(self):
        self.next_button.clicked.connect(self.on_next)

    def on_next(self):
        connection_type = self.connection_type_list.selectedItems()

        connection_methods = {self.connection_type_list.item(0).text(): self.odbc_using_dsn,
                              self.connection_type_list.item(1).text(): self.odbc,
                              self.connection_type_list.item(2).text(): self.jdbc,
                              self.connection_type_list.item(3).text(): self.native_python}

        connection_methods[connection_type[0].text()]()

    def odbc_using_dsn(self):
        self.parent().odbc()
        pass

    def odbc(self):
        pass

    def jdbc(self):
        pass

    def native_python(self):
        pass


class CreateProjectDialog(QtWidgets.QWidget):

    def __init__(self, parent):
        super().__init__(parent=parent, flags=QtCore.Qt.Window)

        self.setObjectName("create_project")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.resize(400, 135)
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

        self.re_translate_ui()
        self.setup_signals()

    def re_translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("create_project", "Form"))
        self.project_name_label.setText(_translate("create_project", "Project Name:"))
        self.create_project_button.setText(_translate("create_project", "Create Project"))
        self.cancel_button.setText(_translate("create_project", "Cancel"))

    def setup_signals(self):
        self.create_project_button.clicked.connect(self.on_create_project)

    def on_create_project(self):
        project_name = self.project_name_field.text()
        project = TestProject(project_name)
        self.parent().add_project(project)
        self.close()
