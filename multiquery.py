#!/usr/bin/env python3
"""
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
"""
import datetime
import sys
import traceback

import docopt
import pymysql
import pymysql.cursors

__version__ = "0.0.1"

def main(argv=None):
    args = docopt.docopt(__doc__, argv=argv)

    query = open(args['<sqlfile>']).read()

    mysql_kwargs = {}
    if args['--host']: mysql_kwargs['host'] = args['--host']
    if args['--port']: mysql_kwargs['port'] = args['--port']
    if args['--user']: mysql_kwargs['user'] = args['--user']
    if args['--password']: mysql_kwargs['password'] = args['--password']
    if args['--defaults-file']:
        mysql_kwargs['read_default_file'] = args['--defaults-file']

    #mysql_kwargs['cursorclass'] = pymysql.cursors.DictCursor

    conn = pymysql.connect(**mysql_kwargs)

    if len(args['<dbname>']) > 0:
        dbnames = args['<dbname>']
    else:
        if args['--dbnames'] is None:
            raise Exception("If no <dbname> is specified, --dbnames must " +
                            "be specified. ")
        dbnames = [name.strip() for name in open(args['--dbnames'])]

    run(conn, query, dbnames)


def run(conn, query, dbnames):

    headers_printed = False
    for i, dbname in enumerate(dbnames):
        with conn.cursor() as cursor:

            # Try to run the query
            sys.stderr.write("Executing query on {0}\n".format(dbname))
            try:
                # Select the right database
                cursor.execute("use {0};".format(conn.escape_string(dbname)))
                cursor.execute(query)

                # If we haven't printed headers, print them now
                if not headers_printed:
                    print("\t".join(encode(d[0]) for d in cursor.description))
                    headers_printed = True

                for row in cursor:
                    print("\t".join(encode(v) for v in row))
            except KeyboardInterrupt as e:
                sys.stderr.write("^C received.  Shutting down.\n")
                raise
            except Exception as e:
                sys.stderr.write(traceback.format_exc())

def encode(val, none_val="NULL"):
    if val == None:
        return none_val
    elif isinstance(val, bytes):
        val = str(val, 'utf-8', "replace")
    else:
        val = str(val)

    return val.replace("\t", "\\t").replace("\n", "\\n")

if __name__ == "__main__": main()
