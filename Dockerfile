FROM python:3.8

RUN apt-get update -y && apt-get upgrade -y && pip install --upgrade pip

WORKDIR /kylearthurs

COPY .

modern depency and package management.
RUN  python -m pip install -r requirements.txt

RUN pip install -e .
