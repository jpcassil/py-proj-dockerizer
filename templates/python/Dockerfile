FROM python:3.9.16-slim-bullseye

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git;

COPY . /code/
WORKDIR /code/
ENV PYTHONPATH /code/

RUN pip install -r requirements.txt

ENTRYPOINT ["/usr/local/bin/python"]