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

%-dot.pdf: %.dot $(DOT_INCLUDE)
	m4 $(DOT_INCLUDE) $*.dot | dot -Tpdf -o $*-dot.pdf

%-neato.pdf: %.dot $(DOT_INCLUDE)
	m4 $(DOT_INCLUDE) $*.dot | neato -Tpdf -o $*-neato.pdf
