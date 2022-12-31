FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /django_grapql

RUN pip install --upgrade pip
COPY requirements.txt /django_grapql/requirements.txt
RUN pip install -r requirements.txt

COPY . /django_grapql/