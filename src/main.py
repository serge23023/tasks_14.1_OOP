from src.for_in_categories import ForInCategories
from src.utils import create_categories

if __name__ == '__main__':
    categories = create_categories()

    for product in ForInCategories(categories[0].products):
        print(product)

    print('---------------')
    for category in categories:
        print(category)

    print('---------------')
    print(categories[0].products[0] + categories[0].products[1])
