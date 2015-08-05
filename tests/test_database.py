from mock import Mock
from mocks import Column, MockCursor
from pgmboi.config import Config


def cursor_for_schemas():

    result_set = [('public',),
                  ('schema2',),
                  ('schema3',),
                  ('schema4',)]

    cursor = MockCursor()
    cursor.mock_data(result_set)
    return cursor


def cursor_for_functions():
    description = (Column(name='name'),
                   Column(name='lang'),
                   Column(name='schema'),
                   Column(name='code'))

    result_set = [('function1', 'plpgsql', 'public', '...'),
                  ('function2', 'plpgsql', 'public', '...'),
                  ('function3', 'plpgsql', 'public', '...')]

    cursor = MockCursor()
    cursor.mock_data(result_set, description)
    return cursor


def cursor_for_tables():
    description = (Column(name='name'),
                   Column(name='oid'))

    result_set = [(10000, 'table1'),
                  (10001, 'table2'),
                  (10002, 'table3'),
                  (10003, 'table4'),
                  (10007, 'table5')]

    cursor = MockCursor()
    cursor.mock_data(result_set, description)
    return cursor


def cursor_for_dependecies():
    description = (Column(name='fk_table_name'),
                   Column(name='referenced_table_name'))

    result_set = [('table1', 'table09'),
                  ('table2', 'table10'),
                  ('table3', 'table11'),
                  ('table4', 'table12'),
                  ('table7', 'table15'),
                  ('table8', 'table16')]

    cursor = MockCursor()
    cursor.mock_data(result_set, description)
    return cursor


def get_tables(schema_name='public'):
    return [{'oid': 00000, 'name': 'table1'},
            {'oid': 00000, 'name': 'table2'},
            {'oid': 00000, 'name': 'table3'},
            {'oid': 00000, 'name': 'table4'}]


# ---------------------------
#
# Tests
#
# ---------------------------

def test_connection(mocker):

    from pgmboi import database

    # connection with a invalid config instance
    config = Config()
    assert not database.connect(config)

    # connection with invalid credentials
    config.database = 'database1'
    config.password = '123'
    assert not database.connect(config)

    # mock for a successful connection
    conn = mocker.patch('pgmboi.database.psycopg2.connect')
    conn().closed = 0

    assert database.connect(config)


def test_get_schemas():
    from pgmboi import database

    database.cursor = cursor_for_schemas()
    result = database.get_schemas()
    # check if at least the first item is a string
    assert type(result[0]) == str


def test_get_functions():
    from pgmboi import database

    database.cursor = cursor_for_functions()
    item = database.get_functions()[0]  # get the first item

    assert type(item) == dict
    assert 'name' in item


def test_get_tables():

    from pgmboi import database
    database.cursor = cursor_for_tables()
    item = database.get_tables()[0]

    assert type(item) == dict
    assert 'name' in item


def test_get_tables_realationships():

    from pgmboi import database

    # the table relationship call to database.get_tables, so mocks it.
    database.get_tables = get_tables
    database.cursor = cursor_for_dependecies()

    item = database.get_tables_relationships('public')[0]

    assert type(item) == dict
    assert 'name' in item
    assert 'dependencies' in item
