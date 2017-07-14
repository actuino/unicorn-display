NS = actuino
VERSION ?= 1.0.1
REPO = unicorn-display-client

build:
	docker build --no-cache=true -t $(NS)/$(REPO) .
	docker tag $(NS)/$(REPO) $(NS)/$(REPO):$(VERSION)
push:
	docker push $(NS)/$(REPO):$(VERSION)
	docker push $(NS)/$(REPO)

default: build
