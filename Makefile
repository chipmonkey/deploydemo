.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: all
all: load-users  ## Load users and open docs
	open http://localhost:8000/docs

.PHONY: docker-start
docker-start:  ## Start most recent build
	docker compose up -d

.PHONY: docker-stop
docker-stop:  ## Murder the system
	docker compose down

.PHONY: docker-rebuild
docker-rebuild: docker-stop  ## Update everything
	docker compose build

.PHONY: load-users
load-users: docker-start  ## Load users
	docker compose exec demo-bash python3 example.py

.PHONY: bash
bash:  ## Open dev bash shell
	docker compose exec demo-bash bash