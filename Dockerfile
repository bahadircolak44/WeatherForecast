FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /rest
WORKDIR /rest
COPY requirements.txt /rest/
RUN pip install -r requirements.txt
COPY . /rest/
RUN chmod 777 docker-entrypoint.sh