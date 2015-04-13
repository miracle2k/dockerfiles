docker-sentry
================

A [Docker](http://www.docker.io/) image for deploying
[Sentry 7.x](https://pypi.python.org/pypi/sentry).

Forked from grue/docker-sentry, which was forked from
crosbymichael/docker-cookbooks.


Setup
=====

You need to run separately (not included in the image):

- A PostgreSQL database.
- A Redis server.

Further, this image includes both the Sentry server and the Sentry
queue worker, so you need to run two instances of it. At the end,
you might end up with four containers.

1. Use the environmentment variables below to provide the connection
details for the database and redis.

2. Let sentry create the database with: ``docker run sentry upgrade``

3. Create a sentry user with command ``docker run -it sentry createsuperuser``

4. Run sentry and the worker. ``docker run sentry celery worker -B``



Upgrade from a previous version
-------------------------------

    $ docker run sentry sentry upgrade


Environment Variables
---------------------

### General settings
* SENTRY_URL_PREFIX - Absolute URI to sentry. This MUST be set.
* SENTRY_KEY    - Django secret key, if omitted it will generate a random one on launch

### DB settings
* SENTRY_NAME   - Sentry db name
* SENTRY_USER   - Sentry db user
* SENTRY_PASS   - Sentry db password
* SENTRY_HOST   - Sentry db host
* SENTRY_PORT   - Sentry db port
* SENTRY_ENGINE - Django db backend, defaults to sqlite

### Redis settings
* REDIS_HOST
* REDIS_PORT

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
