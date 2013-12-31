#!/bin/sh

# Merge configuration via environment variable into default.
config="/usr/local/lib/node_modules/hipache/config/config_generated.json"
echo $HIPACHE_CONFIG | cat /usr/local/lib/node_modules/hipache/config/config.json - | json --merge > $config

if [ -n "$SSL_KEY" ]; then
    file=$(cat $config | json server.https.key)
    echo "Writing SSL_KEY to $file"
    echo "$SSL_KEY" > file
fi

if [ -n "$SSL_CERT" ]; then
    file=$(cat $config | json server.https.cert)
    echo "Writing SSL_CERT to $file"
    echo "$SSL_CERT" > file
fi

# Start services as the base image does.
supervisord -n
