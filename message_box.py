#  Copyright (C) 2019. Noorulhasan Peersab <npeersab77@gmail.com>
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

from PyQt5.QtWidgets import QMessageBox


class MessageBox(QMessageBox):
    def __init__(self, parent, title, message):
        super().__init__(parent)

        self.setWindowTitle(title)
        self.setText(message)


class ErrorMessageBox(MessageBox):
    def __init__(self, parent, title, message, details):
        super().__init__(parent, title, message)

        self.setIcon(MessageBox.Critical)
        self.setDetailedText(details)
        self.setStandardButtons(MessageBox.Ok)


class InformationMessageBox(MessageBox):
    def __init__(self, parent, title, message):
        super().__init__(parent, title, message)

        self.setIcon(MessageBox.Information)
        self.setStandardButtons(MessageBox.Ok)


class WarningMessageBox(MessageBox):
    def __init__(self, parent, title, message):
        super().__init__(parent, title, message)

        self.setIcon(MessageBox.Warning)
        self.setStandardButtons(MessageBox.Ok)
