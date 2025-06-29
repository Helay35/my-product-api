import pytest
from CRUD.products import app  # Adjust this import if your app is located elsewhere

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_read_product_route(client):
    # Act: request the product by id 1 (adjust id if needed)
    response = client.get('/products/1')

    # Assert
    assert response.status_code == 200
    data = response.get_json()
    assert data is not None
    assert 'id' in data
    assert data['id'] == 1

def test_list_products_by_category(client):
    category = "office"  # Adjust this category based on your data

    # Act: request products filtered by category
    response = client.get(f'/products?category={category}')

    # Assert
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    for product in data:
        assert 'category' in product
        assert product['category'] == category
