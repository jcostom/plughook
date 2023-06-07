FROM python:3.12.0b2-slim-bullseye

ARG TZ=America/New_York

EXPOSE 8080/tcp

RUN pip install flask python-kasa waitress

RUN mkdir /app
COPY ./app.py /app
RUN chmod 755 /app/app.py

ENTRYPOINT [ "python3", "-u", "/app/app.py" ]