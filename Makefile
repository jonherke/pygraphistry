jupyter:
	docker-compose up jupyter

test:
	sudo rm -rf ./graphistry/test/__pycache__
	docker-compose build test
	docker-compose run --rm test bash -c "/pygraphistry/run-tests.sh"
