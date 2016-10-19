#!/usr/bin/env python

import ast
import argparse
import math
import sys
import unittest

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


def all_same_value(vals):
    for val in vals[1:]:
        if val != vals[0]:
            return False
    return True


class ListProcessorTests(unittest.TestCase):
    def test_all_same_value(self):
        self.assertEqual(all_same_value([0,0,0,0,0]), True)
        self.assertEqual(all_same_value([1,0,0,0,0]), False)
        self.assertEqual(all_same_value([0,0,0,0,1]), False)


def mean(vals):
    return float(sum(vals)) / len(vals)


def stddev(vals):
    avg = mean(vals)
    return math.sqrt( sum([(x-avg)**2 for x in vals]) / len(vals) )


class MeanStdTests(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([2,4]), 3)
        self.assertEqual(mean([1,2,3,4,5]), 3)

    def test_stddev(self):
        self.assertEqual(stddev([2,4,4,4,5,5,7,9]), 2)


def tabulate(rows):
    max_widths = [0] * len(rows[0])
    for row in rows:
        for i,val in enumerate(row):
            max_widths[i] = max(max_widths[i], len(str(val)))

    lines = []
    for row in rows:
        padded_row = [ '{0:{1}}'.format(val,max_widths[i]) for i,val in enumerate(row) ]
        lines.append('  '.join(padded_row))

    return lines


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

    def append_line_group(self, linegroup):
        linegroup = [ line.split() for line in linegroup ]
        row = []

        keycol = self.specified_cols[0]
        keyvals = [ line[self.colindexes[i][keycol]] for i,line in enumerate(linegroup) ]
        if not all_same_value(keyvals):
            raise ValueError("Mismatched independent variables (first column): {0}".format(keyvals))
        row.append(keyvals[0])

        for col in self.specified_cols[1:]:
            vals = [ line[self.colindexes[i][col]] for i,line in enumerate(linegroup) ]
            vals = [ ast.literal_eval(val) for val in vals ]
            #print col, vals, mean(vals), stddev(vals)
            row.append(mean(vals))
            row.append(stddev(vals))

        self.out_rows.append(row)

def main():
    args = parse_args()

    with multi_open(args.files) as filegroup:

        calculator = ColumnMeanCalculator(args.columns, args.files)
        calculator.set_input_headers(filegroup.read_skip_all())

        for linegroup in filegroup:
            calculator.append_line_group(linegroup)

        for line in tabulate(calculator.out_rows):
            print line


if __name__ == '__main__':
    main()
