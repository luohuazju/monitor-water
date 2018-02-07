#Set up FTP in Docker

#Prepre the OS
FROM resin/raspberrypi3-python
MAINTAINER Carl Luo <luohuazju@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -y update
RUN apt-get -y dist-upgrade

#install the software
RUN pip install django
RUN pip install djangorestframework
RUN pip install markdown
RUN pip install django-filter
RUN pip install gunicorn

RUN pip install greenlet
RUN pip install gevent
RUN pip install eventlet

#start the application
EXPOSE  8000
RUN     mkdir -p /app/
ADD     start.sh /app/
WORKDIR /app/
CMD	[ "./start.sh" ]