import sys
import os
import pytest
from app import create_app

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
os.environ["TESTING"] = "1"  # Prevent Tkinter from running during tests

@pytest.fixture
def app():
    app = create_app({"TESTING": True})
    yield app

@pytest.fixture
def client(app):
    return app.test_client()
