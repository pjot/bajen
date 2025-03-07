RUN=docker run -v $(PWD):/app bajen:latest

build:
	docker build . -t bajen:latest

test:
	$(RUN) pytest -v tests/

lint: black mypy

format:
	$(RUN) black .

black:
	$(RUN) black . --check

mypy:
	$(RUN) mypy .

cron:
	$(RUN) latest python cron.py
