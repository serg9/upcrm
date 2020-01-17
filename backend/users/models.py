from django.conf import settings
from django.db import models

from utils.models import Enum


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    journal = models.IntegerField()
    surname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    number1 = models.CharField(max_length=12)
    number2 = models.CharField(max_length=12)
    email = models.CharField(max_length=100)
    notification = models.ForeignKey(
        Enum, on_delete=models.PROTECT, related_name='notification')
    birthday = models.DateField()
    comment = models.CharField(max_length=500)
    source = models.ForeignKey(
        Enum, on_delete=models.PROTECT, related_name='source')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT, related_name='user')
    cuser = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.PROTECT, related_name='cuser')
    cdate = models.DateField(auto_now_add=True)
    uuser = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.PROTECT, related_name='uuser')
    udate = models.DateField(auto_now=True)
