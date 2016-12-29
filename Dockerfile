#FROM hypriot/rpi-alpine-scratch
FROM forumi0721/alpine-armv7h-gpio-rpi
MAINTAINER Andrew Petelin <petelin78@gmail.com>

RUN apk update && \
apk upgrade && \
apk add bash  

# RUN rm -rf /var/cache/apk/*
# CMD ["/bin/bash"]  

# basic flask environment
RUN apk add git nginx uwsgi uwsgi-python3 && \ 
	pip3 install --upgrade pip && \
	pip3 install flask 

RUN apk update && apk add gcc && apk add python3-dev 
RUN apk add musl-dev && pip3 install RPi.GPIO

# application folder
ENV APP_DIR /app

# app dir
RUN mkdir ${APP_DIR} \
	&& chown -R nginx:nginx ${APP_DIR} \
	&& chmod 777 /run/ -R \
	&& chmod 777 /root/ -R 


VOLUME ${APP_DIR}
WORKDIR ${APP_DIR}

# expose web server port
# only http, for ssl use reverse proxy
EXPOSE 80

# copy config files into filesystem
COPY nginx.conf /etc/nginx/nginx.conf
COPY app.ini /app.ini
COPY entrypoint.sh /entrypoint.sh

# exectute start up script
ENTRYPOINT ["/entrypoint.sh"]
