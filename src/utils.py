from src.category import Category
from src.read_file import open_json


def create_categories():
    categories = []
    for item in open_json('products.json'):
        categories.append(Category(**item))
    return categories
