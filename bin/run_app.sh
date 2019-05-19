#!/bin/bash   

source myvenv/bin/activate

python manage.py migrate

python manage.py runserver
