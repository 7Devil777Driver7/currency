from os import spawnle
from django.db import models


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField()
    type = models.CharField(max_length=3)
    source = models.CharField(max_length=25, default='Unknown')


class ContactUs(models.Model):
    email_from = models.CharField(max_length=60)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=1500)


# УДАЛИТЬ ЭТО ВСЁ ПОЗЖЕ!
