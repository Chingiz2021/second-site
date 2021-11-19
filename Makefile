start_migrate:
	docker-compose run appdjango python manage.py migrate --noinput
create_user:
	docker-compose run appdjango python manage.py createsuperuser
build:
	docker-compose up --build

up:
	docker-compose up -d

run_dev:
	docker-compose --file docker-compose.dev.yml up 