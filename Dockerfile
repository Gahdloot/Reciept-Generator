FROM python:3.11.3-slim-bullseye

WORKDIR /app

RUN apt-get -y update && apt-get install -y \
  wget

RUN pip install --upgrade setuptools

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . .

CMD cd reciepts

CMD python manage.py runserver