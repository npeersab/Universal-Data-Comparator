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


def main():

    '''user = UserDetails(username='postgres', password='123')
    connection = Connection(
        name='Test', host='localhost', db_name='postgres', port='5432')
    connection.connect(user)

    source_query = 'select * from test2'
    target_query = 'select * from test1'
    test_case = TestCase(test_case_name='Test Case 1', source_connection=connection, source_query=source_query,
                         target_connection=connection, target_query=target_query, max_mismatch_size=100000)

    test_result = test_case.execute()
    print('source mismatch length: {}'.format(len(test_result.source_mismatch)))
    print('target mismatch length: {}'.format(len(test_result.target_mismatch)))

    '''
    '''

    start = time.perf_counter()
    connection.execute_query('select * from test1')
    print('source time {} sec'.format(time.perf_counter() - start))
    source = connection.get_result_generator()

    connection2 = Connection(
        connection_name='Test', database='postgres', host='localhost', db_name='postgres', port='5432')
    connection2.connect(user)
    start = time.perf_counter()
    connection2.execute_query('select * from test2')
    target = connection2.get_result_generator()
    print('target time {} sec'.format(time.perf_counter() - start))
    
    start = time.perf_counter()
    source_mis, target_mis = comparator.compare(source, target, max_mismatch_size=10000)
    print('compare time {} sec'.format(time.perf_counter() - start))

    print('source mismatch length: {}'.format(len(source_mis)))
    print('target mismatch length: {}'.format(len(target_mis)))
    pass'''


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
    config_logger()

    logger.info('Starting Application...')
    app = QtWidgets.QApplication(sys.argv)
    main_window = None
    welcome_dialog = WelcomeDialog(start_main)
    welcome_dialog.show()
    logger.info('Application Started')
    sys.exit(app.exec_())
