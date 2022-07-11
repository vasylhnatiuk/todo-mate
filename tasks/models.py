from django.db import models
from django.contrib.auth.models import AbstractUser


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=63)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=None)
    done = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["done"]

    def __str__(self):
        return f"{self.content} {self.datetime}"


