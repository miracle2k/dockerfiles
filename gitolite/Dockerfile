FROM ubuntu

MAINTAINER Mike Gardiner <conversationing@gmail.com>

RUN apt-get update

RUN apt-get -y install sudo
RUN apt-get -y install openssh-server
RUN apt-get -y install git

RUN locale-gen en_US.UTF-8
RUN dpkg-reconfigure locales

RUN mkdir /var/run/sshd

RUN adduser --system --group --shell /bin/sh git
RUN su git -c "mkdir /home/git/bin"

RUN cd /home/git; su git -c "git clone git://github.com/sitaramc/gitolite";
RUN cd /home/git; su git -c "gitolite/install -ln";

ADD ./init.sh /init
RUN chmod +x /init
ENTRYPOINT ["/init", "/usr/sbin/sshd", "-D"]

EXPOSE 22
