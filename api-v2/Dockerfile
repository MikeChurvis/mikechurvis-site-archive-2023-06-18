FROM python:3-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /portfolio-api/source

RUN pip install virtualenv &&\
    python -m virtualenv venv &&\
    source venv/scripts/activate &&\
    pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .