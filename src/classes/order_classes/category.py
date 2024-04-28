from src.classes.mixins_classes.mixin_log import MixinCreationLogger
from src.classes.order_classes.abstract_order import AbstractOrder
from src.classes.products_classes.product import Product


class Category(AbstractOrder, MixinCreationLogger):
    __total_categories = 0
    __total_unique_products = 0

    @classmethod
    def total_categories(cls):
        return cls.__total_categories

    @classmethod
    def total_unique_products(cls):
        return cls.__total_unique_products

    @classmethod
    def reset(cls):
        cls.__total_categories = 0
        cls.__total_unique_products = 0

    def __init__(self, name: str, description: str, products: list[Product] = None):
        self.__name = name
        self.__description = description
        self.__products = products if products else []
        Category.__total_categories += 1
        Category.__total_unique_products += len(set(p.name for p in self.__products))
        self.log_creation()

    @property
    def products(self):
        return self.__products

    @property
    def name(self):
        return self.__name

    def __len__(self):
        count = 0
        for product in self.__products:
            count += product.quantity
        return count

    def __str__(self):
        return f"\n{self.__name}, количество продуктов: {len(self)} шт."

    def add_product(self, product: Product):
        if issubclass(product.__class__, Product):
            if product.name not in (p.name for p in self.__products):
                Category.__total_unique_products += 1
            self.__products.append(product)
        else:
            raise TypeError

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__name}, {self.__description}, {self.__products}'
