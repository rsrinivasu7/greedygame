from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Genre(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 150)
    def __str__(self):
        return self.name
    
class Track(models.Model):
    id      = models.AutoField(primary_key = True)
    title   = models.CharField(max_length = 150)
    genres  = models.ManyToManyField(Genre)
    rating  = models.FloatField(default= 0,validators=[MinValueValidator(0)])
    def __str__(self):
        return self.title