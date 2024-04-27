import pytest

from src.classes.category import Category
from src.classes.product import Product


@pytest.fixture()
def product_dict_test():
    return {
        'product1': {'name': 'name', 'description': 'description', 'price': 1.0, 'quantity': 0},
        'product2': {'name': 'name', 'description': 'description', 'price': 10.0, 'quantity': 10},
        'product3': {'name': 'name', 'description': 'description', 'price': 100.0, 'quantity': 10},
        'product4': {'name': 'name1', 'description': 'description', 'price': 100.0, 'quantity': 100},
        'product5': {'name': 'name2', 'description': 'description', 'price': 100.0, 'quantity': 100}
    }.copy()


@pytest.fixture()
def categories_test(product_dict_test):
    Category.reset()
    return [
        Category(
            'test1',
            'description',
            [Product.create_product(product_dict_test['product1'])])
    ].copy()
