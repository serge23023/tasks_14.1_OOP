class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self._name = name
        self._description = description
        self._price = price
        self._quantity = quantity

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity
