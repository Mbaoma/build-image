# FROM python:3.9-slim

# # Set the working directory in the container
# WORKDIR /action

# # Copy the Python action code to the container
# COPY . .

# # Install the dependencies
# RUN pip install -r requirements.txt

# # Set the entry point for the action
# ENTRYPOINT ["python", "/action/main.py"]

# This file is used by CI pipeline when testing this action
FROM alpine:latest

RUN apk update \
  && apk -a info curl \
  && apk add curl

# these two are passed as build args
ARG BUILD_DATE
ARG GITHUB_SHA

ENV GITHUB_SHA=$GITHUB_SHA

RUN env | sort