###############################################################################
# Docker file for mood sync API
# Author: Anurag Bhatt
# Date: 2023-06-10
# Version: 1.0
# Description: Docker file to build the image for the Django application
# Usage: docker build .
# docker run -p 8000:8000 <image_id>
###############################################################################


FROM python:3.9-alpine3.13
LABEL maintainer="anuragbhatt1805@gmail.com"


ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        anurag
ENV PATH="/py/bin:$PATH"


USER anurag