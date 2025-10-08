python manage.py makemigrations
python manage.py migrate

python manage.py collectstatic

pip freeze > requirements.txt

docker build -t django-immage .
