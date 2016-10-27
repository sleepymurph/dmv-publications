default: test-results.pdf

test-results.pdf: \
    graph--increasing-file-size--c1-cpu.pdf \
    graph--increasing-file-size--c1-time.pdf \
    graph--increasing-file-size--c1-time--detail-high-end.pdf \
    graph--increasing-file-size--repo-size.pdf \
    graph--increasing-number-of-files--c1-cpu.pdf \
    graph--increasing-number-of-files--c1-time.pdf \
    graph--increasing-number-of-files--stat1-time.pdf \
    graph--increasing-number-of-files--repo-size.pdf \

%.pdf: %.tex
	pdflatex $*.tex

%.pdf: %.gpi exp*/*.txt
	gnuplot -e 'set terminal pdf' $*.gpi > $*.pdf
