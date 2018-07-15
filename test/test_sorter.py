import datetime
import unittest

from record_manager import record, sorter


def _get_list_in_order(l, order):
    """ Helper to return a copy of a list l ordered by order """
    ordered = []

    for i in order:
        ordered.append(l[i])

    return ordered


class TestSort(unittest.TestCase):
    def setUp(self):
        self.records = [
            record.Record('Washington', 'George', 'M', 'Red', datetime.datetime(1732, 2, 22)),
            record.Record('Washington', 'Martha', 'F', 'Blue', datetime.datetime(1731, 6, 13)),
            record.Record('Curie', 'Marie', 'F', 'Green', datetime.datetime(1867, 11, 7)),
            record.Record('Curie', 'Pierre', 'M', 'Yellow', datetime.datetime(1859, 5, 15)),
            record.Record('Becquerel', 'Antoine', 'M', 'Red', datetime.datetime(1852, 12, 15))
        ]

    def test_sort_records_by_gender(self):
        sorted_records = sorter.sort_records_by_gender(self.records)

        expected_order = _get_list_in_order(self.records, (2, 1, 4, 3, 0))

        self.assertEqual(sorted_records, expected_order)

    def test_sort_records_by_dob(self):
        sorted_records = sorter.sort_records_by_dob(self.records)

        expected_order = _get_list_in_order(self.records, (1, 0, 4, 3, 2))

        self.assertEqual(sorted_records, expected_order)

    def test_sort_records_by_name(self):
        sorted_records = sorter.sort_records_by_name(self.records)

        expected_order = _get_list_in_order(self.records, (1, 0, 3, 2, 4))

        self.assertEqual(sorted_records, expected_order)


if __name__ == '__main__':
    unittest.main()