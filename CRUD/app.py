from flask import Flask, jsonify, request
import json
from flask_cors import CORS

app = Flask("Product Server")
CORS(app)

# Sample product list
products = [
    {'id': 1, 'name': 'Sample Product', 'price': 9.99, 'category': 'test', 'available': True},
    {'id': 143, 'name': 'Notebook', 'price': 5.49, 'category': 'office', 'available': True},
    {'id': 144, 'name': 'Black Marker', 'price': 1.99, 'category': 'office', 'available': False}
]

# READ single product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    for product in products:
        if product['id'] == product_id:
            return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404

# READ list of products with optional filtering
@app.route('/products', methods=['GET'])
def list_products():
    category = request.args.get('category')
    available = request.args.get('available')

    filtered = products

    if category:
        filtered = [p for p in filtered if p.get('category') == category]
    if available is not None:
        if available.lower() == 'true':
            filtered = [p for p in filtered if p.get('available') is True]
        elif available.lower() == 'false':
            filtered = [p for p in filtered if p.get('available') is False]

    return jsonify(filtered)

# UPDATE product by ID
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    for product in products:
        if product['id'] == product_id:
            product['name'] = data.get('name', product['name'])
            product['price'] = data.get('price', product['price'])
            product['category'] = data.get('category', product['category'])
            product['available'] = data.get('available', product['available'])
            return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404

# DELETE product by ID
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    updated_products = [p for p in products if p['id'] != product_id]

    if len(updated_products) == len(products):
        return jsonify({'error': 'Product not found'}), 404

    products = updated_products
    return jsonify({'message': f'Product with ID {product_id} deleted.'}), 200

# Start the Flask server
if __name__ == "__main__":
    app.run(port=5000, debug=True)
