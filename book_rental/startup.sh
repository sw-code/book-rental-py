#!/bin/sh
python manage.py makemigrations
python manage.py migrate
hypercorn --bind "0.0.0.0:8000" book_rental.wsgi:application
