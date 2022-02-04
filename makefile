all: scrape plot

scrape:
	./scrape.py

plot: scrape
	./plot.py