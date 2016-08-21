default: ../specification.pdf

specification.pdf: \
    new-dag-dot.pdf \
    object-db-and-working-directory-dot.pdf \
    workflow-personal-dot.pdf \
    workflow-corporate-dot.pdf \
    workflow-sensors-dot.pdf

%.pdf: %.tex %.bib
	pdflatex $*.tex
	# bibtex $*.aux
	# pdflatex $*.tex
	# pdflatex $*.tex

../%.pdf: %.pdf
	cp $*.pdf ../$*.pdf


# Diagrams with Graphviz
#
# Add diagram-whatever-dot.pdf or diagram-whatever-neato.pdf (depending on the
# program you want to use to create the graph) to the dependency list of the
# report that uses them.

DOT_INCLUDE=diagram-common.m4.dot

%-preprocessed.dot: %.dot $(DOT_INCLUDE)
	m4 $(DOT_INCLUDE) $*.dot > $*-preprocessed.dot

%-dot.pdf: %-preprocessed.dot $(DOT_INCLUDE)
	dot -Tpdf -o $*-dot.pdf $*-preprocessed.dot

%-neato.pdf: %-preprocessed.dot $(DOT_INCLUDE)
	neato -Tpdf -o $*-neato.pdf $*-preprocessed.dot
