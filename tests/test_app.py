from app import app


def test_home_page():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Hello from my first DevOps project!"


def test_health_endpoint():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {"status": "healthy"}
