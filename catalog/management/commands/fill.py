from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()


        category_list = [
            {'pk': 1, 'category_name': 'продукты', 'description': 'продукты питания'},
            {'pk': 2, 'category_name': '[хоз.товары]', 'description': 'товары для дома и хозяйственных нужд'},
            {'pk': 3, 'category_name': 'техника', 'description': 'электротовары и техника для дома'}
        ]
        category_objects = []
        for category_item in category_list:
            category_objects.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(category_objects)

        product_list = [
            {'product_name': 'молоко', 'description': 'пейте дети молоко, будете здоровы', 'preview': '',
             'category': Category.objects.get(pk=1), 'price': '98', 'production_data': '2023-08-21', 'change_data': '2023-08-21'},
            {'product_name': 'Сорти', 'description': 'ваша посуда, скажет спасибо', 'preview': '',
             'category': Category.objects.get(pk=2), 'price': '72', 'production_data': '2023-08-21', 'change_data': '2023-08-21'},
            {'product_name': 'холодильник', 'description': 'сохранияет продукты свежими',
             'preview': '', 'category': Category.objects.get(pk=3), 'price': '1980', 'production_data': '2023-08-21',
             'change_data': '2023-08-21'},
        ]

        product_objects = []

        for product_item in product_list:
            product_objects.append(
                Product(**product_item)
            )

        Product.objects.bulk_create(product_objects)
