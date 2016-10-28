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


# Multiple Files

class multi_open(object):
    def __init__(self, paths, mode='r'):
        self.paths = paths
        self.mode = mode
        self.fds = []

        try:
            for path in paths:
                self.fds.append(open(path, self.mode))
        except:
            self.close_all()
            raise

    def close_all(self):
        for fd in self.fds:
            fd.close()

    def read_skip_all(self):
        nextlines = []
        for fd in self.fds:
            nextlines.append(read_skip(fd))
        return nextlines

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close_all()

    def __iter__(self):
        return self

    def next(self):
        lines = self.read_skip_all()
        if None in lines:
            raise StopIteration
        return lines


def read_skip(fd):
    for line in fd:
        if line == "" or line.startswith('#'):
            continue
        else:
            return line


# List combiners

def all_same_value(vals):
    for val in vals[1:]:
        if val != vals[0]:
            return False
    return True


def mean(vals):
    return float(sum(vals)) / len(vals)


def stddev(vals):
    avg = mean(vals)
    return math.sqrt( sum([(x-avg)**2 for x in vals]) / len(vals) )


class ListCombinerTests(unittest.TestCase):
    def test_all_same_value(self):
        self.assertEqual(all_same_value([0,0,0,0,0]), True)
        self.assertEqual(all_same_value([1,0,0,0,0]), False)
        self.assertEqual(all_same_value([0,0,0,0,1]), False)

    def test_mean(self):
        self.assertEqual(mean([2,4]), 3)
        self.assertEqual(mean([1,2,3,4,5]), 3)

    def test_stddev(self):
        self.assertEqual(stddev([2,4,4,4,5,5,7,9]), 2)


# Column Mean Calculator

class ColumnMeanCalculator(object):

    def __init__(self, specified_cols, filepaths):
        self.specified_cols = specified_cols
        self.filepaths = filepaths

        # Build a column name list for the output
        self.out_cols = [ self.specified_cols[0] ]
        for colname in self.specified_cols[1:]:
            self.out_cols.append(colname+'_avg')
            self.out_cols.append(colname+'_std')

        self.out_rows = [ self.out_cols ]

    def set_input_headers(self, input_header_lines):
        self.colindexes = []
        for i,header in enumerate(input_header_lines):
            colnames = header.split()
            lookup = { colname:i for i,colname in enumerate(colnames) }
            self.colindexes.append(lookup)
            for expectedcol in self.specified_cols:
                if expectedcol not in lookup.keys():
                    raise KeyError("Expected column '{0}' not found in '{1}'".format(expectedcol, self.filepaths[i]))

    def extract_column_values(self, col, splitgroup):
        return [ line[self.colindexes[i][col]]
                for i,line in enumerate(splitgroup) ]

    def append_line_group(self, linegroup):
        splitgroup = [ line.split() for line in linegroup ]
        row = []

        for i,col in enumerate(self.specified_cols):
            vals = self.extract_column_values(col, splitgroup)

            if i==0:    # Key column
                if not all_same_value(vals):
                    raise ValueError("Mismatched independent variables (first column): {0}".format(keyvals))
                row.append(vals[0])

            else:
                vals = [ ast.literal_eval(val) for val in vals ]
                if None in vals:
                    row.append(None)
                    row.append(None)
                else:
                    row.append(mean(vals))
                    row.append(stddev(vals))

        self.out_rows.append(row)


class ColumnMeanCalculatorTests(unittest.TestCase):
    def test_simple_values(self):
        calculator = ColumnMeanCalculator(
                specified_cols = ['filebytes', 'c1_time'],
                filepaths = ['file1', 'file2', 'file3'])

        calculator.set_input_headers([
            'mag     filebytes   c1_time       c1_size   c1_cmd    c1_ver',
            'mag     filebytes   c1_time       c1_size   c1_cmd    c1_ver',
            'mag     filebytes   c1_time       c1_size   c1_cmd    c1_ver',
            ])

        calculator.append_line_group([
            ' 24  0x0001000000     0.827  0x0002015000       ok  verified',
            ' 24  0x0001000000     0.871  0x0002015000       ok  verified',
            ' 24  0x0001000000     0.830  0x0002015000       ok  verified',
            ])

        self.assertEqual(calculator.out_rows,
            [['filebytes', 'c1_time_avg', 'c1_time_std'],
             ['0x0001000000', 0.8426666666666667, 0.02007209228976615]])

    def test_missing_column(self):
        calculator = ColumnMeanCalculator(
                specified_cols = ['filebytes', 'c1_time'],
                filepaths = ['file1', 'file2', 'file3'])

        with self.assertRaises(KeyError) as raises:
            calculator.set_input_headers([
                'mag     filebytes   c1_time       c1_size   c1_cmd    c1_ver',
                'mag     filebytes                 c1_size   c1_cmd    c1_ver',
                'mag     filebytes   c1_time       c1_size   c1_cmd    c1_ver',
                ])

        self.assertIn('c1_time', str(raises.exception))
        self.assertIn('file2', str(raises.exception))


    def test_missing_values(self):
        calculator = ColumnMeanCalculator(
                specified_cols = ['filebytes', 'c1_time'],
                filepaths = ['file1', 'file2', 'file3'])

        calculator.set_input_headers([
            'mag     filebytes   c1_time       c1_size   c1_cmd    c1_ver',
            'mag     filebytes   c1_time       c1_size   c1_cmd    c1_ver',
            'mag     filebytes   c1_time       c1_size   c1_cmd    c1_ver',
            ])

        calculator.append_line_group([
            ' 24  0x0001000000     0.827  0x0002015000       ok  verified',
            ' 24  0x0001000000     0.871  0x0002015000       ok  verified',
            ' 24  0x0001000000    (None)  0x0002015000       ok  verified',
            ])

        self.assertEqual(calculator.out_rows,
            [['filebytes', 'c1_time_avg', 'c1_time_std'],
             ['0x0001000000', None, None]])


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
                # TODO: accept some Nones
                if None in colvals:
                    row.append(None)
                    row.append(None)
                else:
                    row.append(mean(colvals))
                    row.append(stddev(colvals))

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
