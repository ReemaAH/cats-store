FROM python:3.7-slim


RUN mkdir /code

WORKDIR /code
ENV PYTHONPATH=/code/

COPY . /code/

RUN pip install virtualenv

RUN virtualenv env

ENV ENV=./env

RUN ./env/bin/pip install -r requirements.txt

RUN ./env/bin/python manage.py collectstatic --noinput


RUN ["chmod", "+x", "./docker-entrypoint.sh"]
