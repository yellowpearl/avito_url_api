from django.db import models

class Link(models.Model):
    full_link = models.CharField(max_length=2048)
    short_link_hash = models.CharField(max_length=200)
