# TODO: CHANGE TO NAME OF OTHER FILES
# default: dmv-nik.pdf
default: ../dmv-nik.pdf

## Specific documents

dmv-nik.pdf: \
    dmv-nik*.tex \
    dmv-nik.bib \
    dmv-nik-abstract.txt \
    dia_dmv_dag_example_three_commits.pdf \
    dia_new_dag.pdf \
    plot-file-size--c1-time.pdf \
    plot-num-files--c1-time.pdf \




## Generic LaTeX

%.pdf: %.tex %.bib
	pdflatex $*.tex
	bibtex $*.aux
	pdflatex $*.tex
	pdflatex $*.tex

../%.pdf: %.pdf
	cp $*.pdf ../$*.pdf


## Plots with GnuPlot

%.pdf: \
    %.gpi \
    #*-common.gpi \
    ../data/** \
    ../data/meantable.py \
    #*.sh \

	gnuplot -e 'set terminal pdf monochrome size 3in,2in' $*.gpi > $*.pdf

%.svg: \
    %.gpi \
    #*-common.gpi \
    ../data/** \
    ../data/meantable.py \
    #*.sh \

	gnuplot -e 'set terminal svg size 480,360' $*.gpi > $*.svg

## Diagrams with Graphviz
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

%.preprocessed.dot: %.dot $(DOT_INCLUDE)
	m4 $(DOT_INCLUDE) $*.dot > $*.preprocessed.dot

%.pdf: %.preprocessed.dot
	dot -Tpdf -o $*.pdf $*.preprocessed.dot

%.png: %.preprocessed.dot
	dot -Tpng -o $*.png $*.preprocessed.dot
