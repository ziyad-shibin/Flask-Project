from app import app

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the Flask REST API' in response.data

def test_example_route(client):
    response = client.get('/example')
    assert response.status_code == 200
    assert b'Example response' in response.data

def test_not_found_route(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404