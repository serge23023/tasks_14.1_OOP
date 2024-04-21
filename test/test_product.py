import pytest

from src.product import Product


def test_product(product_dict_test):
    key_dict = 'product1'
    product1 = Product(**product_dict_test[key_dict])
    expected_repr = f"{product1.name}, {product1.price} руб. Остаток: {product1.quantity} шт."
    assert repr(product1) == expected_repr
    assert isinstance(product1, Product)
    assert product1.name == product_dict_test[key_dict]['name']
    assert product1.description == product_dict_test[key_dict]['description']
    assert product1.price == product_dict_test[key_dict]['price']
    assert product1.quantity == product_dict_test[key_dict]['quantity']


if __name__ == '__main__':
    pytest.main()
