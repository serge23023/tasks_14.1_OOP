from src.classes.mixins_classes.mixin_log import MixinCreationLogger
from src.classes.products_classes.product import Product


class Smartphone(Product, MixinCreationLogger):
    def __init__(self, name, description, price, quantity, performance, model, memory, color):
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

    def __repr__(self):
        return f"{Product.__repr__(self)}, '{self.performance}', '{self.model}', '{self.memory}', '{self.color}'"
