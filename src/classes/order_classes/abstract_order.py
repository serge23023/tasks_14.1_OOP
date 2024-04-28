from abc import ABC, abstractmethod


class AbstractOrder(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass