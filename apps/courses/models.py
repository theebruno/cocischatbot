from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

# from django.contrib.auth.models import User
from django.urls import reverse

from apps.departments.models import Department

# User = settings.AUTH_USER_MODEL
User = get_user_model()


class Course(models.Model):
    name = models.CharField(max_length=255, null=True, blank=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('courses', kwargs={'pk': self.pk})
        return reverse('courses')

