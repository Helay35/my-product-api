from behave import given, when, then
import requests

BASE_URL = "http://localhost:5000"  # or wherever your API runs

@given('a product with ID {product_id:d} exists')
def step_given_product_exists(context, product_id):
    context.product_id = product_id

@when('I request the product details for product ID {product_id:d}')
def step_when_request_product(context, product_id):
    context.response = requests.get(f"{BASE_URL}/products/{product_id}")

@then('I receive the product information for product ID {product_id:d}')
def step_then_receive_product_info(context, product_id):
    assert context.response.status_code == 200
    data = context.response.json()
    assert data['id'] == product_id
