docker-sentry
================

This is a [Docker](http://www.docker.io/) cookbook for deploying the 
[Sentry](https://pypi.python.org/pypi/sentry) realtime event logging and
aggregation platform.

Authorship History
------------------

Forked from crosbymichael/docker-cookbooks, this is a continuation of his work.

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
