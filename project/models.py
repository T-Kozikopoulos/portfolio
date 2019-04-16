from django.db import models
from django.utils import timezone


class Project(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
    frontend = models.CharField(max_length=100)
    backend = models.CharField(max_length=100)
    demo = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)
    date_published = models.DateTimeField(default=timezone.now)

    # To showcase some of the most recent projects on the homepage.
    # Modified version of the last() Model function.
    def last_four(self):
        for obj in (self.reverse() if self.ordered else self.order_by('-pk'))[:1]:
            return obj

    def __str__(self):
        return self.title
