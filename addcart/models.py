from django.db import models

class Cart(models.Model):
    customer = models.CharField(max_length=10)
    product = models.CharField(max_length=15)
    date = models.DateField(null=True,auto_now_add=True)
