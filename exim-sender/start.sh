#!/bin/sh

path=/etc/exim4

mkdir -p $path
echo $PRIMARY_HOST > $path/primary_host
echo "127.0.0.1 ; ::1 ;" "$ALLOWED_HOSTS" > $path/allowed_hosts

# Make sure spool directory is writable (if a mounted volume)
chown Debian-exim /var/spool/exim4

# Sort of hack to send logs to stdout
xtail /var/log/exim4 &
# Note: Using exec here means Ctrl-C via an attached docker client no
# longer works - it sends the key strokes to the non-existant shell
# process, I assume.
/usr/sbin/exim4 ${*:--bdf -q30m}
