up:
	docker-compose up

down:
	docker-compose down

build:
	docker-compose build

fill-db:
	docker-compose exec web python populate.py

exec:
	docker-compose exec web /bin/sh