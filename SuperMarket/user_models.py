from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20, blank=True)
    middle_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    media = models.FileField(upload_to='users/%Y/%m/%d', blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Addresses(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='addresses')
    address = models.TextField()
    postal_code = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=25)

    def __str__(self):
        return self.address


class Numbers(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='numbers')
    country_code = models.CharField(max_length=5)
    number = models.CharField(max_length=12)

    def __str__(self):
        return self.number
