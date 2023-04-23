FROM python:3.8.13-slim-bullseye

WORKDIR /app

RUN apt-get -y update && apt-get install -y \
  wget

RUN pip install --upgrade setuptools

ADD requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# RUN python manage.py collectstatic

EXPOSE 8000

CMD gunicorn reciepts.wsgi:application --bind 0.0.0.0:8000
