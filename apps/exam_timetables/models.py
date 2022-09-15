from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

# from django.contrib.auth.models import User
from django.urls import reverse

# User = settings.AUTH_USER_MODEL
User = get_user_model()


class ExamTimetable(models.Model):
    COCIS_BLOCKS = [
        ('A', 'A'),
        ('B', 'B')
    ]
    course_unit_name = models.CharField(max_length=255, null=True, blank=False)
    course_unit_code = models.CharField(max_length=255, null=True, blank=False)
    room_number = models.CharField(max_length=255, null=True, blank=False)
    block = models.CharField(max_length=255, null=True, blank=False, choices=COCIS_BLOCKS)
    exam_date = models.CharField(max_length=255, null=True, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_unit_name

    # def get_absolute_url(self):
    #     return reverse('stories:post_detail', kwargs={'pk': self.pk})
