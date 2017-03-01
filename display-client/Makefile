NS = actuino
VERSION ?= 1
REPO = unicorn-display-client

build:
	docker build -t $(NS)/$(REPO):$(VERSION) .
push:
	docker push $(NS)/$(REPO):$(VERSION)

default: build