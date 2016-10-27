default: test-results.pdf

test-results.pdf: \
    graph--increasing-file-size--c1-time.pdf \
    increasing-file-size--space-comparison.pdf \
    increasing-file-count--commit-time-comparison.pdf \
    increasing-file-count--status-time-comparison.pdf \
    increasing-file-count--space-comparison.pdf \

%.pdf: %.tex
	pdflatex $*.tex

%.pdf: %.gpi exp*/*.txt
	gnuplot -e 'set terminal pdf' $*.gpi > $*.pdf
