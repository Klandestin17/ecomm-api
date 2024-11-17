from django.db import models


class Extras(models.Model):
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=25)
