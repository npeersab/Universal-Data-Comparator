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


def compare(source_records: iter, target_records: iter, *, max_mismatch_size):
    source_mismatch_records = SortedList()
    target_mismatch_records = SortedList()
    fetch_source = fetch_target = True
    source_record = target_record = None
    source_found = target_found = False

    while True:
        try:
            if fetch_target:
                target_record = target_records.__next__()
                target_found = False
        except StopIteration:
            if not source_found:
                if source_record != target_record:
                    source_mismatch_records.insert(source_record)
            check_remaining(source_records, source_mismatch_records, target_records, target_mismatch_records)
            break

        try:
            if fetch_source:
                source_record = source_records.__next__()
                source_found = False
        except StopIteration:
            if not target_found:
                if source_record != target_record:
                    target_mismatch_records.insert(target_record)
            check_remaining(source_records, source_mismatch_records, target_records, target_mismatch_records)
            break
        
        if source_record == target_record:
            fetch_source = fetch_target = True
        
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

            if not fetch_source and not fetch_target and source_found and target_found:
                fetch_source = fetch_target = True

    return source_mismatch_records, target_mismatch_records


def check_remaining(source_records, source_mismatch_records, target_records, target_mismatch_records):
    for source_record in source_records:
        source_record = source_record
        if target_mismatch_records.remove(source_record):
            pass
        else:
            source_mismatch_records.insert(source_record)

    for target_record in target_records:
        target_record = target_record
        if source_mismatch_records.remove(target_record):
            pass
        else:
            target_mismatch_records.insert(target_record)
