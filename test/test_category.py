from src.category import Category
from src.product import Product


def test_category(categories_test, product_test):
    for category in categories_test:
        assert isinstance(category, Category)
        assert category.__repr__() is not None
        for product in category._products:
            assert isinstance(product, Product)
            assert product.__repr__() is not None
    assert Category.total_categories() == 1
    assert Category.total_unique_products() == 1
    categories_test.append(Category('', '', product_test))
    assert Category.total_categories() == 2
    assert Category.total_unique_products() == 2
