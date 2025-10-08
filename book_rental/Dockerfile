FROM python:3.13.8-alpine

WORKDIR /usr/src/book_rental

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
#CMD [ "python", "manage.py", "migrate"]
#RUN chmod 777 /usr/src/book_rental/test.sh

#RUN chmod +x test.sh
#RUN python manage.py migrate
#ENTRYPOINT ["/test.sh"]
RUN chmod +x startup.sh

CMD ["/usr/src/book_rental/startup.sh"]
#CMD  [ "hypercorn", "--bind", "0.0.0.0:8000" ,"book_rental.wsgi:application" ]
#CMD [ "python", "./manage.py", "runserver" , "0.0.0.0:8000" , "--noreload" ]
#CMD [ "python", "./manage.py", "migrate" ]
