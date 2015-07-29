from mock import mock_open
from mocks import ContextualStringIO
from pg_dump import dumped_schema

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
