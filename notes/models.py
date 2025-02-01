# in notes/models.py

from django.db import models
from django.conf import settings
class Note(models.Model):
   
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
     

    def __str__(self):
        return self.title
