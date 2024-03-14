from django.db import models

# Create your models here.

class Property(models.Model):
    title = models.CharField(max_length = 200)
    address = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.title

