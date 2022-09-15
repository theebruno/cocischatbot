from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

# from django.contrib.auth.models import User
from django.urls import reverse

# User = settings.AUTH_USER_MODEL
User = get_user_model()


class ClassTimetable(models.Model):
    DAYS_OF_THE_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    course_unit_name = models.CharField(max_length=255, null=True, blank=False)
    course_unit_code = models.CharField(max_length=255, null=True, blank=False)
    course_unit_lecturer = models.ForeignKey(User, on_delete=models.CASCADE)
    days_of_the_week = models.CharField(max_length=255, null=True, blank=False, choices=DAYS_OF_THE_WEEK)
    time_of_class = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_unit_name

    # def get_absolute_url(self):
    #     return reverse('stories:post_detail', kwargs={'pk': self.pk})
