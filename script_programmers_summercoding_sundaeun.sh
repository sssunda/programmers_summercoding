#!/bin/bash   
set 

virtualenv --python=python3.6 myvenv

source myvenv/bin/activate

pip install django~=2.0

python manage.py migrate

python manage.py runserver
