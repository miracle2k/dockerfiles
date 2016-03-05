#!/bin/bash

set -e

# Install thumbor
pip install thumbor==${ver}
pip install opencv-engine

# For sentry error reporting
pip install "raven<5"


cat /setup/config/thumbor.conf >> /etc/thumbor.conf
cat /setup/config/thumbor-${THUMBOR_ENGINE}.conf >> /etc/thumbor.conf

mkdir -p "${APPDIR}"
chown www-data:www-data "${APPDIR}"
