#!/bin/sh

export DOCKER_HOST=tcp://$DOCKER_HOST
exec $*
