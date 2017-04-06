default: results.pdf

results.pdf: \
    plot-filesystem-limits--directory-takeover.pdf \
    plot-file-size--c1-cpu-a.pdf \
    plot-file-size--c1-cpu-b.pdf \
    plot-file-size--c1-time.pdf \
    plot-file-size--c1-time--detail-high-end.pdf \
    plot-file-size--c1-time--detail-high-end--prototype-improvements.pdf \
    plot-file-size--c1-time--detail-low-end.pdf \
    plot-file-size--repo-size.pdf \
    plot-num-files--c1-cpu-a.pdf \
    plot-num-files--c1-cpu-b.pdf \
    plot-num-files--c1-time.pdf \
    plot-num-files--c1-time-detail.pdf \
    plot-num-files--stat1-time.pdf \
    plot-num-files--repo-size.pdf \
    plot-num-files--prototype-improvements--c1-time-detail.pdf \
    plot-rolling-hash.pdf \


%.pdf: %.tex
	pdflatex $*.tex

%.pdf: %.gpi exp*/*.txt *.py *.sh
	gnuplot -e 'set terminal pdf' $*.gpi > $*.pdf
