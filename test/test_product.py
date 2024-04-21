import pytest

from src.product import Product


def test_product(product_dict_test):
    # Тестирование создания продукта
    key_dict = 'product1'
    product1 = Product(**product_dict_test[key_dict])
    expected_repr = f"{product1.name}, {product1.price} руб. Остаток: {product1.quantity} шт."
    assert repr(product1) == expected_repr  # Проверка строкового представления
    assert isinstance(product1, Product)  # Проверка типа объекта
    assert product1.name == product_dict_test[key_dict]['name']  # Проверка имени
    assert product1.description == product_dict_test[key_dict]['description']  # Проверка описания
    assert product1.price == product_dict_test[key_dict]['price']  # Проверка цены
    assert product1.quantity == product_dict_test[key_dict]['quantity']  # Проверка количества


def test_create_product_new_price(product_dict_test):
    # Тестирование создания нового продукта с обновлением цены
    key_dict1 = 'product1'
    key_dict2 = 'product2'
    product1 = Product(**product_dict_test[key_dict1])
    product2 = Product.create_product(product_dict_test[key_dict2], [product1])
    assert isinstance(product2, type(None))  # Ожидается, что новый продукт не будет создан
    assert product1.price == product_dict_test[key_dict2]['price']  # Проверка обновления цены
    assert product1.quantity == product_dict_test[key_dict2]['quantity']  # Проверка обновления количества


def test_create_product_existing_price(product_dict_test):
    # Тестирование создания нового продукта с существующей ценой
    key_dict1 = 'product3'
    key_dict2 = 'product2'
    product1 = Product(**product_dict_test[key_dict1])
    product2 = Product.create_product(product_dict_test[key_dict1], [product1])
    assert isinstance(product2, type(None))  # Ожидается, что новый продукт не будет создан
    assert product1.price == product_dict_test[key_dict1]['price']  # Проверка сохранения цены
    # Проверка обновления количества
    assert product1.quantity == product_dict_test[key_dict1]['quantity'] + product_dict_test[key_dict2]['quantity']


def test_create_product_new_product(product_dict_test):
    # Тестирование создания нового продукта
    key_dict1 = 'product1'
    key_dict2 = 'product4'
    product1 = Product(**product_dict_test[key_dict1])
    product2 = Product.create_product(product_dict_test[key_dict2], [product1])
    assert isinstance(product2, Product)  # Ожидается, что новый продукт будет создан
    assert product2.name == product_dict_test[key_dict2]['name']  # Проверка имени
    assert product2.price == product_dict_test[key_dict2]['price']  # Проверка цены
    assert product2.quantity == product_dict_test[key_dict2]['quantity']  # Проверка количества


if __name__ == '__main__':
    pytest.main()
