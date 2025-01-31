# TESTING THE ROUTES USING FIXTURES
from app import App

def test_home_page():
    """
    GIVEN the Flask application
    WHEN the index route is reached via GET method
    THEN check that it returns a 200 status code
    """
    app = App().create_app()
    with app.test_client() as test_client:
        response = test_client.get("/")
        assert response.status_code == 200
    