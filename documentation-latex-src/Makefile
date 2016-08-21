default: ../specification.pdf

specification.pdf: \
    new-dag.pdf \
    object-db-and-working-directory.pdf \
    workflow-personal.pdf \
    workflow-corporate.pdf \
    workflow-sensors.pdf

%.pdf: %.tex %.bib
	pdflatex $*.tex
	# bibtex $*.aux
	# pdflatex $*.tex
	# pdflatex $*.tex

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

DOT_INCLUDE=diagram-common.m4.dot

# Leave intermediate files after use (e.g. %.preprocessed.dot)
.SECONDARY:

%.preprocessed.dot: %.dot $(DOT_INCLUDE)
	m4 $(DOT_INCLUDE) $*.dot > $*.preprocessed.dot

%.pdf: %.preprocessed.dot
	dot -Tpdf -o $*.pdf $*.preprocessed.dot

%.png: %.preprocessed.dot
	dot -Tpng -o $*.png $*.preprocessed.dot
