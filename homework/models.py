from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
    name = models.CharField(max_length=100, verbose_name='название')

    def __str__(self):
        return self.name

class Product (models.Model):
    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
    title = models.CharField(max_length=100, verbose_name='наименование продукта')
    description = models.TextField(verbose_name='описание')
    price = models.IntegerField(null=True, verbose_name='цена')
    category = models.ForeignKey(Category, null=True,
                                 verbose_name='тип товара',
                               on_delete=models.CASCADE)
    def __str__(self):
         return self.title


class Review (models.Model):
    class Meta:
        verbose_name = 'обзор'
        verbose_name_plural = 'обзоры'
    text = models.TextField(verbose_name='о продукте')
    product = models.ForeignKey(Product, null=True,
                                verbose_name='продукт',
                                    on_delete=models.CASCADE)
    def __str__(self):
        return 'Обзор товара'





