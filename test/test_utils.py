import pytest

from src.classes.order_classes.category import Category
from src.utils import create_categories, add_product_to_category

if __name__ == '__main__':
    pytest.main()


def test_create_categories():
    assert all(isinstance(category, Category) for category in create_categories())


def test_add_property_to_category(categories_test):
    initial_total_unique_products = Category.total_unique_products()
    add_product_to_category(
        categories_test,
        'test1',
        {
            'name': 'name1',
            'description': 'description',
            'price': 0.0,
            'quantity': 0}
    )
    assert Category.total_categories() == 1
    assert Category.total_unique_products() == initial_total_unique_products + 1
