# CTFInstancer
Standalone docker instancer for CTF challenges, particularly web ones. Compatible with docker compose.

## A word of caution
If you are here because this was used in a CTF, this instancer is not part of the challenge. Do not waste your time.
I did not make this with security or efficiency in mind. I just wanted to make something fast to develop, and easy to understand and use.

## Deployment
To run the instancer:
```
$ docker build -t instancer .
$ docker run -v "/var/run/docker.sock:/var/run/docker.sock" -p 80:80 instancer
```

The second command mounts the host's socket to allow sharing of the daemon between the container and the host. This also means that instances
of the challenge will appear on the host's daemon as well.

## Customisation
These files go in the same directory as `docker-compose.yaml`.

`run-compose.sh` is responsible for managing the creation and deletion of docker containers.
If you want to set an instance timeout, edit environment variables, or customise the container building process, this is where to do it.

`app.py` is responsible for serving the instancer to CTF players. Port allocation and subprocess creation is done here.
This will be where you can change port bindings or the execution of `run-compose.sh`.

`templates/index.html` is the instancer's main page. This is where you can edit the instancer's UI.
