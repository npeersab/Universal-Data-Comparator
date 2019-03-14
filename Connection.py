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

from UserDetails import UserDetails
import psycopg2


class Connection(object):
    """
    Connection to the database
    """
    name: str
    database: str
    host: str
    db_name: str
    port: str

    def __init__(self, *, connection_name: str, database: str, host: str, db_name: str, port: str) -> None:
        """
        constructor to create new Connection
        """
        
        self.name = connection_name
        self.database = database
        self.host = host
        self.db_name = db_name
        self.port = port
        self.connection = None
        self.cursor = None

    def connect(self, user_details: UserDetails):
        """
        Create connection with database
        """

        url = 'dbname={0} host={1} port={2} user={3} password={4}'.format(
            self.db_name, self.host, self.port, user_details.username, user_details.password)
        self.connection = psycopg2.connect(url)

    def execute_query(self, query: str):
        self.cursor = self.connection.cursor()
        self.cursor.execute(query)
