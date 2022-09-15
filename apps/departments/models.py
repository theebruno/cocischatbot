"""
"""
from django.db import models
from django.urls import reverse


class Department(models.Model):
    name = models.CharField(max_length=255, null=True, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('stories:post_detail', kwargs={'pk': self.pk})
