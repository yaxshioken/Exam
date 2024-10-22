mig:
	python3 manage.py makemigrations
	python3 manage.py migrate
runs:
	python3 manage.py runserver