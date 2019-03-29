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

import pyodbc


class Connection(object):
    """
    Connection to the database
    """

    def __init__(self, name: str) -> None:
        """
        constructor to create new Connection
        """

        self.name = name
        self.connection = None
        self.cursor = None

    '''def connect(self, user_details) -> None:
        """
        Create connection with database
        """

        url = 'dbname={0} host={1} port={2} user={3} password={4}'.format(
            self.db_name, self.host, self.port, user_details.username, user_details.password)
        self.connection = psycopg2.connect(url)'''

    def execute_query(self, query: str, sort=False):
        self.cursor = self.connection.cursor()
        self.cursor.execute(query)

        """
        Create a generator to fetch rows from database
        if data is sorted program will require more memory space to execute
        """
        data = self.cursor
        if sort:
            data = sorted(data.fetchall())

        return (replace_null(row) for row in data)


class OdbcDsnConnection(Connection):
    def __init__(self, name, dsn):
        super().__init__(name)

        self.dsn = dsn

    def connect(self, user_details):
        url = 'DSN={0};UID={1};PWD={2}'.format(self.dsn, user_details.username, user_details.password)
        self.connection = pyodbc.connect(url)


class OdbcConnection(Connection):
    def __init__(self, name, driver, server, database):
        super().__init__(name)

        self.driver = driver
        self.server = server
        self.database = database

    def connect(self, user_details):
        url = 'DRIVER={%s};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s' % (self.driver, self.server, self.database,
                                                                   user_details.username, user_details.password)
        self.connection = pyodbc.connect(url)


def replace_null(row: tuple) -> tuple:
    """
    Replace all None values in the tuple with __NULL__

    :param row:
    :return row with replaced None values:
    """
    row = list(row)
    try:
        while True:
            index = row.index(None)
            row.pop(index)
            row.insert(index, '__NULL__')
    except ValueError:
        pass

    return tuple(row)


class UserDetails(object):
    """
    Store Username and password
    """

    def __init__(self, *, password: str, username: str):
        """
        Create new user details
        :param username: str
        :param password: str
        """

        self.username = username
        self.password = password
