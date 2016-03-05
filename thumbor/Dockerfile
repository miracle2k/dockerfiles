FROM ubuntu:14.04
MAINTAINER michael@elsdoerfer.com

ENV APPDIR /srv/thumbor
ENV THUMBOR_VERSION 6.0.0b4

EXPOSE 8888

VOLUME ["/etc/persistent-conf"]
VOLUME ["/srv/thumbor/storage"]

ENTRYPOINT ["/init"]
CMD ["start"]

RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update && apt-get install --no-install-recommends -y language-pack-en-base
ENV LANG en_US.UTF-8

# The deps defined in thumbor/requirements
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
	libcurl4-openssl-dev \
	python-numpy \
	python-opencv \
	libopencv-dev \
	libjpeg-dev \
	libpng-dev \
	libx264-dev \
	libass-dev \
	libvpx1 \
	libvpx-dev \
	libwebp-dev \
	webp \
	gifsicle \
	memcached \
	libmemcache-dev \
	libmemcached-dev \
	python-scipy \
	python-pyexiv2 \
	cython

# A bunch of dependencies of our particular deployment (some from the original forked version)
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
	libpngwriter libfaac libtiffxx0c2 libavcodec53 libavformat53 gstreamer0.10-ffmpeg libtiff4 redis-server

# thumbor needs python-dev for pip install
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
    wget unzip python-dev python-pip && apt-get clean

ADD setup.sh /setup
ADD thumbor.conf /thumbor.conf

RUN DEBIAN_FRONTEND=noninteractive \
        /setup

ADD init /init