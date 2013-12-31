FROM stackbrew/hipache

# We'll be using it to merge with the default configuration file.
RUN npm install -g jsontool

# The base supervisor conf file is a bit stupid. For example, it runs the
# redis server w/o a config file.
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Equally, the production config.json of the base points to a non-existant
# log file location.
ADD config.json /usr/local/lib/node_modules/hipache/config/config.json

# Use a wrapper script that updates the config from ENV before starting.
ADD start.sh /start
CMD ["/start"]
