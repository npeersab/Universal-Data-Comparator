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

import abc
from typing import Callable, Generator

import pyodbc


class Connection(object):
    """
    Connection to the database
    """

    def __init__(self, name: str, trusted_connection: bool):
        """
        constructor to create new Connection
        """

        self.name = name
        self.connection = None
        self.cursor = None
        self.trusted_connection = trusted_connection
        self.user_details = None

    def execute_query(self, query: str, on_fetch: Callable, sort: bool = False) -> Generator:
        """
        Execute the query on the connection and return the result generator

        :return: Generator for Data Rows
        :param query: The query which has to be executed
        :param on_fetch: The method which has to be executed if record is fetched
        :param sort: To sort the data
        """

        self.connect()
        self.cursor = self.connection.cursor()
        self.cursor.execute(query)

        data = self.cursor
        if sort:
            data = sorted(data.fetchall())

        def result_generator():
            for row in data:
                on_fetch(row)
                yield DataRow(row)

        return result_generator()

    @abc.abstractmethod
    def connect(self):
        pass

    def close_connection(self):
        self.connection = None
        self.cursor = None


class UserDetails(object):
    """
    Store Username and password
    """

    def __init__(self, username: str, password: str):
        """
        Create new user details
        :param username: str
        :param password: str
        """

        self.username = username
        self.password = password


class OdbcDsnConnection(Connection):
    def __init__(self, name: str, dsn: str, trusted_connection: bool = False):
        super().__init__(name, trusted_connection)

        self.dsn = dsn

    def connect(self):
        conn_str = 'DSN={};UID={};PWD={};'
        conn_str = conn_str.format(self.dsn, self.user_details.username, self.user_details.password)
        if self.trusted_connection:
            conn_str += 'Trusted_Connection=yes'

        self.connection = pyodbc.connect(conn_str)


class OdbcConnection(Connection):
    def __init__(self, name: str, driver: str, server: str, port: str, database: str, trusted_connection: bool = False):
        super().__init__(name, trusted_connection)

        self.driver = driver
        self.server = server + ',{}'.format(port) if port else ''
        self.database = database

    def connect(self):
        conn_str = 'DRIVER={{{}}};SERVER={};DATABASE={};UID={};PWD={}'
        conn_str = conn_str.format(self.driver, self.server, self.database, self.user_details.username,
                                   self.user_details.password)
        if self.trusted_connection:
            conn_str += 'Trusted_Connection=yes'

        self.connection = pyodbc.connect(conn_str)


class DataRow:
    def __init__(self, data):
        self.data = tuple(data)

    def __eq__(self, other):
        if other is None:
            return False
        return self.data == other.data

    def __ne__(self, other):
        if other is None:
            return True
        return self.data != other.data

    def __lt__(self, other):
        for value1, value2 in zip(self.data, other.data):
            if value1:
                if value2:
                    if value1 == value2:
                        continue
                    else:
                        return value1 < value2
                else:
                    return False
            else:
                if value2:
                    return True
                else:
                    continue
        return False

    def __le__(self, other):
        for value1, value2 in zip(self.data, other.data):
            if value1:
                if value2:
                    if value1 == value2:
                        continue
                    else:
                        return value1 <= value2
                else:
                    return False
            else:
                if value2:
                    return True
                else:
                    continue
        return True

    def __gt__(self, other):
        for value1, value2 in zip(self.data, other.data):
            if value1:
                if value2:
                    if value1 == value2:
                        continue
                    else:
                        return value1 > value2
                else:
                    return True
            else:
                if value2:
                    return False
                else:
                    continue
        return False

    def __ge__(self, other):
        for value1, value2 in zip(self.data, other.data):
            if value1:
                if value2:
                    if value1 == value2:
                        continue
                    else:
                        return value1 >= value2
                else:
                    return True
            else:
                if value2:
                    return False
                else:
                    continue
        return True

    def __iter__(self):
        return self.data.__iter__()
