COMPOSE_FILE=$(CURDIR)/compose/docker-compose.yml
CONDA_PYGRAPHISTRY_ENV_FILE=$(CURDIR)/environment.yml

include ./.env

chown:
	sudo chown -R $(shell whoami) .

test: chown
	docker-compose -f $(COMPOSE_FILE) build test
	docker-compose -f $(COMPOSE_FILE) run test

jupyter: chown
	docker-compose -f $(COMPOSE_FILE) build jupyter
	docker-compose -f $(COMPOSE_FILE) up jupyter

echo:
	echo $(CURDIR)