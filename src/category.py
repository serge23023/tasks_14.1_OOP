from src.product import Product


class Category:
    _total_categories = 0
    _total_unique_products = 0

    def __init__(self, name: str, description: str, products: list[dict]):
        self._name = name
        self._description = description
        self._products = self.init_products(products)
        Category._total_categories += 1

    @classmethod
    def total_categories(cls):
        return cls._total_categories

    @classmethod
    def total_unique_products(cls):
        return cls._total_unique_products

    @staticmethod
    def init_products(products: list[dict]) -> list[Product]:
        list_products = []
        set_name = set()
        for product in products:
            list_products.append(Product(**product))
            set_name.add(product['name'])
        Category._total_unique_products += len(set_name)
        return list_products

    # def add_product(self, product: dict):
    #     self.products.append(Product(**product))
    #     self.count_unique_product(product)
    #
    # def count_unique_product(self, product: dict):
    #     if product not in [product.name for product in self.products]:
    #         Category._total_unique_products += 1
