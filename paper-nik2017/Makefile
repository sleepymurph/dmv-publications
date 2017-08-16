# TODO: CHANGE TO NAME OF OTHER FILES
# default: dmv-nik.pdf
default: ../dmv-nik.pdf

dmv-nik.pdf: \
    dmv-nik*.tex \
    dmv-nik.bib \
    dmv-nik-abstract.txt \
    dia_architecture.pdf \
    dia_dmv_dag_example_three_commits.pdf \


%.pdf: %.tex %.bib
	pdflatex $*.tex
	bibtex $*.aux
	pdflatex $*.tex
	pdflatex $*.tex

../%.pdf: %.pdf
	cp $*.pdf ../$*.pdf


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

DOT_INCLUDE=

%.preprocessed.dot: %.dot $(DOT_INCLUDE)
	m4 $(DOT_INCLUDE) $*.dot > $*.preprocessed.dot

%.pdf: %.preprocessed.dot
	dot -Tpdf -o $*.pdf $*.preprocessed.dot

%.png: %.preprocessed.dot
	dot -Tpng -o $*.png $*.preprocessed.dot
