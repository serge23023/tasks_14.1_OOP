from src.category import Category
from src.utils import create_categories


def test_create_categories():
    for category in create_categories():
        assert isinstance(category, Category)
