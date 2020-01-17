from django.db import models


class Enum(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    dict = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
