PORT ?= 8001

data:
	python manage.py seed_site

run:
	python manage.py runserver $(PORT)
