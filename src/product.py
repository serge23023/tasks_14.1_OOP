class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.__name = name
        self.__description = description
        self.__price = price
        self.__quantity = quantity

    def __repr__(self):
        return ("{" + f"'name': '{self.__name}', 'description': '{self.__description}',"
                f" 'price': {self.__price}, 'quantity': {self.__quantity}" + "}")
