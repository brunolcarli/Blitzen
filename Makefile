run:
	python manage.py runserver 0.0.0.0:8222 --settings=blitzen.settings.development

install:
	pip install -r blitzen/requirements/development.txt

migrate:
	python manage.py makemigrations --settings=blitzen.settings.development
	python manage.py migrate --settings=blitzen.settings.development

replit_pipeline:
	make install
	make migrate
	make run

shell:
	python manage.py shell --settings=blitzen.settings.development	