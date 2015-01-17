docker-sentry
================

This is a [Docker](http://www.docker.io/) cookbook for deploying the 
[Sentry](https://pypi.python.org/pypi/sentry) realtime event logging and
aggregation platform.


Michael's setup notes
=====================

- The initial syncdb attempt probably fails due to some weird tty.
- Run again to complete.
- Then run with command "createsupseruser".

To setup the database, run the postgres server template with a shell to
access to client tool, and then do:

    CREATE USER sentry CREATEROLE NOSUPERUSER ENCRYPTED PASSWORD 'ahvo5EiyLi0Ri4vu';
    CREATE DATABASE sentry WITH OWNER sentry ENCODING = 'UTF-8';

I initially configured in pg_hba.conf:

    host all all 172.17.42.1/16   trust

and then later switched it to:

    host all all 172.17.42.1/16 md5

"ip addr show" will give you the netmask of the docker0 bridge.


Authorship History
------------------

Forked from grue/docker-sentry, which was forked from crosbymichael/docker-cookbooks.

Environment Variables
---------------------

### General settings
* SENTRY_KEY    - Django secret key, if omitted it will generate a random one on launch
* SENTRY_URL_PREFIX - Absolute URI to sentry. It will attempt to guess if not set

### DB settings
* SENTRY_NAME   - Sentry db name
* SENTRY_USER   - Sentry db user
* SENTRY_PASS   - Sentry db password
* SENTRY_HOST   - Sentry db host
* SENTRY_PORT   - Sentry db port
* SENTRY_ENGINE - Django db backend, defaults to sqlite

### Email settings
* SENTRY_EMAIL_FROM     - Address to send mail as
* SENTRY_EMAIL_ENABLED  - Set to True if you wish to use SMTP to send mail
* SENTRY_EMAIL_HOST     - SMTP host
* SENTRY_EMAIL_PASSWORD - SMTP password
* SENTRY_EMAIL_USER     - SMTP username
* SENTRY_EMAIL_PORT     - SMTP port
* SENTRY_EMAIL_USE_TLS  - Set to True to enable TLS

### API keys
* TWITTER_CONSUMER_KEY 
* TWITTER_CONSUMER_SECRET
* FACEBOOK_APP_ID
* FACEBOOK_APP_SECRET
* GOOGLE_OAUTH2_CLIENT_ID
* GOOGLE_OAUTH2_CLIENT_SECRET
* GITHUB_APP_ID
* GITHUB_APP_SECRET
* TRELLO_API_KEY
* TRELLO_API_SECRET
