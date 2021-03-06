from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Show(models.Model):
  title = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  runtime = models.CharField(max_length=50)
  episodes = models.CharField(max_length=50)
  timestop = models.CharField(max_length=50)
  progress = models.CharField(max_length=50)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
      return reverse("shows_detail", kwargs={"show_id": self.id})
  