include ./.env

chown:
	sudo chown -R $(shell whoami) .

test: chown
	docker-compose build test
	docker-compose run --rm test bash -c "/pygraphistry/run-tests.sh"

jupyter: chown
	docker-compose build jupyter
	docker-compose up -d jupyter
	docker-compose exec jupyter bash -c 'source activate pygraphistry-test ; pip install -e .'
