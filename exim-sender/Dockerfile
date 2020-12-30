FROM ubuntu:20.04

RUN DEBIAN_FRONTEND='noninteractive' apt-get update && \
                                     apt-get install -y apt-utils && \
                                     apt-get -y upgrade

RUN DEBIAN_FRONTEND='noninteractive' apt-get install -y exim4
RUN DEBIAN_FRONTEND='noninteractive' apt-get install -y xtail

# We control the config outselves entirely
RUN rm -rf /etc/exim4 && mkdir -p /etc/exim4
ADD exim4.conf /etc/exim4/exim4.conf

ADD start.sh /exim
RUN chmod +x /exim

VOLUME /var/spool/exim4

ENTRYPOINT ["/exim"]
