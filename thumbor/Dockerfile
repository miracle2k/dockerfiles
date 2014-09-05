FROM ubuntu:14.04
MAINTAINER elprans@sprymix.com

ENV APPDIR /srv/thumbor
ENV THUMBOR_VERSION 4.4.1
ENV THUMBOR_ENGINE graphicsmagick
ENV GRAPHICSMAGICK_ENGINE_VERSION 0.1.1

EXPOSE 8888

VOLUME ["/etc/persistent-conf"]
VOLUME ["/srv/thumbor/storage"]
VOLUME ["/dev/log"]

ENTRYPOINT ["/init"]
CMD ["start"]

RUN DEBIAN_FRONTEND=noninteractive \
        apt-get update && apt-get install --no-install-recommends -y \
            language-pack-en-base

ENV LANG en_US.UTF-8

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
                patch wget unzip python-dev python-pip \
        && apt-get clean

RUN mkdir -p /setup

ADD setup /setup
RUN DEBIAN_FRONTEND=noninteractive \
        /setup/install

ADD config /setup/config
RUN DEBIAN_FRONTEND=noninteractive \
        /setup/configure

ADD init /init
