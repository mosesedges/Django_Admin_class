from django.db import models
from django.utils import timezone

# Create your models here.


class FirstCustomer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    complain = models.TextField(max_length=500)
    published = models.DateField(default=timezone.now)

    class meta:
        verbose_name = ('FirstCustomer')
        verbose_name_plural = ('FirstCustomers')
        ordering = ('-published')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
