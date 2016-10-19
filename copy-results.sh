#!/bin/bash
for i in 01 02 03 04
do
    host="murphytest${i}"
    filename=$(sed "s/{host}/${host}/; ${i}q;d" current-runs.txt)
    echo "${host} --> ${filename}"
    scp ${host}.sleepymurph.com:masters-thesis/code/vc-benchmarks/output.txt \
        ${filename}
done
