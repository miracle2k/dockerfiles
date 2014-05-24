Run [ripple-rest](https://github.com/ripple/ripple-rest/):

    docker run elsdoerfer/ripple-rest

To run with a production database, specify the DATABASE_URL env variable:

    DATABASE_URL="postgres://ripple_rest_user:password@localhost:5432/ripple_rest_db"

Services runs on port 5990.

TODO: Support custom config for rippled_servers, ssl_certs, host.
