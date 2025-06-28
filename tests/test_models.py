import pytest
from models.product import Product  # Adjust the import path as needed

def test_read_product():
    # Arrange: create a product instance
    product = Product(name="Test Product", category="Electronics", price=100.0, available=True)
    product.save()

    # Act: try to read/find the product by its ID
    found = Product.find_by_id(product.id)

    # Assert
    assert found is not None
    assert found.name == "Test Product"
    assert found.category == "Electronics"
    assert found.price == 100.0
    assert found.available is True

def test_update_product():
    # Arrange
    product = Product(name="Old Name", category="Books", price=20.0, available=True)
    product.save()

    # Act
    product.name = "Updated Name"
    product.price = 25.0
    product.save()

    updated = Product.find_by_id(product.id)

    # Assert
    assert updated is not None
    assert updated.name == "Updated Name"
    assert updated.price == 25.0

def test_delete_product():
    # Arrange
    product = Product(name="Delete Me", category="Books", price=15.0, available=True)
    product.save()

    # Act
    deleted = Product.delete_by_id(product.id)

    # Assert
    assert deleted is True
    assert Product.find_by_id(product.id) is None

def test_list_all_products():
    # Arrange
    product1 = Product(name="Product 1", category="Toys", price=10.0, available=True)
    product1.save()

    product2 = Product(name="Product 2", category="Toys", price=15.0, available=False)
    product2.save()

    # Act
    all_products = Product.all()

    # Assert
    assert isinstance(all_products, list)
    assert len(all_products) >= 2
    assert product1 in all_products
    assert product2 in all_products
