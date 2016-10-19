#!/usr/bin/env python

import subprocess

remotefname = 'masters-thesis/code/vc-benchmarks/output.txt'
domain = 'sleepymurph.com'

with open('current-runs.txt') as f:
    for line in f:
        if line.startswith('#'): continue
        host, dst = line.split()
        dst = dst.replace('{host}', host)
        src = "{0}.{1}:{2}".format(host, domain, remotefname)
        print src, ' --> ', dst
        subprocess.call(['scp', src, dst])
