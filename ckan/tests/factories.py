from faker import Faker
import random

fake = Faker()

class Product:
    def __init__(self, name, price, description, category):
        self.name = name
        self.price = price
        self.description = description
        self.category = category

def create_fake_product():
    """Generate a fake product with random attributes."""
    name = fake.commerce_product_name()
    price = round(random.uniform(5.0, 100.0), 2)  # Random price between $5.00 and $100.00
    description = fake.text(max_nb_chars=200)  # Random product description
    category = fake.word()  # Random category name

    return Product(name, price, description, category)

def create_multiple_fake_products(n=5):
    """Generate a list of fake products."""
    return [create_fake_product() for _ in range(n)]

# Example usage
if __name__ == "__main__":
    fake_products = create_multiple_fake_products(10)
    for product in fake_products:
        print(f"Name: {product.name}, Price: ${product.price}, Description: {product.description}, Category: {product.category}")
