from django.db import models
from django import utils  # import timezone


class Product(models.Model):
    title = models.CharField(max_length=200, default=None, blank=True, null=True)
    brand = models.CharField(max_length=200, default=None, blank=True, null=True)
    price = models.CharField(max_length=200, default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=utils.timezone.now, blank=True)
    updated_date = models.DateTimeField(null=True)
