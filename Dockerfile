FROM jfloff/alpine-python:3.7

WORKDIR /usr/src/app

COPY ./python .

RUN \
  apk add --no-cache postgresql-libs && \
  apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
  python -m pip install -r requirements.txt --no-cache-dir && \
  apk --purge del .build-deps

CMD tail -f /dev/null
