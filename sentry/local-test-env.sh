#docker run $(cat env.sh | xargs) -it -p 8080:9000 sentry start

-e SENTRY_NAME=postgres
-e SENTRY_USER=postgres
-e SENTRY_PASS=mysecretpassword
-e SENTRY_HOST=172.17.0.19
-e SENTRY_PORT=5432
-e SENTRY_ENGINE=django.db.backends.postgresql_psycopg2
-e REDIS_HOST=172.17.0.7
-e REDIS_PORT=6379
-e SENTRY_URL_PREFIX=http://docker:8080/
