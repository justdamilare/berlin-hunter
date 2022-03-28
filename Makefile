build:
	go build

crawl:
	python3 pycrawler/crawler.py

run:
	go run main.go

clean: 
	rm berlin-hunter