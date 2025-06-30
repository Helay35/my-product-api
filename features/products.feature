Feature: Products API

  Scenario: Reading a product by ID
    Given a product with ID 143 exists
    When I request the product details for product ID 143
    Then I receive the product information for product ID 143
