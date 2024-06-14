#!/bin/bash

# Run the project

docker run --rm -it --name torch-flask \
    -p 5000:5000 \
    torch-flask:latest