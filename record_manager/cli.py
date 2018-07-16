#!/usr/bin/python3
import argparse

from . import parser, sorter

def load_files(files):
    lines = []

    for filename in files:
        with open(filename) as f:
            lines.extend(f.read().split('\n'))

    return lines

def main():
    argparser = argparse.ArgumentParser(description="Process data records")
    argparser.add_argument('--sort', default='gender',
                        choices=('gender', 'dob', 'name'))
    argparser.add_argument('files', nargs='+', help='List of files to process')

    args = argparser.parse_args()

    record_strings = load_files(args.files)
    records = parser.parse_records(record_strings)

    if args.sort == 'gender':
        sorted_records = sorter.sort_records_by_gender(records)
    elif args.sort == 'dob':
        sorted_records = sorter.sort_records_by_dob(records)
    else:
        sorted_records = sorter.sort_records_by_name(records)

    for r in sorted_records:
        print(r)