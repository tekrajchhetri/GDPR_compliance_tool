FROM tiangolo/uwsgi-nginx-flask:python3.8

ENV NGINX_WORKER_PROCESSES auto

MAINTAINER tekrajchhetri@gmail.com

WORKDIR ./

COPY ./requirements.txt /app/
RUN apt-get update && apt-get install -y ca-certificates
RUN pip3 install -r /app/requirements.txt
RUN pip3 install -U pip setuptools wheel
RUN pip3 install -U spacy==3.0.6
RUN python3.8 -m spacy download en_core_web_md
COPY ./ /app
CMD ["uwsgi", "uwsgi.ini"]