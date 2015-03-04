from django.db import models


class TestModel(models.Model):
    field = models.CharField(max_length=25)
