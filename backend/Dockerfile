# docker/backend/Dockerfile
FROM python:3.9.0-alpine

RUN mkdir -p /app
RUN mkdir -p /app/backend
RUN mkdir -p /app/backend/static

WORKDIR /app/backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update
RUN apk add bash
RUN apk --no-cache add mariadb-client
RUN apk add --no-cache mariadb-dev build-base jpeg-dev
RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install mysqlclient

ADD ./backend/requirements.txt /app/backend/
RUN pip install --no-cache -r /app/backend/requirements.txt

ADD . /app/backend

EXPOSE 8003

COPY ./backend/entrypoint.sh /app/backend/entrypoint.sh

RUN chmod +x /app/backend/entrypoint.sh