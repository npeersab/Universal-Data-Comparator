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

import datetime
import logging
import os
import sys

from PyQt5 import QtWidgets

from dialog import WelcomeDialog
from window import MainWindow

logger = logging.getLogger()


def start_main(project):
    global main_window
    main_window = MainWindow(project)
    main_window.show()


def config_logger():
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.DEBUG)

    folder_name = 'logs'
    os.makedirs(folder_name, exist_ok=True)
    file_name = str(datetime.datetime.now()).replace(':', '-').replace('.', '-')
    file_handler = logging.FileHandler('{0}/{1}.log'.format(folder_name, file_name), mode='w')
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(stream_handler)
    root_logger.addHandler(file_handler)


if __name__ == '__main__':
    main_window = None

    config_logger()

    # Create Welcome dialog
    logger.info('Starting Application...')
    app = QtWidgets.QApplication(sys.argv)
    welcome_dialog = WelcomeDialog(start_main)
    welcome_dialog.show()
    logger.info('Application Started')

    sys.exit(app.exec_())
