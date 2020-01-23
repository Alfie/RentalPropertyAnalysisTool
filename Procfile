release: python manage.py makemigrations propertyanalaysis
release: python manage.py sqlmigrate propertyanalysis 0001
release: python manage.py migrate
web: gunicorn rentalapp.wsgi
