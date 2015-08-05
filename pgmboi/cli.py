import sys
import click
from click import secho
from .dump import dump_database
from . import database, config


@click.group()
@click.option('--host', help='database server host')
@click.option('--port', help='connection port number')
@click.option('--database', help='the name of the database')
@click.option('--user', help='user name')
@click.option('--password', help='password')
def main(host, port, database, user, password):
    """Dump a PostgreSQL database schema for easy revision control."""

    global config

    # star trying to load the configuration from the file system
    config.load_json()
    print config

    if host:
        config.host = host

    if port:
        config.port = port

    if database:
        config.database = database

    if user:
        config.user = host

    if password:
        config.password = password

    # Recheck if the configuration is valid or sufficient
    # to run the application
    if not config.is_valid:
        secho('Wrong config, something is missing:', fg='red')
        secho(str(config))
        sys.exit(1)

    return True


@main.command()
def dump():
    if not database.connect(config):
        sys.exit(1)

    dump_database()
    database.close()
