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


@patch('pgmboi.restore.restore_tables', return_value=True)
@patch('pgmboi.restore.restore_functions')
def test_restore_schema(mock_restore_functions, mock_restore_tables):

    assert restore.restore_schema('public')
    assert mock_restore_functions.called
    assert mock_restore_tables.called


@patch('pgmboi.restore.config', new=Config(database='mydb', password='123'))
@patch('pgmboi.restore.call_psql', return_value=True)
@patch('pgmboi.restore.path.exists', return_value=False)
@patch('pgmboi.restore.path.isdir', return_value=True)
@patch('pgmboi.restore.listdir')
@patch('pgmboi.restore.restore_schema', return_value=True)
def test_restore_database(m_restore_schema, m_listdir,
                          m_isdir, m_exists, m_call_psql):

    # 1 - Here we dont have set a fake __heade__.sql file, so, the restore
    # task must return False
    assert not restore.restore_database()

    m_exists.return_value = True
    m_listdir.return_value = ['public', 'private', 'other']

    assert restore.restore_database()
    assert restore.call_psql.called
    assert m_restore_schema.call_count == 3
