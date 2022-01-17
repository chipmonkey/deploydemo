# All the make things

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: docker-start
docker-start:  ## Start most recent build
	# docker-compose up -d --scale demo-api=2
	docker-compose up -d

.PHONY: docker-stop
docker-stop:  ## Murder the system
	docker-compose down

.PHONY: docker-rebuild
docker-rebuild: docker-stop  ## Update everything
	docker-compose build

.PHONY: bash
bash:  ## Open dev bash shell
	docker-compose exec demo-api bash

.PHONY: sql
sql:  ## Open a psql shell
	docker compose exec demo-postgres psql -U demo -W -h localhost

.PHONY: db-init db-migrate db-upgrade
db-init:  ## Initialize the database
	docker-compose exec --env FLASK_APP=demo demo-api flask db init

db-migrate:  ## Create an alembic migration for the database version
	docker-compose exec --env FLASK_APP=demo demo-api flask db migrate

db-upgrade:  ## Apply the latest database version definition
	docker-compose exec --env FLASK_APP=demo demo-api flask db upgrade

make-users:  ## Create 100 random user records
	docker-compose exec --env FLASK_APP=demo demo-api python makeusers.py

.PHONY: dlogs
dlogs:  ## Follow docker-api logs
	docker-compose logs -f demo-api

reload_nginx:  ## No-downtime reload nginx config
	docker-compose exec demo-nginx /usr/sbin/nginx -s reload

.PHONY: perftest
perftest:
	$(MAKE) -C perftest perftest

wheel:
	pip wheel ./demo -w ./wheels --no-deps
