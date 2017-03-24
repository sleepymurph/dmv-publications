default: test-results.pdf

test-results.pdf: \
    graph--filesystem-limits--directory-takeover.pdf \
    graph--increasing-file-size--c1-cpu-a.pdf \
    graph--increasing-file-size--c1-cpu-b.pdf \
    graph--increasing-file-size--c1-time.pdf \
    graph--increasing-file-size--c1-time--detail-high-end.pdf \
    graph--increasing-file-size--c1-time--detail-low-end.pdf \
    graph--increasing-file-size--repo-size.pdf \
    graph--increasing-number-of-files--c1-cpu.pdf \
    graph--increasing-number-of-files--c1-time.pdf \
    graph--increasing-number-of-files--c1-time-detail.pdf \
    graph--increasing-number-of-files--stat1-time.pdf \
    graph--increasing-number-of-files--repo-size.pdf \
    graph--rolling-hash.pdf \


%.pdf: %.tex
	pdflatex $*.tex

%.pdf: %.gpi exp*/*.txt *.py *.sh
	gnuplot -e 'set terminal pdf' $*.gpi > $*.pdf
