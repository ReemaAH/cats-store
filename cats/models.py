
from django.db import models

class Cat(models.Model):
    name = models.CharField(blank=False, max_length=100)
    age = models.IntegerField(blank=False, default=0)
    category =  models.CharField(blank=False, max_length=100)
    image = models.ImageField(upload_to ='uploads/')

    def __str__(self):
        return self.name
