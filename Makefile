#!/bin/bash

default: build

build:
	docker build -t aepetelin/alpine-flask-gpio . 

run:
	docker run --name flask8 --restart=always \
		--privileged --device=/dev/mem \
		-p 8096:80 \
		-v ~/projects/flask7/app/:/app \
		-d aepetelin/alpine-flask-gpio

run83:
	docker run --name flask83 --restart=always \
		--device /dev/ttyAMA0:/dev/ttyAMA0 --device /dev/mem:/dev/mem \
		--privileged \
		-p 8098:80 \
		-v ~/projects/flask7/app/:/app \
		-d aepetelin/alpine-flask-gpio 
		
run84:
	docker run --name flask84 --restart=always \
		--device /dev/ttyAMA0:/dev/ttyAMA0 --device /dev/mem:/dev/mem --device /dev/gpiomem:/dev/gpiomem \
		--privileged \
		-p 8099:80 \
		-v ~/projects/flask7/app/:/app \
		-d aepetelin/alpine-flask-gpio 

