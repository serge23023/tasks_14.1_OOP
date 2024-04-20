from src.category import Category
from src.product import Product


def test_category(categories_test, product_test):
    for category in categories_test:
        assert isinstance(category, Category)
        assert repr(category) == ("\nname: name, description: description, products: [\n\t\t\t\t{'name': 'name', "
                                  "'description': 'description', 'price': 0.0, 'quantity': 0}]")
        for product in category._products:
            assert isinstance(product, Product)
            assert (repr(product) ==
                    "\n\t\t\t\t{'name': 'name', 'description': 'description', 'price': 0.0, 'quantity': 0}")
    assert Category.total_categories() == 1
    assert Category.total_unique_products() == 1
    categories_test.append(Category('', '', product_test))
    assert Category.total_categories() == 2
    assert Category.total_unique_products() == 2
