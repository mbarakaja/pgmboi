"""
    pgmboi.dump
    ~~~~~~~~~~~

    This module dumps a database creating a folder for each
    schema and dumping inside it all the tables in a separate SQL file.

    The dump process is the next order:

    #. Create a **__header__.sql** in the directory where the application \
    was invoked. (need more documentation about what contains this file)
    #. Create a folder with the **name** of the current **schema** inspected.
    #. Dump inside the folder created all the tables in a separate SQL file \
    with the name of the *tables* in the database.
    #. Generat a **relations.json** file. This file container the \
    relationshiop and dependencies between each table in the schema.

"""


from os import path, remove, linesep, makedirs
import json
from subprocess import call
from click import secho

from .utils import parse_dir
from . import database
from . import config


def dump_header(config):
    """ Dump a **__header__.sql** file. This file contain the SQL code for
        Schemas and extensions definition.

        :returns: Boolean
    """

    file_dump = parse_dir('header',  ext='sql.temp')

    code = call(['pg_dump', '-h', config.host, '-p', str(config.port),
                 '-d', str(config.database), '-U', config.user,
                 '--no-owner', '--no-tablespaces',
                 '-s', '-Fp', '-f', file_dump])

    if code:
        return False

    if not path.exists(file_dump):
        secho('Unable to create HEADER file', fg='cyan', bold=True)
        return False

    filebuffer = []

    def parse(line):
        boundary = 'SET search_path ='
        boundary_variant = 'SET search_path='
        if line[:17] != boundary and line[:16] != boundary_variant:
            filebuffer.append(line)
            return True
        return False

    with open(file_dump) as f:

        print f

        for line in f:
            if not parse(line):
                break
        f.close()
        remove(file_dump)

    header_path = parse_dir('__header__', ext='sql')
    header_file = open(header_path, 'w')
    header_file.writelines(filebuffer)
    header_file.close()

    secho('__header__', fg='magenta', bold=True)

    return True


def dump_functions(schema_name='public'):
    '''Dump all functions of a given schema into a __functions__.sql file.'''

    functions = database.get_functions(schema_name)

    if len(functions) == 0:
        return False

    file_path = parse_dir(schema_name, '__functions__', ext='sql')

    with open(file_path, 'w') as func_file:

        for f in functions:
            # we add a `;` character to the SQL code to separate
            # every function in the sql file and prevent error while
            # executing
            code = f['code'] + ';'
            func_file.write(make_comment('My Awesome comment'))
            func_file.write(linesep)
            func_file.write(code)
            func_file.write(linesep)

        func_file.close()

    secho(' |-- __functions__')
    return True


def dump_table(table_name, schema_name='public'):
    ''' Dump a Table SQL code in a file with the name of the table'''

    temp_file = parse_dir(schema_name, table_name, ext='temp.sql')

    # -s schema only
    # -Fp : -File -plain text
    call(['pg_dump', '-h', config.host, '-p', str(config.port),
                     '-d', config.database, '-U', config.user,
                     '--no-owner', '-s', '--no-tablespaces',
                     '-Fp', '-t', schema_name + '.' + table_name,
                     '-f', temp_file])

    if not path.exists(temp_file):
        message = ' |-- ' + str(table_name) + ' -- dump failed'
        secho(message)
        return False

    filebuffer = []

    excluded_code = [
        'SET statement_timeout =',
        'SET lock_timeout =',
        'SET client_encoding =',
        'SET standard_conforming_strings =',
        'SET check_function_bodies =',
        'SET client_min_messages =',
        'SET default_with_oids ='
    ]

    def parse(line):
        valid = True

        for s in excluded_code:
            exclude = line.startswith(s, 0, len(s))
            if exclude:
                valid = False
                break

        if valid:
            filebuffer.append(line)

    with open(temp_file) as f:
        for line in f:
            # print ' --- ', line
            parse(line)
        f.close()
        remove(temp_file)

    table_path = parse_dir(schema_name, table_name, ext='sql')
    table_file = open(table_path, 'w')
    table_file.writelines(filebuffer)
    table_file.close()

    secho(' |-- ' + table_name)

    return True


def dump_database():
    """ Dump an entire database in the current working directory.

        Create a folder for each database schema and dumps inside it
        all tables that correspond to that schema.
    """

    if not dump_header(config):
        return False

    schemas = database.get_schemas()

    for schema_name in schemas:
        secho(schema_name, fg='blue', bold=True)

        folder_path = parse_dir(schema_name)
        if not path.exists(folder_path):
            makedirs(folder_path)

        dump_functions(schema_name)

        tables = database.get_tables(schema_name)

        for table in tables:
            table_name = table['name']
            dump_table(schema_name, table_name)

        # before dump all individual files dump a file with the relationships
        relations = database.get_tables_relationships(schema_name)
        file_path = folder_path + '/relations.json'

        with open(file_path, 'w') as relations_json:
            json.dump(relations, relations_json)

    return True


def make_comment(comment=None):

    text = '--' + linesep

    if comment:
        text = text + '-- ' + comment + linesep
        text = text + '--' + linesep
        return text

    return text
