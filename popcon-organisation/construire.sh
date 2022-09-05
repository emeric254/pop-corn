#!/bin/sh

podman pull docker.io/python:3.10-alpine
podman build -t localhost/popcon-organisation:latest .
