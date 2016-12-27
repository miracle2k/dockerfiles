FROM ubuntu:16.04

RUN apt-get update
RUN apt-get -y upgrade

# We'll be needing to compile native Ruby extensions (thin/EventMachine).
# Put it up here for re-use.
RUN apt-get -y install build-essential

# Install ruby and rubygems
RUN apt-get -y install rubygems
# Again, ruby dev libs required to build EventMachine.
RUN apt-get -y install ruby-dev

RUN gem install --no-ri --no-rdoc qless -v 0.10.2

# There are more dependencies that the current git version packaged here
# does not seem to properly declare, see:
# https://github.com/seomoz/qless/issues/172
RUN gem install --no-ri --no-rdoc sinatra -v "~>1.3.2"
RUN gem install --no-ri --no-rdoc vegas -v "~>0.1.1"

# I'm guessing this may be legitimately not included in the gem.
# It's probably like gunicorn.
RUN gem install thin --no-ri --no-rdoc

# Make sure we run on UTF8. The qless web interface will run into encoding
# trouble otherwise; without this the system locale is POSIX, and Ruby 
# by default tries to read US-ASCII when calling things like JSON.parse.
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8 

# HTTP
EXPOSE 5678


# Giving the redis url to qless-web can be done via an environment variable
# (alternative: --url-file option). We need to have a runner script for this.
ADD run /qless-web


CMD ["/qless-web"]
