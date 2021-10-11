from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return f'{self.title}: {self.description[:25]}...'