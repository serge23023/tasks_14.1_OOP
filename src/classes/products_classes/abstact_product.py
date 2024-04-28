from abc import ABC, abstractmethod


class AbstractProduct(ABC):

    @classmethod
    @abstractmethod
    def create_product(cls, new_product: dict, product_list: list = None):
        pass

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass
