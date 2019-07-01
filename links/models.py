from django.db import models

class Link(models.Model):
  url = models.URLField()
  description = models.TextField(blank=True)
  rank = models.IntegerField(blank=True, default=1)
