all: pull scrape plot push

pull:
	git pull

scrape: pull
	./scrape.py

plot: scrape
	./plot.py

push: plot
	git add .
	git commit -m "new numbers"
	git push
