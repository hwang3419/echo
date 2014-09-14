from django.db import models
class Entry(models.Model):
    ask = models.TextField()
    response = models.TextField()
    ip = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now=True)
# Create your models here.
