build:
	docker build . -t bajen:latest --no-cache

cron:
	docker run -v $(PWD):/app bajen:latest python cron.py
