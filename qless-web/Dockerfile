FROM ubuntu:12.04

RUN apt-get update
RUN apt-get -y upgrade

# Install ruby and rubygems
RUN apt-get -y install rubygems1.9.1

# We need the git version of qless, since the released one is old and broken.
# Installing from git on the server is a mess, so I simply prebuilt the gem,
# using version 038a438f73d7af2c82541cdc0b1c5d12879a7bad and the command:
# "gem build qless.gemspec".
ADD qless-0.10.0.pre.gem /tmp/qless-0.10.0.pre.gem
RUN gem install --no-ri --no-rdoc /tmp/qless-0.10.0.pre.gem

# There are more dependencies that the current git version packaged here
# does not seem to properly declare, see:
# https://github.com/seomoz/qless/issues/172
RUN gem install --no-ri --no-rdoc sinatra -v "~>1.3.2"
RUN gem install --no-ri --no-rdoc vegas "~>0.1.1"

# Installing thin requires EventMachine requires compiling native stuff
RUN apt-get install build-essential ruby1.9.1-dev
RUN gem install thin--no-ri --no-rdoc


# HTTP
EXPOSE 5678


# Giving the redis url to qless-web can be done via an environment variable
# (alternative: --url-file option). We need to have a runner script for this.
ADD run /start


CMD ["/start"]
