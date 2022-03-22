# syntax = docker/dockerfile:1.3
FROM python:3.9-slim

WORKDIR /usr/src/portfolio

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY entrypoint.sh .
RUN ["chmod", "+x", "/usr/src/portfolio/entrypoint.sh"]
COPY . .

ENTRYPOINT ["/usr/src/portfolio/entrypoint.sh"]