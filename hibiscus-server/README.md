------------------------------------
Hibiscus Payment-Server Docker Image
------------------------------------

[Hibiscus](http://www.willuhn.de/products/hibiscus-server/) communicates with
(German) banks using the HBCI/FinTS protocol.

Usage:

    $ docker run -e PASSWORD=foo -p 8080:8080 elsdoerfer/hibiscus-server

PASSWORD is the password used to encrypt the database.

The data directory is set to ``/srv/hibiscus``.


Database
--------

By default, an embedded database will be created within the data directory.

You may use PostgreSQL or MySQL instead by specifying some environment variables:

**DB_DRIVER**: ``postgres`` (default) or ``mysql``.

**DB_ADDR**, **DB_NAME**, **DB_USERNAME**, **DB_PASSWORD**: Connection info.
