import factory
from faker import Faker

fake = Faker()

class ProductFactory(factory.Factory):
    class Meta:
        model = dict  # Using dict for simplicity

    id = factory.Sequence(lambda n: n + 1)
    name = factory.LazyAttribute(lambda x: fake.word().title())
    category = factory.LazyAttribute(lambda x: fake.random_element(elements=('Electronics', 'Clothing', 'Toys')))
    price = factory.LazyAttribute(lambda x: round(fake.random_number(digits=3) + fake.random.random(), 2))
    available = factory.LazyAttribute(lambda x: fake.boolean())
