FROM python:3.11.3-slim-bullseye

WORKDIR /app


ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . .


CMD python manage.py runserver