FROM python:3.9

WORKDIR /app

COPY . .
RUN apt-get update && apt-get install -y npm

RUN pip install lektor
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
RUN pip install --no-cache-dir --upgrade lektor



CMD ["lektor server -f webpack","--host","0.0.0.0", "--port", "80"]
