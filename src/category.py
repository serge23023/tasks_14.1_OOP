from src.product import Product


class Category:
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
        if product.name not in (p.name for p in self.__products):
            Category.__total_unique_products += 1
            self.__products.append(product)
