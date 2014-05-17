Hibiscus Payment-Server Docker Image
------------------------------------

[Hibiscus](http://www.willuhn.de/products/hibiscus-server/) communicates with
(German) banks using the HBCI/FinTS protocol.

Usage:

    $ docker run -e PASSWORD=foo -p 8080:8080 elsdoerfer/hibiscus-server

PASSWORD is the password used to encrypt the database.
