FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/be
COPY src ./be


RUN pip install --upgrade pip && pip install -r requirements.txt