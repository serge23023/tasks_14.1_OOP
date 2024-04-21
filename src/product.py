class Product:

    @classmethod
    def create_product(cls, new_product: dict, product_list: list = None):
        if product_list is None:
            product_list = []

        for product in product_list:
            if product.name == new_product['name']:
                # Найден дубликат товара
                if product.price >= new_product['price']:
                    # Если у существующего товара цена выше, используем его цену
                    product.quantity += new_product['quantity']
                    return
                else:
                    # Иначе используем новую цену
                    product.price = new_product['price']
                    product.quantity += new_product['quantity']
                    return
        return cls(**new_product)

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."
