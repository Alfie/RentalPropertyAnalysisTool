#!/bin/bash

python manage.py makemigrations propertyanalysis
python manage.py sqlmigrate propertyanalysis 0001
python manage.py migrate
