FROM python:3.8.15-slim-buster
COPY ./app ./app
WORKDIR /app
RUN pip install -r requirement.txt
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000
