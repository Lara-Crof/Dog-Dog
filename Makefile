SHELL := /bin/bash
.DEFAULT_GOAL := default
.PHONY: all

build:
	docker build . -t dog-dog:latest

run:
	docker-compose up

default: build run