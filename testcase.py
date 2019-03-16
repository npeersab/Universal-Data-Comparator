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

from connection import Connection
import comparator


class TestCase(object):
    """
    Test Case
    """
    source_connection: Connection
    target_connection: Connection

    def __init__(self, *, test_case_name, source_connection, source_query, sort_source=False, target_connection,
                 target_query, sort_target=False, max_mismatch_size):
        """
        Constructor
        """
        self.test_case_name = test_case_name
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

        self.source_connection.execute_query(self.source_query)
        source_records = self.source_connection.get_result_generator(self.sort_source)

        self.target_connection.execute_query(self.target_query)
        target_records = self.target_connection.get_result_generator(self.sort_target)

        source_mismatch, target_mismatch = comparator.compare(source_records, target_records,
                                                              max_mismatch_size=self.max_mismatch_size)
        test_result = TestResult(self, source_mismatch, target_mismatch)
        return test_result


class TestResult(object):
    def __init__(self, test_case, source_mismatch, target_mismatch):
        self.source_mismatch = source_mismatch
        self.target_mismatch = target_mismatch
        self.test_case = test_case

        if len(source_mismatch) == 0 and len(target_mismatch) == 0:
            self.status = 'Pass'
        else:
            self.status = 'Fail'
