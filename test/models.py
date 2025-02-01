from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.



class Test(models.Model):
    date = models.DateField(default=None)
    Botany = models.IntegerField(default=None)
    Zoology = models.IntegerField(default=None)
    Physical = models.IntegerField(default=None)
    Inorganic = models.IntegerField(default=None)
    Organic = models.IntegerField(default=None)
    Physics = models.IntegerField(default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return f"{self.date}"