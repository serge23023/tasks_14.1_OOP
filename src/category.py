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

    def __init__(self, name: str, description: str, products: list[Product] = None):
        self.__name = name
        self.__description = description
        self.__products = products if (products is not None) else []
        Category.__total_categories += 1
        Category.__total_unique_products += len(set(self.products)) if self.products else 0

    @property
    def products(self):
        return self.__products

    @property
    def name(self):
        return self.__name

    def __repr__(self):
        return f"\nname: {self.__name}, description: {self.__description}, products: {self.products}"

    def add_product(self, product: Product):
        if product.name not in set(p.name for p in self.products):
            Category.__total_unique_products += 1
        self.products.append(product)
