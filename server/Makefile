NS = actuino
VERSION ?= 1.0.1
REPO = unicorn-server-armhf

build:
	docker build --no-cache=true -t $(NS)/$(REPO) .
	docker tag $(NS)/$(REPO) $(NS)/$(REPO):$(VERSION)
push:
	docker push $(NS)/$(REPO):$(VERSION)
	docker push $(NS)/$(REPO)

default: build