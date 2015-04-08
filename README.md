# Multiquery

Runs a single SQL query against a set of databases concatenates the results
together.

    Usage:
        multiquery --help
        multiquery <sqlfile> [<dbname>...] [-d=<path>]
                   [-h=<host>] [-p=<port>] [-u=<user>] [--password=<pass>]
                   [--defaults-file=<path>]

    Options:
        --help                  Prints this documentation
        <dbname>                The name of a database to query.  If none are
                                specified then a file name is expected via
                                -d/--dbnames
        -d --dbnames=<path>     A file containing the names of databases to execute
                                a query.
        -h --host=<host>        The hostname of a mysql/mariadb server
        -p --port=<port>        The port number of a mysql/mariadb server
        -u --user=<user>        The user account to use when connecting
        --password=<pass>       The password to use when connecting
        --defaults-file=<path>  The path to MySQL defaults file
