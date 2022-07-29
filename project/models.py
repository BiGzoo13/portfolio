from django.db import models

# Create your models here.


class Projects(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    technologie = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")