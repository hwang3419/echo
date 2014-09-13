from django.db import models
class Entry(models.Model):
    ask = models.CharField(max_length=300)
    response = models.CharField(max_length=300)
    ip = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now=True)
# Create your models here.
