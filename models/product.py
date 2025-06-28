# models/product.py

class Product:
    _db = {}  # class-level dictionary to simulate a database
    _next_id = 1

    def __init__(self, name, category, price, available):
        self.id = None
        self.name = name
        self.category = category
        self.price = price
        self.available = available

    def save(self):
        if self.id is None:
            self.id = Product._next_id
            Product._next_id += 1
        Product._db[self.id] = self

    @classmethod
    def find_by_id(cls, product_id):
        return cls._db.get(product_id)

    @classmethod
    def delete_by_id(cls, product_id):
        product = cls._db.pop(product_id, None)
        if product:
            return True
        return False

    @classmethod
    def all(cls):
        return list(cls._db.values())

    @classmethod
    def find_by_name(cls, name):
        return [p for p in cls._db.values() if p.name == name]
