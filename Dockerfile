# FROM python:3.8-slim-buster
FROM python:3.10.11
ENV PYTHONDONTWRITEBYCODE=1
ENV PYTHONBUFFERED=1

WORKDIR /app
ADD requirements.txt /app/

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ADD ./core /app/

# CMD ["python3","manage.py","runserver","0.0.0.0:8000"]