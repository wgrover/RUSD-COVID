all: scrape plot push

scrape:
	./scrape.py

plot: scrape
	./plot.py

push: plot
	git add .
	git commit -m "new numbers"
	git push
