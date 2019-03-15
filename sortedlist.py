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


import bisect


class SortedList(object):
    """
    Stores data in ascending order using bisect
    """

    def __init__(self):
        self.data = []

    def insert(self, value):
        bisect.insort(self.data, value)

    def remove(self, value):
        index = bisect.bisect_left(self.data, value)
        if index != len(self.data) and self.data[index] == value:
            self.data.pop(index)
            return True
        else:
            return False

    def __len__(self):
        return len(self.data)
