#!/bin/bash

# See for instructions:
# http://www.willuhn.de/products/hibiscus-server/install.php

dbconfig=/hibiscus-server/cfg/de.willuhn.jameica.hbci.rmi.HBCIDBService.properties

case "$DB_DRIVER" in

# Be sure to escape a ':' in DB_ADDR
mysql)
    echo "Configuring MySQL db connection to $DB_ADDR"
    cat > $dbconfig <<EOF
database.driver=de.willuhn.jameica.hbci.server.DBSupportMySqlImpl
database.driver.mysql.jdbcurl=jdbc\:mysql\://${DB_ADDR/:/\\:}/${DB_NAME}?useUnicode\=Yes&characterEncoding\=ISO8859_1
database.driver.mysql.username=${DB_USERNAME}
database.driver.mysql.password=${DB_PASSWORD}
EOF
    ;;

postgres)
    echo "Configuring PostgreSQL db connection to $DB_ADDR"
    cat > $dbconfig <<EOF
database.driver=de.willuhn.jameica.hbci.server.DBSupportPostgreSQLImpl
database.driver.postgresql.jdbcurl=jdbc\:postgresql\://${DB_ADDR/:/\\:}/${DB_NAME}
database.driver.postgresql.username=${DB_USERNAME}
database.driver.postgresql.password=${DB_PASSWORD}
EOF
    ;;

*)
    echo "Configuring local embedded database"
    # We'll delete the mysql config for now to use the embedded db
    rm $dbconfig
    ;;

esac


# Write configuration file based on desired database driver
exec $*
