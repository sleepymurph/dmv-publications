#!/bin/bash

DEPTH=$1
shift
FILES=$*

./aggregate_last_lines.sh $FILES \
    | awk '$2=='$DEPTH' {print $0}' \
