FROM ubuntu:12.04

# Add PPA for Redis 2.8; add-apt-repository has a huge dep list, do it manually
RUN echo "deb http://ppa.launchpad.net/chris-lea/redis-server/ubuntu precise main" >> /etc/apt/sources.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-key C7917B12

# Install Redis
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install redis-server

# Install our custom config
ADD redis.conf /etc/redis/redis.conf

# Persist the volume
VOLUME /var/lib/redis

EXPOSE 6379
CMD ["redis-server", "/etc/redis/redis.conf"]
