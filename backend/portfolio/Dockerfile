# syntax = docker/dockerfile:1.3
FROM python:3.9-slim

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN --mount=type=secret,id=env_backend_secrets ./load-env.sh
RUN --mount=type=secret,id=env_django_secrets ./load-env.sh

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]