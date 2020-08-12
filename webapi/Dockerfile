FROM python:3.8-slim-buster
LABEL maintainer="zacronan@naver.com"

RUN apt-get update && apt-get install -y python3 python3-pip && pip install pipenv

RUN mkdir -p /app
COPY . /app
WORKDIR /app
RUN pipenv install --deploy --system

RUN chmod +x ./entrypoint.sh
CMD ["sh", "./entrypoint.sh"]
