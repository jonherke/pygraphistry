COMPOSE_FILE=$(CURDIR)/compose/docker-compose.yml

include ./.env

test:
	docker-compose -f $(COMPOSE_FILE) run test

jupyter:
	docker-compose -f $(COMPOSE_FILE) up jupyter
