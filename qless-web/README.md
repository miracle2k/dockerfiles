Runs the qless webinterface:
    https://github.com/seomoz/qless

Specify the Redis instance to connect to using a *REDIS_URL* environment variable:

    $ docker run -e REDIS_URL="redis://some-host:7000/3" elsdoerfer/qless-web

Alternatively, you can also specify *REDIS_HOST*, containing only the hostname.
