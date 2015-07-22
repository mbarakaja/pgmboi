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

    :pareama host: hostname where the database server is located
    :pareama port: connection port
    :pareama database: database name.
    :pareama user: username
    :pareama password: password
    :type port: int
    """

    def __init__(self, host='locahost',
                 port=5432, database=None,
                 user='postgres', password=None):
        self.host = host
        self.port = port
        self.database = None
        self.user = user
        self.password = None

    def load_json(self):
        """ Load the configuration from a json file from the working directory,
        the directory where the application was called."""

        _config = Config()
        config_dic = None

        file_path = working_dir + '/config.json'

        if not path.exists(file_path):
            return False

        with open(file_path) as f:
            config_dic = json.load(f)
            f.close()

        for key in config_dic:
            try:
                setattr(_config, key, config_dic[key])
            except Exception, e:
                secho(e)

        self.merge(_config)

        return True

    @property
    def is_validate(self):
        """ This attribute is set to ``True`` if all configuration
        values are not None."""

        for prop in self.__dict__:
            if self.__dict__[prop] is None:
                return False
        return True

    def __str__(self):
        _s = self
        s = 'host: {0}, port: {1}, database: {2}, user: {3}, password: {4}'
        return s.format(_s.host, _s.port, _s.database, _s.user, _s.password)
