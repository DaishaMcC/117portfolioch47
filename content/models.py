from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=100)

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='static/img')
    repository = models.URLField()
    skill = models.ManyToManyField(Skill)
