from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=30)
    price = models.IntegerField()
    stock = models.IntegerField()
    sold = models.IntegerField() 

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'],name='name_unique')
        ]
 