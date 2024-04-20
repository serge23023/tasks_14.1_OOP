import pytest

from src.category import Category


@pytest.fixture()
def categories_test():
    return [Category('name', 'description',
                     [{'name': 'name', 'description': 'description', 'price': 0.0, 'quantity': 0}])]
