from src.app import create_app
import pytest

@pytest.fixture
def app():
    app = create_app('testing')
    return app

def client(app):
    return app.test_Client()

