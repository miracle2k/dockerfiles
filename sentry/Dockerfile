FROM ubuntu

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y language-pack-en
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN locale-gen en_US.UTF-8
RUN dpkg-reconfigure locales

RUN apt-get install -y openssh-server git-core libxml2-dev curl python build-essential make gcc python-dev wget
RUN apt-get install -y postgresql-client postgresql-client-common libpq5
RUN apt-get install -y libpq-dev
RUN apt-get install -y mysql-client
RUN apt-get install -y libmysqlclient-dev
RUN apt-get install -y python-distribute
RUN apt-get install -y libxml2-dev libxslt1-dev python-dev
RUN apt-get install -y libffi-dev

RUN wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
RUN python get-pip.py

RUN pip install psycopg2
RUN pip install MySQL-python
RUN pip install sentry==7.4.3

EXPOSE 9000

ADD sentry.conf.py /sentry.conf.py

ENTRYPOINT ["/usr/local/bin/sentry", "--config=/sentry.conf.py"]

CMD ["start"]