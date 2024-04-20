import pytest

from src.category import Category
from src.product import Product


def test_category(categories_test, product_test):
    for category in categories_test:
        assert isinstance(category, Category)
        assert category._name == 'name'
        assert category._description == 'description'
        for product in category._products:
            assert isinstance(product, Product)
            assert product._name == 'name'
            assert product._description == 'description'
            assert product._price == 0.0
            assert product._quantity == 0
    assert Category.total_categories() == 1
    assert Category.total_unique_products() == 1
    categories_test.append(Category('', '', product_test))
    assert Category.total_categories() == 2
    assert Category.total_unique_products() == 2
