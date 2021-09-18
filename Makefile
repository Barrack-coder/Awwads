serve:
	python3 manage.py runserver
migrate:
	python3 manage.py migrate
migrations:
	python3 manage.py makemigrations ${name}
superuser:
	python3 manage.py createsuperuser --username ${name}
collectstatic:
	python3 manage.py collectstatic