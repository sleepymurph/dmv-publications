default: test-results.pdf

test-results.pdf: \
    graph--filesystem-limits--directory-takeover.pdf \
    graph--file-size--c1-cpu-a.pdf \
    graph--file-size--c1-cpu-b.pdf \
    graph--file-size--c1-time.pdf \
    graph--file-size--c1-time--detail-high-end.pdf \
    graph--file-size--c1-time--detail-high-end--prototype-improvements.pdf \
    graph--file-size--c1-time--detail-low-end.pdf \
    graph--file-size--repo-size.pdf \
    graph--increasing-number-of-files--c1-cpu-a.pdf \
    graph--increasing-number-of-files--c1-cpu-b.pdf \
    graph--increasing-number-of-files--c1-time.pdf \
    graph--increasing-number-of-files--c1-time-detail.pdf \
    graph--increasing-number-of-files--stat1-time.pdf \
    graph--increasing-number-of-files--repo-size.pdf \
    graph--increasing-number-of-files--prototype-improvements--c1-time-detail.pdf \
    graph--rolling-hash.pdf \


%.pdf: %.tex
	pdflatex $*.tex

%.pdf: %.gpi exp*/*.txt *.py *.sh
	gnuplot -e 'set terminal pdf' $*.gpi > $*.pdf
