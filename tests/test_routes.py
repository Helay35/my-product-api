import pytest
from CRUD.products import app  # adjust path if needed

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_read_product_route(client):
    # Act: request an existing product by id (143 or 144)
    response = client.get('/products/143')

    # Assert
    assert response.status_code == 200
    data = response.get_json()
    assert data is not None
    assert 'id' in data
    assert data['id'] == 143
