#!/bin/bash

DEPTH=$1
shift
FILES=$*

../data/aggregate_last_lines.sh $FILES \
    | awk '$2==0 || $2=='$DEPTH' {print $0}' \
