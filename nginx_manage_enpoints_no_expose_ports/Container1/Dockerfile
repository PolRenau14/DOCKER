FROM python:3.7-slim-stretch
WORKDIR /app

ADD . /app
RUN apt-get update
RUN apt-get install -y gcc
RUN pip install -r requirements.txt


# Start uwsgi
CMD [ "uwsgi", "app.ini" ]
