Tracking experiment runs
==================================================

Spring: First prototype, FS-limits, chunk-size
-----------------------------------------------

### Run grid

                    File size (pro)
                    |   Number of files (too many dirs)
                    |   |   Object dir structure
                    |   |   |   Created smalltest
                    |   |   |   |   Object dir structure on big partition
    murphytest01 [  f   p   -   s   -   ]
    murphytest02 [  f   -   d   s   -   ]
    murphytest03 [  f   -   d   s   -   ]
    murphytest04 [  f   -   d   s   -   ]



Spring: Prototype and num-files re-tests
--------------------------------------------------

### Run grid

                    Number of files with 00/000000000000
                    cp  git hg  bup prototype2x1
                    |   |   |   |   |   prototype2x1mem
                    |   |   |   |   |   |   prototype2x1memdeadline
                    |   |   |   |   |   |   |   prototype2x1memnoop
                    |   |   |   |   |   |   |   |   prototype2x1memcfqfilebuf
                    |   |   |   |   |   |   |   |   |   prototype2x1membufwrite
    murphytest01 [  c   g   h   @                       pwb]
    murphytest02 [  c   g   h   b   pd  pdm pdd pnp @      ]
    murphytest03 [  c           b       pdm         pfb    ]
    murphytest04 [      g                   pdd            ]


                    File size
                    protototype
                    |   prototype2x1
                    |   |   prototype2x1mem
                    |   |   |   prototype2x1memcfqfilebuf
                    |   |   |   |   prototype2x1membufwrite
                    |   |   |   |   |   prototype2x1chunks32kx16k
                    |   |   |   |   |   |   prototype2x1chunks32kx16kdeadline
                    |   |   |   |   |   |   |   prototype2x1chunks32kx16knoop
    murphytest01 [  p   pd          pbw             ]
    murphytest02 [  p                   pc          ]
    murphytest03 [  p   pd  pdm pfb pbw @           ]
    murphytest04 [  p   pd  @   pfb         pcd     ]


### Command lines

    # Timeouts: 5.5 hours is 19800 seconds. An even 20000 would be 5h33m30s.

    # Versions:
    # prototype2x1:                 f464604
    # prototype2x1mem:              c9baf3a
    # prototype2x1memcfqfilebuf:    bfd6f31
    # prototype2x1membufwrite:      856d3ea
    # prototype2x1chunks32kx16k:    b134cca

    # File size
    export RUST_LOG=warn,disk_backed=debug
    ./increasing_file_size.py prototype 0 38 --mag-step=2 --data-gen=random --timeout=19800 --tmp=/test --reformat-partition /dev/$(hostname)-vg/test | tee -i output.txt

    # Number of files
    export RUST_LOG=warn,disk_backed=debug
    ./increasing_number_of_files.py prototype 0 8 --mag-step=4 --data-gen=random --timeout=19800 --tmp=/test --reformat-partition /dev/$(hostname)-vg/test | tee -i output.txt

    # Filesystem (need to adjust params)
    ./filesystem_limit.py --each-file-size=4096 --dir-split=2 --dir-depth=2 --data-gen random --tmp=/smalltest --reformat-partition /dev/$(hostname)-vg/smalltest | tee -i output.txt

    # Filesystem on big partition
    ./filesystem_limit_micro.py --each-file-size=4096 --dir-split=0 --dir-depth=0 --data-gen random --tmp=/test --reformat-partition /dev/$(hostname)-vg/test | tee -i output.txt

    # Watch filesystem outliers
    tail -F output.txt | awk '$8 > 0 {print $0}'

    # Multiples
    ./filesystem_limit_multi.sh 4096 4 10 --data-gen random --tmp=/smalltest --reformat-partition /dev/$(hostname)-vg/smalltest

    # Copy multiples
    for I in $(seq 2 4); do scp murphytest0$I.sleepymurph.com:masters-thesis/code/vc-benchmarks/'*.txt' exp--filesystem-limits--micro/; done

    # Remove combos that have more splits than file name length
    git rm $(grep -l '^ .*/$' exp--filesystem-limits--micro/*)
