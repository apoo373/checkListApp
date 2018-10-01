# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CheckList(models.Model):
    userId = models.ForeignKey(User, on_delete=None)
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=500)
    PRIORITY = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
    )
    priority = models.IntegerField(choices=PRIORITY, default=1)
    timeCreated = models.DateTimeField(auto_now_add=True)
    dateConcerned = models.DateTimeField('event Date')
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
