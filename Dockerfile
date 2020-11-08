FROM python:3.8-alpine

ENV PATH ="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-chae --virtual .tmp gcc libc-dev linux-header
RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mdkir /app
COPY ../DNA_backend /app
WORKDIR /app
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mdir -p /vol/web/static



