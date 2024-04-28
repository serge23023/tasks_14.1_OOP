from src.classes.order_classes.for_in_categories import ForInCategories
from src.classes.products_classes.lawn_grass import LawnGrass
from src.utils import create_categories

if __name__ == '__main__':
    categories = create_categories()
    g = LawnGrass('d', 'dd', 0.0, 0, 'ddd', 'dddd', 'ddddd')

    print('---------------')
    for product in ForInCategories(categories[0].products):
        print(product)

    print('---------------')
    for category in categories:
        print(category)

    print('---------------')
    print(categories[0].products[0] + categories[0].products[1])
