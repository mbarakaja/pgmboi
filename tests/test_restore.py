from mock import patch
from mocks import ContextualStringIO
from pgmboi.config import Config
from pgmboi import restore


@patch('pgmboi.restore.config', new=Config())
@patch('pgmboi.restore.call')
def test_call_psql(mock_call):

    mock_call.return_value = 0
    assert restore.call_psql('...')
    assert mock_call.call_count == 1

    mock_call.return_value = 1
    assert not restore.call_psql('...')
    assert mock_call.call_count == 2


def test_restore_functions(mocker):
    mocker.patch('pgmboi.restore.call_psql', return_value=True)
    _exists = mocker.patch('pgmboi.dump.path.exists', return_value=False)

    schema_name = 'public'
    assert not restore.restore_functions(schema_name)

    _exists.return_value = True
    assert restore.restore_functions(schema_name)


# def test_restore_schema(mocker):
#     assert restore.restore_database()


def test_tables(mocker):
    # mocks
    _exists = mocker.patch('pgmboi.restore.path.exists', return_value=False)
    relations_string = "{}"
    _open = mocker.patch('pgmboi.restore.open',
                         side_effect=[ContextualStringIO(relations_string),
                                      ContextualStringIO()])
    r = [{'name': 'table1', 'dependencies': []},
         {'name': 'table2', 'dependencies': ['table1']}]

    _load = mocker.patch('pgmboi.restore.json.load', return_value=r)
    mocker.patch('pgmboi.restore.call_psql').return_value = True

    # test when the relations.json file doesn't exist
    assert not restore.restore_tables('public')

    _exists.return_value = True  # relations.json file exists

    assert restore.restore_tables('public')
    assert _open.called
    assert _load.called


def test_restore_database(mocker):
    config = Config(database='mydb', password='123')
    mocker.patch('pgmboi.restore.config', new=config)
    mocker.patch('pgmboi.restore.call_psql').return_value = True

    # 1 - Here we dont have set a fake __heade__.sql file, so, the restore
    # task must return False
    assert not restore.restore_database()

    mocker.patch('pgmboi.restore.path.exists').return_value = True
    assert restore.restore_database()
    assert restore.call_psql.called
