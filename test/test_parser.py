import datetime
import unittest

from record_manager import parser, record

class TestGetdelimiter(unittest.TestCase):

    def test_comma(self):
        line = 'Washington,George,M,Red,2/22/1732'

        self.assertEqual(parser.get_delimiter(line), ',')

    def test_pipe(self):
        line = 'Washington|George|M|White|2/22/1732'

        self.assertEqual(parser.get_delimiter(line), '|')

    def test_space(self):
        line = 'Washington George M Blue 2/22/1732'

        self.assertEqual(parser.get_delimiter(line), ' ')

    def test_unknown(self):
        line = 'Washington\tGeorge\tM\tWhite\t2/22/1732'

        with self.assertRaises(Exception):
            parser.get_delimiter(line)


class TestParseRecord(unittest.TestCase):

    def test_comma(self):
        line = 'Washington,George,M,Red,2/22/1732'
        expected = record.Record('Washington', 'George', 'M', 'Red', datetime.datetime(1732, 2, 22))

        self.assertEqual(parser.parse_record(line), expected)
        self.assertEqual(parser.parse_record(line, delimiter=','), expected)

    def test_pipe(self):
        line = 'Washington|George|M|White|2/22/1732'
        expected = record.Record('Washington', 'George', 'M', 'White', datetime.datetime(1732, 2, 22))

        self.assertEqual(parser.parse_record(line), expected)
        self.assertEqual(parser.parse_record(line, '|'), expected)

    def test_space(self):
        line = 'Washington George M Blue 2/22/1732'
        expected = record.Record('Washington', 'George', 'M', 'Blue', datetime.datetime(1732, 2, 22))

        self.assertEqual(parser.parse_record(line), expected)
        self.assertEqual(parser.parse_record(line, ' '), expected)

    def test_missing_data(self):
        line = 'Washington George M Blue'

        with self.assertRaises(Exception):
            parser.parse_record(line)

    def test_bad_date(self):
        line = 'Washington George M Blue 100/22/1732'

        with self.assertRaises(ValueError):
            parser.parse_record(line)

class TestParseRecords(unittest.TestCase):
    def setUp(self):
        # These lists are joined with the relevant delimimter before each test
        self.people = [
            ['Curie', 'Marie', 'F', 'Green', '11/7/1867'],
            ['Curie', 'Pierre', 'M', 'Yellow', '5/15/1859'],
            ['Becquerel', 'Antoine', 'M', 'Red', '12/15/1852']
        ]

    def _test_template(self, record_strings):
        expected_records = [parser.parse_record(r) for r in record_strings]

        self.assertEqual(parser.parse_records(record_strings), expected_records)

    def test_commas(self):
        self._test_template([','.join(p) for p in self.people])

    def test_pipes(self):
        self._test_template(['|'.join(p) for p in self.people])

    def test_spaces(self):
        self._test_template([' '.join(p) for p in self.people])

    def test_various(self):
        self._test_template([
            ','.join(self.people[0]),
            '|'.join(self.people[1]),
            ' '.join(self.people[2])
        ])

    def test_missing_data(self):
        record_strings = ['Washington George M Blue 100/22/1732']

        with self.assertRaises(Exception):
            parser.parse_records(record_strings)

    def test_bad_date(self):
        record_strings = ['Washington George M Blue 100/22/1732']

        with self.assertRaises(ValueError):
            parser.parse_records(record_strings)


if __name__ == '__main__':
    unittest.main()