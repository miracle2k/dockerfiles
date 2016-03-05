Docker Thumbor container
========================

Adapted from https://github.com/sprymix/docker-thumbor.

sicle engine, gifs


Usage:
------

    $ docker run -p 80:8888 elsdoerfer/thumbor
    $ wget http://dockerip:80/unsafe/300x0/smart/http://i.imgur.com/MwZwcOY.jpg


Configuration
-------------

The container comes with a default configuration, that includes:

- Using OpenCV feature/face detection (in non-lazy mode).
- Using the filesystem storage, in ``/srv/thumbor/storage``.
- Unsafe urls are enabled.
- The Sentry **raven** package is installed, but Sentry-based error reporting
   is not enabled by default, use the ``CONFIG`` option.

You can find the full default configuration in the ``./config`` directory.

To customize the configuration, you have two options:

First, you can provide the file ``/etc/persistent-conf/thumbor.conf`` via
mounting. The contents of this file will be appended to the default
configuration.

Second, you can provide the environment variable ``CONFIG``, which will
be appended to the default configuration.


Volumes
-------

/srv/thumbor/storage
    In the default configuration, this is the image cache.

/etc/persistent-conf
    A place to mount in custom configuration.


Environment variables
---------------------

CONFIG
   Custom configuration; inserted directly into the Python-syntax
   configuration file.

SECURITY_KEY
    Sets the security key and disallows **"unsafe"** urls.
    This is applied after CONFIG.


Note
----

This message:

"libdc1394 error: Failed to initialize libdc1394"

from OpenCV seems to be a warning only.
