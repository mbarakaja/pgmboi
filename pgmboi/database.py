"""
    pgmboi.database
    ~~~~~~~~~~~~~~~

"""

import psycopg2
import psycopg2.extensions
import sys
import os

from click import secho


psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)


connection = None
cursor = None


def pgpass(config):
    """ Check if a .pgpass file exist in the user home directory.
        If not, create a new file and write in it the database
        connection configuration in the next format::

            hostname:port:database:username:password
    """

    # The home directory for the current operating system user
    # For instance: /home/user
    home_dir = os.path.expanduser('~')
    pgpass_path = home_dir + '/.pgpass'
    pgpass_file = None

    if not os.path.exists(pgpass_path):
        pgpass_file = open(pgpass_path, 'w')
    else:
        pgpass_file = open(pgpass_path, 'w')

    # hostname:port:database:username:password
    pgpass_string = config.host + ':'
    pgpass_string += str(config.port) + ':'
    pgpass_string += config.database + ':'
    pgpass_string += config.user + ':'
    pgpass_string += config.password

    try:
        pgpass_file = os.fdopen(
            os.open(pgpass_path, os.O_WRONLY | os.O_CREAT), 'w')
    except:
        secho('Unable to create .pgpass', bold=True, fg='red')

    pgpass_file.write(pgpass_string)
    pgpass_file.close()

    os.chmod(pgpass_path, 0600)


def connect(config):
    """ Connect to a PostgreSQL database

        :param config: parameters object used in database connection
        :type config: pgmboi.config.Config
        :returns: bool : True if the connection was successful
    """

    pgpass(config)

    print 'connecting to ' + config.database + ' ...'

    connection_config = 'host=' + config.host +\
                        ' dbname=' + config.database +\
                        ' user=' + config.user +\
                        ' password=' + config.password +\
                        ' port=' + str(config.port)
    try:
        global connection
        global cursor
        connection = psycopg2.connect(connection_config)
        cursor = connection.cursor()
    except ValueError as e:
        print e
        sys.exit()
        return False

    secho('successful connection', fg='green')

    return True


def close():
    ''' Close the database connection

        :resturns: bool
    '''

    global cursor
    global connection

    try:
        cursor.close()
        connection.close()
    except Exception:
        print 'An exception occurrent white closing database connection'
        return False

    secho('Database connection closed', fg='green')

    return True


def get_schemas():
    ''' Returns a list of schemas for a given database.'''

    query = '''SELECT n.nspname AS "name"
        FROM pg_catalog.pg_namespace n
        WHERE n.nspname !~ '^pg_' AND n.nspname <> 'information_schema'
        ORDER BY 1;'''

    cursor.execute(query)
    query_result = cursor.fetchall()

    data = []

    for row in query_result:
        data.append(row[0])

    return data


def get_functions(schema_name=None):
    """ Returns a list of function definitions for all or one schema.

        Each list item are dictionaries with the next values::

            {'schema': 'public',  # name of the schema
             'name': 'my_function1',  # name of the function
             'lang': 'plpgsql',  # languaje used
             'code': "..."}  # the function definition.

        :returns: list
    """

    _list = []

    sql = '''SELECT pp.proname AS name,
                    pl.lanname AS lang,
                    pn.nspname AS schema,
                    pg_get_functiondef(pp.oid) AS code
            FROM pg_proc pp
              inner join pg_namespace pn on (pp.pronamespace = pn.oid)
              inner join pg_language pl on (pp.prolang = pl.oid)
            WHERE pl.lanname NOT IN ('c','internal')
              and pn.nspname NOT LIKE 'pg_%'
              and pn.nspname <> 'information_schema' '''

    if schema_name:
        sql = sql + '''and pn.nspname = '{0}' '''.format(schema_name)

    sql = sql + ''';'''

    cursor.execute(sql)

    result_set = cursor.fetchall()
    description = cursor.description

    for row in result_set:
        _dict = {}

        for index, value in enumerate(row):
            _dict[description[index].name] = value

        _list.append(_dict)

    return _list


def get_triggers():
    """List all triggers"""

    sql_code = '''SELECT
                n.nspname as "Schema",
                p.proname as "Name",
                pg_catalog.pg_get_function_result(p.oid) as "rdt",
                pg_catalog.pg_get_function_arguments(p.oid) as "adt",
            CASE
                WHEN p.proisagg THEN 'agg'
                WHEN p.proiswindow THEN 'window'
                WHEN p.prorettype = 'pg_catalog.trigger'::pg_catalog.regtype
                    THEN 'trigger'

            ELSE 'normal'

            END as "Type"

            FROM pg_catalog.pg_proc p
                LEFT JOIN pg_catalog.pg_namespace n ON n.oid = p.pronamespace
            WHERE (p.prorettype = 'pg_catalog.trigger'::pg_catalog.regtype)
                AND pg_catalog.pg_function_is_visible(p.oid)
                AND n.nspname <> 'pg_catalog'
                AND n.nspname <> 'information_schema'
                ORDER BY 1, 2, 4;'''

    cursor.execute(sql_code)

    return cursor.fetchall()


def get_tables_relationships(schema_name='public'):
    """ Returns the relationship between tables in a *schema*.

        Returns a list of dictionaries with the following structure::

            [{'name': 'table1', 'dependencies': []},
             {'name': 'table2', 'dependencies': ['table1']},
             {'name': 'table4', 'dependencies': ['table2', 'table4']},
             {'name': 'table5', 'dependencies': ['table4']}]

        If a table has no dependencies/relationshiop with other tables,
        the attribute **dependencies** only has an empty list.

    """

    # the next query I find in:
    # http://stackoverflow.com/questions/3907879/sql-server-howto-get-foreign-
    # key-reference-from-information-schema/3907999#3907999

    query = '''SELECT
        kcu1.table_name AS fk_table_name,
        kcu2.table_name AS referenced_table_name,
        kcu1.constraint_name AS fk_constraint_name,
        kcu1.column_name AS fk_column_name,
        kcu1.ordinal_position AS fk_ordinal_position,
        kcu2.constraint_name AS referenced_constraint_name,
        kcu2.column_name AS referenced_column_name,
        kcu2.ordinal_position AS referenced_ordinal_position
    FROM information_schema.referential_constraints AS rc

    INNER JOIN information_schema.key_column_usage AS kcu1
        ON kcu1.constraint_catalog = rc.constraint_catalog
        AND kcu1.constraint_schema = rc.constraint_schema
        AND kcu1.constraint_name = rc.constraint_name

    INNER JOIN information_schema.key_column_usage AS kcu2
        ON kcu2.constraint_catalog = rc.unique_constraint_catalog
        AND kcu2.constraint_schema = rc.unique_constraint_schema
        AND kcu2.constraint_name = rc.unique_constraint_name
        AND kcu2.ordinal_position = kcu1.ordinal_position;'''

    cursor.execute(query)

    query_result = cursor.fetchall()
    description = cursor.description

    relations = []

    for row in query_result:
        dic = {}

        for index, value in enumerate(row):
            dic[description[index].name] = value

        relations.append(dic)

    tables = get_tables(schema_name)

    data = []

    for table in tables:

        table_name = table['name']
        raw = {'name': table_name, 'dependencies': []}

        for r in relations:
            if table_name == r['fk_table_name']:
                raw['dependencies'].append(r['referenced_table_name'])

        data.append(raw)

    return data


def get_tables(schema_name='public'):
    """ List all table for a given schema

        Returns a list of dictionaries in the next format::

            [{'oid': 00000, 'name': 'table1'},
             {'oid': 00000, 'name': 'table2'},
             {'oid': 00000, 'name': 'table3'}]

        :param schema_name: The name to use.
        :returns: list
    """

    query = '''SELECT
        c.relname as name,
        c.oid as oid

    FROM pg_catalog.pg_class c
        LEFT JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace
    WHERE c.relkind IN ('r','')
        AND n.nspname = %s
    ORDER BY 1,2;'''

    cursor.execute(query, (schema_name, ))

    query_result = cursor.fetchall()
    description = cursor.description

    data = []

    for row in query_result:
        dic = {}

        for index, value in enumerate(row):
            dic[description[index].name] = value

        data.append(dic)

    return data
