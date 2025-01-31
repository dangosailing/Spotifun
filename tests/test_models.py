

def test_new_user_with_fixture(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check username is defined correctly
    """
    assert new_user.username == "testUser"
    #TODO check hash PASSWORD SHOULD NOT BE STORED IN CLEAR TEXT
    assert new_user.password == "password123"
    