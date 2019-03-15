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


from bst import Tree


def compare(source_records, target_records, *, max_mismatch_size, sort_source=False, sort_target=False):
    source_mismatch_records = Tree()
    target_mismatch_records = Tree()
    fetch_source = fetch_target = True

    while True:
        try:
            if fetch_target:
                target_record = getTupple(target_records.__next__())
            if fetch_source:
                source_record = getTupple(source_records.__next__())
        except StopIteration:
            break
        
        #print('source_record', source_record)
        #print('target_record', target_record)
        
        if source_record == target_record:
            fetch_source = fetch_target = True
            pass
        
        else:
            if target_mismatch_records.delete(source_record):
                
                fetch_target = False
                source_found = True
            else:
                source_found = False
                
            if source_mismatch_records.delete(target_record):
                
                fetch_source = False
                target_found = True
            else:
                target_found = False

            if not source_found and not target_found:
                source_mismatch_records.insert(source_record)
                target_mismatch_records.insert(target_record)

                if source_mismatch_records.len >= max_mismatch_size or target_mismatch_records.len >= max_mismatch_size:
                    return source_mismatch_records, target_mismatch_records

    #source_mismatch_records.extend(source_records)
    #target_mismatch_records.extend(target_records)

    return source_mismatch_records, target_mismatch_records

def getTupple(row):
    L = list(row)
    del row
    while True:
        try:
            index = L.index(None)
            L.pop(index)
            L.insert(index, '__NULL__')
        except:
            break;
    return tuple(L)