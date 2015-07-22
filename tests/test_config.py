from pgmboi.config import Config


def test_valid_config():
    # The config object hold default values for
    # host, port, user
    # database and password are set to None
    # So, adding a database and a password is the basic
    # properties that must to be filled
    config = Config()
    config.database = 'mydatabase'
    config.password = '123'
    assert config.is_validate


def test_invalid_config():
    # if any of the properties is None, the configuration
    # are invalid
    config = Config()
    assert not config.is_validate

    config.database = None
    config.password = '123'
    assert not config.is_validate

    config.database = 'mydatabase'
    config.password = None
    assert not config.is_validate


def test_config_json_missing():
    config = Config()
    assert not config.load_json()
