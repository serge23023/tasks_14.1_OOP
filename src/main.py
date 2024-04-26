# from src.utils import add_property_to_category
from src.utils import create_categories

if __name__ == '__main__':
    categories = create_categories()
    for category in categories:
        print(category)
    # categories = create_categories()
    # add_property_to_category(categories, 'Смартфоны',
    #                          {'name': 'name', 'description': 'description', 'price': 0.0, 'quantity': 0})
    # print([p for p in categories])
