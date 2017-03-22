#!/bin/bash

cat $1 | sed '/^#/d' | head -n1
(
for FILE in $*
do
    cat $FILE | sed '/^#/d' | tail -n1
done
) | sort -n -k1 -k2 -k3
