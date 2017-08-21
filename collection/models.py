from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, blank=True, null=True)
