# in todo/models.py

from django.db import models
from django.conf import settings
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class syallbuss(models.Model):
    Cname = models.CharField(max_length=100,default=None)
    Subject = models.CharField(max_length=100,default=None)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.Cname
