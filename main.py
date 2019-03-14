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
from userdetails import UserDetails

if __name__ == '__main__':
    user = UserDetails(username='postgres', password='123')
    connection = Connection(
        connection_name='Test', database='postgres', host='localhost', db_name='postgres', port='5432')
    connection.connect(user)
    connection.execute_query('select * from test2')
    pass
