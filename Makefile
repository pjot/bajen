RUN=docker compose run --rm api

build:
	docker compose build api

test:
	$(RUN) pytest -v tests/

lint: black mypy

format:
	$(RUN) black .

black:
	$(RUN) black . --check

mypy:
	$(RUN) mypy .

api:
	docker compose up -d

cron:
	$(RUN) python cron.py
