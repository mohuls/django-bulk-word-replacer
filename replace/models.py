from django.db import models


class My_model(models.Model):
    find = models.CharField(max_length=65)
    replace = models.CharField(max_length=65)
    file = models.FileField()
    path = models.CharField(max_length=120, blank=True, null=True)
    def __str__(self):
        return self.find