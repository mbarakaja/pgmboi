"""
    pgmboi.restore
    ~~~~~~~~~~~~~~

    Restore to the database al SQL files found in the working directory

    :copyright: (c) 2015 by Jose Moreno
"""

from os import path, listdir
from subprocess import call
import json
from click import secho
from . import config
from .utils import parse_dir, working_dir


def restore_database():
    """Restore a database from SQL files in the file system."""

    secho('restoring ' + str(config.database) + ' database')

    # start restoring from the header file
    header_file = parse_dir('__header__', ext='sql')

    if not path.exists(header_file):
        secho('Unable to find the header in:', fg='red')
        secho('    ' + header_file)
        return False

    if not call_psql(header_file):
        secho('Unable to restore:', fg='red')
        secho('    ' + header_file)
        return False

    # list of names of the schemas to be restored from the file system.
    schemas = []

    # Get the list of folders in the current working directory
    # asuming that every folder name is the name of the schema
    # every folder must contain a `relation.json` file.

    dirs = listdir(working_dir)

    for d in dirs:
        folder_path = parse_dir(d)
        relations_path = parse_dir(d, 'relations', ext='json')
        if path.isdir(folder_path) and path.exists(relations_path):
            schemas.append(d)

    if len(schemas) == 0:
        secho('No schema folder was found to restore to database.',
              fg='magenta', bold=True)

    for schema_name in schemas:
        restore_schema(schema_name)

    return True


def restore_functions(schema_name):
    """Restore all functions to the database for a given schema."""

    file_path = parse_dir(schema_name, '__functions__', ext='sql')
    if not path.exists(file_path):
        return False

    if not call_psql(file_path):
        return False

    secho(' |-- functions')
    return True


def is_satisfied(related_to, tables):
    """ Check if the relation dependencies are satisfied
        for the current table.
    """

    for table in tables:
        for r in related_to:
            if r == table['name']:
                return False

    return True


def restore_tables(schema_name):
    """Restore all tables for a given schema"""

    relations_path = parse_dir(schema_name, 'relations', ext='json')
    relations = None

    if not path.exists(relations_path):
        secho('Unable to find relations.json', fg='red')
        return False

    with open(relations_path, 'r') as f:
        relations = json.load(f)

    while len(relations) > 0:

        # this iterates over a copy of the original list
        for r in relations[:]:

            related_to = r['dependencies']
            # check if the dependencies are satisfied
            satisfied = is_satisfied(related_to, relations)

            if len(related_to) == 0 or satisfied:

                file_name = r['name']
                file_path = parse_dir(schema_name, file_name, ext='sql')

                if call_psql(file_path):
                    secho(' |-- ' + file_name)
                    relations.remove(r)
                else:
                    return False
    return True


def restore_schema(schema_name):
    """ Restore a database schema from the file system.
        Starting with the functions and then with the tables
    """

    secho(schema_name, fg='blue', bold=True)

    # 1 ~ retore functions
    restore_functions(schema_name)

    # 2 ~ retore tables
    if not restore_tables(schema_name):
        secho('schema ' + schema_name + ' was unable to restore',
              fg='red', bold=True)
        return False

    return True


def call_psql(file_path):

    status = call(['psql', '-h', config.host,
                           '-p', str(config.port),
                           '-d', config.database,
                           '-U', config.user,
                           '--quiet',
                           '-f', file_path])

    if status == 0:
        return True

    return False
