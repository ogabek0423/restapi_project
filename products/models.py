from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# from mdeditor.fields import MDTextField


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='products/my_pic')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]


class Bestsellers(models.Model):
    name = models.CharField(max_length=20)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} {self.product}'

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]


class FeaturedItems(models.Model):
    name = models.CharField(max_length=20)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    chegirma = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]
