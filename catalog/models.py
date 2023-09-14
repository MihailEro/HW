from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=25, verbose_name='наименование')
    description = models.CharField(max_length=255, verbose_name='описание')
    preview = models.ImageField(upload_to='products/', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    production_data = models.DateField(verbose_name='дата создания', auto_now_add=True)
    change_data = models.DateField(verbose_name='дата последнешо изменения', auto_now=True)

    def __str__(self):
        return f'{self.product_name} ({self.description}): {self.price} {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    category_name = models.CharField(max_length=25, verbose_name='наименование')
    description = models.CharField(max_length=255, verbose_name='описание')

    def __str__(self):
        return f'{self.category_name} ({self.description})'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Blog(models.Model):
    objects = None
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    body = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='Изображение')
    date_create = models.DateField(**NULLABLE, verbose_name='Дата создания', auto_now_add=True)
    is_published = models.BooleanField(verbose_name='Опубликовано', default=True)
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'


class Version(models.Model):
    SIGN_TRUE = True
    SIGN_FALSE = False
    SIGN = ((SIGN_TRUE, 'Активная'),
            (SIGN_FALSE, 'Неактивная'),)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.PositiveIntegerField(verbose_name='Номер версии', null=False, blank=False)
    version_name = models.CharField(max_length=50, verbose_name='Название версии', **NULLABLE)
    is_active = models.BooleanField(default=SIGN_TRUE, choices=SIGN, verbose_name='Признак версии')



    def __str__(self):
        return f'{self.version_number}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'

