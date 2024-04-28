from src.classes.mixins_classes.mixin_log import MixinCreationLogger
from src.classes.products_classes.product import Product


class LawnGrass(Product, MixinCreationLogger):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)

    def __repr__(self):
        return f"{Product.__repr__(self)}, '{self.country}', '{self.germination_period}', '{self.color}'"
