from django.core.serializers import serialize
from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'
    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    class Meta:
        db_table = 'product'

    @property
    def available(self):
        return True if self.stock != 0 else False
