from src.category import Category
from src.product import Product


def test_category(categories_test, product_test):
    for category in categories_test:
        assert isinstance(category, Category)
        assert repr(category) == f"\nname: name, description: description, products: [name, 0.0 руб. Остаток: 0 шт.]"
        assert category.name == 'name'
        for product in category.products:
            assert isinstance(product, Product)
            assert product.name == 'name'
            assert product.description == 'description'
            assert product.price == 0.0
            assert product.quantity == 0
            assert repr(product) == "name, 0.0 руб. Остаток: 0 шт."
    assert Category.total_categories() == 1
    assert Category.total_unique_products() == 1
    categories_test.append(Category('test2', 'test'))
    assert Category.total_categories() == 2
    for c in categories_test:
        print(c)
    assert Category.total_unique_products() == 1
    for category in categories_test:
        if category.name == 'test2':
            category.add_product(Product('name1', 'description', 0.0, 0))
    assert Category.total_categories() == 2
    assert Category.total_unique_products() == 2
