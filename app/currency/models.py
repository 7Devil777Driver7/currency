from currency import model_choices as mch

from django.db import models
from django.utils import timezone


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(default=timezone.now)
    cur_type = models.PositiveSmallIntegerField(choices=mch.TYPE_CHOICES, default=mch.TYPE_USD)
    source = models.CharField(max_length=25, default='Unknown')


class ContactUs(models.Model):
    email_from = models.CharField(max_length=60)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=1500)


class Source(models.Model):
    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
