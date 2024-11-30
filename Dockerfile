FROM python:3.13-bullseye

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app
