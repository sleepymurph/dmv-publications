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
#
# You can define common things in an M4 macro and include it in several files.
# If you do, remember to add it to the dependency lists here.

%-dot.pdf: %.dot diagram-common.m4.dot
	m4 diagram-common.m4.dot $*.dot | dot -Tpdf -o $*-dot.pdf

%-neato.pdf: %.dot diagram-common.m4.dot
	m4 diagram-common.m4.dot $*.dot | neato -Tpdf -o $*-neato.pdf
