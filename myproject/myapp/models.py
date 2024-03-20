from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class Team(models.Model):
    tname=models.CharField(max_length=200)
    timg=models.ImageField(upload_to='pics')
    tdesc=models.TextField()

    def __str__(self):
        return self.tname

