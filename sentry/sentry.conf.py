import base64
import os.path
import os

CONF_ROOT = os.path.dirname(__file__)

database_name = os.environ.get('SENTRY_NAME', 'sentry')
database_user = os.environ.get('SENTRY_USER', 'sentry')
database_password = os.environ.get('SENTRY_PASS', 'sentry')
database_host = os.environ.get('SENTRY_HOST', '127.0.0.1')
database_port = os.environ.get('SENTRY_PORT', '')

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

SENTRY_KEY = os.environ.get('SENTRY_KEY', base64.urlsafe_b64encode(os.urandom(50)))


# Set this to false to require authentication
SENTRY_PUBLIC = False
SENTRY_ALLOW_REGISTRATION = False

SERVER_EMAIL = os.environ.get('SENTRY_EMAIL_FROM', 'root@localhost')

# You should configure the absolute URI to Sentry. It will attempt to guess it if you don't
# but proxies may interfere with this.
SENTRY_URL_PREFIX = os.environ.get('SENTRY_URL_PREFIX', '')

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = 9000
SENTRY_WEB_OPTIONS = {
    'workers': 3,  # the number of gunicorn workers
    'secure_scheme_headers': {'X-FORWARDED-PROTO': 'https'},  # detect HTTPS mode from X-Forwarded-Proto header
}

# Mail server configuration

# For more information check Django's documentation:
#  https://docs.djangoproject.com/en/1.3/topics/email/?from=olddocs#e-mail-backends

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' if os.environ.get('SENTRY_EMAIL_ENABLED') else 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = os.environ.get('SENTRY_EMAIL_HOST', 'localhost')
EMAIL_HOST_PASSWORD = os.environ.get('SENTRY_EMAIL_PASSWORD', '')
EMAIL_HOST_USER = os.environ.get('SENTRY_EMAIL_USER','')
EMAIL_PORT = os.environ.get('SENTRY_EMAIL_PORT', 25)
EMAIL_USE_TLS = os.environ.get('SENTRY_EMAIL_USE_TLS', False)

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

ALLOWED_HOSTS=['*']
