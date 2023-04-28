# Configure environment variables
ARG PYTORCH_BASE_IMAGE="nvcr.io/nvidia/pytorch"
ARG PYTORCH_RELEASE_DATE="23.04"

# Download base image
FROM "${PYTORCH_BASE_IMAGE}:${PYTORCH_RELEASE_DATE}-py3" as base

# Install pip dependencies
ADD ./requirements.txt ./requirements.txt
RUN python3 -m pip install --no-cache-dir --requirement ./requirements.txt \
    # Cleanup
    && find /usr -type d -name '*__pycache__' -prune -exec rm -rf {} \; \
    && rm ./requirements.txt

# Configure environment variables
ENV DATA_HOME="/data"

# Configure executable entrypoint
ENTRYPOINT [ "/usr/bin/env" ]
CMD [ "./entrypoint.sh" ]

# Add your files
# NOTE: If you want to exclude some files (such as outputs) from being included,
#   you can add them to [`.dockerignore`](.dockerignore).
#   The usage is same as `.gitignore`.
ADD . /src
WORKDIR /src
