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
DATA_HOME=$(pwd)  # your data source

docker run \
    --gpus all \
    --volume ${DATA_HOME}:/data \
    --shm-size 20G \
    cs-project
```

## Control

> Describe in detail below how to use a running container for its purpose.

1. You can check the information of containerized `PyTorch` in the console output.
2. You can check the information of the mounted `DATA_HOME` directory in the console output.
