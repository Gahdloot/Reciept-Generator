FROM python:3.11.3-slim-bullseye

WORKDIR /app


ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . .

EXPOSE 8000

CMD gunicorn reciepts.wsgi:application --bind 0.0.0.0:8000 --workers 3