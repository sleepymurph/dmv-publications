default: \
    ../design-document.pdf \
    ../design-document-2-short.pdf \
    ../thesis.pdf \


thesis.pdf: \
    thesis.tex \
    research.bib \
    dia_architecture.pdf \
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

	pdflatex thesis.tex
	bibtex thesis.aux
	pdflatex thesis.tex
	pdflatex thesis.tex


design-document.pdf: \
    design-document.tex \
    research.bib \
    dia_new_dag.pdf \
    dia_obj_db_and_wd.pdf \
    dia_workflow_personal.pdf \
    dia_workflow_corporate.pdf \
    dia_workflow_sensors.pdf \



design-document-2-short.pdf: \
    design-document-2-short.tex \
    research.bib \
    dia_architecture.pdf \


# General LaTeX

%.pdf: %.tex
	pdflatex $*.tex
	pdflatex $*.tex

../%.pdf: %.pdf
	cp $*.pdf ../$*.pdf


# Plots with GnuPlot

%.pdf: %.gpi ../data/** *.sh
	gnuplot -e 'set terminal pdf' $*.gpi > $*.pdf


# Diagrams with Graphviz
#
# These are generic rules to render Graphviz graphs with an M4 processing step.
# PDF seems to be the best vector graphics format for including in LaTeX
# documents.
#
# X.dot -> (m4) X.preprocessed.dot -> (dot) X.pdf OR X.png
#
# You can create a commin file of M4 macros to be used in all documents. Just
# add it to the DOT_INCLUDE variable.
#
# If a specific diagram needs to be processed with Neato or other Graphviz
# program, you can create a more specific rule for that diagram.
#

DOT_INCLUDE=dia_common.m4.dot

# Leave intermediate files after use (e.g. %.preprocessed.dot)
.SECONDARY:

%.preprocessed.dot: %.dot $(DOT_INCLUDE)
	m4 $(DOT_INCLUDE) $*.dot > $*.preprocessed.dot

%.pdf: %.preprocessed.dot
	dot -Tpdf -o $*.pdf $*.preprocessed.dot

%.png: %.preprocessed.dot
	dot -Tpng -o $*.png $*.preprocessed.dot
