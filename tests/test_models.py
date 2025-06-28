import pytest
from models.product import Product  # Adjust the import path as needed

def test_read_product():
    # Arrange: create a product instance
    product = Product(name="Test Product", category="Electronics", price=100.0, available=True)
    product.save()  # Save to DB or in-memory list depending on your setup

    # Act: try to read/find the product by its ID
    found = Product.find_by_id(product.id)

    # Assert: verify the product was found and fields match
    assert found is not None
    assert found.name == "Test Product"
    assert found.category == "Electronics"
    assert found.price == 100.0
    assert found.available is True

def test_update_product():
    # Arrange: create and save the original product
    product = Product(name="Old Name", category="Books", price=20.0, available=True)
    product.save()

    # Act: update some fields
    product.name = "Updated Name"
    product.price = 25.0
    product.save()

    # Retrieve again to verify changes
    updated = Product.find_by_id(product.id)

    # Assert
    assert updated is not None
    assert updated.name == "Updated Name"
    assert updated.price == 25.0

def test_delete_product():
    # Arrange: create and save a product
    product = Product(name="Delete Me", category="Books", price=15.0, available=True)
    product.save()

    # Act: delete the product
    deleted = Product.delete_by_id(product.id)

    # Assert: verify the product was deleted
    assert deleted is True
    assert Product.find_by_id(product.id) is None
