from src.for_in_categories import ForInCategories
from src.utils import create_categories

if __name__ == '__main__':
    for product in ForInCategories(create_categories()[0].products):
        print(product)
    categories = create_categories()
    for category in categories:
        print(category)
