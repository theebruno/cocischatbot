"""
"""
from django.db import models
from django.urls import reverse


class LecturerOffice(models.Model):
    COCIS_BLOCKS = [
        ('A', 'A'),
        ('B', 'B')
    ]

    office_number = models.CharField(max_length=255, null=True, blank=False)
    block = models.CharField(max_length=255, null=True, blank=False, choices=COCIS_BLOCKS)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.office_number

    # def get_absolute_url(self):
    #     return reverse('stories:post_detail', kwargs={'pk': self.pk})
