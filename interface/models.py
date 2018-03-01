from django.db import models

class UPost(models.Model):
    pid = models.CharField(max_length=120, unique=True)
    status = models.TextField()
    r_votes = models.IntegerField(default=1)

class PPost(models.Model):
    pid = models.CharField(max_length=120)
    status = models.TextField()
    label = models.CharField(max_length=10)
