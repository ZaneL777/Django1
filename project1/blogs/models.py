from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    detail = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    dmy = models.CharField(max_length=255)
