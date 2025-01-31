from app.models import User

def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check username is defined correctly
    """
    user = User(username="testUser", password="password123")
    assert user.username == "testUser"
    #TODO check hash PASSWORD SHOULD NOT BE STORED IN CLEAR TEXT
    assert user.password == "password123"
    