SHELL := /bin/bash
PYTHON_ENV = . venv/bin/activate && 
NODE_ENV = npm run --prefix vue_frontend/

build:
	python3 -m venv venv
	$(PYTHON_ENV) pip3 install -r requirements.txt
	npm install --prefix vue_frontend
	
migrations:
	$(PYTHON_ENV) python manage.py makemigrations
	$(PYTHON_ENV) python manage.py migrate

vue_build:
	$(NODE_ENV) build

start:
	$(PYTHON_ENV) python manage.py runserver


build_and_start: build migrations vue_build start

vue_dev:
	$(NODE_ENV) dev

sass_compile:
	$(PYTHON_ENV) python manage.py sass app/static/scss/style.scss app/static/css/style.min.css -t compressed
	$(PYTHON_ENV) python manage.py sass app/static/scss/home_style.scss app/static/css/home_style.min.css -t compressed
	
