# from src.utils import add_property_to_category
from src.for_in_categories import ForInCategories
from src.utils import create_categories

if __name__ == '__main__':
    for product in ForInCategories(create_categories()[0].products):
        print(product)
    categories = create_categories()
    for category in categories:
        print(category)
    # categories = create_categories()
    # add_property_to_category(categories, 'Смартфоны',
    #                          {'name': 'name', 'description': 'description', 'price': 0.0, 'quantity': 0})
    # print([p for p in categories])
