mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

csu:
	python3 manage.py createsuperuser

cov:
	pytest --cov-report html --cov .

build_index:
	python manage.py search_index --rebuild