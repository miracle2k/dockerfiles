FROM stackbrew/hipache

# We'll be using it to merge with the default configuration file.
RUN npm install -g jsontool

# Use a wrapper script that updates the config from ENV before starting.
ADD start.sh /start
CMD ["/start"]
