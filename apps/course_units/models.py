from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

# from django.contrib.auth.models import User
from django.urls import reverse

# User = settings.AUTH_USER_MODEL
User = get_user_model()


class CourseUnit(models.Model):
    name = models.CharField(max_length=255, null=True, blank=False)
    code = models.CharField(max_length=255, null=True, blank=False)
    lecturer = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('stories:post_detail', kwargs={'pk': self.pk})
