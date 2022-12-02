SHELL := /bin/bash
.PHONY : all

SOURCE_CODE = src

IMAGE_NAME := cultural-index-arm64:latest
IMAGE_NAME_ARM:= cultural-index-arm64:latest
IMAGE_NAME_AMD:=cultural-index-amd64:latest
REGISTRY := rg.fr-par.scw.cloud/cultural-index
PROFILE := cultural-index

PORT := 8080

########
# DEV  #
########

help:
	cat Makefile

# format code
fmt:
	python -m black $(SOURCE_CODE)
	python -m isort --profile black $(SOURCE_CODE)

poetry_export:
	poetry export --without-hashes --format=requirements.txt > requirements.txt

########
# OPS  #
########

registry__login:
	docker login $(REGISTRY) -u nologin --password-stdin <<< $(SCW_SECRET_KEY)

registry__list:
	scw registry image list --profile $(PROFILE)

build_docker:
	docker build -t $(IMAGE_NAME) .

build_docker_arm:
	docker buildx build --platform linux/arm64 --output "type=docker,name=$(IMAGE_NAME_ARM)" .

build_docker_amd:
	docker buildx build --platform linux/amd64 --output "type=docker,name=$(IMAGE_NAME_AMD)" .


build_docker_no_cache:
	docker build -t $(IMAGE_NAME) --no-cache .

stop_docker:
	docker stop $$(docker ps -q --filter ancestor=$(IMAGE_NAME))

stop_docker_arm:
	docker stop $$(docker ps -q --filter ancestor=$(IMAGE_NAME_ARM))

run_docker:
	docker run --net=host $(IMAGE_NAME)

run_docker_mac:
	docker run -p 8080:8080 $(IMAGE_NAME)

run_docker_mac_amd:
	docker run -p 8080:8080 $(IMAGE_NAME_AMD)

run_docker_mac_arm:
	docker run -p 8080:8080 $(IMAGE_NAME_ARM)

publish_docker_to_registry:
	docker tag $(IMAGE_NAME) $(REGISTRY)/$(IMAGE_NAME)
	docker push $(REGISTRY)/$(IMAGE_NAME)

publish_docker_amd_to_registry:
	docker tag $(IMAGE_NAME_AMD) $(REGISTRY)/$(IMAGE_NAME_AMD)
	docker push $(REGISTRY)/$(IMAGE_NAME_AMD)

publish_docker_arm_to_registry:
	docker tag $(IMAGE_NAME_ARM) $(REGISTRY)/$(IMAGE_NAME_ARM)
	docker push $(REGISTRY)/$(IMAGE_NAME_ARM)

container__list:
	scw container container list --profile $(PROFILE)

container__get:
	scw container container get $(ID)

launch:
	python -m streamlit run src/app.py
