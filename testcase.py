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


class TestCase(object):
    """
    Test Case
    """

    def __init__(self, *, test_case_name, source_connection, source_query, target_connection, target_query):
        """
        Constructor
        """
        self.test_case_name = test_case_name
        self.source_connection = source_connection
        self.source_query = source_query
        self.target_connection = target_connection
        self.target_query = target_query

    def execute(self):
        """
        Execute the Test Case
        """
        pass
