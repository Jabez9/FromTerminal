from django.db import models

# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=100)
    author =models.CharField(max_length=100)
    description = models.TextField()
    image= models.ImageField(upload_to='blog/')

    def __str__(self):
        return self.title


