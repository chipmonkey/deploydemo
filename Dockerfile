FROM python:3.8

RUN apt-get update -y && \
    apt-get install -y build-essential

ADD requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt

ADD demo /demo
WORKDIR /demo
RUN pip install -e .

WORKDIR /mnt
