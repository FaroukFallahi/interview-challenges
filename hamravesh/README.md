# RestDockerApi

## Description
a rest api for docker containers.


## Run
```bash
docker pull registry.gitlab.com/faroukfallahi/restdockerapi:v0.1  
docker run --rm -t \
        -v /var/run/docker.sock:/var/run/docker.sock \
        -p 8000:8000 \
        rest_docker:v0.1
```

## API

- GET localhost:8000/containers
    - list of all containers (same as `docker ps -a`)
- GET localhost:8000/containers/<container_id_or_container_name>
    - returns single container with container_id or container_name
- POST localhost:8000/containers
    - create a container with this json (same as `docker run`)
    - ```json
        {
            "name": "alp",
            "image": "alpine", # required
            "env": { "env1":"val1","env2":"val2" },
            "command": "sleep 1000"
        }
    ```
    Equivalent:
    `docker run  -e env1=val1 -e env2=val2 --name alp alpine sleep 1000`
- DELETE localhost:8000/containers/<container_id_or_container_name>
    - remove container with `container_id` or `container_name` (same as `docker rm`)
        - if container is running it will be stoped the removed

### handy curls
- POST
``` bash
curl --header "Content-Type: application/json" -v \
  --request POST \
  --data '{ "name": "alp", "image": "alpine", "env": { "env1":"val1","env2":"val2" },"command": "sleep 1000"}' \
  http://localhost:8000/containers/
```
- GET 
``` bash
curl --header "Content-Type: application/json" -v \
  --request GET \
  http://localhost:8000/containers/alp
```
``` bash
curl --header "Content-Type: application/json" -v \
  --request GET \
  http://localhost:8000/containers/
```
- DELETE
``` bash
curl --header "Content-Type: application/json" -v \
  --request DELETE \
  http://localhost:8000/containers/alp
```
