#!/bin/bash

default: build

build:
	docker build -t aepetelin/alpine-flask . 

run:
	docker run --name flask7 --restart=always \
		-p 8094:80 \
		-v ~/projects/flask7/app/:/app \
		-d aepetelin/alpine-flask 
