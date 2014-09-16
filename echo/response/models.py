from django.db import models
class Entry(models.Model):
    ask = models.TextField()
    response = models.TextField()
    ip = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
# Create your models here.

class KeyErr(models.Model):
    keyname = models.TextField()
    fucname = models.TextField()
    created = models.DateTimeField(auto_now_add=True)