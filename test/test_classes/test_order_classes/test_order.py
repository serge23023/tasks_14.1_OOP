import pytest

from src.classes.order_classes.order import Order
from src.classes.products_classes.product import Product

if __name__ == '__main__':
    pytest.main()


def test_order(product_dict_test):
    product = Product(**product_dict_test['product4'])
    count = 4
    order = Order(product, count)
    assert order.product == product
    assert order.quantity == count
    assert order.total_cost == count * product.price
