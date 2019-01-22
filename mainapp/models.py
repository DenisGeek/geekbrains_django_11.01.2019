from django.db import models


# Create your models here.


class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    dateCreation = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField(auto_now=True)

    name = models.CharField(verbose_name='Name', max_length=64, blank=False, unique=True)
    description = models.TextField(verbose_name='Description', blank=True)

    # def __init__(self, name: str):
    #     self.name = name

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    dateCreation = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField(auto_now=True)

    categoryId = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    name = models.CharField(verbose_name='Product name', max_length=128)
    price = models.DecimalField(verbose_name='Product price', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='Product available in store', default=0)
    descriptionShort = models.CharField(verbose_name='Product short description', max_length=60, blank=True)
    description = models.TextField(verbose_name='Product description', blank=True)
    image = models.ImageField(upload_to='product.images', blank=True)

    def __str__(self):
        return f"{self.name} ({self.categoryId})"
