import pytest
from starlette.config import environ
from starlette.testclient import TestClient

from app.main import app

# This line would raise an error if we use it after 'settings' has been imported.
environ['TESTING'] = 'TRUE'


@pytest.fixture()
def client():
    """
    Make a 'client' fixture available to test cases.
    """
    # Our fixture is created within a context manager. This ensures that
    # application startup and shutdown run for every test case.
    #
    with TestClient(app) as test_client:
        yield test_client
