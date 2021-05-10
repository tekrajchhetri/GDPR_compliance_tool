FROM tiangolo/uwsgi-nginx-flask:python3.8

WORKDIR ./

COPY ./requirements.txt /app/
RUN pip3 install -r /app/requirements.txt

COPY ./ /app
CMD ["uwsgi", "uwsgi.ini"]