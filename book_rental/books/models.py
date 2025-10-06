from django.db import models

# Create your models here.

class Books(models.Model):
    BookName = models.CharField(max_length=255)
    BookDescription = models.CharField(max_length=10000)