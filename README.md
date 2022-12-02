# Description

Streamlit app for Cultural Index
.
<http://localhost:8080>

# Help

'https://github.com/docker/buildx#-o---outputpath-typetypekeyvalue'

Usage

```shell
make launch
```

1) Build the image for M1 MAC

```shell
make build_docker_arm
```

or

```shell
make build_docker_amd
```

"https://medium.com/geekculture/docker-build-with-mac-m1-d668c802ab96"
"https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker"

docker buildx build --tag cultural-index:latest -o type=image --platform=linux/arm64 --output=oci

docker buildx build --platform linux/arm64 --output "type=docker,name=cultural-index-arm64:latest"

docker run -p 8080:8080 cultural-index-arm64:latest

2) create a project on Scawelay
3) Get the API keys of the project
4) Create a namespace on Scawelay
5) Send the image to the Scawelay Container Registry

```shell
make publish_docker_amd_to_registry
```

or

```shell
make publish_docker_arm_to_registry
```

docker tag cultural-index-arm64:latest rg.fr-par.scw.cloud/cultural-index/cultural-index-arm64:latest

docker push rg.fr-par.scw.cloud/cultural-index/cultural-index:latest

6) Deploy the image on Serverless Container

## Docker

```shell

make build_docker
# or make build_docker_no_cache

# ensure it works as expected
make run_docker

# stop the container, from another terminal if need be
make stop_docker

make publish_docker_to_registry
```
