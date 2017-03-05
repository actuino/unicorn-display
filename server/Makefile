NS = actuino
VERSION ?= 1
REPO = unicorn-server-armhf

build:
	docker build -t $(NS)/$(REPO):$(VERSION) .
push:
	docker push $(NS)/$(REPO):$(VERSION)

default: build