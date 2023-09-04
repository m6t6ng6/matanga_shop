# precios_locos_web



INSTALLATION IN TARGET SYSTEM

flask_app.py -> listens on 0.0.0.0 TCP/ 8000

1) Login to Docker Hub

docker login -u "<username>" -p "<password>" docker.io

2) Pull latest docker container

docker pull m6t6ng6/precios_locos_web_lite:latest

3) Run docker for this container in the target machine as a daemon

docker run --rm --name precios_locos_web -d -p 80:8000 m6t6ng6/precios_locos_web_lite



BUILD FOR LINUX/ AMD64 IN M1

1) BUILD THE IMAGE FOR PLATFORM LINUX/ AMD64

docker build -t m6t6ng6/precios_locos_web_lite . --no-cache --platform linux/amd64

2) CHECK IF THE IMAGE IS COMPATIBLE WITH PLATFORM LINUX/ AMD64

docker image inspect <image_id> | grep -i Architecture
        "Architecture": "amd64",

SOURCE: https://www.macstadium.com/blog/building-docker-images-on-apple-silicon-with-buildx

