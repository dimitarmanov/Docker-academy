FROM python:latest AS builder

WORKDIR /app

COPY ./requirements.txt /app
RUN apt-get update && apt-get install -y npm
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app

CMD ["lektor", "server", "-f", "webpack", "--host", "0.0.0.0", "--port", "8080"]

