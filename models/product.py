class Product:
    _db = {}  # class-level "database" dictionary
    _id_counter = 1

    def __init__(self, name, category, price, available):
        self.id = Product._id_counter
        Product._id_counter += 1

        self.name = name
        self.category = category
        self.price = price
        self.available = available

    def save(self):
        Product._db[self.id] = self

    @classmethod
    def find_by_id(cls, product_id):
        return cls._db.get(product_id)

    @classmethod
    def delete_by_id(cls, product_id):
        if product_id in cls._db:
            del cls._db[product_id]
            return True  # Return True when deleted successfully
        return False

    @classmethod
    def all(cls):
        return list(cls._db.values())
