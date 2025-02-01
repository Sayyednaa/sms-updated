from django.db import models
from django.conf import settings

# Create your models here.
class TimeEntry(models.Model):
    date = models.DateField(default=None)
    duration = models.DecimalField(default=None , max_digits=4,decimal_places=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )

    def __str__(self):
        return f"{self.date} - {self.duration}"
