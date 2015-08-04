from mock import mock_open, Mock
from mocks import ContextualStringIO
from pg_dump import dumped_schema, dumped_table

from pgmboi import Config, dump


def test_dump_header(mocker):
    # MOCKS
    mocker.patch('pgmboi.dump.remove').return_value = True
    mocker.patch('pgmboi.dump.call').return_value = 0
    mocker.patch('pgmboi.dump.path.exists').return_value = True
    mocker.patch('__builtin__.open',
                 side_effect=[ContextualStringIO(dumped_schema),
                              ContextualStringIO()])

    config = Config(database='mydatabase', password='123')

    assert dump.dump_header(config)


def test_dump_functions(mocker):

    # MOCKS
    # WHEN:
    func_list = [{'schema': 'public',
                  'name': 'my_function1',
                  'lang': 'plpgsql',
                  'code': "..."},
                 {'schema': 'public',
                  'name': 'my_function2',
                  'lang': 'plpgsql',
                  'code': "..."}]

    mocker.patch('pgmboi.dump.database.get_functions', return_value=func_list)
    # generate a mocked open function
    m = mocker.patch('__builtin__.open', mock_open(), create=True)

    # THEN:
    assert dump.dump_functions('public')  # must return True
    assert m.called  # must be called
    assert m().write.called  # get a file-lick object from the mock function


def test_dump_table(mocker):
    # MOCKS:
    mocker.patch('pgmboi.dump.remove').return_value = True
    mocker.patch('pgmboi.dump.call').return_value = 0
    mocker.patch('pgmboi.dump.path.exists').return_value = True
    mocker.patch('pgmboi.dump.config').return_value = Config()

    temp_file = ContextualStringIO(dumped_table)
    parsed_file = ContextualStringIO()
    parsed_file.writelines = Mock(return_value=None, nama="writelines")

    file_objects = [temp_file, parsed_file]

    m = mocker.patch('__builtin__.open', side_effect=file_objects)

    assert dump.dump_table('table1')
    assert m.called
    assert len(m.mock_calls) == 2
    assert parsed_file.writelines.called


def test_dump_database(mocker):
    mocker.patch('__builtin__.open')
    mocker.patch('pgmboi.dump.makedirs').return_value = None

    mocker.patch('pgmboi.database.get_schemas').return_value = ['public',
                                                                'private']

    tables = [{'oid': 00000, 'name': 'table1'},
              {'oid': 00000, 'name': 'table2'},
              {'oid': 00000, 'name': 'table3'}]
    mocker.patch('pgmboi.database.get_tables').return_value = tables

    r = [{'name': 'table1', 'dependencies': []},
         {'name': 'table2', 'dependencies': ['table1']},
         {'name': 'table4', 'dependencies': ['table2', 'table4']},
         {'name': 'table5', 'dependencies': ['table4']}]
    mocker.patch('pgmboi.database.get_tables_relationships').return_value = r

    mocker.patch('pgmboi.dump.dump_header').return_value = True
    mocker.patch('pgmboi.dump.dump_functions').return_value = True
    mocker.patch('pgmboi.dump.dump_table').return_value = True

    c = Config(database='database1', password='123')
    mocker.patch('pgmboi.dump.config').return_value = c

    assert dump.dump_database()
