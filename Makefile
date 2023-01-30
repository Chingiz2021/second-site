start_migrate:
	docker-compose run appdjango python manage.py migrate --noinput
create_user:
	docker-compose run appdjango python manage.py createsuperuser
build:
	docker-compose up --build

up:
	docker-compose up -d

run_dev:
	sudo docker-compose --file docker-compose.dev.yml up

dump:
	docker exec -i data_appsdb /bin/bash -c "PGPASSWORD=postgres pg_dump --username postgres postgres" > dump11.sql

docker-compose run backend python manage.py startapp bot