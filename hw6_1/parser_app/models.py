from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='')
    year = models.CharField(max_length=4)

