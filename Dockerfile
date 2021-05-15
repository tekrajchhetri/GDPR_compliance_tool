FROM tiangolo/uwsgi-nginx-flask:python3.8

MAINTAINER tekrajchhetri@gmail.com

WORKDIR ./

COPY ./requirements.txt /app/
RUN apt-get update && apt-get install -y ca-certificates
RUN pip3 install -r /app/requirements.txt

COPY ./ /app
CMD ["uwsgi", "uwsgi.ini"]