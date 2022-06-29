FROM python:3.10.5-slim-buster

EXPOSE 9001

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install supervisor

WORKDIR /app

COPY . .

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["/usr/bin/supervisord"]