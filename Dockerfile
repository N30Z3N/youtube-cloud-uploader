FROM python:3.7.8-slim-buster
LABEL MAINTAINER="Swetank Mohanty (shortthirdman) <swetank.mohanty@outlook.com>"

RUN python --version
RUN pip --version

WORKDIR /usr/app/src
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
COPY main.py ./
COPY ./static ./
COPY ./templates ./

ENTRYPOINT [ "gunicorn", "main:app", "--preload", "--max-requests", "1200", "--timeout", "3600" ]