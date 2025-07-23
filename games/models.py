from django.db import models
from django.utils import timezone


class Game(models.Model):
    class Status(models.TextChoices):
        FROZEN = 'FR', 'Frozen'
        RELEASED = 'RL', 'Released'
        DEMO = 'DM', 'Demo'
        DEVELOPED = 'DV', 'In Dev'
        GAMEJAM = 'GJ', 'Gamejam'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    link = models.URLField(default='https://ortty.itch.io/')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=5,
        choices=Status,
        default=Status.DEVELOPED
    )

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def str(self):
        return self.title
