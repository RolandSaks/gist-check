FROM python:3.8.5-slim

COPY . /app/

ENV FLASK_APP main.py
ENV FLASK_RUN_PORT 8080
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_ENV development

RUN pip3 install -r /app/requirements.txt
RUN  apt-get update \
     && apt-get install -y \
        curl

WORKDIR /app/
CMD flask run --host=0.0.0.0
