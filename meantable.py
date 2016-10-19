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


def mean(vals):
    return float(sum(vals)) / len(vals)


def stddev(vals):
    avg = mean(vals)
    return math.sqrt( sum([(x-avg)**2 for x in vals]) / len(vals) )


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


def main():
    args = parse_args()

    with multi_open(args.files) as filegroup:

        colindexes = []

        # Find header line and build a column name to index dict for each file
        for i,header in enumerate(filegroup.read_skip_all()):
            colnames = header.split()
            lookup = { colname:i for i,colname in enumerate(colnames) }
            colindexes.append(lookup)
            for expectedcol in args.columns:
                if expectedcol not in lookup.keys():
                    raise KeyError("Expected column '{0}' not found in '{1}'".format(expectedcol, args.files[i]))

        # Build a column name list for the output
        resultheader = [ args.columns[0] ]
        for colname in args.columns[1:]:
            resultheader.append(colname+'_avg')
            resultheader.append(colname+'_std')

        resultrows = [ resultheader ]

        for linegroup in filegroup:
            linegroup = [ line.split() for line in linegroup ]
            row = []

            keycol = args.columns[0]
            keyvals = [ line[colindexes[i][keycol]] for i,line in enumerate(linegroup) ]
            if not all_same_value(keyvals):
                raise ValueError("Mismatched independent variables (first column): {0}".format(keyvals))
            row.append(keyvals[0])

            for col in args.columns[1:]:
                vals = [ line[colindexes[i][col]] for i,line in enumerate(linegroup) ]
                vals = [ ast.literal_eval(val) for val in vals ]
                #print col, vals, mean(vals), stddev(vals)
                row.append(mean(vals))
                row.append(stddev(vals))

            resultrows.append(row)

        for line in tabulate(resultrows):
            print line


if __name__ == '__main__':
    main()
