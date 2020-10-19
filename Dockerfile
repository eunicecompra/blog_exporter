FROM python:3.9-alpine

WORKDIR /app

RUN apk update && apk add bash \
    && apk add curl \
    && curl -LO "https://github.com/vishnubob/wait-for-it/archive/master.zip" \
    && unzip -q master.zip \
    && rm -f master.zip

COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]
