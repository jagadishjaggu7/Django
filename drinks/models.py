from django.db import models
class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    MRP = models.IntegerField(default=0,verbose_name="Price",blank=False)
    
    def __str__(self):
        return self.name+ ' : '+self.description    