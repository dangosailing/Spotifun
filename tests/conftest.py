import pytest
from app.models import User
from app import App

@pytest.fixture(scope="module")
def new_user():
    user = User(username="testUser", password="password123")
    return user

@pytest.fixture(scope="module")
def test_client():
    app = App().create_app()
    with app.test_client() as testing_client:
        yield testing_client
    