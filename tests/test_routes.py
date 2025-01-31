def test_home_page(test_client):
    """
    GIVEN the Flask application
    WHEN the index route is reached via GET method
    THEN check that it returns a 200 status code
    """
    response = test_client.get("/")
    assert response.status_code == 200
    