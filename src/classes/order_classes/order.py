from src.classes.mixins_classes.mixin_log import MixinCreationLogger
from src.classes.order_classes.abstract_order import AbstractOrder


class Order(AbstractOrder, MixinCreationLogger):
    __slots__ = ('product', 'quantity', 'total_cost')

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.total_cost = self.quantity * self.product.price
        self.log_creation()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.product.name}', '{self.quantity}', '{self.total_cost}')"
