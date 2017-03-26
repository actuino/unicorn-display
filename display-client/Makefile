NS = actuino
VERSION ?= 2
REPO = unicorn-display-client

build:
	docker build --no-cache=true -t $(NS)/$(REPO):$(VERSION) .
push:
	docker push $(NS)/$(REPO):$(VERSION)

default: build
