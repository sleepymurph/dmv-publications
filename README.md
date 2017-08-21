DMV: Distributed Media Versioning -- Publications
==================================================

DMV is a project to generalize version control beyond source code and into
larger files such as photos and video, and also into larger collections that
might not fit on one disk. It hopes to be a cross between a version control
system and a generalized distributed data store.

Publications
==================================================

This repository contains the LaTeX source and other source materials for the
master's thesis and other DMV publications. It also includes experiment results
data.

The master's thesis PDF is checked into the repository. It is also available in
the University of Tromsø's open research archive
(<http://hdl.handle.net/10037/11213>), so you do not have to clone and compile
this source.

Generated documents:

- `thesis.pdf` -- The DMV master's thesis itself
- `design-document.pdf` -- An old design document from the beginning of the
  project
- `design-document-2-short.pdf` -- Another old design document, this one shorter
  and more direct

Other files reside in subdirectories:

- `data/` -- Experiment results data
- `doc-src/` -- LaTeX, Graphviz, GNUPlot, and other document source materials


Compiling the Documents
--------------------------------------------------

There is a Makefile in the `doc-src/` directory that should generate everything
with a simple `make`.

The documents are built with LaTeX for overall typesetting, GNUPlot for data
plots, and Graphviz for diagrams. Development took place on a Debian 8 (Jessie)
system with vanilla versions of the TeX Live, GNUPlot, and Graphviz packages
installed. So it should build easily on any Unix system with reasonably
up-to-date versions of those programs.

The only non-standard LaTeX package used is the Open Sans font, which is used by
the thesis. Open Sans is part of TeX Live, in the [`opensans` CTAN package](
https://www.ctan.org/pkg/opensans?lang=en), which is provided on Debian by the
[`texlive-fonts-extra` APT package](
https://packages.debian.org/search?keywords=texlive-fonts-extra).


Data Files
--------------------------------------------------

Experiment data files are in the `data/` directory, organized into
subdirectories that start with `exp--`.

Results actually used in the thesis:

```
exp--file-size--v04--w-cpu          The file-size experiment
exp--num-files--v03--less-dirs      The number-of-files experiment
exp--filesystem-limits--micro       The directory-layout experiment
exp--rolling-hash                   The chunk-size experiment
```

The other directories are results that are not used in the thesis, from early
runs and early versions of the experiment scripts. The version numbers in the
file-size and num-files directories represent changes to the columns that
required changes in the GNUPlot scripts.


### Data file naming convention

Data files for the file-size and num-files experiments are named like
`vcs-date-host.txt`, for example:

```
git-2016-10-21-murphytest02.txt         A Git run
hg-2016-10-19-murphytest01.txt          A Mercurial run
bup-2016-10-20-murphytest04.txt         A Bup run
prototype-2017-03-17-murphytest03.txt   A DMV run
copy-2016-10-20-murphytest01.txt        A Copy run
```

Note that Mercurial is referred to as "hg", and DMV is "prototype" because it
did not yet have a name at the time.

Host names are the names of the four test computers, `murphytest01` -
`murphytest04`. Each experiment was run on each host.

The file-size runs include git files named `gitallowrepoerr`. Those are later
git runs where the experiment script had been modified to let Git continue after
a commit and verification failed, since we had determined that the errors were
probably a false alarm. Those are the results used in the thesis.


### Different DMV prototypes

The different variations of `prototype` represent different versions of the
prototype. Each has a corresponding tag in the DMV code repository.

- The first version that could be run in the experiments, with a directory
  scheme of 2 hex digits and a depth of 2, and the window-reset bug

        prototype                       fb2f43d

- The reference version, with a directory scheme of 2 hex digits and depth of 1
  (hence 2x1) the window-reset bug, plus some memory usage fixes

        prototype2x1mem                 c9baf3a      4 Kib window, window bug

- Other versions with a 2x1 directory scheme, but different chunk sizes

        prototype2x1chunks32kx16k       b134cca     32 KiB window, window bug
        prototypenochunkreset           a660730      4 KiB window, no window bug
        prototypenochunkreset32kx16k    3e599e3     32 KiB window, no window bug

- Other versions that I did not have time to write up in the thesis. All had
  very little variation.

        prototype2x1                    f464604     2x1 without memory usage fix
        prototype2x1memcfqfilebuf       bfd6f31     Using a filebuffer for reads
        prototype2x1membufwrite         856d3ea     Using buffered writes

- There are also several variations of with `deadline` or `noop` appended to
  them. Those represent runs with the I/O scheduler switched to `deadline` or
  `noop`.


### The Directory-Layout Experiment

Names in the `data/exp--filesystem-limits--micro/` directory look like this:

```
4096x02x01--2017-03-22-murphytest04.txt
```

That represents a test file size of 4096 bytes, 2 hex digits per subdirectory,
and a depth of 1, performed March 7th 2017 on `murphytest04`.

Only the `*-murphytest04.txt` results are used in the thesis.


### The Chunk-Size Experiment

The files in the `data/exp--rolling-hash/` directory that are used in the thesis
are:

```
2017-03-20--rolling-hash.txt                With window reset bug
2017-04-28--rolling-hash--no-reset.txt      No window reset bug
```

The two with `reuse-rand` in the name did not re-seed their RNG's between
trials. Looking at this confirmed that the "flat tops" of the graph were caused
by re-using the same input data, but I did not directly use them in the thesis.


Data Scripts
--------------------------------------------------

The repository also includes a few generic data processing scripts.

- `meantable.py` -- Aggregates the results of the multiple runs and calculates
  the mean and standard deviation of specified columns across all runs

- `aggregate_last_lines.sh` -- Makes a new table containing the last lines of
  many input tables. Used to analyze the directory-layout data to examine the
  state when the filesystem filled up

- `copy-results.py` -- Copies output files from the experiment computers to
  files named in `current-runs.txt`. Made it easier to keep track of the different multi-day
  experiment runs going on all four test machines at any given time.

Finally, `experiment-tracker.markdown` is my own human-readable notes on what
runs where done, what were in progress, and what needed to be done.



More About DMV
==================================================

DMV hopes to extend the distributed part of the distributed version control
concept so that the actual collection/history can be distributed across several
repositories, making it easy to transfer the files you need to the locations
where you need them and to keep everything synchronized.

DMV was created as a master's thesis project at the University of Tromsø,
Norway's Arctic University, by a student named Mike Murphy (that's me). The
prototype is definitely not ready for prime time yet, but I do think I'm on to
something here.


Documentation and other related repositories
--------------------------------------------------

At this point the best source of documentation for the project is the master's
thesis itself. An archived PDF version of the thesis is available in Munin, the
University of Tromsø's open research archive
(<http://hdl.handle.net/10037/11213>).

Beyond that there are three source repositories of interest:

1. [DMV Source Code]( https://github.com/sleepymurph/dmv), the prototype source
   code itself.
2. [DMV Publications]( https://github.com/sleepymurph/dmv-publications), LaTeX
   and other materials used to generate publication PDFs, including the master's
   thesis itself and presentation slides. Also includes experiment data.
3. [DMV Test Code]( https://github.com/sleepymurph/dmv-test-code), including
   helpers scripts used in my research and experiment/benchmark scripts.

I welcome any feedback or questions at <dmv@sleepymurph.com>.
