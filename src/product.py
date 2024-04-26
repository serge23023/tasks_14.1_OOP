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
        self.__price = price  # !!!!!!!!! setter при инициализации?
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print(f'Введена некорректная цена: {value}')
        elif value < self.__price:
            if input(f'Цена после подтверждения: {value} руб.\nВведите "y" для подтверждения понижения цены:') == 'y':
                self.__price = float(value)
        else:
            self.__price = float(value)

    def __str__(self):
        return f"\n{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self.__price * self.quantity + other.__price * other.quantity
