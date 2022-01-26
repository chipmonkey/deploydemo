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
	docker-compose down --remove-orphans

.PHONY: docker-rebuild
docker-rebuild: docker-stop  ## Update everything
	docker-compose build

.PHONY: v2-start
v2-start:  ## Start v2 api alone
	docker-compose up -d demo-api-v2

.PHONY: bash
bash:  ## Open dev bash shell
	docker-compose exec demo-api bash

.PHONY: sql
sql:  ## Open a psql shell
	docker compose exec demo-postgres psql -U demo -W -h localhost

.PHONY: db-init db-migrate db-upgrade
db-init:  ## Initialize the database
	docker-compose exec --env FLASK_APP=demo demo-api flask db init --directory /mnt/migrations

db-migrate:  ## Create an alembic migration for the database version
	docker-compose exec --env FLASK_APP=demo demo-api flask db migrate --directory /mnt/migrations

db-v1:  ## Apply v1 of the database
	docker-compose exec --env FLASK_APP=demo demo-api flask db upgrade --directory /mnt/migrations a5d47eb28402

db-upgrade:  ## Apply the latest database version definition
	docker-compose exec --env FLASK_APP=demo demo-api flask db upgrade --directory /mnt/migrations

.PHONY: dlogs
dlogs:  ## Follow docker-api logs
	docker-compose logs -f demo-api

reload_nginx:
	docker-compose exec demo-nginx /usr/sbin/nginx -s reload

wheel:
	pip wheel ./demo -w ./wheels --no-deps

.PHONY: perftest
perftest:
	$(MAKE) -C perftest perftest
