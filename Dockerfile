FROM python:3.9-alpine

RUN apk update && apk add bash

WORKDIR /app

COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]
