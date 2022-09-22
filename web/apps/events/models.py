from django.contrib.auth import get_user_model
from django.db import models
# from django.contrib.auth.models import User
from django.urls import reverse

from apps.event_organisers.models import EventOrganiser

# User = settings.AUTH_USER_MODEL
User = get_user_model()


class Event(models.Model):
    name = models.CharField(max_length=255, null=True, blank=False)
    location = models.CharField(max_length=255, null=True, blank=False)
    # event_date = models.DateTimeField()
    event_date = models.DateField()
    # event_time = models.TimeField()
    organiser = models.ForeignKey(EventOrganiser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('events', kwargs={'pk': self.pk})
        return reverse('events')

