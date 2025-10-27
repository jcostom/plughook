FROM python:3.14.0-slim-bookworm AS builder

ARG TZ=America/New_York
RUN apt update && apt -yq install gcc make
RUN pip install flask python-kasa==0.6.2.1 waitress

FROM python:3.14.0-slim-bookworm

ARG TZ=America/New_York
ARG PYVER=3.14

EXPOSE 8080/tcp

COPY --from=builder /usr/local/lib/python$PYVER/site-packages/ /usr/local/lib/python$PYVER/site-packages/

RUN mkdir /app
COPY ./app.py /app
RUN chmod 755 /app/app.py

ENTRYPOINT [ "python3", "-u", "/app/app.py" ]
