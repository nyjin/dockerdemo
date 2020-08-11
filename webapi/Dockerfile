FROM python:3.8-slim-buster
MAINTAINER zacronan@naver.com

RUN apt-get update && apt-get install -y python3 python3-pip && pip install pipenv

RUN mkdir -p /app
COPY . /app
WORKDIR /app
RUN pipenv install --deploy --system

CMD ["pipenv", "run", "flask", "run"]