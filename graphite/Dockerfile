# DOCKER-VERSION 0.4.0

from	ubuntu:12.04
run	echo 'deb http://us.archive.ubuntu.com/ubuntu/ precise universe' >> /etc/apt/sources.list
run	apt-get -y update

# Install required packages
run	apt-get -y install python-ldap python-cairo python-django python-twisted python-django-tagging python-simplejson python-memcache python-pysqlite2 python-support python-pip gunicorn supervisor nginx-light
run	pip install whisper supervisor-stdout
run	pip install --install-option="--prefix=/var/lib/graphite" --install-option="--install-lib=/var/lib/graphite/lib" carbon
run	pip install --install-option="--prefix=/var/lib/graphite" --install-option="--install-lib=/var/lib/graphite/webapp" graphite-web

# Add system service config
add	./nginx.conf /etc/nginx/nginx.conf
add	./supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Add configuration for the webapp
add	./initial_data.json /var/lib/graphite/webapp/graphite/initial_data.json
run echo break
add	./local_settings.py /var/lib/graphite/webapp/graphite/local_settings.py

# Add config template for carbon. We'll be copying this to a volume.
add	./carbon.conf /var/lib/graphite/conf/carbon.conf
add	./storage-schemas.conf /var/lib/graphite/conf/storage-schemas.conf
run	mkdir -p /var/lib/graphite/storage/whisper
run	touch /var/lib/graphite/storage/graphite.db /var/lib/graphite/storage/index

# Create locations for pid/log files
run     mkdir -p /var/run/graphite && chown www-data /var/run/graphite
run     mkdir -p /var/log/carbon && chown www-data /var/log/carbon

# initialize the webapp
run	cd /var/lib/graphite/webapp/graphite && python manage.py syncdb --noinput

# Nginx
expose	80
# Carbon line receiver port
expose	2003
# Carbon pickle receiver port
expose	2004
# Carbon cache query port
expose	7002

# carbon in debug mode is expected to log a lot, move out of container
volume /var/log/supervisor/

# Our start wrapper
add docker_tools.sh /docker_tools.sh
add start.sh        /start

cmd	["/start", "/usr/bin/supervisord""]

# vim:ts=8:noet:
