from mock import patch
from pgmboi.config import Config
from mocks import ContextualStringIO


# -----------------------
#
# Valid Configuration
#
# -----------------------


def test_valid_config():
    # The config object hold default values for host, port and user
    # database and password are set to None
    # So, adding a database and a password is the basic
    # properties that must be filled
    config = Config()
    config.database = 'mydatabase'
    config.password = '123'
    assert config.is_valid


def test_invalid_config():

    # A config instance with at least one property with value
    # equal to `None` is invalid
    config = Config()
    assert not config.is_valid

    config.database = None
    config.password = '123'
    assert not config.is_valid

    config.database = 'mydatabase'
    config.password = None
    assert not config.is_valid


@patch('__builtin__.open')
@patch('os.path.exists')
def test_config_from_json_file(mock_exists, mock_open):

    mock_exists.return_value = False

    # 1 - trying to load a nonexistent file
    config = Config()
    config.load_json()
    assert not config.is_valid

    mock_exists.return_value = True

    # 2 - Load a INVALID JSON File
    mock_open.return_value = ContextualStringIO('')
    config = Config()
    config.load_json()
    assert not config.is_valid

    # 3 - Load a JSON File with a missing `password` property
    mock_open.return_value = ContextualStringIO('{"database": "database"}')
    config = Config()
    config.load_json()
    assert not config.is_valid

    # 4 - Load a JSON File with a missing `database` property
    mock_open.return_value = ContextualStringIO('{"password": "123"}')
    config = Config()
    config.load_json()
    assert not config.is_valid

    # # 5 - Load a minimun configuration from a JSON file
    # # Virtual JSON file content
    json_string = '{"database": "database", "password": "123"}'
    mock_open.return_value = ContextualStringIO(json_string)
    config = Config()
    config.load_json()
    assert config.is_valid


@patch('__builtin__.open')
@patch('os.path.exists')
def test_load_values_from_json_file(mock_exists, mock_open):
    mock_exists.return_value = True

    json_string = '{"host": "127.0.0.1", "port": 3333,\
                    "database": "test1", "user": "cat",\
                    "password":"free"}'

    mock_open.return_value = ContextualStringIO(json_string)
    config = Config()
    config.load_json()

    # when you load a json file, the values in the json file
    # must ovewrite the actual values in the object.
    assert config.is_valid
    assert config.host == '127.0.0.1'
    assert config.port == 3333
    assert config.database == 'test1'
    assert config.user == 'cat'
    assert config.password == 'free'
