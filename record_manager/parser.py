import datetime

from . import record


def get_delimiter(record_string):
    """ Returns the delimiter for a given string record """
    if ',' in record_string:
        return ','
    elif '|' in record_string:
        return '|'
    elif ' ' in record_string:
        return ' '
    else:
        raise Exception('Delimiter must be ",", "|", or " "')


def parse_record(s, delimiter=None):
    if delimiter is None:
        delimiter = get_delimiter(s)

    record_data = s.split(delimiter)

    # This function could do a lot of data normalization and assertions, but
    # for now we'll just ensure all the fields are there and parse the date
    if len(record_data) != 5:
        raise Exception('Cannot parse {}, record must contain LastName, '
                        'FirstName, Gender, Color, and DateOfBirth')

    return record.Record(
        record_data[0],
        record_data[1],
        record_data[2],
        record_data[3],
        datetime.datetime.strptime(record_data[4], '%m/%d/%Y')
    )


def parse_records(record_strings, delimiter=None):
    records = []

    for record_string in record_strings:
        records.append(parse_record(record_string, delimiter=delimiter))

    return records