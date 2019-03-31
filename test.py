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

import comparator
import datetime

from connection import Connection


class TestProject(object):
    """
    Contains all details about Test Project
    """

    def __init__(self, project_name):
        """
        Create new Test Project with name
        """
        self.name = project_name
        self.connections = []
        self.test_cases = []
        
    def add_connection(self, connection):
        """
        Add new Connection to the Test Project
        """
        self.connections.append(connection)
        
    def add_test_case(self, test_case):
        """
        Add new Test Case in the Test Project
        """
        self.test_cases.append(test_case)


class TestCase(object):
    """
    Test Case
    """
    source_connection: Connection
    target_connection: Connection

    def __init__(self, *, name, source_connection, source_query, sort_source=False, target_connection,
                 target_query, sort_target=False, max_mismatch_size):
        """
        Constructor
        """
        self.name = name
        self.source_connection = source_connection
        self.source_query = source_query
        self.sort_source = sort_source
        self.target_connection = target_connection
        self.target_query = target_query
        self.sort_target = sort_target
        self.max_mismatch_size = max_mismatch_size

    def execute(self):
        """
        Execute the Test Case
        """

        source_records = self.source_connection.execute_query(self.source_query, self.sort_source)
        target_records = self.target_connection.execute_query(self.target_query, self.sort_target)

        source_mismatch, target_mismatch = comparator.compare(source_records, target_records,
                                                              max_mismatch_size=self.max_mismatch_size)
        test_result = TestResult(self.name, self.source_query, self.target_query, source_mismatch,
                                 target_mismatch)
        return test_result


class TestResult(object):

    def __init__(self, test_case_name, source_query, target_query, source_mismatch, target_mismatch):
        self.test_case_name = test_case_name
        self.execution_timestamp = datetime.datetime.now()
        self.source_query = source_query
        self.target_query = target_query
        self.source_mismatch = source_mismatch
        self.target_mismatch = target_mismatch

        if len(source_mismatch) == 0 and len(target_mismatch) == 0:
            self.status = 'Pass'
        else:
            self.status = 'Fail'
