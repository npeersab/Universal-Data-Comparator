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


from connection import Connection, UserDetails
import comparator
import time


def main():
    user = UserDetails(username='postgres', password='su123')
    connection = Connection(
        connection_name='Test', database='postgres', host='localhost', db_name='postgres', port='5432')
    connection.connect(user)
    start = time.perf_counter()
    connection.execute_query('select * from test1 order by pk')
    print('source time {} sec'.format(time.perf_counter() - start))
    source = connection.get_result_generator()

    connection2 = Connection(
        connection_name='Test', database='postgres', host='localhost', db_name='postgres', port='5432')
    connection2.connect(user)
    start = time.perf_counter()
    connection2.execute_query('select * from test2 order by pk')
    target = connection2.get_result_generator()
    print('target time {} sec'.format(time.perf_counter() - start))
    
    start = time.perf_counter()
    source_mis, target_mis = comparator.compare(source, target, max_mismatch_size=200000)
    print('compare time {} sec'.format(time.perf_counter() - start))
    
    print('source mismatch length: {}'.format(source_mis.len))
    print('target mismatch length: {}'.format(target_mis.len))
    
    pass

if __name__ == '__main__':
    main()
    pass
