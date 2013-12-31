This is like the stackbrew/hipache image, but supports some environment
variables for customization:

HIPACHE_CONFIG
    Has to contain a JSON object, will be merged into
    the default config.

SSL_KEY
    The content of this variable will be saved in the location
    of server.https.key.

SSL_CERT
    Like SSL_KEY, will be saved in the location defined by
    server.https.cert.
