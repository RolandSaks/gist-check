FROM python:3.8.5-slim

COPY . /app/

RUN pip3 install -r /app/requirements.txt
RUN  apt-get update \
     && apt-get install -y \
        curl

WORKDIR /app/
CMD python3 main.py
