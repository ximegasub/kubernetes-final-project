FROM python:3.8-slim-buster as build
EXPOSE 8000
COPY . .
RUN pip install --no-cache-dir --upgrade wheel setuptools pip
RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get -y install gcc
RUN apt install -y default-libmysqlclient-dev
RUN pip3 install -r requirements.txt
WORKDIR src/
ENV FLASK_APP=app.py

CMD ["flask", "run", "--port=8000", "--host=0.0.0.0"]