FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN apt-get update
RUN apt-get install -y gettext libgettextpo-dev
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/