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
def test_update_product_route(client):
    # Create a new product first
    new_product = {
        "name": "Old Name",
        "category": "Test",
        "price": 10.0,
        "available": True
    }
    post_response = client.post('/products', json=new_product)
    assert post_response.status_code == 201
    product_id = post_response.get_json()['id']

    # Update the product
    updated_data = {
        "name": "Updated Name",
        "price": 20.0,
        "available": False
    }
    put_response = client.put(f'/products/{product_id}', json=updated_data)
    assert put_response.status_code == 200
    updated_product = put_response.get_json()
    assert updated_product['name'] == "Updated Name"
    assert updated_product['price'] == 20.0
    assert updated_product['available'] is False

def test_delete_product_route(client):
    # Create a product to delete
    new_product = {
        "name": "Delete Me",
        "category": "Test",
        "price": 15.0,
        "available": True
    }
    post_response = client.post('/products', json=new_product)
    assert post_response.status_code == 201
    product_id = post_response.get_json()['id']

    # Delete the product
    delete_response = client.delete(f'/products/{product_id}')
    assert delete_response.status_code == 204

    # Verify deletion
    get_response = client.get(f'/products/{product_id}')
    assert get_response.status_code == 404
