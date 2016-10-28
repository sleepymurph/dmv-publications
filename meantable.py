#!/usr/bin/env python

import ast
import argparse
import math
import sys
import unittest


# Arguments

def parse_args(args=None):
    parser = argparse.ArgumentParser(
                description = "Calculate mean and standard deviation from matching experiment run files"
            )
    parser.add_argument('--columns', metavar='col', nargs='+', required=True,
            help='columns from tables to average')
    parser.add_argument('--files', metavar='file', nargs='+', required=True,
            help='table files to use as input')

    return parser.parse_args(args)


class ParseArgsTests(unittest.TestCase):
    def test_multi_optional_args(self):
        args = parse_args("--columns x y --files file1 file2".split())
        self.assertEqual(args.columns, ['x','y'])
        self.assertEqual(args.files, ['file1','file2'])

    def test_column_required(self):
        with self.assertRaises(SystemExit):
            args = parse_args("--files file1 file2".split())

    def test_files_required(self):
        with self.assertRaises(SystemExit):
            args = parse_args("--columns x y".split())


def read_skip(fd):
    for line in fd:
        if line == "" or line.startswith('#'):
            continue
        else:
            return line


# List combiners

def mean(vals):
    return float(sum(vals)) / len(vals)


def stddev(vals):
    avg = mean(vals)
    return math.sqrt( sum([(x-avg)**2 for x in vals]) / len(vals) )


class ListCombinerTests(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([2,4]), 3)
        self.assertEqual(mean([1,2,3,4,5]), 3)

    def test_stddev(self):
        self.assertEqual(stddev([2,4,4,4,5,5,7,9]), 2)


# Column Mean Calculator

class ColumnAggregator(object):

    def __init__(self, columns):
        self.columns = columns
        self.key_col = columns[0]
        self.other_cols = columns[1:]

        # { key val -> column name -> [values] }
        self.values = { }

    def create_column_map(self, header_line):
        colnames = header_line.split()
        column_map = { colname:i for i,colname in enumerate(colnames) }
        for expected_col in self.columns:
            if expected_col not in column_map.keys():
                raise KeyError("Expected column '{0}' not found".format(expectedcol))
        # column name -> column index in file
        return column_map

    def extract_value_map(self, column_map, value_line):
        strings = value_line.split()
        # column name -> value in row
        return { col: ast.literal_eval( strings[ column_map[col] ] ) for col in self.columns }

    def append_values(self, value_map):
        for col in self.other_cols:
            keyval = value_map[self.key_col]
            colval = value_map[col]

            if keyval not in self.values.keys():
                self.values[keyval] = {}
            if col not in self.values[keyval].keys():
                self.values[keyval][col] = []
            self.values[keyval][col].append(colval)

    def build_output_table(self):
        # Build a column name list for the output
        out_header = [ self.key_col ]
        for col_name in self.other_cols:
            out_header.append(col_name+'_avg')
            out_header.append(col_name+'_std')

        out_rows = [ out_header ]

        keyvals = list(self.values.keys())
        keyvals.sort()

        for keyval in keyvals:
            row = [ keyval ]

            for col_name in self.other_cols:
                colvals = self.values[keyval][col_name]
                colvals = [ x for x in colvals if x is not None ]
                if colvals:
                    row.append(mean(colvals))
                    row.append(stddev(colvals))
                else:
                    row.append(None)
                    row.append(None)

            out_rows.append(row)

        return out_rows

# Output

def tabulate(rows):
    max_widths = [0] * len(rows[0])
    for row in rows:
        for i,val in enumerate(row):
            max_widths[i] = max(max_widths[i], len(str(val)))

    lines = []
    for row in rows:
        padded_row = [ '{0:>{1}}'.format(val,max_widths[i]) for i,val in enumerate(row) ]
        lines.append('  '.join(padded_row))

    return lines


# Main

def main():
    args = parse_args()

    aggregator = ColumnAggregator(args.columns)
    for path in args.files:
        with open(path) as f:
            header_line = read_skip(f)
            column_map = aggregator.create_column_map(header_line)
            while True:
                line = read_skip(f)
                if not line: break
                vals = aggregator.extract_value_map(column_map, line)
                aggregator.append_values(vals)

    rows = aggregator.build_output_table()
    for line in tabulate(rows):
        print line

if __name__ == '__main__':
    main()
