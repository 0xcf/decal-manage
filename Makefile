BIN := venv/bin
PYTHON := $(BIN)/python

venv: requirements.txt
	/usr/bin/env python3 -m venv venv
	$(BIN)/pip install -r requirements.txt

.PHONY: dev
dev: venv
	$(PYTHON) ./manage.py runserver

.PHONY: clean
clean:
	rm -rf venv

migrations: decaladmin/main/models.py
	$(PYTHON) ./manage.py makemigrations main

migrate:
	$(PYTHON) ./manage.py migrate main

cook-image: Dockerfile
	docker build -t decaladmin .

.PHONY: docker-dev
docker-dev: Dockerfile cook-image
	docker run --rm -it -p 8000:8000 -v "$$(pwd)"/decaladmin:/opt/decal/decaladmin decaladmin
