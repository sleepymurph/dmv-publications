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

The master's thesis is available as a finished PDF in the University of Tromsø's
open research archive (TODO: LINK), so you don't have to clone and compile this
source.

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

TODO: Explain data file naming conventions



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
thesis itself. The official PDF version of the thesis is available in the
University of Tromsø's open research archive, Munin (named for one of Odin's
ravens, whose name means Memory) (TODO: LINK, AFTER I SUBMIT).

Beyond that there are three source repositories of interest:

1. [DMV Source Code]( https://github.com/sleepymurph/dmv), the prototype source
   code itself.
2. [DMV Publications]( https://github.com/sleepymurph/dmv-publications), LaTeX
   and other materials used to generate publication PDFs, including the master's
   thesis itself and presentation slides. Also includes experiment data.
3. [DMV Test Code]( https://github.com/sleepymurph/dmv-test-code), including
   helpers scripts used in my research and experiment/benchmark scripts.

I welcome any feedback or questions at <dmv@sleepymurph.com>.
