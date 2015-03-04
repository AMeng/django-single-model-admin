.PHONY: test

install:
	pip install .
	pip install -r requirements.txt

test:
	cd test && python manage.py test app

lint:
	flake8
