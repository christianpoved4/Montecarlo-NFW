LATEX = pdflatex
MAIN  = ms

all: $(MAIN).pdf

$(MAIN).pdf: 	$(MAIN).tex  
	$(LATEX) $(MAIN).tex 
	bibtex $(MAIN)
	$(LATEX) $(MAIN).tex 
	$(LATEX) $(MAIN).tex 

diff:	$(MAIN)_diff.pdf

$(MAIN)_diff.pdf: $(MAIN).tex $(MAIN)_old.tex
	latexdiff $(MAIN)_old.tex $(MAIN).tex > $(MAIN)_diff.tex
	$(LATEX) $(MAIN)_diff.tex 
#	bibtex $(MAIN)_diff
	$(LATEX) $(MAIN)_diff.tex 
	$(LATEX) $(MAIN)_diff.tex 

tar : 
	tar -czvf $(MAIN).tar.gz $(MAIN).tex mn2e.cls  mn2e.bst error.pdf avg_foff_bolshoi.pdf  error_conc_bolshoi.pdf concentration_bolshoi.pdf concentration_bolshoi_corrected.pdf paper.pdf 


clean:
	rm -f $(MAIN).pdf $(MAIN).out $(MAIN).bbl $(MAIN).aux $(MAIN)_diff.pdf *~

view: 
	open $(MAIN).pdf &

