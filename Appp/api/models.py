from django.db import models


# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=20)
    ticker = models.CharField(max_length=10)
    desc = models.CharField(max_length=100)
    remarks = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.name