from classes.category import Category
from classes.product import Product
from read_file import open_json


def create_categories():
    categories = []
    for item in open_json('products.json', True):
        item['products'] = [Product.create_product(product) for product in item['products']]
        categories.append(Category(**item))
    return categories


def add_product_to_category(categories: list[Category], name: str, product: dict):
    for category in categories:
        if category.name == name:
            category.add_product(Product.create_product(product, category.products))
