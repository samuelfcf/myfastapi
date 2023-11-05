from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_should_return_hello_world_and_200():
    client = TestClient(app)

    response = client.get('/')
    breakpoint()
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello!'}
