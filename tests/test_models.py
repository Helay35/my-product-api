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
