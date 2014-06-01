FROM ubuntu

RUN apt-get update && apt-get upgrade -y

# Install packages we need
RUN apt-get install -y git npm

# Get source code
RUN cd / && git clone https://github.com/ripple/ripple-rest.git && cd /ripple-rest

# Install dependencies
# debian renamed the binary which causes problems installing some packages.
# There is also a nodejs-legacy package with the old name.
RUN sudo ln -s /usr/bin/nodejs /usr/bin/node
RUN npm install -g pg supervisor
RUN cd /ripple-rest && npm install

# Provide a config file
ADD config.json /ripple-rest/config.json

# Get going
ADD run.sh /run
RUN chmod +x /run

EXPOSE 5990
CMD /run
