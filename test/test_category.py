import pytest

from src.category import Category
from src.product import Product


def test_category(categories_test):
    for category in categories_test:
        assert isinstance(category, Category)
        assert category.name == 'name'
        assert category.description == 'description'
        for product in category.products:
            assert isinstance(product, Product)
            assert product.name == 'name'
            assert product.description == 'description'
            assert product.price == 0.0
            assert product.quantity == 0
    assert Category.total_categories() == 1
    assert Category.total_unique_products() == 1
    categories_test.append(Category('', '',
                                    [{'name': 'name1', 'description': 'description1', 'price': 0.0, 'quantity': 0}]))
    assert Category.total_categories() == 2
    assert Category.total_unique_products() == 2
