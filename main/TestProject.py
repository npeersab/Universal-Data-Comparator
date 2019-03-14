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
