from django.db import models


class Veterinary(models.Model):
    name = models.CharField(max_length=200)
