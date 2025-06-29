class Product:
    _db = {}
    _id_counter = 1

    def __init__(self, name, category, price, available):
        self.id = None
        self.name = name
        self.category = category
        self.price = price
        self.available = available

    def save(self):
        if self.id is None:
            self.id = Product._id_counter
            Product._id_counter += 1
        Product._db[self.id] = self
        return self

    @classmethod
    def all(cls):
        return list(cls._db.values())

    @classmethod
    def find_by_id(cls, id):
        return cls._db.get(id)

    # Change find_by_name to return a list of products (matching the test expectation)
    @classmethod
    def find_by_name(cls, name):
        return [product for product in cls._db.values() if product.name == name]

    @classmethod
    def find_by_category(cls, category):
        return [product for product in cls._db.values() if product.category == category]

    # Change delete_by_id to return True if deleted, False otherwise (matching the test expectation)
    @classmethod
    def delete_by_id(cls, id):
        if id in cls._db:
            cls._db.pop(id)
            return True
        return False
