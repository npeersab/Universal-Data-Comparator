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


from sortedlist import SortedList


def compare(source_records, target_records, *, max_mismatch_size, sort_source=False, sort_target=False):
    source_mismatch_records = SortedList()
    target_mismatch_records = SortedList()
    fetch_source = fetch_target = True

    while True:
        try:
            if fetch_target:
                target_record = get_tuple(target_records.__next__())
            if fetch_source:
                source_record = get_tuple(source_records.__next__())
        except StopIteration:
            break
        
        if source_record == target_record:
            fetch_source = fetch_target = True
            pass
        
        else:
            if target_mismatch_records.remove(source_record):
                fetch_target = False
                source_found = True
            else:
                source_found = False

            if source_mismatch_records.remove(target_record):
                fetch_source = False
                target_found = True
            else:
                target_found = False

            if not source_found and not target_found:
                source_mismatch_records.insert(source_record)
                target_mismatch_records.insert(target_record)

                if len(source_mismatch_records) >= max_mismatch_size or \
                        len(target_mismatch_records) >= max_mismatch_size:
                    return source_mismatch_records, target_mismatch_records

    return source_mismatch_records, target_mismatch_records


def get_tuple(row):
    L = list(row)
    del row
    try:
        while True:
            index = L.index(None)
            L.pop(index)
            L.insert(index, '__NULL__')
    except ValueError:
        pass
    return tuple(L)
