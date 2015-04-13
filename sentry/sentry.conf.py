
# This file is just Python, with a touch of Django which means you
# you can inherit and tweak settings to your hearts content.
from sentry.conf.server import *

import base64
import os.path

CONF_ROOT = os.path.dirname(__file__)


database_name = os.environ.get('SENTRY_NAME', 'sentry')
database_user = os.environ.get('SENTRY_USER', 'sentry')
database_password = os.environ.get('SENTRY_PASS', 'sentry')
database_host = os.environ.get('SENTRY_HOST', '127.0.0.1')
database_port = os.environ.get('SENTRY_PORT', '')

redis_host = os.environ.get('REDIS_HOST', '')
redis_port = os.environ.get('REDIS_PORT', 6379)


DATABASES = {
    'default': {
        'ENGINE': os.environ.get('SENTRY_ENGINE', 'django.db.backends.sqlite3'),  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': database_name,                      # Or path to database file if using sqlite3.
        'USER': database_user,                      # Not used with sqlite3.
        'PASSWORD': database_password,                  # Not used with sqlite3.
        'HOST': database_host,                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': database_port,                      # Set to empty string for default. Not used with sqlite3.
    }
}

# You should not change this setting after your database has been created
# unless you have altered all schemas first
SENTRY_USE_BIG_INTS = False if os.environ.get('NO_BIG_INTS', False) else True

# If you're expecting any kind of real traffic on Sentry, we highly recommend
# configuring the CACHES and Redis settings

###########
## Redis ##
###########

# Generic Redis configuration used as defaults for various things including:
# Buffers, Quotas, TSDB

SENTRY_REDIS_OPTIONS = {
    'hosts': {
        0: {
            'host': redis_host,
            'port': redis_port,
        }
    }
}

###########
## Cache ##
###########

# If you wish to use memcached, install the dependencies and adjust the config
# as shown:
#
#   pip install python-memcached
#
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': ['127.0.0.1:11211'],
#     }
# }
#
# SENTRY_CACHE = 'sentry.cache.django.DjangoCache'

SENTRY_CACHE = 'sentry.cache.redis.RedisCache'

###########
## Queue ##
###########

# See http://sentry.readthedocs.org/en/latest/queue/index.html for more
# information on configuring your queue broker and workers. Sentry relies
# on a Python framework called Celery to manage queues.

CELERY_ALWAYS_EAGER = False
BROKER_URL = 'redis://{}:{}'.format(redis_host, redis_port)

#################
## Rate Limits ##
#################

SENTRY_RATELIMITER = 'sentry.ratelimits.redis.RedisRateLimiter'

####################
## Update Buffers ##
####################

# Buffers (combined with queueing) act as an intermediate layer between the
# database and the storage API. They will greatly improve efficiency on large
# numbers of the same events being sent to the API in a short amount of time.
# (read: if you send any kind of real data to Sentry, you should enable buffers)

SENTRY_BUFFER = 'sentry.buffer.redis.RedisBuffer'

############
## Quotas ##
############

# Quotas allow you to rate limit individual projects or the Sentry install as
# a whole.

SENTRY_QUOTAS = 'sentry.quotas.redis.RedisQuota'

##########
## TSDB ##
##########

# The TSDB is used for building charts as well as making things like per-rate
# alerts possible.

SENTRY_TSDB = 'sentry.tsdb.redis.RedisTSDB'

##################
## File storage ##
##################

# Any Django storage backend is compatible with Sentry. For more solutions see
# the django-storages package: https://django-storages.readthedocs.org/en/latest/

SENTRY_FILESTORE = 'django.core.files.storage.FileSystemStorage'
SENTRY_FILESTORE_OPTIONS = {
    'location': '/tmp/sentry-files',
}

################
## Web Server ##
################

# You MUST configure the absolute URI root for Sentry:
SENTRY_URL_PREFIX = os.environ.get('SENTRY_URL_PREFIX', '')

# If you're using a reverse proxy, you should enable the X-Forwarded-Proto
# and X-Forwarded-Host headers, and uncomment the following settings
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# USE_X_FORWARDED_HOST = True

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = 9000
SENTRY_WEB_OPTIONS = {
    'workers': 3,  # the number of gunicorn workers
    'limit_request_line': 0,  # required for raven-js
    'secure_scheme_headers': {'X-FORWARDED-PROTO': 'https'},
}

#################
## Mail Server ##
#################

# For more information check Django's documentation:
#  https://docs.djangoproject.com/en/1.3/topics/email/?from=olddocs#e-mail-backends

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' if os.environ.get('SENTRY_EMAIL_ENABLED') else 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = os.environ.get('SENTRY_EMAIL_HOST', 'localhost')
EMAIL_HOST_PASSWORD = os.environ.get('SENTRY_EMAIL_PASSWORD', '')
EMAIL_HOST_USER = os.environ.get('SENTRY_EMAIL_USER','')
EMAIL_PORT = os.environ.get('SENTRY_EMAIL_PORT', 25)
EMAIL_USE_TLS = os.environ.get('SENTRY_EMAIL_USE_TLS', False)

# The email address to send on behalf of

SERVER_EMAIL = os.environ.get('SENTRY_EMAIL_FROM', 'root@localhost')

###########
## etc. ##
###########

## Set this to false to require authentication
SENTRY_PUBLIC = False
SENTRY_ALLOW_REGISTRATION = False

# If this file ever becomes compromised, it's important to regenerate your SECRET_KEY
# Changing this value will result in all current sessions being invalidated
SENTRY_KEY = os.environ.get('SENTRY_KEY', base64.urlsafe_b64encode(os.urandom(50)))

# CORS
SENTRY_ALLOW_ORIGIN = os.environ.get('SENTRY_ALLOW_ORIGIN', '')

# http://twitter.com/apps/new
# It's important that input a callback URL, even if its useless. We have no idea why, consult Twitter.
TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')

# http://developers.facebook.com/setup/
FACEBOOK_APP_ID = os.environ.get('FACEBOOK_APP_ID')
FACEBOOK_API_SECRET = os.environ.get('FACEBOOK_APP_SECRET')

# http://code.google.com/apis/accounts/docs/OAuth2.html#Registering
GOOGLE_OAUTH2_CLIENT_ID = os.environ.get('GOOGLE_OAUTH2_CLIENT_ID')
GOOGLE_OAUTH2_CLIENT_SECRET = os.environ.get('GOOGLE_OAUTH2_CLIENT_SECRET')

# https://github.com/settings/applications/new
GITHUB_APP_ID = os.environ.get('GITHUB_APP_ID')
GITHUB_API_SECRET = os.environ.get('GITHUB_APP_SECRET')

# https://trello.com/1/appKey/generate
TRELLO_API_KEY = os.environ.get('TRELLO_API_KEY')
TRELLO_API_SECRET = os.environ.get('TRELLO_API_SECRET')

# https://confluence.atlassian.com/display/BITBUCKET/OAuth+Consumers
BITBUCKET_CONSUMER_KEY = ''
BITBUCKET_CONSUMER_SECRET = ''
