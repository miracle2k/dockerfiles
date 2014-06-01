Run [ripple-rest](https://github.com/ripple/ripple-rest/):

    docker run elsdoerfer/ripple-rest

To run with a production database, specify the DATABASE_URL env variable:

    DATABASE_URL="postgres://ripple_rest_user:password@localhost:5432/ripple_rest_db"

Services runs on port 5990.

Note: If run in the foreground without -i, the output seems to halt after the first line,
though "docker logs" will show you it works.

TODO: Support custom config for rippled_servers, ssl_certs, host.
