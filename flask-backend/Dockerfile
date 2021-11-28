FROM python:alpine

RUN apk --no-cache --update-cache add g++ musl-dev postgresql-dev

WORKDIR /usr/src/flask

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
