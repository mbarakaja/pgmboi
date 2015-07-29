"""
    pgmboi.config
    ~~~~~~~~~~~~~
"""

import json
from os import path
from click import secho

from . import working_dir


class Config(object):
    """The Config object hold all the properties needed to connect
    to the database.

    :param host: hostname where the database server is located
    :param port: connection port
    :param database: database name
    :param user: username
    :param password: password
    :type port: int
    """

    def __init__(self, host='localhost',
                 port=5432, database=None,
                 user='postgres', password=None):

        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    def load_json(self, overwrite=False):
        """ Load the configuration from a json file from the working directory,
        the directory where the application was called."""

        file_path = working_dir + '/config.json'

        # If we can not load the file
        # at least try to merge the raw config instance
        # values to the host instance.
        if not path.exists(file_path):
            secho('Unable to find a config.json file in the working directory')
            return False

        with open(file_path) as f:
            try:
                config_dic = json.load(f)
            except ValueError, e:
                secho('Invalid JSON file.')
                return False

        for prop in self.__dict__:
            try:
                self.__dict__[prop] = config_dic[prop]
            except KeyError, e:
                secho('KeyError: ' + str(e))

        return True

    @property
    def is_valid(self):
        """ Returns ``True`` if all configuration values are not None."""

        for prop in self.__dict__:
            if self.__dict__[prop] is None:
                return False
        return True

    def __str__(self):
        _s = self
        s = 'host: {0}, port: {1}, database: {2}, user: {3}, password: {4}'
        return s.format(_s.host, _s.port, _s.database, _s.user, _s.password)
