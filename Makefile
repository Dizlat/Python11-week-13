
run:
	echo "Hello World"
	python manage.py runserver

migrates:
	python manage.py makemigrations
	python manage.py migrate

super:
	python manage.py createsuperuser

