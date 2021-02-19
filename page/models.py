from django.db import models
from django.utils import timezone

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=10)
    message = models.TextField(max_length=500)
    date = models.DateField(default=timezone.now)