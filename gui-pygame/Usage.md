# Usage

## Build

> The commands below **cannot be modified**. Be sure to implement the Dockerfile so that it can run.
> If you need more than one `Dockerfile` , you can add the command below.

```bash
docker build --tag cs-project .
```

## Run

> Please replace the `run-argument` and `argument` items with specific descriptions.

```bash
# NOTE: You can learn more about `GUI` to: https://github.com/mviereck/x11docker

docker run \
    --env DISPLAY=$DISPLAY \
    --volume /dev/snd:/dev/snd \
    --volume /tmp/.X11-unix:/tmp/.X11-unix \
    cs-project
```

## Control

> Describe in detail below how to use a running container for its purpose.

1. A desktop app is created.
2. You can adjust the spawning position of star particles by clicking on the screen with the mouse.
