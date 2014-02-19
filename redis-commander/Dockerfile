FROM ubuntu:12.04

# Make sure we have the most recent base first
RUN apt-get -y update
RUN apt-get -y upgrade

# Add PPA for recent node.js; add-apt-repository has a huge dep list, do it manually
RUN echo "deb http://ppa.launchpad.net/chris-lea/node.js/ubuntu precise main" >> /etc/apt/sources.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-key C7917B12
# rlwrap package
RUN echo "deb http://archive.ubuntu.com/ubuntu precise universe" >> /etc/apt/sources.list
# Done with package sources
RUN apt-get -y update

# Install redis-commander
RUN apt-get -y install nodejs
RUN npm install -g redis-commander

ADD /start.py /redis-commander
CMD /redis-commander
