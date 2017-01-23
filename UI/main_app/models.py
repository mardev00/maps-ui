from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Map(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    center_longitude_val = models.FloatField()
    center_latitude_val = models.FloatField()
    left_longitude_val = models.FloatField()
    left_latitude_val = models.FloatField()  
    right_longitude_val = models.FloatField()
    right_latitude_val = models.FloatField()

    def __str__(self):
        return self.name
