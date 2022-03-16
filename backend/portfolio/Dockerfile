# syntax = docker/dockerfile:1.3
FROM python:3.9-slim

# Give the static files a place to go.
RUN mkdir -p /var/www/portfolio/static

WORKDIR /usr/src/portfolio

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN ["chmod", "+x", "/usr/src/portfolio/entrypoint.sh"]
COPY . .

ENTRYPOINT ["/usr/src/portfolio/entrypoint.sh"]