from django.db import models

# Create your models here.
class Show(models.Model):
  title = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  runtime = models.IntegerField()
  episodes = models.IntegerField()