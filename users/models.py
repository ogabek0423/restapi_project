from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField


from products.models import Product, Bestsellers, FeaturedItems


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to='media/users/u_pics')
    age = models.IntegerField()
    creation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.first_name}'

    class Meta:
        ordering = ['age']
        indexes = [
            models.Index(fields=['age'])
        ]


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_title = models.CharField(max_length=200)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.comment_title}'

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]


class Problems(models.Model):
    firstname = models.CharField(max_length=30)
    email = models.EmailField()
    problem_name = models.CharField(max_length=30)
    problem_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.problem_name}'

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]
