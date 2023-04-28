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
PORT=8080  # host port

docker run \
    --publish ${PORT}:8080/tcp \
    cs-project
```

## Control

> Describe in detail below how to use a running container for its purpose.

1. Create a docker container. It should be silenced (no stdout).
2. Browse to: http://localhost:8080/
2. A `Hello World!` message will be displayed on the browser screen.
