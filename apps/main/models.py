from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from py11.utils import autoslug


class TimeABC(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Дата изменения')

    class Meta:
        abstract = True


@autoslug('title')
class Product(TimeABC):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=100,
                             verbose_name='Название товара')
    desc = models.TextField(verbose_name='Описание товара')
    count_bill = models.PositiveIntegerField(default=0,
                                             verbose_name='Кол-во')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                verbose_name='Картинки товара')


class Bill(TimeABC):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='bill')
    quantity = models.PositiveIntegerField(default=0)


@receiver(post_save, sender=Bill)
def count(sender, instance, *args, **kwargs):
    count_bill = getattr(instance.product, 'count_bill')
    q = instance.quantity
    count_bill += q
    setattr(instance.product, 'count_bill', count_bill)
    instance.product.save()





