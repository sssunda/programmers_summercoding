#!/bin/bash   
cd /home/programmers_summercoding

set 

virtualenv --python=python3.6 myvenv

source myvent/bin/activate

pip install django~=2.0

python manage.py migrate

python manage.py runserver
