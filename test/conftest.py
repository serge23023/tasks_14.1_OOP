import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def product_test():
    return [Product('name', 'description', 0.0, 0)]


@pytest.fixture()
def categories_test(product_test):
    return [Category('name', 'description', product_test.copy())]
