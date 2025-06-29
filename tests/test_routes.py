import pytest
from CRUD.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_read_product_route(client):
    response = client.get('/products/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == 1
    assert 'name' in data

def test_list_products_by_category(client):
    response = client.get('/products?category=office')
    assert response.status_code == 200
    products = response.get_json()
    assert isinstance(products, list)
    for product in products:
        assert product['category'] == 'office'

def test_list_products_by_availability(client):
    response = client.get('/products?available=true')
    assert response.status_code == 200
    products = response.get_json()
    assert isinstance(products, list)
    for product in products:
        assert 'available' in product
        assert product['available'] is True
