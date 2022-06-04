# Droplet

`/api/.secrets/`
- Google auth token file (must be manually generated outside a container on a dev machine with a web browser).
- Google client secret file.

`/api/run/`
- Docker compose file.
- Docker compose production overrides file.
- Bash script that spins up the container networks.


# CI

Only one image is needed: the django web app container. It doesn't need any secrets.
```
docker build
docker push
```