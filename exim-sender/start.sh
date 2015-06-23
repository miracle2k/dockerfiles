#!/bin/bash

path=/etc/exim4

mkdir -p $path
echo $PRIMARY_HOST > $path/primary_host
echo "127.0.0.1 ; ::1 ;" "$ALLOWED_HOSTS" > $path/allowed_hosts

# Make sure spool directory is writable (if a mounted volume)
chown Debian-exim /var/spool/exim4

# Sort of hack to send logs to stdout
xtail /var/log/exim4 &
XTAIL_PID=$!

# Start exim
/usr/sbin/exim4 ${*:--bdf -q30m} &
EXIM_PID=$!

# Add a signal trap to clean up the child processs
clean_up() {
    echo "killing exim ($EXIM_PID)"
    kill $EXIM_PID
}
trap clean_up SIGHUP SIGINT SIGTERM

# Wait for the exim process to exit
wait $EXIM_PID
EXIT_STATUS=$?

# Kill the xtail process
echo "killing xtail ($XTAIL_PID)"
kill $XTAIL_PID

exit $EXIT_STATUS
