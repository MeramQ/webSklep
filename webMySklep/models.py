from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    
    def __str__(self):
        return self.name