from django.db import models


class Item(models.Model):
    """ Item model """
    name = models.CharField(max_length=150, verbose_name='name of product')
    description = models.TextField(max_length=1000, verbose_name='description of product')
    price = models.PositiveIntegerField(verbose_name='price of item')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'
