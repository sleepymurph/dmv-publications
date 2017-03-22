#!/bin/bash

DEPTH=$1
shift
FILES=$*

./aggregate_last_lines.sh $FILES \
    | awk '$2=='$DEPTH' {print $0}' \
    | awk '{print $3, 100*strtonum($11)/strtonum($9)}'
