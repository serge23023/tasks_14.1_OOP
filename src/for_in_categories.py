class ForInCategories:
    def __init__(self, product: list):
        self.product = product

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index < len(self.product):
            product = self.product[self.__index]
            self.__index += 1
            return product
        else:
            raise StopIteration
