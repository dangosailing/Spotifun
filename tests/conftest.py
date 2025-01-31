import pytest
from app.models import User

@pytest.fixture(scope="module")
def new_user():
    user = User(username="testUser", password="password123")
    return user