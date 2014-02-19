#!/bin/sh

. ./docker_tools.sh

# Expose data and conf directories.
init_directory /graphite/conf /var/lib/graphite/conf
init_directory /graphite/storage /var/lib/graphite/storage

# Graphite/Carbon runs as www-data
chown -R www-data /graphite/conf /graphite/storage

# Announce the new locations
export GRAPHITE_CONF_DIR="/graphite/conf"
export GRAPHITE_STORAGE_DIR="/graphite/storage/"

exec $*
