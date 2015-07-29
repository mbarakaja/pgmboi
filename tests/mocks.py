""" Some utilities for testing """

from StringIO import StringIO
import subprocess


class ContextualStringIO(StringIO):
    '''Implement Context Manager methods for StringIO object type'''

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()
        # Indicate that we haven't handled the exception, if received
        return False


def call(monkeypatch):
    def fake_call(args, stdin=None, stdout=None, stderr=None, shell=False):
        return 0

    monkeypatch.setattr(subprocess, 'call', fake_call)

# -----------------------------
#
# Mocks for database responses
#
# -----------------------------


class MockCursor(object):
    """A fake database cursor for unit tests"""

    def __init__(self, args=None):
        self.description = []
        self.result = []

    def mock_data(self, result=[], description=None):
        self.result = result
        self.description = description

    def execute(self, *args):
        print args
        return True

    def fetchall(self):
        return self.result


class Column(object):

    def __init__(self, name, type_code=None, display_size=None,
                 internal_size=None, precision=None, scale=None, null_ok=None):
        self.name = name
        self.type_code = type_code
        self.display_size = display_size
        self.internal_size = internal_size
        self.precision = precision
        self.scale = scale
        self.null_ok = null_ok
