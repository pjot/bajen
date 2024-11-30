build:
	docker build . -t bajen:latest

cron:
	docker run -v $(PWD):/app bajen:latest python cron.py
