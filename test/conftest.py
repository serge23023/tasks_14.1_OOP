import pytest

from src.category import Category


@pytest.fixture()
def product_test():
    return [{'name': 'name', 'description': 'description', 'price': 0.0, 'quantity': 0}]


@pytest.fixture()
def categories_test(product_test):
    return [Category('name', 'description', product_test)]
