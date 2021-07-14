# syntax=docker/dockerfile:1
FROM python:3.9

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 7001
COPY . .