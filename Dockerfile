FROM python:3.11.0-alpine

WORKDIR /usr/srv

COPY requirements.txt /usr/srv/requirements.txt

RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
         openssl-dev libffi-dev gcc musl-dev python3-dev \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r /usr/srv/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /usr/srv/
