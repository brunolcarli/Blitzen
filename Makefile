run:
	python manage.py runserver 0.0.0.0:8222 --settings=blitzen.settings.common

install:
	pip install -r blitzen/requirements/development.txt