from django.db import models

# Create your models here.

class Exhibit(models.Model):
    title = models.CharField(max_length=70)
    artist = models.CharField(max_length=70)
    description = models.CharField(max_length=260)
    image = models.ImageField(upload_to="images/")
    for_sale = models.BooleanField(default=False)
    date = models.DateField()
    price = models.FloatField()
    quantity = models.IntegerField()


    def __str__(self):
        return self.title