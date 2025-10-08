FROM python:3.13.8-alpine

WORKDIR /usr/src/book_rental

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#EXPOSE 8000
CMD [ "hypercorn", "--bind", "0.0.0.0:8000" ,"book_rental.wsgi:application" ]
#CMD [ "python", "./manage.py", "runserver" , "0.0.0.0:8000" , "--noreload" ]
