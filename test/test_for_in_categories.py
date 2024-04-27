import pytest

from src.classes.for_in_categories import ForInCategories
from src.classes.product import Product

if __name__ == '__main__':
    pytest.main()


def test_for_in_categories(categories_test, product_dict_test):
    products = categories_test[0].products
    products.append(Product(**product_dict_test['product4']))
    iterator = ForInCategories(products).__iter__()

    # Проверяем, что итератор возвращает продукты в правильном порядке
    for i in range(len(products)):
        assert next(iterator) == products[i]

    # Проверяем, что итератор генерирует исключение StopIteration после прохода по всем продуктам
    with pytest.raises(StopIteration):
        next(iterator)
